import asyncio
import json
import numpy as np
import datetime
import logging
from collections import namedtuple

# ----------------------------------------------------------------------
# --- DUMMY/MOCK FÜGGVÉNYEK ÉS OSZTÁLYOK A Futtatáshoz ---
# ----------------------------------------------------------------------

# A valós CS2000.Read visszatérési típusát utánozza
ReadData = namedtuple('ReadData', ['response', 'code', 'info'])

# Mock a soros kommunikációs protokollhoz és eszközhöz
class MockSerialProtocol:
    """Mock protokoll, csak a szignatúrához."""
    pass

class MockInstrument:
    """Mock CS2000 osztály a szükséges metódusokkal és konstansokkal."""
    
    # 🚨 DUMMY KULCSLISTÁK (Feltételezzük, hogy ezek léteznek a valós CS2000-ben)
    COLORIMETRIC_KEYS = [
        "Le", "Lv", "X", "Y", "Z", "x", "y", "u'", "v'", "T", "delta uv", "lambda d", "Pe",
        "X10", "Y10", "Z10", "x10", "y10", "u'10", "v'10", "T10", "delta uv10", "lambda d10", "Pe10"
    ]
    
    # A mérési feltételek kulcsai (a MEDR,0,0,1 válaszsorrendjében)
    MEASUREMENT_CONDITION_KEYS = [
        "Speed mode", "Sync mode", "Integration time", "Internal ND filter",
        "Optional close-up lens", "Optional external ND filter", 
        "Measurement angle", "Calibration channel"
    ]

    # Dummy adatok a visszatéréshez, a megadott JSON minta alapján
    DUMMY_CONDITIONS = ["0", "0", "000859000", "1", "0", "0", "0", "00"]
    DUMMY_COLORIMETRIC = [
        "6.0544e-1", "133.99", "1.2620e+2", "1.3399e+2", "1.1334e+2", "0.3379", "0.3587",
        "0.2039", "0.4870", " 5303", "+0.0065", "561.36", "9.0400",
        "1.3798e+2", "1.4551e+2", "1.2168e+2", "0.3405", "0.3591", "0.2055",
        "0.4876", " 5253", "+0.0063", "558.71", "9.9100"
    ]
    # Létrehozunk egy dummy spektrális adatsort (100 elem, az Ön mintájához hasonlóan)
    DUMMY_SPECTRAL_BLOCK = [f"{i * 1e-4:.4e}" for i in range(100, 200)] 
    # A 4. blokk 101 elemet igényel, használjuk a dummy értékeket
    DUMMY_SPECTRAL_BLOCK_4 = [f"{i * 1e-4:.4e}" for i in range(200, 301)]


    # Mock a CS2000.Read metódushoz
    @classmethod
    async def Read(cls, protocol):
        """Mock Read metódus, ami a lekérdezéstől függően ad vissza adatot."""
        # A valós implementáció nem itt dönt, de a teszthez kell a viselkedés utánozása
        await asyncio.sleep(0.01) # Kis késleltetés az async viselkedéshez
        
        # Mivel nincs hozzáférésünk az utolsó Write-hoz, az adatokat a hívás sorrendje alapján adjuk vissza,
        # vagy egy egyszerű, de fix értékkel térünk vissza.
        
        # Itt a kódunk fixen a kért adatokat (a valós outputként megadott értékeket) adja vissza:
        # A sorrend a p_measure_read_store-ban: 4x Spectral, 1x Colorimetric, 1x Conditions
        
        # A legutolsó hívás (Conditions)
        if protocol.last_command == b'MEDR,0,0,1':
            return ReadData(cls.DUMMY_CONDITIONS, 0, "OK00")
        
        # Colorimetric hívás
        if protocol.last_command == b'MEDR,2,0,0':
            return ReadData(cls.DUMMY_COLORIMETRIC, 0, "OK00")
            
        # Spektrális hívások
        if protocol.last_command == b'MEDR,1,0,1':
            return ReadData(cls.DUMMY_SPECTRAL_BLOCK, 0, "OK00")
        if protocol.last_command == b'MEDR,1,0,2':
            return ReadData(cls.DUMMY_SPECTRAL_BLOCK, 0, "OK00")
        if protocol.last_command == b'MEDR,1,0,3':
            return ReadData(cls.DUMMY_SPECTRAL_BLOCK, 0, "OK00")
        if protocol.last_command == b'MEDR,1,0,4':
            return ReadData(cls.DUMMY_SPECTRAL_BLOCK_4, 0, "OK00")

        # Alapértelmezett, ha nem illeszkedik egyikre sem
        return ReadData([], 0, "OK00")


    # Mock a CS2000.Write metódushoz (csak tároljuk az utolsó parancsot a Read mockhoz)
    @classmethod
    def Write(cls, protocol, command: bytes):
        protocol.last_command = command
        # print(f"Mock Write: {command.decode()}")

    # Mock a CS2000.connection dekorátorhoz
    @classmethod
    def connection(cls, baudrate):
        def decorator(func):
            async def wrapper(*args, **kwargs):
                mock_protocol = MockSerialProtocol()
                mock_protocol.last_command = None # Tároljuk az utolsó parancsot
                return await func(mock_protocol)
            return wrapper
        return decorator

    # Mock a CS2000.close_connection-hoz
    @classmethod
    async def close_connection(cls):
        print("Mock: Connection closed.")

    # Mock a RemoteModeSelect és MeasuringSwitchEnable parancsokhoz
    @classmethod
    async def command(cls, protocol, operation=None):
        await asyncio.sleep(0.01)
        return ReadData([], 0, "OK00")

