from enum import Enum
from typing import Final
import numpy as np

BRCI_VERSION: Final[str] = "4.23.0"  # Modify in pyproject.toml too!

VALID_DRIVER_SEATS: Final[set[str]] = {'Seat_2x2x7s', 'Seat_3x2x2', 'Seat_5x2x1s'}

class Visibility(Enum):
    PUBLIC = 0
    FRIENDS = 1
    PRIVATE = 2
    HIDDEN = 3

class ColorSpace(Enum):

    """
    ColorSpace is an enum to select which color space you're dealing with for the color-related property utils.
    You may use .value to get the number of values expected.
    """

    RGB = 1
    HSV = 2
    HSL = 3
    CMYK = 4
    # OKLAB = 5
    # OKLCH = 6

    @staticmethod
    def get_len_of(elem):
        match elem:
            case ColorSpace.RGB:
                return 3
            case ColorSpace.HSV:
                return 3
            case ColorSpace.HSL:
                return 3
            case ColorSpace.CMYK:
                return 4
            # case ColorSpace.OKLAB:
            #     return 3
            # case ColorSpace.OKLCH:
            #     return 3


class Connection(Enum):

    """
    Connection is an enum to select which connection type you're dealing with for the connection-related property utils.
    You may use .value to get the number of values expected.
    """

    NONE = 0
    DEFAULT = 1
    HALF = 2
    THIRD = 3

    @staticmethod
    def from_int(i):

        """
        Converts an integer to a Connection enum.

        Arguments:
            i (int): Integer to convert.

        Returns:
            Connection: Connection enum or None if invalid.
        """
        if isinstance(i, Connection):
            return i
        match i:
            case 0:
                return Connection.NONE
            case 1:
                return Connection.DEFAULT
            case 2:
                return Connection.HALF
            case 3:
                return Connection.THIRD


