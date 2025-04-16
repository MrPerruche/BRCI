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
property_types15: dict[str, Type[BinaryType]] = {
    'ActuatorMode': BinaryTypes.String,
    'AmmoType': BinaryTypes.String,
    'AutoHoverInputChannel.InputAxis': BinaryTypes.String,
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
    'BrakeInputChannel.InputAxis': BinaryTypes.String,
    'BrakeInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'BrakeInputChannel.Value': BinaryTypes.Float32,
    'BrickColor': BinaryTypes.List4_UInteger8,
    'BrickMaterial': BinaryTypes.String,
    'BrickPattern': BinaryTypes.String,
    'BrickSize': BinaryTypes.List3_Float32,
    'Brightness': BinaryTypes.Float32,
    'bTankDrive': BinaryTypes.Boolean,
    'CameraName': BinaryTypes.Text,
    'ConnectorSpacing': BinaryTypes.ConnectorSpacingLike,
    'CouplingMode': BinaryTypes.String,
    'DisplayColor': BinaryTypes.List4_UInteger8,
    'EnabledInputChannel.InputAxis': BinaryTypes.String,
    'EnabledInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'EnabledInputChannel.Value': BinaryTypes.Float32,
    'ExhaustEffect': BinaryTypes.String,
    'ExitLocation': BinaryTypes.List3_Float32,
    'FlashSequence': BinaryTypes.String,
    'Font': BinaryTypes.String,
    'FontSize': BinaryTypes.Float32,
    'FuelType': BinaryTypes.String,
    'GearRatioScale': BinaryTypes.Float32,
    'HornPitch': BinaryTypes.Float32,
    'IdlerWheels': BinaryTypes.List_BrickID,
    'Image': BinaryTypes.String,
    'ImageColor': BinaryTypes.List4_UInteger8,
    'InputChannel.InputAxis': BinaryTypes.String,
    'InputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'InputChannel.Value': BinaryTypes.Float32,
    'InputChannelA.InputAxis': BinaryTypes.String,
    'InputChannelA.SourceBricks': BinaryTypes.List_BrickID,
    'InputChannelA.Value': BinaryTypes.Float32,
    'InputChannelB.InputAxis': BinaryTypes.String,
    'InputChannelB.SourceBricks': BinaryTypes.List_BrickID,
    'InputChannelB.Value': BinaryTypes.Float32,
    'InputScale': BinaryTypes.Float32,
    'LightConeAngle': BinaryTypes.Float32,
    'LightDirection': BinaryTypes.String,
    'MaxAngle': BinaryTypes.Float32,
    'MaxLimit': BinaryTypes.Float32,
    'MinAngle': BinaryTypes.Float32,
    'MinLimit': BinaryTypes.Float32,
    'NumFractionalDigits': BinaryTypes.UInteger8,
    'Operation': BinaryTypes.String,
    'OutlineThickness': BinaryTypes.Float32,
    'OutputChannel.MinIn': BinaryTypes.Float32,
    'OutputChannel.MinOut': BinaryTypes.Float32,
    'OutputChannel.MaxIn': BinaryTypes.Float32,
    'OutputChannel.MaxOut': BinaryTypes.Float32,
    'OwningSeat': BinaryTypes.BrickID,
    'PitchInputChannel.InputAxis': BinaryTypes.String,
    'PitchInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'PitchInputChannel.Value': BinaryTypes.Float32,
    'PowerInputChannel.InputAxis': BinaryTypes.String,
    'PowerInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'PowerInputChannel.Value': BinaryTypes.Float32,
    'RollInputChannel.InputAxis': BinaryTypes.String,
    'RollInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'RollInputChannel.Value': BinaryTypes.Float32,
    'SeatName': BinaryTypes.Text,
    'SensorType': BinaryTypes.String,
    'SirenType': BinaryTypes.String,
    'SmokeColor': BinaryTypes.List3_UInteger8,
    'SpawnScale': BinaryTypes.Float32,
    'SpeedFactor': BinaryTypes.Float32,
    'SpinnerAngle': BinaryTypes.Float32,
    'SpinnerRadius': BinaryTypes.List2_Float32,
    'SpinnerShape': BinaryTypes.String,
    'SpinnerSize': BinaryTypes.List2_Float32,
    'SteeringAngle': BinaryTypes.Float32,
    'SteeringInputChannel.InputAxis': BinaryTypes.String,
    'SteeringInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'SteeringInputChannel.Value': BinaryTypes.Float32,
    'SteeringSpeed': BinaryTypes.Float32,
    'SuspensionDamping': BinaryTypes.Float32,
    'SuspensionLength': BinaryTypes.Float32,
    'SuspensionStiffness': BinaryTypes.Float32,
    'SwitchName': BinaryTypes.Text,
    'Text': BinaryTypes.Text,
    'TextColor': BinaryTypes.List3_UInteger8,
    'ThrottleInputChannel.InputAxis': BinaryTypes.String,
    'ThrottleInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'ThrottleInputChannel.Value': BinaryTypes.Float32,
    'TirePressureRatio': BinaryTypes.Float32,
    'TireThickness': BinaryTypes.Float32,
    'TraceMask': BinaryTypes.String,
    'TrackColor': BinaryTypes.List4_UInteger8,
    'WheelDiameter': BinaryTypes.Float32,
    'WheelWidth': BinaryTypes.Float32,
    'WinchSpeed': BinaryTypes.Float32,
    'YawInputChannel.InputAxis': BinaryTypes.String ,
    'YawInputChannel.SourceBricks': BinaryTypes.List_BrickID,
    'YawInputChannel.Value': BinaryTypes.Float32
} # {'brick_id', 'list[4*uint8]', 'uint8', 'strany', 'list[brick_id]', 'str8', 'float', 'list[3*float]', 'list[6*uint2]', 'list[3*uint8]', 'bool'}



