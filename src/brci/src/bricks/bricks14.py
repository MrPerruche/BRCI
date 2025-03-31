from .bricks_utils import _add_mk
from copy import deepcopy
from typing import Any, Final, Type

from ..binary_types import BinaryType, BinaryTypes

"""
    '.InputAxis': 'str8',
    '.SourceBricks': 'list[brick_id]',
    '.Value': 'float',
"""


# All different properties and their type
property_types14: dict[str, Type[BinaryType]] = {
    'ActuatorMode': BinaryTypes.StringOrEnum,
    'AmmoType': BinaryTypes.StringOrEnum,
    'AutoHoverInputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'AutoHoverInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'AutoHoverInputChannel.Value': BinaryTypes.Float32,
    'bAccumulated': BinaryTypes.Boolean,
    'bAccumulateInput': BinaryTypes.Boolean,
    'bCanDisableSteering': BinaryTypes.Boolean,
    'bCanInvertSteering': BinaryTypes.Boolean,
    'bDriven': BinaryTypes.Boolean,
    'bGenerateLift': BinaryTypes.Boolean,
    'bHasBrake': BinaryTypes.Boolean,
    'bHasHandBrake': BinaryTypes.Boolean,
    'bInvertDrive': BinaryTypes.Boolean,
    'bInvertTankSteering': BinaryTypes.Boolean,
    'BrakeStrength': BinaryTypes.Float32,
    'bReturnToZero': BinaryTypes.Boolean,
    'BrakeInputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'BrakeInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'BrakeInputChannel.Value': BinaryTypes.Float32,
    'BrickColor': BinaryTypes.List4_UInteger8,
    'BrickMaterial': BinaryTypes.StringOrEnum,
    'BrickPattern': BinaryTypes.StringOrEnum,
    'BrickSize': BinaryTypes.List3_Float32,
    'Brightness': BinaryTypes.Float32,
    'bTankDrive': BinaryTypes.Boolean,
    'ConnectorSpacing': BinaryTypes.ConnectorSpacingLike,
    'CouplingMode': BinaryTypes.StringOrEnum,
    'DisplayColor': BinaryTypes.List3_UInteger8,
    'EnabledInputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'EnabledInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'EnabledInputChannel.Value': BinaryTypes.Float32,
    'ExitLocation': BinaryTypes.List3_Float32,
    'FlashSequence': BinaryTypes.StringOrEnum,
    'Font': BinaryTypes.StringOrEnum,
    'FontSize': BinaryTypes.Float32,
    'FuelType': BinaryTypes.StringOrEnum,
    'GearRatioScale': BinaryTypes.Float32,
    'HornPitch': BinaryTypes.Float32,
    'IdlerWheels': BinaryTypes.List_BrickID,
    'Image': BinaryTypes.StringOrEnum,
    'ImageColor': BinaryTypes.List3_UInteger8,
    'InputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'InputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'InputChannel.Value': BinaryTypes.Float32,
    'InputChannelA.InputAxis': BinaryTypes.StringOrEnum,
    'InputChannelA.SourceBricks': BinaryTypes.List_BrickID,
    'InputChannelA.Value': BinaryTypes.Float32,
    'InputChannelB.InputAxis': BinaryTypes.StringOrEnum,
    'InputChannelB.SourceBricks': BinaryTypes.List_BrickID,
    'InputChannelB.Value': BinaryTypes.Float32,
    'InputScale': BinaryTypes.Float32,
    'LightConeAngle': BinaryTypes.Float32,
    'LightDirection': BinaryTypes.StringOrEnum,
    'MaxAngle': BinaryTypes.Float32,
    'MaxLimit': BinaryTypes.Float32,
    'MinAngle': BinaryTypes.Float32,
    'MinLimit': BinaryTypes.Float32,
    'NumFractionalDigits': BinaryTypes.UInteger8,
    'Operation': BinaryTypes.StringOrEnum,
    'OutlineThickness': BinaryTypes.Float32,
    'OutputChannel.MinIn': BinaryTypes.Float32,
    'OutputChannel.MinOut': BinaryTypes.Float32,
    'OutputChannel.MaxIn': BinaryTypes.Float32,
    'OutputChannel.MaxOut': BinaryTypes.Float32,
    'OwningSeat': BinaryTypes.BrickID,
    'PitchInputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'PitchInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'PitchInputChannel.Value': BinaryTypes.Float32,
    'PowerInputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'PowerInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'PowerInputChannel.Value': BinaryTypes.Float32,
    'RollInputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'RollInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'RollInputChannel.Value': BinaryTypes.Float32,
    'SensorType': BinaryTypes.StringOrEnum,
    'SirenType': BinaryTypes.StringOrEnum,
    'SmokeColor': BinaryTypes.List3_UInteger8,
    'SpawnScale': BinaryTypes.Float32,
    'SpeedFactor': BinaryTypes.Float32,
    'SteeringAngle': BinaryTypes.Float32,
    'SteeringInputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'SteeringInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'SteeringInputChannel.Value': BinaryTypes.Float32,
    'SteeringSpeed': BinaryTypes.Float32,
    'SuspensionDamping': BinaryTypes.Float32,
    'SuspensionLength': BinaryTypes.Float32,
    'SuspensionStiffness': BinaryTypes.Float32,
    'SwitchName': BinaryTypes.Text,
    'Text': BinaryTypes.Text,
    'TextColor': BinaryTypes.List3_UInteger8,
    'ThrottleInputChannel.InputAxis': BinaryTypes.StringOrEnum,
    'ThrottleInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'ThrottleInputChannel.Value': BinaryTypes.Float32,
    'TirePressureRatio': BinaryTypes.Float32,
    'TireThickness': BinaryTypes.Float32,
    'TraceMask': BinaryTypes.StringOrEnum,
    'TrackColor': BinaryTypes.List4_UInteger8,
    'WheelDiameter': BinaryTypes.Float32,
    'WheelWidth': BinaryTypes.Float32,
    'WinchSpeed': BinaryTypes.Float32,
    'YawInputChannel.InputAxis': BinaryTypes.StringOrEnum ,
    'YawInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'YawInputChannel.Value': BinaryTypes.Float32
} # {'brick_id', 'list[4*uint8]', 'uint8', 'strany', 'list[brick_id]', 'str8', 'float', 'list[3*float]', 'list[6*uint2]', 'list[3*uint8]', 'bool'}


