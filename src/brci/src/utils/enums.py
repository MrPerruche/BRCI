from enum import Enum



class Value:

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
        # TODO



    class LightDirection(Enum):
        pass

    class Material(Enum):
        pass

    class Operation(Enum):
        pass

    class Pattern(Enum):
        pass

    class SensorType(Enum):
        pass

    class SirenType(Enum):
        pass

    class TraceMask(Enum):
        pass
