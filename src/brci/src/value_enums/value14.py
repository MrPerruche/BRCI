from enum import Enum
from typing import Optional

from .value import *
from ..utils import convert_color
from ..constants import ColorSpace


class Value14(Value):

    """
    Will convert a list of integers or floats corresponding to a color from one color space to another.
    Maximum and new_maximum may be "ignored" by some channels if dealing with perceptual color spaces like OKLab or OKLCH.

    Arguments:
        color (list[int | float]): A list of integers or floats (of length depending on the color space) corresponding to the color to convert.
        old_space (ColorSpace): The color space of the color to convert.
        new_space (ColorSpace): The color space to convert the color to.
        return_alpha (Optional[bool]): Whether the output color has an alpha channel. Leave none to determine automatically from the input.
        maximum (float | int | list[float | int]): The maximum value of each color channel.
        new_maximum (Optional[float | int | list[float | int]]): If set, it is the maximum value of each color channel in the new color space.
        return_int (bool): Whether to return the color as integers or floats.
    """

    @staticmethod
    def from_rgb(r: int, g: int, b: int, a: Optional[int] = None):
        return convert_color([r, g, b] + ([a] if a is not None else []), ColorSpace.RGB, ColorSpace.HSV,
                             maximum=255, return_int=True)

    @staticmethod
    def from_hsv(h: float, s: float, v: float, a: Optional[float] = None):
        return convert_color([h, s, v] + ([a] if a is not None else []), ColorSpace.HSV, ColorSpace.HSV,
                             maximum=[360, 100, 100] + ([100] if a is not None else []), new_maximum=255, return_int=True)

    @staticmethod
    def from_hsv_machine(h: float, s: float, v: float, a: Optional[float] = None):
        return convert_color([h, s, v] + ([a] if a is not None else []), ColorSpace.HSV, ColorSpace.HSV,
                             maximum=1, new_maximum=255, return_int=True)

    @staticmethod
    def from_hsl(h: float, s: float, l: float, a: Optional[float] = None):
        return convert_color([h, s, l] + ([a] if a is not None else []), ColorSpace.HSL, ColorSpace.HSV,
                             maximum=[360, 100, 100] + ([100] if a is not None else []), new_maximum=255, return_int=True)

    @staticmethod
    def from_hsl_machine(h: float, s: float, l: float, a: Optional[float] = None):
        return convert_color([h, s, l] + ([a] if a is not None else []), ColorSpace.HSL, ColorSpace.HSV,
                             maximum=1, new_maximum=255, return_int=True)

    @staticmethod
    def from_cmyk(c: float, m: float, y: float, k: float, a: Optional[float] = None):
        return convert_color([c, m, y, k] + ([a] if a is not None else []), ColorSpace.CMYK, ColorSpace.HSV,
                             maximum=100, new_maximum=255, return_int=True)

    @staticmethod
    def from_cmyk_machine(c: float, m: float, y: float, k: float, a: Optional[float] = None):
        return convert_color([c, m, y, k] + ([a] if a is not None else []), ColorSpace.CMYK, ColorSpace.HSV,
                             maximum=1, new_maximum=255, return_int=True)

    @staticmethod
    def from_oklab(l: float, a: float, b: float, alpha: Optional[float] = None):
        return convert_color([l, a, b] + ([alpha] if alpha is not None else []), ColorSpace.OKLAB, ColorSpace.HSV,
                             new_maximum=255, return_int=True)

    @staticmethod
    def from_oklch(l: float, c: float, h: float, a: Optional[float] = None):
        return convert_color([l, c, h] + ([a] if a is not None else []), ColorSpace.OKLCH, ColorSpace.HSV,
                             new_maximum=255, return_int=True)

    class ActuatorMode(Enum):
        ACCUMULATED = 'Accumulated'
        SEEKING = 'Seeking'
        CYCLE = 'Cycle'
        PHYSICS_DRIVEN = 'PhysicsDriven'
        SPRING = 'Spring'
        STATIC = 'Static'

    class AmmoType(Enum):
        STANDARD = 'Standard'
        INCENDIARY = 'Incendiary'
        HIGH_EXPLOSIVE = 'HighExplosive'
        TARGET_SEEKING = 'HeatSeeking'
        GUIDED = 'Guided'

    class CouplingMode(Enum):
        DEFAULT = 'Default'
        STATIC = 'Static'

    class FlashSequence(Enum):
        NONE = 'None'
        BLINKER = 'Blinker_Sequence'
        BLINKER_INVERTED = 'Blinker_Sequence_Inverted'
        DOUBLE_FLASH_INVERTED = 'DoubleFlash_Inverted_Sequence'
        DOUBLE_FLASH = 'DoubleFlash_Sequence'
        RUNNING_LIGHT_1_INVERTED = 'RunningLight_01_Inverted_Sequence'
        RUNNING_LIGHT_1 = 'RunningLight_01_Sequence'
        RUNNING_LIGHT_2_INVERTED = 'RunningLight_02_Inverted_Sequence'
        RUNNING_LIGHT_2 = 'RunningLight_02_Sequence'
        RUNNING_LIGHT_3_INVERTED = 'RunningLight_03_Inverted_Sequence'
        RUNNING_LIGHT_3 = 'RunningLight_03_Sequence'
        RUNNING_LIGHT_4_INVERTED = 'RunningLight_04_Inverted_Sequence'
        RUNNING_LIGHT_4 = 'RunningLight_04_Sequence'
        STROBE = 'Strobe_Sequence'

    class Font(Enum):
        BIG_SHOULDER_STENCIL = 'BigShoulderStencil'
        NOTO_EMOJI = 'NotoEmoji'
        ORBITRON = 'Orbitron'
        PERMANENT_MARKER = 'PermanentMarker'
        ROBOTO = 'Roboto'
        ROBOTO_SERIF = 'RobotoSerif'
        SILKSCREEN = 'Silkscreen'

    class FuelType(Enum):
        C4 = 'C4'
        NITRO = 'Nitro'
        PETROL = 'Petrol'
        ROCKET_FUEL = 'RocketFuel'

    class Image(Enum):
        ARROW = 'Arrow'
        BIOHAZARD = 'Biohazard'
        BRAF = 'BRAF'
        BRICK_RIGS = 'BrickRigs'
        BRICK_RIGS_ARMS = 'BrickRigsArms'
        CAUTION = 'Caution'
        CRIMINALS = 'Criminals'
        CROSSHAIR = 'Crosshair'
        DESERT_WORMS = 'DesertWorms'
        DUMMY = 'Dummy'
        ELECTRICAL_HAZARD = 'ElectricalHazard'
        EXPLOSIVE = 'Explosive'
        FIRE_DEPARTMENT = 'FireDept'
        FIRE_HAZARD = 'FireHazard'
        GAUGE = 'Gauge'
        LIMIT_80 = 'Limit80'
        NO_ENTRANCE = 'NoEntrance'
        ONE_WAY = 'OneWay'
        PHONE = 'Phone'
        POLICE = 'Police'
        RADIOACTIVE = 'Radioactive'
        STAR = 'Star'
        STOP = 'Stop'
        TANK = 'Tank'
        VIRUS = 'Virus'

    class InputAxis(Enum):
        NONE = 'None'
        ALWAYS_ON = 'AlwaysOn'
        CONSTANT_VALUE = ALWAYS_ON
        CUSTOM = 'Custom'
        OUTPUT_CHANNEL = CUSTOM
        STEERING = 'Steering'
        STEERING_ALT = 'SteeringAlt'
        THROTTLE = 'Throttle'
        THROTTLE_ALT = 'ThrottleAlt'
        BRAKE = 'Brake'
        BRAKE_ALT = 'BrakeAlt'
        AUXILIARY = 'Pitch'
        AUXILIARY_ALT = 'PitchAlt'
        PITCH = 'ViewPitch'
        PITCH_ALT = 'ViewPitchAlt'
        YAW = 'ViewYaw'
        YAW_ALT = 'ViewYawAlt'
        HORN = 'Horn'
        DISABLE_STEERING = 'DisableSteering'
        INVERT_STEERING = 'InvertSteering'
        HAND_BRAKE = 'HandBrake'
        OPERATION_MODE = 'OperationMode'
        HEADLIGHT = 'Headlight'
        BEACON = 'Beacon'
        WARNING_LIGHT = 'WarningLight'
        HAZARD_LIGHT = WARNING_LIGHT
        TAILLIGHT = 'Taillight'
        BRAKE_LIGHT = 'BrakeLight'
        REVERSING_LIGHT = 'ReversingLight'
        ACTION_1 = 'Action1'
        ACTION_2 = 'Action2'
        ACTION_3 = 'Action3'
        ACTION_4 = 'Action4'
        ACTION_5 = 'Action5'
        ACTION_6 = 'Action6'
        ACTION_7 = 'Action7'
        ACTION_8 = 'Action8'

    class LightDirection(Enum):
        OFF = 'Off'
        OMNIDIRECTIONAL = 'Omnidirectional'
        X = 'X'
        X_NEG = 'XNeg'
        Y = 'Y'
        Y_NEG = 'YNeg'
        Z = 'Z'
        Z_NEG = 'ZNeg'

    class Material(Enum):
        ALUMINIUM = 'Aluminium'
        BRUSHED_ALU = 'BrushedAlu'
        CARBON = 'Carbon'
        CHANNELLED_ALU = 'ChannelledAlu'
        TRACTION_PLATE = CHANNELLED_ALU
        CHROME = 'Chrome'
        CLOUDY_GLASS = 'CloudyGlass'
        COPPER = 'Copper'
        FOAM = 'Foam'
        GLASS = 'Glass'
        GLOW = 'Glow'
        GOLD = 'Gold'
        LED_MATRIX = 'LEDMatrix'
        OAK = 'Oak'
        PINE = 'Pine'
        PLASTIC = 'Plastic'
        ROUGH_WOOD = 'RoughWood'
        OLD_WOOD = ROUGH_WOOD
        RUBBER = 'Rubber'
        RUSTED_STEEL = 'RustedSteel'
        STEEL = 'Steel'
        TUNGSTEN = 'Tungsten'

    class Operation(Enum):
        ADD = 'Add'
        SUBTRACT = 'Subtract'
        MULTIPLY = 'Multiply'
        DIVIDE = 'Divide'
        MODULO = 'FMod'
        POWER = 'Power'
        GREATER = 'Greater'
        LESS = 'Less'
        MIN = 'Min'
        MAX = 'Max'
        ABS = 'Abs'
        SIGN = 'Sign'
        ROUND = 'Round'
        CEIL = 'Ceil'
        FLOOR = 'Floor'
        SQRT = 'Sqrt'
        SIN_DEG = 'SinDeg'
        SIN_RAD = 'Sin'
        ASIN_DEG = 'AsinDeg'
        ASIN_RAD = 'Asin'
        COS_DEG = 'CosDeg'
        COS_RAD = 'Cos'
        ACOS_DEG = 'AcosDeg'
        ACOS_RAD = 'Acos'
        TAN_DEG = 'TanDeg'
        TAN_RAD = 'Tan'
        ATAN_DEG = 'AtanDeg'
        ATAN_RAD = 'Atan'

    class Pattern(Enum):
        DEFAULT = 'Default'
        A1 = NONE = DEFAULT
        ARMY = 'C_Army'
        A2 = ARMY
        ARMY_DIGITAL = 'C_ArmyDigital'
        A3 = ARMY_DIGITAL
        AUTUMN = 'C_Autumn'
        B1 = AUTUMN
        BERLIN_2 = 'C_Berlin_2'
        B2 = BERLIN_2
        BERLIN = 'C_Berlin'
        B3 = BERLIN
        BERLIN_DIGITAL = 'C_Berlin_Digital'
        C1 = BERLIN_DIGITAL
        CRISTAL_CONTRAST = 'C_CristalContrast'
        C2 = CRISTAL_CONTRAST
        CRISTAL_RED = 'C_Cristal_Red'
        C3 = CRISTAL_RED
        DARK = 'C_Dark'
        D1 = DARK
        DESERT_2 = 'C_Desert_2'
        D2 = DESERT_2
        DESERT = 'C_Desert'
        D3 = DESERT
        DESERT_DIGITAL = 'C_Desert_Digital'
        E1 = DESERT_DIGITAL
        FLECKTARN = 'C_Flecktarn'
        E2 = FLECKTARN
        HEAT = 'C_Heat'
        E3 = HEAT
        NAVY = 'C_Navy'
        F1 = NAVY
        SHARP = 'C_Sharp'
        F2 = SHARP
        SKY = 'C_Sky'
        F3 = SKY
        SWEDEN = 'C_Sweden'
        G1 = SWEDEN
        SWIRL = 'C_Swirl'
        G2 = SWIRL
        TIGER = 'C_Tiger'
        G3 = TIGER
        URBAN = 'C_Urban'
        H1 = URBAN
        YELLOW = 'C_Yellow'
        H2 = YELLOW
        BURNT = 'P_Burnt'
        H3 = BURNT
        FIRE = 'P_Fire'
        I1 = FIRE
        HEXAGON = 'P_Hexagon'
        I2 = HEXAGON
        SWIRL_ARABICA = 'P_SwirlArabica'
        I3 = SWIRL_ARABICA
        WARNING = 'P_Warning'
        J1 = WARNING
        WARNING_RED = 'P_Warning_Red'
        J2 = WARNING_RED
        YELLOW_CIRCLES = 'P_YellowCircles'
        J3 = YELLOW_CIRCLES

    class SensorType(Enum):
        SPEED = 'Speed'
        NORMAL_SPEED = 'NormalSpeed'
        ACCELERATION = 'Acceleration'
        NORMAL_ACCELERATION = 'NormalAcceleration'
        ANGULAR_SPEED = 'AngularSpeed'
        NORMAL_ANGULAR_SPEED = 'NormalAngularSpeed'
        DISTANCE = 'Distance'
        TIME = 'Time'
        PROXIMITY = 'Proximity'
        DISTANCE_TO_GROUND = 'DistanceToGround'
        ALTITUDE = 'Altitude'
        PITCH = 'Pitch'
        YAW = 'Yaw'
        ROLL = 'Roll'
        NUMBER_OF_HEAT_SEEKERS = 'NumSeekingProjectiles'

    class SirenType(Enum):
        CAR = 'Car'
        US_SIREN = 'EmsUS'
        GERMAN_FIRE_DEPARTMENT = 'FireDeptGerman'
        GERMAN_POLICE = 'PoliceGerman'
        TRUCK = 'TruckHorn'

    class TraceMask(Enum):
        ALL = 'All'
        STATIC = 'Static'
        VEHICLE = 'Vehicles'
        OTHER_VEHICLE = 'OtherVehicles'
        PLAYER = 'Pawn'
        WATER = 'Water'