class BrickSelector14:

    CATEGORIES: Final[dict[str, tuple[str, ...]]] = {
        'Actuators': ('Brick.Actuator',),
        'Aviation': ('Brick.Wing', 'Brick.Propeller', 'Brick.RotorBlade', 'Brick.BladeHolder', 'Brick.Rotor',
                     'Brick.Flap', 'Brick.FuelConsumer.Turbine'),
        'Cameras': ('Brick.Camera', 'Brick.Camera.TargetMarker'),
        'Couplings': ('Brick.Couplings',),
        'Cylinders': ('Brick.Cylinder', 'Brick.Cone', 'Brick.Hemisphere'),
        'Decoration': ('Brick.Handle', 'Brick.Grille', 'Brick.Antenna', 'Brick.Bumper', 'Brick.Door',
                       'Brick.SteeringWheel', 'Brick.Scalable.Image', 'Brick.Scalable.Text'),
        'DefaultBricks': ('Brick',),
        'Fire': ('Brick.Detonator', 'Brick.Pump', 'Brick.Tank', 'Brick.Scalable.Float'),
        'Guns': ('Brick.Barrel', 'Brick.FuelConsumer.Flamethrower', 'Brick.Gun.Launcher', 'Brick.Gun'),
        'InputAndOutput': ('Brick.Sensor', 'Brick.Switch', 'Brick.Math', 'Brick.Scalable.Display'),
        'Lights': ('Brick.Scalable.Light',),
        'Player': ('Brick.RC', 'Brick.Seat', 'Brick.SteeringWheel'),
        'Ramps': ('Brick.Ramp',),
        'Redirectors': ('Brick.Redirector',),
        'Rods': ('Brick.Rod',),
        'Scalables': ('Brick.Scalable',),
        'Thrusters': ('Brick.FuelConsumer.Thruster', 'Brick.Tank'),
        'Uncategorized': ('BRCI.Uncategorized',)
    }

    SUBSETS: Final[dict[str, tuple[str, ...]]] = {
        'BRCI.Uncategorized': [],
        'Brick': [],
        'Brick.Actuator': [],
        'Brick.Antenna': [],
        'Brick.Barrel': [],
        'Brick.BladeHolder': [],
        'Brick.Bumper': [],
        'Brick.Camera': [],
        'Brick.Camera.TargetMarker': [],
        'Brick.Cone': [],
        'Brick.Couplings': [],
        'Brick.Cylinder': [],
        'Brick.Detonator': [],
        'Brick.Door': [],
        'Brick.Flap': [],
        'Brick.FuelConsumer.Flamethrower': [],
        'Brick.FuelConsumer.Thruster': [],
        'Brick.FuelConsumer.Turbine': [],
        'Brick.Grille': [],
        'Brick.Gun': [],
        'Brick.Gun.Launcher': [],
        'Brick.Handle': [],
        'Brick.Hemisphere': [],
        'Brick.Math': [],
        'Brick.Propeller': [],
        'Brick.Pump': [],
        'Brick.RC': [],
        'Brick.Ramp': [],
        'Brick.Redirector': [],
        'Brick.Rod': [],
        'Brick.Rotor': [],
        'Brick.RotorBlade': [],
        'Brick.Scalable': [],
        'Brick.Scalable.Display': [],
        'Brick.Scalable.Float': [],
        'Brick.Scalable.Image': [],
        'Brick.Scalable.Light': [],
        'Brick.Scalable.Text': [],
        'Brick.Seat': [],
        'Brick.Sensor': [],
        'Brick.SteeringWheel': [],
        'Brick.Switch': [],
        'Brick.Tank': [],
        'Brick.Wing': [],
    }

    def get_category(self, category: str):
        pass


    def get_subset(self, subset: str, get_sub_subsets: bool = False):
        pass