# Assign all properties
def default_properties15() -> dict[str, Any]:
    return {'BrickColor': [0xBC, 0xBC, 0xBC, 0xFF].copy(), 'BrickPattern': 'Default', 'BrickMaterial': 'Plastic'}.copy()


# Initialize bricks for later
bricks15: dict[str, Any] = {}


_add_mk(bricks15, ('Actuator_1sx1sx1s_02_Top', 'Actuator_1sx1sx1s_Male', 'Actuator_1sx1sx1s_Top',
        'Actuator_1sx1sx2s_Top', 'Actuator_1x1x1s_Top', 'Actuator_1x1x1_Top', 'Actuator_1x1x3_Top', 'Actuator_1x1x6_Top',
        'Actuator_2x1x1s_02_Top', 'Actuator_2x1x1s_Male', 'Actuator_2x1x1s_Top', 'Actuator_2x2x1s_Angular_Top',
        'Actuator_2x2x1s_Top', 'Actuator_2x2x2_Top', 'Actuator_2x2x15_Top', 'Actuator_4x1x1s_Top', 'Actuator_4x4x1s_Top',
        'Actuator_6x2x1s_Top', 'Actuator_8x8x1_Top', 'Actuator_20x2x1s_Top'),
    default_properties15())

_add_mk(bricks15, ('Actuator_1sx1sx1s_Bottom', 'Actuator_1sx1sx1s_Female', 'Actuator_1sx1sx2s_Bottom',
        'Actuator_1x1sx1s_Bottom', 'Actuator_1x1x1s_Bottom', 'Actuator_1x1x1_Bottom', 'Actuator_1x1x3_Bottom',
        'Actuator_1x1x6_Bottom', 'Actuator_2x1sx1s_Bottom', 'Actuator_2x1x1s_02_Bottom',
        'Actuator_2x1x1s_Bottom', 'Actuator_2x1x1s_Female', 'Actuator_2x2x1s_Angular_Bottom',
        'Actuator_2x2x1s_Bottom', 'Actuator_2x2x2_Bottom', 'Actuator_2x2x15_Bottom', 'Actuator_4x1x1s_Bottom',
        'Actuator_4x4x1s_Bottom', 'Actuator_6x2x1s_Bottom', 'Actuator_8x8x1_Bottom',
        'Actuator_20x2x1s_Bottom'),
    default_properties15() | {
        'ActuatorMode': 'Accumulated',
        'InputChannel.InputAxis': 'Auxiliary',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'SpeedFactor': 1.0,
        'MinLimit': 0.0,
        'MaxLimit': 0.0
    }
)