class Units:

    """
    Units class for BRCI-D.

    Variables:
        UE_UNIT (Final[float]): Length unit used in Unreal Engine. (0.01m)
        THIRD, STUD, SUB_UNIT (Final[float]): Length of a third of a brick (0.1m)
        BRICK, UNIT (Final[float]): Length of a brick (0.3m)

        QUETTA (float): Metric prefix adopted in 2022. (×10^30)
        RONNA (float): Metric prefix adopted in 2022. (×10^27)
        YOTTA (float): Metric prefix adopted in 1991. (×10^24)
        ZETTA (float): Metric prefix adopted in 1991. (×10^21)
        EXA (float): Metric prefix adopted in 1975. (×10^18)
        PETA (float): Metric prefix adopted in 1975. (×10^15)
        TERA (float): Metric prefix adopted in 1960. (×10^12)
        GIGA (float): Metric prefix adopted in 1960. (×10^9)
        MEGA (float): Metric prefix adopted in 1873. (×10^6)
        KILO (float): Metric prefix adopted in 1795. (×10^3)
        HECTO (float): Metric prefix adopted in 1795. (×10^2)
        DECA (float): Metric prefix adopted in 1795. (×10^1)
        DECI (float): Metric prefix adopted in 1795. (×10^-1)
        CENTI (float): Metric prefix adopted in 1795. (×10^-2)
        MILLI (float): Metric prefix adopted in 1795. (×10^-3)
        MICRO (float): Metric prefix adopted in 1873. (×10^-6)
        NANO (float): Metric prefix adopted in 1960. (×10^-9)
        PICO (float): Metric prefix adopted in 1960. (×10^-12)
        FEMTO (float): Metric prefix adopted in 1964. (×10^-15)
        ATTO (float): Metric prefix adopted in 1964. (×10^-18)
        ZEPTO (float): Metric prefix adopted in 1991. (×10^-21)
        YOCTO (float): Metric prefix adopted in 1991. (×10^-24)
        RONTO (float): Metric prefix adopted in 2022. (×10^-27)
        QUECTO (float): Metric prefix adopted in 2022. (×10^-30)

        KILOMETER, KM (float): A thousand meters. (1_000m)
        HECTOMETER, HM (float): A hundred meters. (100m)
        DECAMETER, DAM (float): Ten meters. (10m)
        METER, M (float): Defined as the distance light travels in 1/299_792_458 of a second. (1m)
        DECIMETER, DM (float): A tenth of a meter. (0.1m)
        CENTIMETER, CM (float): A centimeter. (0.01m)
        MILLIMETER, MM (float): A millimeter. (0.001m)
        MICROMETER, UM (float): A micrometer. (0.000_001m)

        LEAGUE, LEA (float): (4_828.032m)
        NAUTICAL_MILE, NMI (float): (1_852m)
        MILE, MI (float): (1_609.344m)
        FURLONG, FUR (float): (201.168m)
        CABLE (float): (185.2m)
        CHAIN, CH (float): (20.116_8m)
        ROD, POLE, PERCH (float): (5.029_2m)
        FATHOM, FTH (float): (1.852m)
        YARD, YD (float): (0.914_4m)
        FOOT, FEET, FT (float): (0.304_8m)
        LINK (float): (0.201_168m)
        BANANA (float): (0.152_4m)
        HAND, HH (float): (0.101_6m)
        INCH, IN (float): (0.025_4m)
        BARLEYCORN (float): (0.008_466_666_6...m)
        FRENCH_PICA, CICERO (float): (0.004_511_658_1m)
        AMERICAN_PICA (float): (0.004_217_416m)
        COMPUTER_PICA, PICA (float): (0.004_233_333_3...m)
        LINE, L (float): (0.002_166_666_6...m)
        THOU, MIL, TH (float): (0.000_025_4m)
        TWIP (float): (0.000_017_638_9m)

        PARSEC, PC (30_856_775_814_913_673m)
        LIGHT_YEAR, LY (9_460_730_472_580_800m)
        LIGHT_DAY, LD (259_020_683_712_000m)
        LIGHT_HOUR, LH (10_792_528_488_000m)
        ASTRONOMICAL_UNIT, AU (149_597_870_700m)
        LIGHT_MINUTE, LM (179_875_474_800m)
        LIGHT_SECOND, LS (299_792_458m)
        LIGHT_MILLISECOND, LMS (299_792.458m)
        LIGHT_MICROSECOND, LUS (299.792_458m)
        LIGHT_NANOSECOND, LNS (0.299_792_458m)
        LIGHT_PICOSECOND, LPS (0.000_299_792_458m)
    """

    # Metric Prefixes
    QUETTA: Final[float] = 1e30
    RONNA: Final[float] = 1e27
    YOTTA: Final[float] = 1e24
    ZETTA: Final[float] = 1e21
    EXA: Final[float] = 1e18
    PETA: Final[float] = 1e15
    TERA: Final[float] = 1e12
    GIGA: Final[float] = 1e9
    MEGA: Final[float] = 1e6
    KILO: Final[float] = 1e3
    HECTO: Final[float] = 100
    DECA: Final[float] = 10
    DECI: Final[float] = 0.1
    CENTI: Final[float] = 0.01
    MILLI: Final[float] = 1e-3
    MICRO: Final[float] = 1e-6
    NANO: Final[float] = 1e-9
    PICO: Final[float] = 1e-12
    FEMTO: Final[float] = 1e-15
    ATTO: Final[float] = 1e-18
    ZEPTO: Final[float] = 1e-21
    YOCTO: Final[float] = 1e-24
    RONTO: Final[float] = 1e-27
    QUECTO: Final[float] = 1e-30


    # Brick rigs & Unreal Engine
    UE_UNIT: Final[float] = 0.01
    THIRD: Final[float] = 0.1
    SUB_UNIT = STUD = THIRD
    BRICK: Final[float] = 0.3
    UNIT = BRICK

    # Metric & SI-Related
    KILOMETER: Final[float] = 1_000.0
    KM = KILOMETER  # Alias
    HECTOMETER: Final[float] = 100.0
    HM = HECTOMETER  # Alias
    DECAMETER: Final[float] = 10.0
    DAM = DECAMETER  # Alias
    METER: Final[float] = 1.0
    M = METER  # Alias
    DECIMETER: Final[float] = 0.1
    DM = DECIMETER  # Alias
    CENTIMETER: Final[float] = 0.01
    CM = CENTIMETER  # Alias
    MILLIMETER: Final[float] = 0.001
    MM = MILLIMETER  # Alias
    MICROMETER: Final[float] = 0.000001
    UM = MICROMETER  # Alias

    # Imperial
    LEAGUE: Final[float] = 4828.032
    LEA = LEAGUE  # Alias
    NAUTICAL_MILE: Final[float] = 1_852
    NMI = NAUTICAL_MILE  # Alias
    MILE: Final[float] = 1_609.344
    MI = MILE  # Alias
    FURLONG: Final[float] = 201.168
    FUR = FURLONG  # Alias
    CABLE: Final[float] = 185.2
    CHAIN: Final[float] = 20.1168
    CH = CHAIN  # Alias
    ROD: Final[float] = 5.0292
    PERCH = POLE = ROD  # Alias
    FATHOM = 1.852
    FTH = FATHOM  # Alias
    YARD: Final[float] = 0.9144
    YD = YARD  # Alias
    FOOT: Final[float] = 0.3048
    FT = FEET = FOOT  # Alias
    LINK: Final[float] = 0.201168
    BANANA: Final[float] = 0.0254 * 6
    HAND: Final[float] = 0.1016
    HH = HAND  # Alias
    INCH: Final[float] = 0.0254
    IN = INCH  # Alias
    BARLEYCORN: Final[float] = INCH / 3
    FRENCH_PICA: Final[float] = 0.0045116581
    CICERO = FRENCH_PICA  # Alias
    AMERICAN_PICA: Final[float] = INCH * 400 / 2409
    COMPUTER_PICA: Final[float] = INCH / 6
    PICA = COMPUTER_PICA  # Alias
    LINE: Final[float] = INCH / 12
    L = LINE  # Alias
    THOU: Final[float] = INCH / 1_000
    MIL = TH = THOU  # Alias
    TWIP: Final[float] = 0.0000176389

    # Astronomical (length)
    PARSEC: Final[float] = 3.085_677_581_4e16
    PC = PARSEC  # Alias
    LIGHT_YEAR: Final[float] = 9_460_730_472_580_800.0
    LY = LIGHT_YEAR  # Alias
    LIGHT_DAY: Final[float] = 25_902_068_371_200.0
    LD = LIGHT_DAY  # Alias
    LIGHT_HOUR: Final[float] = LIGHT_DAY / 24
    LH = LIGHT_HOUR  # Alias
    ASTRONOMICAL_UNIT: Final[float] = 149_597_870_700.0
    AU = ASTRONOMICAL_UNIT  # Alias
    LIGHT_MINUTE: Final[float] = LIGHT_HOUR / 60
    LM = LIGHT_MINUTE  # Alias
    LIGHT_SECOND: Final[float] = LIGHT_MINUTE / 60
    LS = LIGHT_SECOND  # Alias
    LIGHT_MILLISECOND: Final[float] = LIGHT_SECOND / 1000
    LMS = LIGHT_MILLISECOND  # Alias
    LIGHT_MICROSECOND: Final[float] = LIGHT_MILLISECOND / 1000
    LUS = LIGHT_MICROSECOND  # Alias
    LIGHT_NANOSECOND: Final[float] = LIGHT_MICROSECOND / 1000
    LNS = LIGHT_NANOSECOND  # Alias
    LIGHT_PICOSECOND: Final[float] = LIGHT_NANOSECOND / 1000
    LPS = LIGHT_PICOSECOND  # Alias


