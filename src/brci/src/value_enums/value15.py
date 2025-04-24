from enum import Enum
from typing import Optional

from .value import *
from ..utils import convert_color, convert_len
from ..constants import ColorSpace


class Value15(Value):

    @staticmethod
    def length(*args: int | float, unit: float | int = Units.METER) -> float | list[float]:
        return convert_len(args, unit, Units.UE_UNIT)

    @staticmethod
    def size(*args: int | float, unit: float | int = Units.METER) -> float | list[float]:
        return Value15.length(*args, unit=unit)

    @staticmethod
    def metadata_size(*args: int | float, unit: float | int = Units.METER) -> float | list[float]:
        return Value15.length(*args, unit=unit)

    @staticmethod
    def distance(*args: int | float, unit: float | int = Units.METER) -> float | list[float]:
        return Value15.length(*args, unit=unit)

    @staticmethod
    def position(*args: int | float, unit: float | int = Units.METER) -> float | list[float]:
        return Value15.length(*args, unit=unit)

    @staticmethod
    def sensor_distance(*args: int | float, unit: float | int = Units.METER) -> float | list[float]:
        return convert_len(args, unit, Units.METER)

    @staticmethod
    def from_rgb(r: int, g: int, b: int, a: Optional[int] = None):
        return [r, g, b, 255 if a is None else a]  # Faster, easier

    @staticmethod
    def from_hsv(h: float, s: float, v: float, a: Optional[float] = None):
        return convert_color([h, s, v, 100 if a is None else a], ColorSpace.HSV, ColorSpace.RGB,
                             maximum=[360, 100, 100, 100], new_maximum=255, return_int=True)

    @staticmethod
    def from_hsv_machine(h: float, s: float, v: float, a: Optional[float] = None):
        return convert_color([h, s, v, 1 if a is None else a], ColorSpace.HSV, ColorSpace.RGB,
                             maximum=1, new_maximum=255, return_int=True)

    @staticmethod
    def from_hsl(h: float, s: float, l: float, a: Optional[float] = None):
        return convert_color([h, s, l, 100 if a is None else a], ColorSpace.HSL, ColorSpace.RGB,
                             maximum=[360, 100, 100, 100], new_maximum=255, return_int=True)

    @staticmethod
    def from_hsl_machine(h: float, s: float, l: float, a: Optional[float] = None):
        return convert_color([h, s, l, 1 if a is None else a], ColorSpace.HSL, ColorSpace.RGB,
                             maximum=1, new_maximum=255, return_int=True)

    @staticmethod
    def from_cmyk(c: float, m: float, y: float, k: float, a: Optional[float] = None):
        return convert_color([c, m, y, k, 100 if a is None else a], ColorSpace.CMYK, ColorSpace.RGB,
                             maximum=[100, 100, 100, 100, 100], new_maximum=255, return_int=True)

    @staticmethod
    def from_cmyk_machine(c: float, m: float, y: float, k: float, a: Optional[float] = None):
        return convert_color([c, m, y, k, 1 if a is None else a], ColorSpace.CMYK, ColorSpace.RGB,
                             maximum=1, new_maximum=255, return_int=True)

    @staticmethod
    def from_oklab(l: float, a: float, b: float, alpha: Optional[float] = None):
        return convert_color([l, a, b, 1 if alpha is None else alpha], ColorSpace.OKLAB, ColorSpace.RGB,
                             maximum=1, new_maximum=255, return_int=True)

    @staticmethod
    def from_oklch(l: float, c: float, h: float, a: Optional[float] = None):
        return convert_color([l, c, h, 1 if a is None else a], ColorSpace.OKLCH, ColorSpace.RGB,
                             maximum=1, new_maximum=255, return_int=True)

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
        TARGET_SEEKING = 'TargetSeeking'
        GUIDED = 'Guided'

    class CouplingMode(Enum):
        DEFAULT = 'Default'
        STATIC = 'Static'

    class ExhaustEffect(Enum):
        SMOKE = 'Smoke'
        TRAIL = 'Trail'

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
        CONSTANT_VALUE = ALWAYS_ON = 'AlwaysOn'
        OUTPUT_CHANNEL = CUSTOM = 'Custom'
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
        TRACTION_PLATE = CHANNELLED_ALU = 'ChannelledAlu'
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
        OLD_WOOD = ROUGH_WOOD = 'RoughWood'
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
        A1 = NONE = DEFAULT = 'Default'
        A2 = ARMY = 'C_Army'
        A3 = ARMY_DIGITAL = 'C_ArmyDigital'
        B1 = AUTUMN = 'C_Autumn'
        B2 = BERLIN_2 = 'C_Berlin_2'
        B3 = BERLIN = 'C_Berlin'
        C1 = BERLIN_DIGITAL = 'C_Berlin_Digital'
        C2 = CRISTAL_CONTRAST = 'C_CristalContrast'
        C3 = CRISTAL_RED = 'C_Cristal_Red'
        D1 = DARK = 'C_Dark'
        D2 = DESERT_2 = 'C_Desert_2'
        D3 = DESERT = 'C_Desert'
        E1 = DESERT_DIGITAL = 'C_Desert_Digital'
        E2 = FLECKTARN = 'C_Flecktarn'
        E3 = HEAT = 'C_Heat'
        F1 = NAVY = 'C_Navy'
        F2 = SHARP = 'C_Sharp'
        F3 = SKY = 'C_Sky'
        G1 = SWEDEN = 'C_Sweden'
        G2 = SWIRL = 'C_Swirl'
        G3 = TIGER = 'C_Tiger'
        H1 = URBAN = 'C_Urban'
        H2 = YELLOW = 'C_Yellow'
        H3 = BURNT = 'P_Burnt'
        I1 = FIRE = 'P_Fire'
        I2 = HEXAGON = 'P_Hexagon'
        I3 = SWIRL_ARABICA = 'P_SwirlArabica'
        J1 = WARNING = 'P_Warning'
        J2 = WARNING_RED = 'P_Warning_Red'
        J3 = YELLOW_CIRCLES = 'P_YellowCircles'

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
        DISTANCE_OF_HEAT_SEEKER = 'SeekingProjectileDistance'
        DELTA_TIME = 'DeltaTime'
        FRAMERATE = 'Framerate'
        TIME_OF_DAY = 'TimeOfDay'
        WIND_SPEED = 'WindSpeed'
        WIND_DIRECTION = 'WindDirection'

    class SirenType(Enum):
        CAR = 'Car'
        US_SIREN = 'EmsUS'
        GERMAN_FIRE_DEPARTMENT = 'FireDeptGerman'
        GERMAN_POLICE = 'PoliceGerman'
        TRUCK = 'TruckHorn'

    class SpinnerShape(Enum):
        SQUARE = 'Square'
        TRIANGLE_IN = 'TriangleIn'
        TRIANGLE_OUT = 'TriangleOut'
        ISOSCELES_TRIANGLE_IN = 'IsoscelesTriangleIn'
        ISOSCELES_TRIANGLE_OUT = 'IsoscelesTriangleOut'
        ISOSCELES_TRIANGLE_UP = 'IsoscelesTriangleUp'
        CIRCLE = 'Circle'
        HALF_CIRCLE_IN = 'HalfCircleIn'
        HALF_CIRCLE_OUT = 'HalfCircleOut'
        HALF_CIRCLE_UP = 'HalfCircleUp'
        QUARTER_CIRCLE_IN = 'QuarterCircleIn'
        QUARTER_CIRCLE_OUT = 'QuarterCircleOut'
        DIAMOND = 'Diamond'

    class TraceMask(Enum):
        ALL = 'All'
        STATIC = 'Static'
        VEHICLE = 'Vehicles'
        OTHER_VEHICLE = 'OtherVehicles'
        PLAYER = 'Pawn'
        WATER = 'Water'