import asyncio
from ..invoker import Invoker
from ..config.enums import ModeSelect, SpectralRange, DataMode, DataFormat
from ..commands.rmts import RMTS
from ..commands.meas import MEAS
from ..commands.medr import MEDR

async def BasicProgramAndSave(file_name: str):
    """
    You can make your own programs just like this...
    """
    invoker = Invoker(save_file=True, save_options={"filename": f"{file_name}.json"})

    cstart = RMTS(switch=ModeSelect.ENABLED)
    cmeasure = MEAS(switch=ModeSelect.ENABLED)

    cr1 =  MEDR(data_mode=SpectralRange.RANGE_380_TO_479, data_format=DataFormat.ALPHANUMERIC)
    cr2 =  MEDR(data_mode=SpectralRange.RANGE_480_TO_579, data_format=DataFormat.ALPHANUMERIC)
    cr3 =  MEDR(data_mode=SpectralRange.RANGE_580_TO_679, data_format=DataFormat.ALPHANUMERIC)
    cr4 =  MEDR(data_mode=SpectralRange.RANGE_680_TO_780, data_format=DataFormat.ALPHANUMERIC)
    cr5 =  MEDR(data_mode=DataMode.COLORIMETRIC_DATA, data_format=DataFormat.ALPHANUMERIC)
    cr6 =  MEDR(data_mode=DataMode.MEASUREMENT_CONDITIONS, data_format=DataFormat.ALPHANUMERIC)
    
    cend = RMTS(switch=ModeSelect.DISABLED)

    invoker.add_command(cstart)
    invoker.add_command(cmeasure)
    invoker.add_command(cr1)
    invoker.add_command(cr2)
    invoker.add_command(cr3)
    invoker.add_command(cr4)
    invoker.add_command(cr5)
    invoker.add_command(cr6)
    invoker.add_command(cend)

    await invoker.execute_commands()