# Assign all properties
def default_properties14() -> dict[str, Any]:
    return {'BrickColor': [0, 0, 127, 255].copy(), 'BrickPattern': 'Default', 'BrickMaterial': 'Plastic'}.copy()


# Initialize bricks for later
bricks14: dict[str, Any] = {}

# _add_mk(BrickSelector14.SUBSETS['Brick.Seat'], ())


# ACTUATORS. Last update: 1.7.4

_add_mk(bricks14, ('Actuator_1sx1sx1s_02_Top', 'Actuator_1sx1sx1s_Male', 'Actuator_1sx1sx1s_Top',
        'Actuator_1sx1sx2s_Top', 'Actuator_1x1x1s_Top', 'Actuator_1x1x1_Top', 'Actuator_1x1x3_Top', 'Actuator_1x1x6_Top',
        'Actuator_2x1x1s_02_Top', 'Actuator_2x1x1s_Male', 'Actuator_2x1x1s_Top', 'Actuator_2x2x1s_Angular_Top',
        'Actuator_2x2x1s_Top', 'Actuator_2x2x2_Top', 'Actuator_2x2x15_Top', 'Actuator_4x1x1s_Top', 'Actuator_4x4x1s_Top',
        'Actuator_6x2x1s_Top', 'Actuator_8x8x1_Top', 'Actuator_20x2x1s_Top'),
    default_properties14())

_add_mk(bricks14, ('Actuator_1sx1sx1s_Bottom', 'Actuator_1sx1sx1s_Female', 'Actuator_1sx1sx2s_Bottom',
        'Actuator_1x1sx1s_Bottom', 'Actuator_1x1x1s_Bottom', 'Actuator_1x1x1_Bottom', 'Actuator_1x1x3_Bottom',
        'Actuator_1x1x6_Bottom', 'Actuator_2x1sx1s_Bottom', 'Actuator_2x1x1s_02_Bottom',
        'Actuator_2x1x1s_Bottom', 'Actuator_2x1x1s_Female', 'Actuator_2x2x1s_Angular_Bottom',
        'Actuator_2x2x1s_Bottom', 'Actuator_2x2x2_Bottom', 'Actuator_2x2x15_Bottom', 'Actuator_4x1x1s_Bottom',
        'Actuator_4x4x1s_Bottom', 'Actuator_6x2x1s_Bottom', 'Actuator_8x8x1_Bottom',
        'Actuator_20x2x1s_Bottom'),
    default_properties14() | {
        'ActuatorMode': 'Accumulated',
        'InputChannel.InputAxis': 'Auxiliary',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'SpeedFactor': 1.0,
        'MinLimit': 0.0,
        'MaxLimit': 0.0
    }
)


# AVIATION. Last update: 1.7.4

_add_mk(bricks14, ('BladeHolder_2x1', 'Prop_5x1', 'Prop_10x1', 'Rotor_3x4', 'Rotor_4x8', 'Blade_20x2', 'Blade_26x2'),
    default_properties14()
)

_add_mk(bricks14, ('Wing_2x2x1s', 'Wing_2x2x1s_L', 'Wing_2x2x1s_R', 'WingRounded_2x2x1s', 'Wing_2x3x1s',
        'Wing_2x3x1s_L', 'Wing_2x3x1s_R', 'Wing_2x4x1s_L', 'Wing_2x4x1s_R', 'Wing_3x3x1s', 'Wing_4x8x1s_L',
        'Wing_4x8x1s_R'),
    default_properties14() | {
        'bGenerateLift': True
    }
)

_add_mk(bricks14, ('Flap_1x4x1s', 'Flap_2x8x1s'),
    default_properties14() | {
        'bGenerateLift': True,
        'InputChannel.InputAxis': 'None',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'MinAngle': -22.5,
        'MaxAngle': 22.5,
        'bAccumulateInput': True
    }
)

