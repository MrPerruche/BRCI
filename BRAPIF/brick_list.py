from BRAPIF import append_multiple, BrickInput

br_brick_materials = {
    'aluminium':        {'price': 2.00, 'density': 2.70, 'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'brushed aluminum': {'price': 2.00, 'density': 2.70, 'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'carbon':           {'price': 6.00, 'density': 1.55, 'strength': 10.0, 'friction': 0.70, 'restitution': 0.10},
    'traction plate':   {'price': 2.00, 'density': 2.70, 'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'chrome':           {'price': 2.00, 'density': 8.00, 'strength': 10.0, 'friction': 0.35, 'restitution': 0.10},
    'cloudy glass':     {'price': 1.50, 'density': 1.00, 'strength': 0.50, 'friction': 0.70, 'restitution': 0.10},
    'copper':           {'price': 3.00, 'density': 9.00, 'strength': 10.0, 'friction': 0.35, 'restitution': 0.10},
    'foam':             {'price': 0.50, 'density': 0.10, 'strength': 0.10, 'friction': 0.70, 'restitution': 0.10},
    'glass':            {'price': 1.50, 'density': 1.00, 'strength': 0.50, 'friction': 0.70, 'restitution': 0.10},
    'glow':             {'price': 1.50, 'density': 1.00, 'strength': 3.00, 'friction': 0.60, 'restitution': 0.10},
    'gold':             {'price': 11.0, 'density': 19.3, 'strength': 7.50, 'friction': 0.50, 'restitution': 0.10},
    'oak':              {'price': 1.00, 'density': 0.60, 'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'pine':             {'price': 1.00, 'density': 0.60, 'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'plastic':          {'price': 1.00, 'density': 1.00, 'strength': 3.00, 'friction': 0.60, 'restitution': 0.10},
    'old wood':         {'price': 0.75, 'density': 0.60, 'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'rubber':           {'price': 1.00, 'density': 1.00, 'strength': 3.00, 'friction': 2.00, 'restitution': 0.10},
    'rusted steel':     {'price': 3.00, 'density': 8.00, 'strength': 10.0, 'friction': 0.50, 'restitution': 0.10},
    'steel':            {'price': 4.00, 'density': 8.00, 'strength': 20.0, 'friction': 0.35, 'restitution': 0.10},
    'tungsten':         {'price': 8.50, 'density': 19.25, 'strength': 30.0, 'friction': 0.20, 'restitution': 0.10} # Damn you it was perfect!
}


# --------------------------------------------------
# BRICKS
# --------------------------------------------------

br_brick_list = {
    'default_brick_data': {
        'BrickColor': [0, 0, 127, 255],
        'BrickPattern': 'Default',
        'BrickMaterial': 'Plastic',
        'Position': [0.0, 0.0, 0.0],  # Do not include in special handling list. Already taken care of.
        'Rotation': [0.0, 0.0, 0.0]   # Do not include in special handling list. Already taken care of.
    }
}

append_multiple(br_brick_list, ['Switch_1sx1sx1s', 'Switch_1x1x1s'],
                br_brick_list['default_brick_data'] | {
                    'OutputChannel.MinIn': -1.0,
                    'OutputChannel.MaxIn': 1.0,
                    'OutputChannel.MinOut': -1.0,
                    'OutputChannel.MaxOut': 1.0,
                    'InputChannel.InputAxis': BrickInput('None', None),
                    'bReturnToZero': True,
                    'SwitchName': ''}, True)

append_multiple(br_brick_list, ['DisplayBrick'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False,
                    'BrickSize': [6, 3, 1],
                    'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
                    'InputChannel.InputAxis': BrickInput('Custom', None),
                    'NumFractionalDigits': 1,
                    'DisplayColor': [0, 80, 50]
                }, True)

append_multiple(br_brick_list, ['Sensor_1sx1sx1s', 'Sensor_1x1x1s'],
                br_brick_list['default_brick_data'] | {
                    'OutputChannel.MinIn': -1.0,
                    'OutputChannel.MaxIn': 1.0,
                    'OutputChannel.MinOut': -1.0,
                    'OutputChannel.MaxOut': 1.0,
                    'EnabledInputChannel.InputAxis': BrickInput('ConstantValue', 1.0), # TODO
                    'SensorType': 'Speed',
                    'TraceMask': 'All',
                    'bReturnToZero': False
                }, True)

append_multiple(br_brick_list, ['MathBrick_1sx1sx1s'],
                br_brick_list['default_brick_data'] | {
                    'Operation': 'Add',
                    'InputChannelA.InputAxis': BrickInput('Custom', None),
                    'InputChannelB.InputAxis': BrickInput('ConstantValue', 1.0)
                })

# Scalables w/ aerodynamics
append_multiple(br_brick_list,
                ['ScalableBrick', 'ScalableCone', 'ScalableConeRounded', 'ScalableZylinder', 'ScalableCylinder90R0',
                 'ScalableCylinder90R1', 'ScalableHalfCone', 'ScalableHalfCylinder', 'ScalableHemisphere',
                 'ScalablePyramid', 'ScalableQuarterSphere', 'ScalableRamp', 'ScalableRampRounded', 'ScalableRampRoundedN',
                 'ScalableWedge', 'ScalableWedgeCorner'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False,
                    'BrickSize': [3, 3, 3],
                    'ConnectorSpacing': [3, 3, 3, 3, 3, 3]
                }, True)
# Scalables w/out aerodynamics
append_multiple(br_brick_list,
                ['ScalableCorner', 'ScalableCornerN', 'ScalableCornerRounded', 'ScalableCornerRoundedN',
                 'ScalableQuarterCone', 'ScalablePyramidCorner', 'ScalablePyramidCornerRounded'],
                br_brick_list['default_brick_data'] | {
                    'BrickSize': [3, 3, 3],
                    'ConnectorSpacing': [3, 3, 3, 3, 3, 3]
                }, True)

append_multiple(br_brick_list,
                ['Motor_1x2x5s', 'EMotor_2x2x2', 'Motor_3x2x5s', 'AircraftR4',
                 'Motor_4x2x5s', 'DragV8', 'DieselV12'],
                br_brick_list['default_brick_data'] | {
                    'ThrottleInputChannel.InputAxis': BrickInput('Throttle', None),
                    'GearRatioScale': 1.0,
                    'bTankDrive': False
                })


# -------------------------------------------------
# PROPERTIES
# --------------------------------------------------

"""
Order for Connector Spacing in UI:
    [1] [0]
    [3] [2]
    [5] [4]
"""

br_special_property_instance_list = {
    'BrickColor': '4xINT8',
    'BrickSize': '3xINT16',
    'ConnectorSpacing': '6xINT2',
    'DisplayColor': '3xINT8',
    'NumFractionalDigits': 'INT8'
}
