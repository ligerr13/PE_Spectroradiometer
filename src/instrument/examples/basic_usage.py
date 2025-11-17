import asyncio
from ..src.instrument import Instrument as CS2000
from ..src.commands import IdentificationDataRead, Measure, MeasuringSwitchEnable, RemoteModeSelect
from ...globals.utils import show_toast
from ...globals.enum import ToastType
from ...signals.signals import WorkspaceSignalBus
import pandas as pd
import numpy as np
import datetime, time

@CS2000.connection(baudrate=9600)
async def p_measure_read_store(protocol):
    """Performs the full measurement process"""
    bus = WorkspaceSignalBus.instance()
    state = 0

    save_file = {
        "MeasurementJsonBuilder": {"Measurement Conditions": {}},
        "Spectral380To479JsonBuilder": {"Spectral data": {}},
        "Spectral480To579JsonBuilder": {"Spectral data": {}},
        "Spectral580To679JsonBuilder": {"Spectral data": {}},
        "Spectral680To780JsonBuilder": {"Spectral data": {}},
        "ColorimetricJsonBuilder": {"Colorimetric Data": {}}
    }

    try:
        state = 1
        bus.emitCalibrationStarted()
        await RemoteModeSelect(protocol, operation=1)
        await MeasuringSwitchEnable(protocol, operation=0)
        bus.emitCalibrationEnded()
        
        state = 2
        bus.emitMeasurementStarted()
        data = await Measure(protocol, operation=1)

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

        state = 3
        condition_values = measurement_conditions.response
        conditions_dict = save_file["MeasurementJsonBuilder"]["Measurement Conditions"]
        
        for key, value in zip(CS2000.MEASUREMENT_KEYS, condition_values):
            conditions_dict[key] = {"value": value.strip(), "switch": 0}

        spectral_responses = [
            (save_file["Spectral380To479JsonBuilder"], spectral_irradiance_data_380nm_to_479nm.response),
            (save_file["Spectral480To579JsonBuilder"], spectral_irradiance_data_480nm_to_579nm.response),
            (save_file["Spectral580To679JsonBuilder"], spectral_irradiance_data_580nm_to_679nm.response),
            (save_file["Spectral680To780JsonBuilder"], spectral_irradiance_data_680nm_to_780nm.response)
        ]
        
        for builder_dict, response_list in spectral_responses:
            formatted_values = [f"{float(val):.4e}" for val in response_list]
            
            builder_dict["Spectral data"] = {
                "value": ",".join(formatted_values),
                "switch": 0
            }

        colorimetric_values = colorimetric_data.response
        colorimetric_data_dict = save_file["ColorimetricJsonBuilder"]["Colorimetric Data"]
        
        for key, value in zip(CS2000.COLORIMETRIC_KEYS, colorimetric_values):
            if key in ["T", "delta uv", "T10", "delta uv10"]:
                formatted_value = value.strip() if key.startswith('T') else value.strip()
            elif 'e' in value.lower():
                formatted_value = f"{float(value):.4e}" 
            else:
                formatted_value = value.strip() 

            colorimetric_data_dict[key] = {"value": formatted_value, "switch": 0}

        final_json_string = json.dumps(save_file, indent=4)
        
        state = 4
        _ct = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Measurement_Data_{_ct}.json" 
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(final_json_string)
        except Exception as file_error:
            logging.error(f"Error while writing json file: {file_error}")
            
        await bus.emitMeasurementDoneSuccess(final_json_string)
        return final_json_string

    except Exception as e:
        print(f"Measurement failed: {e}")
        
        if state == 1:
            await bus.emitCalibrationFailed()
        elif state == 2:
            await bus.emitMeasurementFailed()
        elif state == 3:
            await bus.emitProcessingFailed()
        elif state == 4:
            await bus.emitGeneratingFilesFailed()
        
    finally:
        try:
            asyncio.create_task(CS2000.close_connection())
        except Exception as close_err:
            print(f"Error closing instrument connection: {close_err}")