_add_mk(bricks14, ('Turbine_6x2x2', 'Turbine_8x4x2', 'Turbine_12x8x5'),
    default_properties14() | {
        'PowerInputChannel.InputAxis': 'None',
        'PowerInputChannel.SourceBricks': [],
        'PowerInputChannel.Value': 1.0,
        'AutoHoverInputChannel.InputAxis': 'None',
        'AutoHoverInputChannel.SourceBricks': [],
        'AutoHoverInputChannel.Value': 1.0,
        'ThrottleInputChannel.InputAxis': 'None',
        'ThrottleInputChannel.SourceBricks': [],
        'ThrottleInputChannel.Value': 1.0,
        'PitchInputChannel.InputAxis': 'None',
        'PitchInputChannel.SourceBricks': [],
        'PitchInputChannel.Value': 1.0,
        'YawInputChannel.InputAxis': 'None',
        'YawInputChannel.SourceBricks': [],
        'YawInputChannel.Value': 1.0,
        'RollInputChannel.InputAxis': 'None',
        'RollInputChannel.SourceBricks': [],
        'RollInputChannel.Value': 1.0
    }
)


# BRICKS. Last update: 1.7.4

_add_mk(bricks14, ('Brick_1x1x1s', 'Brick_1x1x1s_Flat', 'Brick_1x1x1', 'Brick_1x1x3', 'Brick_1x1x4',  'Brick_1x1x6',
        'Brick_2x1x1s', 'Brick_1x1x1s_Flat', 'BrickRounded_2x1x1s', 'BrickRounded_2x1x1s_Flat', 'Brick_2x1x1',
        'Brick_2x1x6', 'Brick_2x2x1s', 'Brick_2x2x1s_Flat', 'BrickRoundedCorner_2x2x1s', 'CornerBrick_2x2x1s',
        'Brick_2x2x1', 'CornerBrick_2x2x1', 'Brick_3x1x1s', 'Brick_3x1x1s_Flat', 'BrickRounded_3x1x1s',
        'BrickRounded_3x1x1s_Flat', 'Brick_3x1x1', 'Brick_3x2x1s', 'Brick_3x2x1s_Flat', 'Brick_3x2x1', 'Brick_4x1x1s',
        'Brick_4x1x1s_Flat', 'BrickRounded_4x1x1s',  'BrickRounded_4x1x1s_Flat', 'Brick_4x1x1', 'Brick_4x2x1s',
        'Brick_4x4x1s_Flat', 'Brick_5x1x1s', 'Brick_5x1x1s_Flat', 'BrickRounded_5x1x1s', 'BrickRounded_5x1x1s_Flat',
        'Brick_5x1x1', 'BrickRounded_5x1x1s', 'BrickRounded_5x1x1s_Flat', 'Brick_5x1x1', 'Brick_5x2x1s',
        'Brick_5x2x1s_Flat', 'Brick_5x2x1', 'Brick_6x1x1s', 'Brick_6x1x1s_Flat', 'BrickRounded_6x1x1s',
        'BrickRounded_6x1x1s_Flat', 'Brick_6x1x1', 'Brick_6x2x1s', 'Brick_6x2x1s_Flat', 'Brick_6x2x1', 'Weight_6x2x3',
        'Brick_6x4x1s', 'Brick_6x4x1s_Flat', 'Brick_6x6x1s', 'Brick_6x6x1s_Flat', 'Brick_8x1x1s', 'Brick_8x1x1s_Flat',
        'BrickRounded_8x1x1s', 'BrickRounded_8x1x1s_Flat', 'Brick_8x1x1', 'Brick_8x2x1s', 'Brick_8x2x1s_Flat',
        'Brick_8x2x1', 'Brick_8x4x1s', 'Brick_8x4x1s_Flat', 'Brick_8x6x1s', 'Brick_8x6x1s_Flat', 'Brick_8x8x1s',
        'Brick_8x8x1s_Flat', 'Brick_10x1x1s', 'Brick_10x1x1s', 'Brick_10x1x1', 'Brick_10x2x1s', 'Brick_10x2x1s_Flat',
        'Brick_10x2x1', 'Brick_10x4x1s', 'Brick_10x4x1s_Flat', 'Brick_10x6x1s', 'Brick_10x6x1s_Flat', 'Brick_10x8x1s',
        'Brick_10x8x1s_Flat', 'Brick_12x1x1s', 'Brick_12x1x1', 'Brick_12x6x1s', 'Brick_12x6x1s_Flat', 'Brick_12x8x1s',
        'Brick_12x8x1s_Flat', 'Brick_12x12x1', 'Brick_16x1x1', 'Brick_16x8x1s', 'Brick_16x8x1s_Flat', 'Brick_20x1x1',
        'Brick_24x12x1'),
    default_properties14() | {
        'bGenerateLift': False
    }
)


