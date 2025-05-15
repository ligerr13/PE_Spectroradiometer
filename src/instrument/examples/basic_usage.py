import asyncio
from ..src.instrument import Instrument as CS2000
from ..src.commands import Measure, MeasuringSwitchEnable, RemoteModeSelect
from ...globals.utils import show_toast
from ...globals.enum import ToastType
from ...signals.signals import WorkspaceSignalBus
import pandas as pd
import numpy as np
import datetime, time
# from cs2000_commands import * 


# workspace_signal_bus = WorkspaceSignalBus.instance()

@CS2000.connection(baudrate=9600)
async def p_measure_read_store(protocol):
    """Performs the full measurement process"""
    try:
        await RemoteModeSelect(protocol, operation=1)

        await MeasuringSwitchEnable(protocol, operation=0)

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

        await RemoteModeSelect(protocol, operation=0)

        spectral_data = np.concatenate([
            spectral_irradiance_data_380nm_to_479nm.response,
            spectral_irradiance_data_480nm_to_579nm.response,
            spectral_irradiance_data_580nm_to_679nm.response,
            spectral_irradiance_data_680nm_to_780nm.response
        ])

        wavelengths = np.arange(380, 781, 1)

        values = colorimetric_data.response
        colorimetric_dict = {key: float(value) for key, value in zip(CS2000.COLORIMETRIC_KEYS, values)}

        spectral_df = pd.DataFrame({
            "Wavelength": wavelengths,
            "Spectral-Irradiance": spectral_data
        })
        _ct = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        spectral_df.to_csv(f"Spectral_Data_{_ct}.csv", index=False)

        colorimetric_df = pd.DataFrame(list(colorimetric_dict.items()), columns=["Parameter", "Value"])
        colorimetric_df.to_csv(f"Colorimetric_Data_{_ct}.csv", index=False)

        show_toast("Successful measurement and saving!", duration=6500, success=ToastType.SUCCESS)

    except Exception as e:
        show_toast(f"Measurement failed: {str(e)}", duration=7000, success=ToastType.ERROR)