# Mock a külső parancsokhoz
RemoteModeSelect = MockInstrument.command
MeasuringSwitchEnable = MockInstrument.command
Measure = MockInstrument.command
CS2000 = MockInstrument # Helyettesítjük a CS2000-t a Mock-kal

# Mock a jelbuszhoz
class MockWorkspaceSignalBus:
    @classmethod
    def instance(cls):
        return cls()
    async def emitCalibrationStarted(self): pass
    async def emitCalibrationEnded(self): pass
    async def emitMeasurementStarted(self): pass
    async def emitMeasurementEnded(self): pass
    async def emitMeasurementDoneSuccess(self, json_data):
        print("\n--- JSON GENERATED SUCCESSFULLY ---")
        print(json_data)
        
WorkspaceSignalBus = MockWorkspaceSignalBus

# ----------------------------------------------------------------------
# --- A TESZTELENDŐ FŐ FÜGGVÉNY (AZ ÖN MÓDOSÍTOTT KÓDJA) ---
# ----------------------------------------------------------------------

@CS2000.connection(baudrate=9600)
async def p_measure_read_store(protocol):
    """Performs the full measurement process and builds the exact nested JSON structure."""
    bus = WorkspaceSignalBus.instance()
    state = 0
    
    # 🚨 VÉGLEGES JSON OBJEKTUM VÁZA
    save_file = {
        "MeasurementJsonBuilder": {"Measurement Conditions": {}},
        "Spectral380To479JsonBuilder": {"Spectral data": {}},
        "Spectral480To579JsonBuilder": {"Spectral data": {}},
        "Spectral580To679JsonBuilder": {"Spectral data": {}},
        "Spectral680To780JsonBuilder": {"Spectral data": {}},
        "ColorimetricJsonBuilder": {"Colorimetric Data": {}}
    }

    try:
        # ... (Calibration, RemoteModeSelect, MeasuringSwitchEnable) ...
        state = 1
        bus.emitCalibrationStarted()
        await RemoteModeSelect(protocol, operation=1)
        await MeasuringSwitchEnable(protocol, operation=0)
        bus.emitCalibrationEnded()
        
        state = 2
        bus.emitMeasurementStarted()
        # Várjuk meg a mérés befejezését
        data = await Measure(protocol, operation=1) 

        # ------------------- ADATOK OLVASÁSA -------------------
        
        CS2000.Write(protocol, b'MEDR,1,0,1')
        spectral_irradiance_data_380nm_to_479nm = await CS2000.Read(protocol)

        CS2000.Write(protocol, b'MEDR,1,0,2')
        spectral_irradiance_data_480nm_to_579nm = await CS2000.Read(protocol)

        CS2000.Write(protocol, b'MEDR,1,0,3')
        spectral_irradiance_data_580nm_to_679nm = await CS2000.Read(protocol)

        CS2000.Write(protocol, b'MEDR,1,0,4')
        spectral_irradiance_data_680nm_to_780nm = await CS2000.Read(protocol)

        CS2000.Write(protocol, b'MEDR,2,0,0')
        colorimetric_data = await CS2000.Read(protocol)

        CS2000.Write(protocol, b'MEDR,0,0,1')
        measurement_conditions = await CS2000.Read(protocol)
        
        bus.emitMeasurementEnded()
        await RemoteModeSelect(protocol, operation=0)

        # ------------------- JSON STRUKTÚRA ÉPÍTÉSE AZ ELVÁRT FORMÁTUMBAN -------------------

        # 1. Mérési feltételek (MeasurementJsonBuilder)
        condition_values = measurement_conditions.response
        conditions_dict = save_file["MeasurementJsonBuilder"]["Measurement Conditions"]
        
        for key, value in zip(CS2000.MEASUREMENT_CONDITION_KEYS, condition_values):
            conditions_dict[key] = {"value": value.strip(), "switch": 0}


        # 2. Spektrális adatok (SpectralXXXJsonBuilder)
        spectral_responses = [
            (save_file["Spectral380To479JsonBuilder"], spectral_irradiance_data_380nm_to_479nm.response),
            (save_file["Spectral480To579JsonBuilder"], spectral_irradiance_data_480nm_to_579nm.response),
            (save_file["Spectral580To679JsonBuilder"], spectral_irradiance_data_580nm_to_679nm.response),
            (save_file["Spectral680To780JsonBuilder"], spectral_irradiance_data_680nm_to_780nm.response)
        ]
        
        for builder_dict, response_list in spectral_responses:
            # Vesszővel elválasztott string formázása tudományos jelöléssel (4 tizedes pontossággal)
            # A DUMMY adatok már eleve tudományos jelölésű stringek, de a konverzió biztosítja a formátumot
            formatted_values = [f"{float(val):.4e}" for val in response_list]
            
            builder_dict["Spectral data"] = {
                "value": ",".join(formatted_values),
                "switch": 0
            }


        # 3. Kolorimetrikus adatok (ColorimetricJsonBuilder)
        colorimetric_values = colorimetric_data.response
        colorimetric_data_dict = save_file["ColorimetricJsonBuilder"]["Colorimetric Data"]
        
        for key, value in zip(CS2000.COLORIMETRIC_KEYS, colorimetric_values):
            # Formázás a minta alapján (T és delta uv megtartja a szóközöket/előjeleket, a többi float)
            formatted_value = value.strip()
            
            if key not in ["T", "delta uv", "T10", "delta uv10"] and ('e' in value.lower() or '.' in value):
                 # Tudományos jelölés megtartása és formázása, ha lehetséges
                try:
                    # Kényszerítjük a 4 tizedes pontosságú tudományos jelölésre, ha lehetséges
                    if 'e' in value.lower():
                         formatted_value = f"{float(value):.4e}" 
                    else:
                        formatted_value = value.strip()
                except ValueError:
                    # Ha nem szám, megtartjuk stringként (biztonsági háló)
                    pass


            colorimetric_data_dict[key] = {"value": formatted_value, "switch": 0}

        
        # Végleges JSON string generálása és visszaadása
        final_json_string = json.dumps(save_file, indent=4)
        
        await bus.emitMeasurementDoneSuccess(final_json_string)
        return final_json_string

    except Exception as e:
        print(f"Measurement failed: {e}")
        
        if state == 1:
            # await bus.emitCalibrationFailed()
            pass
        elif state == 2:
            # await bus.emitMeasurementFailed()
            pass
        raise 
    finally:
        asyncio.create_task(CS2000.close_connection())

# ----------------------------------------------------------------------
# --- FUTTATÁS ---
# ----------------------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(p_measure_read_store())