# CAMERAS. Last update: 1.7.4

_add_mk(bricks14, ('Camera_1sx1sx1s', 'Camera_2x1x1', 'TargetMaker_1x1x1'),
    default_properties14() | {
        'OwningSeat': None
    }
)


# COUPLINGS. Last update: 1.7.4

_add_mk(bricks14, ('Coupling_1sx1sx1s_Front_Female', 'Coupling_1x1x1s_Front_Female', 'Coupling_2x2x1s_Female',
        'Coupling_2x2x1s_Front_Female', 'Coupling_4x1x2s_Top'),
    default_properties14()
)

_add_mk(bricks14, ('Coupling_1sx1sx1s_Front_Male', 'Coupling_1x1x1s_Front_Male', 'Coupling_2x2x1s_Front_Male',
        'Coupling_2x2x1s_Male', 'Coupling_4x1x2s_Bottom', 'Coupling_6x2x1s_Male'),
    default_properties14() | {
        'CouplingMode': 'Default',
        'InputChannel.InputAxis': 'None',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)


# DECORATIONS. Last update: 1.7.4

_add_mk(bricks14, ('ImageBrick', 'ImageCylinder'),
    default_properties14() | {
        'bGenerateLift': False,
        'BrickSize': [6.0, 6.0, 1.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0],
        'Image': 'Caution',
        'ImageColor': [0, 0, 255]
    }
)

_add_mk(bricks14, ('Flag_3x1x2',),
    default_properties14() | {
        'bGenerateLift': False,
        'BrickSize': [6.0, 1.0, 6.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'Image': 'Caution',
        'ImageColor': [0, 0, 255]
    }
)

_add_mk(bricks14, ('TextBrick', 'TextCylinder'),
    default_properties14() | {
        'bGenerateLift': False,
        'BrickSize': [6.0, 6.0, 1.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0],
        'Text': 'Text',
        'Font': 'Roboto',
        'FontSize': 60.0,
        'TextColor': [0, 0, 0],
        'OutlineThickness': 0.0
    }
)

_add_mk(bricks14, ('Antenna_1x1x8', 'Antenna_2x1x1s', 'Handle_1x2x4s', 'Handle_4x1x1'),
    default_properties14()
)

_add_mk(bricks14, ('Bumper_4sx6x2', 'Bumper_4sx8x7s', 'Door_L_3x1x1', 'Door_R_3x1x1', 'Door_L_3x1x2',
        'Door_R_3x1x2', 'WindowedDoor_L_3x1x4', 'WindowedDoor_R_3x1x4', 'Grid_2x1x1s_02', 'Grid_2x1x1s',
        'GridZylinder_2x2x1s', 'SteeringWheel_5sx5sx1s', 'SteeringWheel_2x2x1s'),
    default_properties14() | {
        'bGenerateLift': False
    }
)


# FIRE AND WATER. Last update: 1.7.4

_add_mk(bricks14, ('Float',),
    default_properties14() | {
        'BrickSize': [3.0, 3.0, 3.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0]
    }
)

_add_mk(bricks14, ('Detonator_1x1x1s',),
    default_properties14() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)

_add_mk(bricks14, ('PumpZylinder_2x2x2',),
    default_properties14() | {
        'InputChannel.InputAxis': 'None',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)

# GUNS. Last update: 1.7.4

_add_mk(bricks14, ('Barrel_1sx1sx3', 'Barrel_1x1x4', 'Barrel_1x1x4_Flat'),
    default_properties14()
)

_add_mk(bricks14, ('Flamethrower_2x2x2',),
    default_properties14() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)

_add_mk(bricks14, ('Gun_2x1x1', 'Gun_2x2x2_Ballistic', 'Gun_2x2x2', 'Gun_4x2x2'),
    default_properties14() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'AmmoType': 'Standard'
    }
)

_add_mk(bricks14, ('Launcher_2x1sx1s', 'Launcher_4x2sx2s', 'Launcher_6x1x1'),
    default_properties14() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'AmmoType': 'HighExplosive'
    }
)


# INPUT AND OUTPUT. Last update: 1.7.4

_add_mk(bricks14, ('Switch_1sx1sx1s', 'Switch_1x1x1s'),
    default_properties14() | {
        'OutputChannel.MinIn': -1.0,
        'OutputChannel.MaxIn': 1.0,
        'OutputChannel.MinOut': -1.0,
        'OutputChannel.MaxOut': 1.0,
        'InputChannel.InputAxis': 'None',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'bReturnToZero': True,
        'SwitchName': ''
    }
)

_add_mk(bricks14, ('DisplayBrick',),
    default_properties14() | {
        'bGenerateLift': False,
        'BrickSize': [6.0, 3.0, 1.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0],
        'InputChannel.InputAxis': 'Custom',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'NumFractionalDigits': 1,
        'DisplayColor': [0, 204, 128],
    }
)

_add_mk(bricks14, ('Sensor_1sx1sx1s', 'Sensor_1x1x1s'),
    default_properties14() | {
        'OutputChannel.MinIn': -1.0,
        'OutputChannel.MaxIn': 1.0,
        'OutputChannel.MinOut': -1.0,
        'OutputChannel.MaxOut': 1.0,
        'EnabledInputChannel.InputAxis': 'AlwaysOn',
        'EnabledInputChannel.SourceBricks': [],
        'EnabledInputChannel.Value': 1.0,
        'SensorType': 'Speed',
        'TraceMask': 'All',
        'bReturnToZero': False
    }
)

_add_mk(bricks14, ('MathBrick_1sx1sx1s',),
    default_properties14() | {
        'Operation': 'Add',
        'InputChannelA.InputAxis': 'Custom',
        'InputChannelA.SourceBricks': [],
        'InputChannelA.Value': 1.0,
        'InputChannelB.InputAxis': 'AlwaysOn',
        'InputChannelB.SourceBricks': [],
        'InputChannelB.Value': 1.0
    }
)


# LIGHTS. Last update: 1.7.4

_add_mk(bricks14, ('LightBrick', 'LightCone', 'LightConeFlat', 'LightCylinder', 'LightHemisphere', 'LightRamp',
        'LightRampRounded', 'LightRampRoundedN'),
    default_properties14() | {
        'bGenerateLift': False,
        'BrickSize': [3.0, 3.0, 3.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'InputChannel.InputAxis': 'Headlight',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'Brightness': 0.5,
        'FlashSequence': 'None',
        'LightDirection': 'Off',
        'LightConeAngle': 45.0
    }
)


# PLAYER. Last update: 1.7.4

_add_mk(bricks14, ('RemoteController_2x1x1s',),
    default_properties14()
)

_add_mk(bricks14, ('Seat_2x2x7s', 'Seat_3x2x2', 'Seat_5x2x1s'),
    default_properties14() | {
        'ExitLocation': None
    }
)


# RAMPS. Last update: 1.7.4

_add_mk(bricks14, ('CornerRamp_1x1x1', 'CornerRounded_1x1x1', 'RampRoundedN_1x1x1', 'CornerRamp_2x2x1_02',
         'CornerRamp_2x2x1', 'CornerRampN_2x2x1', 'CornerRounded_2x2x1_02', 'CornerRamp_3x2x1_L', 'CornerRamp_3x2x1_R'),
    default_properties14()
)

_add_mk(bricks14, ('Ramp_1x1x2s', 'RampRounded_1x1x2s', 'Ramp_1x1x1', 'RampN_1x1x1', 'RampRounded_1x1x1',
        'Ramp_1x2x2s', 'RampRounded_1x2x2s', 'Ramp_1x2x1', 'RampRounded_1x2x1', 'Ramp_1x4x2s', 'RampRounded_1x4x2s',
        'Ramp_1x4x1', 'RampRounded_1x4x1', 'Ramp_2x1x1_02', 'Ramp_2x1x1', 'RampN_2x1x1', 'RampRounded_2x1x1',
        'Trapezoid_2x1x1', 'Ramp_2x1x2', 'RampN_2x1x2', 'RampRoundedN_2x1x2', 'Ramp_2x1x3', 'RampN_2x1x3', 'Ramp_2x1x4',
        'RampN_2x1x4', 'CornerRounded_2x2x1', 'Ramp_2x2x1', 'RampN_2x2x1', 'Ramp_2x4x1', 'Ramp_2x4x1', 'RampN_2x4x1',
        'RampRounded_3x1x2s', 'DoubleRamp_3x1x1', 'DoubleRampN_3x1x1', 'Ramp_3x1x1_02', 'Ramp_3x1x1', 'RampN_3x1x1',
        'Ramp_3x2x1', 'RampN_3x2x1', 'CornerRamp_3x3x1', 'Ramp_3x4x1', 'RampN_3x4x1', 'RampRounded_4x1x2s',
        'RampRoundedN_4x2x4', 'CornerRamp_4x3x1_L', 'CornerRamp_4x3x1_R', 'CornerRamp_4x4x1', 'CornerRamp_5x3x1_L',
        'CornerRamp_5x3x1_R'),
    default_properties14() | {
        'bGenerateLift': False
    }
)


# REDIRECTORS. Last update: 1.7.4

_add_mk(bricks14, ('Redirector_1x1x0', 'CornerBrick_1x1x1s_Flat', 'Redirector_1x1x1s_02', 'Redirector_1x1x1s',
        'RedirectorZylinder_1x1x1s_02', 'RedirectorZylinder_1x1x1s', 'Redirector_1x1x1_02', 'Redirector_1x1x1_03',
        'Redirector_1x1x1_04', 'Redirector_1x1x1', 'Redirector_4sx1x1', 'Redirector_4sx1x4s', 'Redirector_4sx4x1',
        'Redirector_4sx6x1', 'Redirector_2x1x1s_02', 'Redirector_2x1x1s_03', 'Redirector_2x1x1s_04', 'Redirector_2x1x1s',
        'RedirectorZylinder_2x2x1s_02', 'RedirectorZylinder_2x2x1s', 'Octagon_2x4x4', 'Redirector_3x2x1s_02',
        'Redirector_3x2x1s'),
    default_properties14() | {
        'bGenerateLift': False
    }
)


# RODS. Last update: 1.7.4

_add_mk(bricks14, ('Rod_1x1x1', 'Rod_1x1x2', 'Rod_1x1x3', 'Rod_1x1x4', 'Rod_1x1x6', 'Rod_1x1x8', 'Rod_1x1x10',
        'Rod_1x1x12', 'Rod_1x1x16', 'Rod_1x1x20'),
    default_properties14() | {
        'bGenerateLift': False
    }
)


# ROUND STUFF. Last update: 1.7.4

_add_mk(bricks14, ('Cone_1x1x1', 'Cone_2x2x2', 'Cone_4x4x4', 'Zylinder_1x1x1s', 'Zylinder_1x1x1s_Flat',
        'Zylinder_1x1x1', 'Zylinder_2x2x1s', 'Zylinder_2x2x1s_Flat', 'Zylinder_2x2x1', 'Zylinder_2x2x4',
        'HalfSphere_1x1', 'HalfSphere_2x2x1', 'HalfSphere_4x4x2', 'HalfZylinder_4x2x4'),
    default_properties14() | {
        'bGenerateLift': False
    }
)


# SCALABLE. Last update: 1.7.4

_add_mk(bricks14, ('ScalableBrick', 'ScalableCone', 'ScalableConeRounded', 'ScalableConeFlat','ScalableZylinder', 'ScalableCylinder90R0',
        'ScalableCylinder90R1', 'ScalableHalfCone', 'ScalableHalfCylinder', 'ScalableHemisphere',
        'ScalablePyramid', 'ScalableQuarterSphere', 'ScalableRamp', 'ScalableRampRounded', 'ScalableRampRoundedN',
        'ScalableWedge', 'ScalableWedgeCorner',
        'ScalableCorner', 'ScalableCornerN', 'ScalableCornerRounded', 'ScalableCornerRoundedN',
        'ScalableQuarterCone', 'ScalablePyramidCorner', 'ScalablePyramidCornerRounded'),
    default_properties14() | {
        'bGenerateLift': False,
        'BrickSize': [3.0, 3.0, 3.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3]
    }
)


# THRUSTERS. Last update: 1.7.4

_add_mk(bricks14, ('Thruster_1sx1sx1s', 'Thruster_1x1x1', 'Thruster_1x1x3', 'Thruster_2x2x4'),
    default_properties14() | {
        'InputChannel.InputAxis': 'Throttle',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'InputScale' : 1.0,
        'bAccumulated': False
    }
)


# VEHICLES. Last update: 1.7.4

_add_mk(bricks14, ('ExhaustBrick', 'ExhaustCylinder'),
    default_properties14() | {
        'bGenerateLift': False,
        'BrickSize': [3.0, 3.0, 3.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'InputChannel.InputAxis': 'None',
        'SmokeColor': [0, 0, 255],
        'SpawnScale': 1.0
    }
)

_add_mk(bricks14, ('Axle_1sx1sx1s', 'Axle_1x1x1s_02', 'Axle_1x1x1s', 'Axle_1x2x1s', 'Axle_2x2x1s', 'Axle_2x2x1',
        'LandingGear_2x2x2', 'Axle_2x4x1s', 'Axle_2x6x1s'),
    default_properties14() | {
        'SteeringAngle': 0.0,
        'SteeringSpeed': 1.0,
        'SuspensionLength': 0.0,
        'SuspensionStiffness': 2.0,
        'SuspensionDamping': 1.0,
        'bDriven': True,
        'bInvertDrive': False,
        'bHasBrake': True,
        'bHasHandBrake': True,
        'BrakeStrength': 1.0,
        'SteeringInputChannel.InputAxis': 'Steering',
        'SteeringInputChannel.SourceBricks': [],
        'SteeringInputChannel.Value': 1.0,
        'BrakeInputChannel.InputAxis': 'Brake',
        'BrakeInputChannel.SourceBricks': [],
        'BrakeInputChannel.Value': 1.0,
        'bCanDisableSteering': False,
        'bCanInvertSteering': False
    }
)

_add_mk(bricks14, ('Compressor_4x1x4s', 'Mudguard_2x1sx3', 'Mudguard_2x1x1s', 'Mudguard_2x2x2s', 'Mudguard_4x2x5s'),
    default_properties14() | {
        'bGenerateLift': False
    }
)

_add_mk(bricks14, ('Motor_1x2x5s', 'EMotor_2x2x2', 'Motor_3x2x5s', 'AircraftR4', 'Motor_4x2x5s', 'DragV8',
        'DieselV12'),
    default_properties14() | {
        'ThrottleInputChannel.InputAxis': 'Throttle',
        'ThrottleInputChannel.SourceBricks': [],
        'ThrottleInputChannel.Value': 1.0,
        'GearRatioScale': 1.0,
        'bTankDrive': False
    }
)

_add_mk(bricks14, ('Tank_1x1x1', 'Tank_2x2x1', 'Tank_2x2x4'),
    default_properties14() | {
        'FuelType': 'Petrol'
    }
)

_add_mk(bricks14, ('Wheels_2x2s',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 6.0,
        'WheelWidth': 2.0,
        'TireThickness': 1.2,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('RacingWheel_4x2s',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 9.0,
        'WheelWidth': 2.0,
        'TireThickness': 1.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('Wheel_7sx2',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 7.0,
        'WheelWidth': 3.0,
        'TireThickness': 1.25,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('Wheel_10sx1',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 10.0,
        'WheelWidth': 3.0,
        'TireThickness': 2.2,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('OffroadWheel_3x4s',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 8.2,
        'WheelWidth': 4.0,
        'TireThickness': 1.85,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('RacingWheel_3x4s',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 9.0,
        'WheelWidth': 4.0,
        'TireThickness': 1.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('Wheel_3x4s',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 8.1,
        'WheelWidth': 4.0,
        'TireThickness': 1.8,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('DragWheel_4x2',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 12.0,
        'WheelWidth': 6.0,
        'TireThickness': 3.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('Wheel_4x2',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 12.0,
        'WheelWidth': 6.0,
        'TireThickness': 2.65,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('OffroadWheel_5x2',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 15.0,
        'WheelWidth': 6.0,
        'TireThickness': 4.5,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('Wheel_10x4',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 30.0,
        'WheelWidth': 12.0,
        'TireThickness': 9.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks14, ('IdlerWheel',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 9.0,
        'WheelWidth': 3.0,
    }
)

_add_mk(bricks14, ('SprocketWheel',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 9.0,
        'WheelWidth': 3.0,
        'IdlerWheels': [],
        'TrackColor': [0, 0, 26, 255]
    }
)

_add_mk(bricks14, ('TrainWheel_2x2s',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 6.0,
        'WheelWidth': 2.0,
    }
)

_add_mk(bricks14, ('TrainWheel_3x2s',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 9.0,
        'WheelWidth': 2.0,
    }
)

_add_mk(bricks14, ('TrainWheel_4x2s',),
    default_properties14() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 12.0,
        'WheelWidth': 2.0,
    }
)

_add_mk(bricks14, ('Wheel_1sx1sx1s', 'Wheel_1x1x1'),
    default_properties14()
)


# WINDOWS. Last update: 1.7.4

_add_mk(bricks14, ('Panel_1x2x4', 'Panel_1x4x4', 'Panel_1x6x6', 'Windscreen_2x4x2', 'Windscreen_2x4x3',
        'Windscreen_2x6x2', 'Windscreen_2x6x3', 'Windscreen_2x8x3', 'Windscreen_4x6x3'),
    default_properties14() | {
        'bGenerateLift': False
    }
)


# UNCATEGORIZED. Last update: 1.7.4

_add_mk(bricks14, ('Arch_2x1x2', 'Arch_4x1x2', 'Arch_6x1x1', 'Arch_8x1x8', 'CornerLedge_1x1x1', 'Ledge_1x1x1',
        'Ledge_1x2x1', 'Ledge_1x4x1', 'PlaneTail_10x10x6'),
    default_properties14() | {
        'bGenerateLift': False
    }
)

_add_mk(bricks14, ('DoubleSiren_1x2x1s',),
    default_properties14() | {
        'SirenType': 'Car',
        'HornPitch': 1.0,
        'InputChannel.InputAxis': 'Horn',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)

_add_mk(bricks14, ('Winch_3x2x1',),
    default_properties14() | {
        'InputChannel.InputAxis': 'Auxiliary',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'WinchSpeed': 100.0
    }
)

_add_mk(bricks14, ('FlareGun_1x1x1',),
    default_properties14() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)