class Limits:

    """
    Class for holding notable (mostly integer and floating-point) limits.

    Variables:
        U2_MAX (int): Maximum unsigned 2-bit integer (3)
        U8_MAX (int): Maximum unsigned 8-bit integer (255)
        U16_MAX (int): Maximum unsigned 16-bit integer (65535)
        U32_MAX (int): Maximum unsigned 32-bit integer (4294967295)
        U64_MAX (int): Maximum unsigned 64-bit integer (18446744073709551615)

        I2_MAX (int): Maximum signed 2-bit integer (1)
        I8_MAX (int): Maximum signed 8-bit integer (127)
        I16_MAX (int): Maximum signed 16-bit integer (32767)
        I32_MAX (int): Maximum signed 32-bit integer (2147483647)
        I64_MAX (int): Maximum signed 64-bit integer (9223372036854775807)

        U2_MIN (int): Minimum unsigned 2-bit integer (0)
        U8_MIN (int): Minimum unsigned 8-bit integer (0)
        U16_MIN (int): Minimum unsigned 16-bit integer (0)
        U32_MIN (int): Minimum unsigned 32-bit integer (0)
        U64_MIN (int): Minimum unsigned 64-bit integer (0)

        I2_MIN (int): Minimum signed 2-bit integer (-2)
        I8_MIN (int): Minimum signed 8-bit integer (-128)
        I16_MIN (int): Minimum signed 16-bit integer (-32768)
        I32_MIN (int): Minimum signed 32-bit integer (-2147483648)
        I64_MIN (int): Minimum signed 64-bit integer (-9223372036854775808)

        FP32_MAX (float): Maximum 32-bit floating-point number (3.402823466e+38)
        FP64_MAX (float): Maximum 64-bit floating-point number (1.7976931348623157e+308)

        FP32_MIN (float): Minimum 32-bit floating-point number (-3.402823466e+38)
        FP64_MIN (float): Minimum 64-bit floating-point number (-1.7976931348623157e+308)

        BR_BRICK_LIMIT (int): Maximum number of bricks (50000)
    """

    # Integer limits
    U2_MAX: Final[int] = 3
    U8_MAX: Final[int] = np.iinfo(np.uint8).max
    U16_MAX: Final[int] = np.iinfo(np.uint16).max
    U32_MAX: Final[int] = np.iinfo(np.uint32).max
    U64_MAX: Final[int] = np.iinfo(np.uint64).max

    I2_MAX = 1
    I8_MAX: Final[int] = np.iinfo(np.int8).max
    I16_MAX: Final[int] = np.iinfo(np.int16).max
    I32_MAX: Final[int] = np.iinfo(np.int32).max
    I64_MAX: Final[int] = np.iinfo(np.int64).max

    U2_MIN: Final[int] = 0
    U8_MIN: Final[int] = 0
    U16_MIN: Final[int] = 0
    U32_MIN: Final[int] = 0
    U64_MIN: Final[int] = 0

    I2_MIN: Final[int] = -2
    I8_MIN: Final[int] = np.iinfo(np.int8).min
    I16_MIN: Final[int] = np.iinfo(np.int16).min
    I32_MIN: Final[int] = np.iinfo(np.int32).min
    I64_MIN: Final[int] = np.iinfo(np.int64).min

    # Floating-point limits
    F32_MAX: Final[int] = np.finfo(np.float32).max
    F64_MAX: Final[int] = np.finfo(np.float64).max

    F32_MIN: Final[int] = np.finfo(np.float32).min
    F64_MIN: Final[int] = np.finfo(np.float64).min

    BR_BRICK_LIMIT: Final[int] = 50000