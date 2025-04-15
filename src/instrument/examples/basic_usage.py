import asyncio
from ..src.instrument import Instrument as CS2000
from ..src.commands import Measure, MeasuringSwitchEnable, RemoteModeSelect
import pandas as pd
import numpy as np
import datetime

@CS2000.connection(port='/dev/cu.usbmodem12345678901', baudrate=9600)
async def _measure_read_store(protocol):
    """Performs the full measurement process"""

    await RemoteModeSelect(protocol, operation=1)

    """
        This ensures that only fresh, accurate data is used for each new measurement.
    """
    await MeasuringSwitchEnable(protocol, operation=0)

    """
        Start of measurement.
    """
    data = await Measure(protocol, operation=1)

    """
        Request for 380nm to 479nm spectral irradiance data.
    """
    CS2000.Write(protocol, b'MEDR,1,0,1')
    spectral_irradiance_data_380nm_to_479nm = await CS2000.Read(protocol)

    """
        Request for 480nm to 579nm spectral irradiance data.
    """
    CS2000.Write(protocol, b'MEDR,1,0,2')
    spectral_irradiance_data_480nm_to_579nm = await CS2000.Read(protocol)

    """
        Request for 580nm to 679nm spectral irradiance data.
    """
    CS2000.Write(protocol, b'MEDR,1,0,3')
    spectral_irradiance_data_580nm_to_679nm = await CS2000.Read(protocol)

    """
        Request for 680nm to 780nm spectral irradiance data.
    """
    CS2000.Write(protocol, b'MEDR,1,0,4')
    spectral_irradiance_data_680nm_to_780nm = await CS2000.Read(protocol)

    """
        Request for colorimetric data.
    """
    CS2000.Write(protocol, b'MEDR,2,0,0')
    colorimetric_data = await CS2000.Read(protocol)

    """
        Request for measurement conditions.
    """
    CS2000.Write(protocol, b'MEDR,0,0,1')
    measurement_conditions = await CS2000.Read(protocol)

    await RemoteModeSelect(protocol, operation=0)

    """
        Saving data to a .csv (optional).
    """

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

def run_program(program, error_handler):
    try:
        asyncio.run(program())
    except Exception as e:
        error_handler(e)

def error_handler(e):
    print(f"An Error has happened: {e}")
    print("Shutting down...")
