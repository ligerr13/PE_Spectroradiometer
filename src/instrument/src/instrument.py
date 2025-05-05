import asyncio
import functools
import logging
import enum
from typing import Union, Optional
from dataclasses import dataclass
import json
import serial_asyncio

from ...globals.utils import find_serial_port

logging.basicConfig(level=logging.DEBUG)

class Delimiter(enum.Enum):
    CRLF = b'\r\n'
    CR = b'\r'
    LF = b'\n'

class SerialProtocol(asyncio.Protocol):
    def __init__(self):
        self._ready_event = asyncio.Event()
        self._rbuffer = asyncio.Queue()
        self._transport = None
        self._timeout = 10.0
        self._delimiter = Delimiter.CRLF.value
        self._partial_data = ''

    def connection_lost(self, exc) -> None:
        logging.error("Connection: lost.")
        return super().connection_lost(exc)

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
            logging.warning("Connection: lost.")
            return None
        
        try:
            self._transport.write(command + delimiter.value)
            logging.debug(f">> Sending data: {command} + {delimiter.value}")
        
        except Exception as e:
            logging.error(f"Error while sending data: {e}")
            return None

    async def read_until_delimiter(self) -> tuple[str, Union[list[str], None]]:
        """Read a line from the buffer with a timeout."""
        if self._transport is None or self._transport.is_closing():
            logging.error("Connection: lost.")
            return 'ER100', None

        try:
            line = await asyncio.wait_for(self._rbuffer.get(), timeout=self._timeout)

            if line:
                parts = line.split(',', 1)
                if len(parts) > 1:
                    return parts[0], parts[1].split(',')
                return parts[0], None

        except asyncio.TimeoutError:
            logging.error("Timeout while waiting for response.")
            if self._transport:
                self._transport.close()
            return 'ER101', None
        
        except Exception as e:
            logging.error(f"Unexpected error while reading: {e}")
            if self._transport:
                self._transport.close()
            return 'ER99', None


class Instrument:

    active_connection: Optional[asyncio.Protocol] = None

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
        """Read response and check for errors."""

        err, response = await protocol.read_until_delimiter()
        code, info = Instrument.check_error_code(err)

        if code != 0:
            return Instrument.ReadData(None, code, info)

        return Instrument.ReadData(response, code, info)

    @classmethod
    def connection(cls, port: str = None, baudrate: int = 9600, protocol: asyncio.Protocol = SerialProtocol, idVendor=0xfffe, idProduct=0x0001):
        """Decorator to handle serial connection. Reuses active connection if available."""

        def decorator(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                if cls.active_connection is None:
                    _port = port or find_serial_port(idVendor, idProduct)

                    loop = asyncio.get_running_loop()
                    
                    _transport, _protocol = await serial_asyncio.create_serial_connection(
                        loop, protocol, _port, baudrate
                    )
                    cls.active_connection = _protocol
                    try:
                        await _protocol._ready_event.wait()
                        return await func(_protocol, *args, **kwargs)
                    finally:
                        _transport.close()
                        cls.active_connection = None
                else:
                    return await func(cls.active_connection, *args, **kwargs)

            return wrapper
        return decorator
    
    @staticmethod
    def check_error_code(error_code: str) -> tuple[int, str]:
        """Check the error code, raise an exception if it starts with 'ER'"""
        try:
            with open('./src/error_codes.json', 'r') as file:
                error_codes = json.load(file)

            meaning = error_codes.get(error_code, "Unknown error code.")

            if error_code.startswith("ER"):
                return 1, meaning
                
            return 0, meaning
                    
        except Exception as e:
            return 1, f'{e}'
