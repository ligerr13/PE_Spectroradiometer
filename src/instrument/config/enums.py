from enum import Enum


class DataMode(Enum):
    MEASUREMENT_CONDITIONS = 0
    SPECTRAL_DATA = 1
    COLORIMETRIC_DATA = 2

class DataFormat(Enum):
    ALPHANUMERIC = 0
    HEXADECIMAL = 1

class DataBlockNumber(Enum):
    MEASUREMENT_CONDITIONS = 1
    COLORIMETRIC_DATA = 0

class SpectralRange(Enum):
    RANGE_380_TO_479 = 1
    RANGE_480_TO_579 = 2
    RANGE_580_TO_679 = 3
    RANGE_680_TO_780 = 4

class ModeSelect(Enum):
    ENABLED = 1
    DISABLED = 0