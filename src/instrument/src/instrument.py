import asyncio
import functools
import logging
import enum
from typing import Union, Optional
from dataclasses import dataclass
import json
import serial_asyncio

# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger('no_spam')

class Delimiter(enum.Enum):
    CRLF = b'\r\n'
    CR = b'\r'
    LF = b'\n'

class SerialProtocol(asyncio.Protocol):
    def __init__(self):
        self._ready_event = asyncio.Event()
        self._rbuffer = asyncio.Queue()
        self._transport = None
        self._timeout = 1.0
        self._delimiter = Delimiter.CRLF.value
        self._partial_data = ''

    def connection_lost(self, exc) -> None:
        logging.error("Connection: lost.")

    def connection_made(self, transport) -> None:
        """called when  the serial connection is established."""
        self._transport = transport
        logging.debug("Connection: connected.")
        self._ready_event.set()

    def data_received(self, data: bytes) -> None:
        """Handle incoming data, collect until delimiter is received."""
        try:
            self._partial_data += data.decode('utf-8', errors='ignore')
            delimiter_str = self._delimiter.decode('utf-8')

            while delimiter_str in self._partial_data:
                line, self._partial_data = self._partial_data.split(delimiter_str, 1)
                
                try:
                    line_decoded = line.strip()
                    
                    if line_decoded:
                        self._rbuffer.put_nowait(line_decoded)
                        logging.debug(f"<< Receiving full line: {line_decoded}")

                except UnicodeDecodeError as e:
                    logging.error(f"Failed to decode received data: {e}")
                    
        except Exception as e:
            logging.error(f"Error while processing received data: {e}")
                
        except UnicodeDecodeError as e:
            logging.error(f"Failed to decode data: {e}")


    def write_command(self, command: bytes, delimiter: Delimiter = Delimiter.CRLF) -> None:
        """Write command to the instrument as a byte string."""
        if not isinstance(command, (bytes)):
            logging.error("Data must be of type bytes")
            return None
                
        if self._transport is None or self._transport.is_closing():
            logging.warning("Connection: lost in the write phase.")
            return None
        
        try:
            self._transport.write(command + delimiter.value)
            logging.debug(f">> Sending data: {command} + {delimiter.value}")
        
        except Exception as e:
            logging.error(f"Error while sending data: {e}")
            raise

    async def read_until_delimiter(self) -> tuple[str, Union[list[str], None]]:
        """Read a line from the buffer with a timeout."""
        if self._transport is None or self._transport.is_closing():
            logging.error("Connection: lost.")
            raise ConnectionError("Serial connection lost before reading.")

        try:
            line = await asyncio.wait_for(self._rbuffer.get(), timeout=self._timeout)

            if line:
                parts = line.split(',', 1)
                if len(parts) > 1:
                    return parts[0], parts[1].split(',')

        except asyncio.TimeoutError:
            logging.error("Timeout while waiting for response.")
            raise TimeoutError("Timeout while reading from serial connection.")
        
        except Exception as e:
            logging.error(f"Unexpected error while reading: {e}")
            raise RuntimeError(f"Unexpected error during serial read: {e}")


class Instrument:

    active_connection: Optional[asyncio.Protocol] = None
    config: dict = {}

    @dataclass
    class ReadData:
        response: str
        code: int
        info: str
    
    COLORIMETRIC_KEYS = [
        "Le", "Lv", "X", "Y", "Z", "x", "y", "u'", "v'", "T", "delta uv", "lambda d", 
        "Pe","X10", "Y10", "Z10", "x10", "y10", "u'10", "v'10", "T10", "delta uv10", "lambda d10", "Pe10"
    ]
    
    def Write(protocol: SerialProtocol, command: bytes):
        """Write to the instrument."""
        if protocol and command:
            protocol.write_command(command)

    async def Read(protocol: SerialProtocol) -> ReadData:
        try:
            err, response = await protocol.read_until_delimiter()

        except asyncio.TimeoutError:
            logging.error("Timeout: No response from instrument.")
            raise RuntimeError("Timeout: No response from instrument.")
        
        code, info = Instrument.check_error_code(err)

        if code != 0:
            logging.error(f"Instrument error [{code}]: {info}")
            raise RuntimeError(f"Instrument error [{code}]: {info}")

        return Instrument.ReadData(response, code, info)

    @classmethod
    def load_config(cls, path='src\\instrument\\config\\connection_config.json'):
        if not cls.config:
            try:
                with open(path, 'r') as f:
                    raw = json.load(f)
                    cls.config = raw
            except FileNotFoundError:
                logging.error(f"Config file not found: {path}")
            except json.JSONDecodeError as e:
                logging.error(f"JSON decode error in config file: {e}")
            except Exception as e:
                logging.error(f"Unexpected error while loading config: {e}")

    @classmethod
    async def close_connection(cls):
        if cls.active_connection:
            transport = getattr(cls.active_connection, '_transport', None)
            if transport:
                await transport.close()
            cls.active_connection = None

    @classmethod
    def connection(cls, port: str = None, baudrate: int = 9600, protocol: asyncio.Protocol = SerialProtocol, idVendor=0xfffe, idProduct=0x0001):
        """Decorator to handle serial connection."""
        
        cls.load_config()
        port = port or cls.config.get("port")
        baudrate = baudrate or cls.config.get("baudrate")

        if port is None:
            logging.error(f"No valid serial port found.")

        def decorator(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                if cls.active_connection is None:
                    loop = asyncio.get_running_loop()
                    _transport = None
                    _protocol = None

                    try:
                        _transport, _protocol = await serial_asyncio.create_serial_connection(
                            loop, protocol, port, baudrate
                        )

                        cls.active_connection = _protocol

                        await _protocol._ready_event.wait()
                        return await func(_protocol, *args, **kwargs)

                    except Exception as e:
                        raise RuntimeError(f"Failed during serial communication on port {port}: {e}")
                else:
                    return await func(cls.active_connection, *args, **kwargs)

            return wrapper
        return decorator

    
    @staticmethod
    def check_error_code(error_code: Optional[str]) -> tuple[int, str]:
        if not error_code:
            raise RuntimeError("No error code received: communication failure or no response.")

        try:
            with open('./src/error_codes.json', 'r') as file:
                error_codes = json.load(file)

            meaning = error_codes.get(error_code, "Unknown error code.")

            if error_code.startswith("ER"):
                raise RuntimeError(f"Instrument error [{error_code}]: {meaning}")

            return 0, meaning

        except FileNotFoundError:
            raise RuntimeError("Error codes file not found.")
        except json.JSONDecodeError:
            raise RuntimeError("Error codes JSON file is corrupted.")
        except Exception as e:
            raise RuntimeError(f"Unexpected error during error code checking: {e}")