# AVIATION. Last update: 1.8.0

_add_mk(bricks15, ('BladeHolder_2x1', 'Prop_5x1', 'Prop_10x1', 'Rotor_3x4', 'Rotor_4x8', 'Blade_20x2', 'Blade_26x2'),
    default_properties15()
)

_add_mk(bricks15, ('Wing_2x2x1s', 'Wing_2x2x1s_L', 'Wing_2x2x1s_R', 'WingRounded_2x2x1s', 'Wing_2x3x1s',
        'Wing_2x3x1s_L', 'Wing_2x3x1s_R', 'Wing_2x4x1s_L', 'Wing_2x4x1s_R', 'Wing_3x3x1s', 'Wing_4x8x1s_L',
        'Wing_4x8x1s_R'),
    default_properties15() | {
        'bGenerateLift': True
    }
)

_add_mk(bricks15, ('FlapBrick', 'FlapWedge'),
    default_properties15() | {
        'BrickSize': [60.0, 120.0, 10.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'InputChannel.InputAxis': 'None',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'InputScale': 1.0,
        'MinAngle': -22.5,
        'MaxAngle': 22.5,
        'bAccumulateInput': True
    }
)

_add_mk(bricks15, ('Turbine_6x2x2', 'Turbine_8x4x2', 'Turbine_12x8x5'),
    default_properties15() | {
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


# BRICKS. Last update: 1.8.0

_add_mk(bricks15, ('Brick_1x1x1s', 'Brick_1x1x1s_Flat', 'Brick_1x1x1', 'Brick_1x1x3', 'Brick_1x1x4',  'Brick_1x1x6',
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
    default_properties15() | {
        'bGenerateLift': False
    }
)


# CAMERAS. Last update: 1.8.0

_add_mk(bricks15, ('Camera_1sx1sx1s', 'Camera_2x1x1', 'TargetMaker_1x1x1'),
    default_properties15() | {
        'CameraName': '',
        'OwningSeat': None
    }
)


# COUPLINGS. Last update: 1.8.0

_add_mk(bricks15, ('Coupling_1sx1sx1s_Front_Female', 'Coupling_1x1x1s_Front_Female', 'Coupling_2x2x1s_Female',
        'Coupling_2x2x1s_Front_Female', 'Coupling_4x1x2s_Top'),
    default_properties15()
)

_add_mk(bricks15, ('Coupling_1sx1sx1s_Front_Male', 'Coupling_1x1x1s_Front_Male', 'Coupling_2x2x1s_Front_Male',
        'Coupling_2x2x1s_Male', 'Coupling_4x1x2s_Bottom', 'Coupling_6x2x1s_Male'),
    default_properties15() | {
        'CouplingMode': 'Default',
        'InputChannel.InputAxis': 'None',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)


# DECORATIONS. Last update: 1.8.0

_add_mk(bricks15, ('ImageBrick', 'ImageCylinder'),
    default_properties15() | {
        'bGenerateLift': False,
        'BrickSize': [60.0, 60.0, 10.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0],
        'Image': 'Caution',
        'ImageColor': [0xFF, 0xFF, 0xFF, 0xFF]
    }
)

_add_mk(bricks15, ('Flag_3x1x2',),
    default_properties15() | {
        'bGenerateLift': False,
        'BrickSize': [60.0, 10.0, 60.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'Image': 'Caution',
        'ImageColor': [0xFF, 0xFF, 0xFF, 0xFF]
    }
)

_add_mk(bricks15, ('TextBrick', 'TextCylinder'),
    default_properties15() | {
        'bGenerateLift': False,
        'BrickSize': [60.0, 60.0, 10.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0],
        'Text': 'Text',
        'Font': 'Roboto',
        'FontSize': 60.0,
        'TextColor': [0x00, 0x00, 0x00, 0xFF],
        'OutlineThickness': 0.0
    }
)

_add_mk(bricks15, ('TextBrick', 'TextCylinder'),
    default_properties15() | {
        'bGenerateLift': False,
        'BrickSize': [60.0, 60.0, 10.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0],
        'Text': 'Text',
        'Font': 'Roboto',
        'FontSize': 60.0,
        'TextColor': [0x00, 0x00, 0x00, 0xFF],
        'OutlineThickness': 0.0
    }
)

_add_mk(bricks15, ('Antenna_1x1x8', 'Antenna_2x1x1s', 'Handle_1x2x4s', 'Handle_4x1x1'),
    default_properties15()
)

_add_mk(bricks15, ('Bumper_4sx6x2', 'Bumper_4sx8x7s', 'Door_L_3x1x1', 'Door_R_3x1x1', 'Door_L_3x1x2',
        'Door_R_3x1x2', 'WindowedDoor_L_3x1x4', 'WindowedDoor_R_3x1x4', 'Grid_2x1x1s_02', 'Grid_2x1x1s',
        'GridZylinder_2x2x1s', 'SteeringWheel_5sx5sx1s', 'SteeringWheel_2x2x1s'),
    default_properties15() | {
        'bGenerateLift': False
    }
)


# FIRE AND WATER. Last update: 1.8.0

_add_mk(bricks15, ('Float',),
    default_properties15() | {
        'BrickSize': [30.0, 30.0, 30.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0]
    }
)

_add_mk(bricks15, ('DetonatorBrick', 'DetonatorCylinder'),
    default_properties15() | {
        'BrickSize': [30.0, 30.0, 30.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)

_add_mk(bricks15, ('TankBrick', 'TankCylinder', 'TankCylinder_02'),
    default_properties15() | {
        'BrickSize': [30.0, 30.0, 30.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'FuelType': 'Petrol'
    }
)


_add_mk(bricks15, ('PumpZylinder_2x2x2',),
    default_properties15() | {
        'InputChannel.InputAxis': 'None',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)

# GUNS. Last update: 1.8.0

_add_mk(bricks15, ('Barrel_1sx1sx3', 'Barrel_1x1x4', 'Barrel_1x1x4_Flat'),
    default_properties15()
)

_add_mk(bricks15, ('Flamethrower_2x2x2',),
    default_properties15() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)

_add_mk(bricks15, ('Gun_2x1x1', 'Gun_2x2x2_Ballistic', 'Gun_2x2x2', 'Gun_4x2x2'),
    default_properties15() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'AmmoType': 'Standard'
    }
)

_add_mk(bricks15, ('Launcher_2x1sx1s', 'Launcher_4x2sx2s', 'Launcher_6x1x1'),
    default_properties15() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'AmmoType': 'HighExplosive'
    }
)


# INPUT AND OUTPUT. Last update: 1.8.0

_add_mk(bricks15, ('DisplayBrick',),
    default_properties15() | {
        'bGenerateLift': False,
        'BrickSize': [60.0, 30.0, 10.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 0],
        'InputChannel.InputAxis': 'Custom',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'NumFractionalDigits': 1,
        'DisplayColor': [0xBC, 0x59, 0x59, 0xFF],
    }
)

_add_mk(bricks15, ('Switch_1sx1sx1s', 'Switch_1x1x1s'),
    default_properties15() | {
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


_add_mk(bricks15, ('Sensor_1sx1sx1s', 'Sensor_1x1x1s'),
    default_properties15() | {
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

_add_mk(bricks15, ('MathBrick_1sx1sx1s',),
    default_properties15() | {
        'Operation': 'Add',
        'InputChannelA.InputAxis': 'Custom',
        'InputChannelA.SourceBricks': [],
        'InputChannelA.Value': 1.0,
        'InputChannelB.InputAxis': 'AlwaysOn',
        'InputChannelB.SourceBricks': [],
        'InputChannelB.Value': 1.0
    }
)


# LIGHTS. Last update: 1.8.0

_add_mk(bricks15, ('LightBrick', 'LightCone', 'LightConeFlat', 'LightCylinder', 'LightHemisphere', 'LightRamp',
        'LightRampRounded', 'LightRampRoundedN'),
    default_properties15() | {
        'bGenerateLift': False,
        'BrickSize': [30.0, 30.0, 30.0],
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


# PLAYER. Last update: 1.8.0

_add_mk(bricks15, ('RemoteController_2x1x1s',),
    default_properties15()
)

_add_mk(bricks15, ('Seat_2x2x7s', 'Seat_3x2x2', 'Seat_5x2x1s'),
    default_properties15() | {
        'ExitLocation': None,
        'SeatName': ''
    }
)


# RAMPS. Last update: 1.8.0

_add_mk(bricks15, ('CornerRamp_1x1x1', 'CornerRounded_1x1x1', 'RampRoundedN_1x1x1', 'CornerRamp_2x2x1_02',
         'CornerRamp_2x2x1', 'CornerRampN_2x2x1', 'CornerRounded_2x2x1_02', 'CornerRamp_3x2x1_L', 'CornerRamp_3x2x1_R'),
    default_properties15()
)

_add_mk(bricks15, ('Ramp_1x1x2s', 'RampRounded_1x1x2s', 'Ramp_1x1x1', 'RampN_1x1x1', 'RampRounded_1x1x1',
        'Ramp_1x2x2s', 'RampRounded_1x2x2s', 'Ramp_1x2x1', 'RampRounded_1x2x1', 'Ramp_1x4x2s', 'RampRounded_1x4x2s',
        'Ramp_1x4x1', 'RampRounded_1x4x1', 'Ramp_2x1x1_02', 'Ramp_2x1x1', 'RampN_2x1x1', 'RampRounded_2x1x1',
        'Trapezoid_2x1x1', 'Ramp_2x1x2', 'RampN_2x1x2', 'RampRoundedN_2x1x2', 'Ramp_2x1x3', 'RampN_2x1x3', 'Ramp_2x1x4',
        'RampN_2x1x4', 'CornerRounded_2x2x1', 'Ramp_2x2x1', 'RampN_2x2x1', 'Ramp_2x4x1', 'Ramp_2x4x1', 'RampN_2x4x1',
        'RampRounded_3x1x2s', 'DoubleRamp_3x1x1', 'DoubleRampN_3x1x1', 'Ramp_3x1x1_02', 'Ramp_3x1x1', 'RampN_3x1x1',
        'Ramp_3x2x1', 'RampN_3x2x1', 'CornerRamp_3x3x1', 'Ramp_3x4x1', 'RampN_3x4x1', 'RampRounded_4x1x2s',
        'RampRoundedN_4x2x4', 'CornerRamp_4x3x1_L', 'CornerRamp_4x3x1_R', 'CornerRamp_4x4x1', 'CornerRamp_5x3x1_L',
        'CornerRamp_5x3x1_R'),
    default_properties15() | {
        'bGenerateLift': False
    }
)


# REDIRECTORS. Last update: 1.8.0

_add_mk(bricks15, ('Redirector_1x1x0', 'CornerBrick_1x1x1s_Flat', 'Redirector_1x1x1s_02', 'Redirector_1x1x1s',
        'RedirectorZylinder_1x1x1s_02', 'RedirectorZylinder_1x1x1s', 'Redirector_1x1x1_02', 'Redirector_1x1x1_03',
        'Redirector_1x1x1_04', 'Redirector_1x1x1', 'Redirector_4sx1x1', 'Redirector_4sx1x4s', 'Redirector_4sx4x1',
        'Redirector_4sx6x1', 'Redirector_2x1x1s_02', 'Redirector_2x1x1s_03', 'Redirector_2x1x1s_04', 'Redirector_2x1x1s',
        'RedirectorZylinder_2x2x1s_02', 'RedirectorZylinder_2x2x1s', 'Octagon_2x4x4', 'Redirector_3x2x1s_02',
        'Redirector_3x2x1s'),
    default_properties15() | {
        'bGenerateLift': False
    }
)


# RODS. Last update: 1.8.0

_add_mk(bricks15, ('Rod_1x1x1', 'Rod_1x1x2', 'Rod_1x1x3', 'Rod_1x1x4', 'Rod_1x1x6', 'Rod_1x1x8', 'Rod_1x1x10',
        'Rod_1x1x12', 'Rod_1x1x16', 'Rod_1x1x20'),
    default_properties15() | {
        'bGenerateLift': False
    }
)


# ROUND STUFF. Last update: 1.8.0

_add_mk(bricks15, ('Cone_1x1x1', 'Cone_2x2x2', 'Cone_4x4x4', 'Zylinder_1x1x1s', 'Zylinder_1x1x1s_Flat',
        'Zylinder_1x1x1', 'Zylinder_2x2x1s', 'Zylinder_2x2x1s_Flat', 'Zylinder_2x2x1', 'Zylinder_2x2x4',
        'HalfSphere_1x1', 'HalfSphere_2x2x1', 'HalfSphere_4x4x2', 'HalfZylinder_4x2x4'),
    default_properties15() | {
        'bGenerateLift': False
    }
)


# SCALABLE. Last update: 1.8.0

_add_mk(bricks15, ('ScalableBrick', 'ScalableCone', 'ScalableConeRounded', 'ScalableConeFlat','ScalableZylinder', 'ScalableCylinder90R0',
        'ScalableCylinder90R1', 'ScalableHalfCone', 'ScalableHalfCylinder', 'ScalableHemisphere',
        'ScalablePyramid', 'ScalableQuarterSphere', 'ScalableRamp', 'ScalableRampRounded', 'ScalableRampRoundedN',
        'ScalableWedge', 'ScalableWedgeCorner',
        'ScalableCorner', 'ScalableCornerN', 'ScalableCornerRounded', 'ScalableCornerRoundedN',
        'ScalableQuarterCone', 'ScalablePyramidCorner', 'ScalablePyramidCornerRounded'),
    default_properties15() | {
        'bGenerateLift': False,
        'BrickSize': [30.0, 30.0, 30.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3]
    }
)

_add_mk(bricks15, ('SpinnerBrick',),
    default_properties15() | {
        'ConnectorSpacing': [3, 3, 0, 0, 0, 0],
        'SpinnerAngle': 90.0,
        'SpinnerRadius': [30.0, 30.0],
        'SpinnerShape': 'Square',  # TODO: Add enum
        'SpinnerSize': [30.0, 30.0],
    })


# THRUSTERS. Last update: 1.8.0

_add_mk(bricks15, ('ThrusterBrick', 'ThrusterCylinder', 'ThrusterCylinder_02'),
    default_properties15() | {
        'BrickSize': [30.0, 30.0, 30.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'InputChannel.InputAxis': 'Throttle',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'InputScale' : 1.0,
        'bAccumulated': False
    }
)


# VEHICLES. Last update: 1.8.0

_add_mk(bricks15, ('ExhaustBrick', 'ExhaustCylinder'),
    default_properties15() | {
        'bGenerateLift': False,
        'BrickSize': [30.0, 30.0, 30.0],
        'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
        'ExhaustEffect': 'Trail',  # TODO: Add enum
        'InputChannel.InputAxis': 'None',
        'SmokeColor': [0xFF, 0xFF, 0xFF, 0xFF],
        'SpawnScale': 1.0
    }
)

_add_mk(bricks15, ('Axle_1sx1sx1s', 'Axle_1x1x1s_02', 'Axle_1x1x1s', 'Axle_1x2x1s', 'Axle_2x2x1s', 'Axle_2x2x1',
        'LandingGear_2x2x2', 'Axle_2x4x1s', 'Axle_2x6x1s'),
    default_properties15() | {
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

_add_mk(bricks15, ('Compressor_4x1x4s', 'Mudguard_2x1sx3', 'Mudguard_2x1x1s', 'Mudguard_2x2x2s', 'Mudguard_4x2x5s'),
    default_properties15() | {
        'bGenerateLift': False
    }
)

_add_mk(bricks15, ('Motor_1x2x5s', 'EMotor_2x2x2', 'Motor_3x2x5s', 'AircraftR4', 'Motor_4x2x5s', 'DragV8',
        'DieselV12'),
    default_properties15() | {
        'ThrottleInputChannel.InputAxis': 'Throttle',
        'ThrottleInputChannel.SourceBricks': [],
        'ThrottleInputChannel.Value': 1.0,
        'GearRatioScale': 1.0,
        'bTankDrive': False
    }
)

_add_mk(bricks15, ('Wheels_2x2s',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 60.0,
        'WheelWidth': 20.0,
        'TireThickness': 12.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('RacingWheel_4x2s',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 90.0,
        'WheelWidth': 20.0,
        'TireThickness': 10.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('Wheel_7sx2',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 70.0,
        'WheelWidth': 30.0,
        'TireThickness': 12.5,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('Wheel_10sx1',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 100.0,
        'WheelWidth': 30.0,
        'TireThickness': 22.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('OffroadWheel_3x4s',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 82.0,
        'WheelWidth': 40.0,
        'TireThickness': 18.5,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('RacingWheel_3x4s',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 90.0,
        'WheelWidth': 40.0,
        'TireThickness': 10.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('Wheel_3x4s',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 81.0,
        'WheelWidth': 40.0,
        'TireThickness': 18.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('DragWheel_4x2',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 120.0,
        'WheelWidth': 60.0,
        'TireThickness': 30.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('Wheel_4x2',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 120.0,
        'WheelWidth': 60.0,
        'TireThickness': 26.5,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('OffroadWheel_5x2',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 150.0,
        'WheelWidth': 60.0,
        'TireThickness': 45.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('Wheel_10x4',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 300.0,
        'WheelWidth': 120.0,
        'TireThickness': 90.0,
        'TirePressureRatio': 0.8
    }
)

_add_mk(bricks15, ('IdlerWheel',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 90.0,
        'WheelWidth': 30.0,
    }
)

_add_mk(bricks15, ('SprocketWheel',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 90.0,
        'WheelWidth': 30.0,
        'IdlerWheels': [],
        'TrackColor': [0x59, 0x59, 0x59, 0xFF]
    }
)

_add_mk(bricks15, ('TrainWheel_2x2s',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 60.0,
        'WheelWidth': 20.0,
    }
)

_add_mk(bricks15, ('TrainWheel_3x2s',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 90.0,
        'WheelWidth': 20.0,
    }
)

_add_mk(bricks15, ('TrainWheel_4x2s',),
    default_properties15() | {
        'bInvertTankSteering': False,
        'WheelDiameter': 120.0,
        'WheelWidth': 20.0,
    }
)

_add_mk(bricks15, ('Wheel_1sx1sx1s', 'Wheel_1x1x1'),
    default_properties15()
)


# WINDOWS. Last update: 1.7.4

_add_mk(bricks15, ('Panel_1x2x4', 'Panel_1x4x4', 'Panel_1x6x6', 'Windscreen_2x4x2', 'Windscreen_2x4x3',
        'Windscreen_2x6x2', 'Windscreen_2x6x3', 'Windscreen_2x8x3', 'Windscreen_4x6x3'),
    default_properties15() | {
        'bGenerateLift': False
    }
)


# UNCATEGORIZED. Last update: 1.7.4

_add_mk(bricks15, ('Arch_2x1x2', 'Arch_4x1x2', 'Arch_6x1x1', 'Arch_8x1x8', 'CornerLedge_1x1x1', 'Ledge_1x1x1',
        'Ledge_1x2x1', 'Ledge_1x4x1', 'PlaneTail_10x10x6'),
    default_properties15() | {
        'bGenerateLift': False
    }
)

_add_mk(bricks15, ('DoubleSiren_1x2x1s',),
    default_properties15() | {
        'SirenType': 'Car',
        'HornPitch': 1.0,
        'InputChannel.InputAxis': 'Horn',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)

_add_mk(bricks15, ('Winch_3x2x1',),
    default_properties15() | {
        'InputChannel.InputAxis': 'Auxiliary',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0,
        'WinchSpeed': 100.0
    }
)

_add_mk(bricks15, ('FlareGun_1x1x1',),
    default_properties15() | {
        'InputChannel.InputAxis': 'Action1',
        'InputChannel.SourceBricks': [],
        'InputChannel.Value': 1.0
    }
)
