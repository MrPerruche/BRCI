from .bricks_utils import _add_mk
from copy import deepcopy
from typing import Any


# All different properties and their type
property_types14: dict[str, str] = {
    'ActuatorMode': 'str8',
    'AmmoType': 'str8',
    'bAccumulated': 'bool',
    'bAccumulateInput': 'bool',
    'bCanDisableSteering': 'bool',
    'bCanInvertSteering': 'bool',
    'bDriven': 'bool',
    'bGenerateLift': 'bool',
    'bHasBrake': 'bool',
    'bHasHandBrake': 'bool',
    'bInvertDrive': 'bool',
    'bInvertTankSteering': 'bool',
    'BrakeStrength': 'float',
    'bReturnToZero': 'bool',
    'BrickColor': 'list[4*uint8]',
    'BrickMaterial': 'str8',
    'BrickPattern': 'str8',
    'BrickSize': 'list[3*float]',
    'Brightness': 'float',
    'bTankDrive': 'bool',
    'ConnectorSpacing': 'list[6*uint2]',
    'CouplingMode': 'str8',
    'DisplayColor': 'list[3*uint8]',
    'ExitLocation': 'list[3*float]',
    'FlashSequence': 'str8',
    'Font': 'str8',
    'FontSize': 'float',
    'FuelType': 'str8',
    'GearRatioScale': 'float',
    'HornPitch': 'float',
    'IdlerWheels': 'list[brick_id]',
    'Image': 'str8',
    'ImageColor': 'list[3*uint8]',
    'InputScale': 'float',
    'LightConeAngle': 'float',
    'LightDirection': 'str8',
    'MaxAngle': 'float',
    'MaxLimit': 'float',
    'MinAngle': 'float',
    'MinLimit': 'float',
    'NumFractionalDigits': 'uint8',
    'Operation': 'str8',
    'OutlineThickness': 'float',
    'OutputChannel.MinIn': 'float',
    'OutputChannel.MinOut': 'float',
    'OutputChannel.MaxIn': 'float',
    'OutputChannel.MaxOut': 'float',
    'OwningSeat': 'brick_id',
    'SensorType': 'str8',
    'SirenType': 'str8',
    'SmokeColor': 'list[3*uint8]',
    'SpawnScale': 'float',
    'SpeedFactor': 'float',
    'SteeringAngle': 'float',
    'SteeringSpeed': 'float',
    'SuspensionDamping': 'float',
    'SuspensionLength': 'float',
    'SuspensionStiffness': 'float',
    'SwitchName': 'strany',
    'Text': 'strany',
    'TextColor': 'list[3*uint8]',
    'TirePressureRatio': 'float',
    'TireThickness': 'float',
    'TraceMask': 'str8',
    'TrackColor': 'list[4*uint8]',
    'WheelDiameter': 'float',
    'WheelWidth': 'float',
    'WinchSpeed': 'float'
} # {'brick_id', 'list[4*uint8]', 'uint8', 'strany', 'list[brick_id]', 'str8', 'float', 'list[3*float]', 'list[6*uint2]', 'list[3*uint8]', 'bool'}


# Assign all properties
def _default_properties14() -> dict[str, Any]:
    return deepcopy({'BrickColor': [0, 0, 127, 255], 'BrickPattern': 'Default', 'BrickMaterial': 'Plastic'})


# Initialize bricks for later
bricks14: dict[str, Any] = {}


_add_mk(bricks14, ('TestBrick1', 'TestBrick2'), _default_properties14())
_add_mk(bricks14, ('TestBrick11', 'TestBrick12'), _default_properties14() | {
    'TestProperty': 1
})
_add_mk(bricks14, ('TestBrick21', 'TestBrick22'), _default_properties14() | {
    'AnotherTestProperty': 2,
    "TestProperty": 3
})