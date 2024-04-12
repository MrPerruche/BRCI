from BRAPIF import append_multiple, BrickInput

br_brick_materials = {
    'aluminium':        {'price': 2.00, 'density': 2.70,  'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'brushed aluminum': {'price': 2.00, 'density': 2.70,  'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'carbon':           {'price': 6.00, 'density': 1.55,  'strength': 10.0, 'friction': 0.70, 'restitution': 0.10},
    'traction plate':   {'price': 2.00, 'density': 2.70,  'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'chrome':           {'price': 2.00, 'density': 8.00,  'strength': 10.0, 'friction': 0.35, 'restitution': 0.10},
    'cloudy glass':     {'price': 1.50, 'density': 1.00,  'strength': 0.50, 'friction': 0.70, 'restitution': 0.10},
    'copper':           {'price': 3.00, 'density': 9.00,  'strength': 10.0, 'friction': 0.35, 'restitution': 0.10},
    'foam':             {'price': 0.50, 'density': 0.10,  'strength': 0.10, 'friction': 0.70, 'restitution': 0.10},
    'glass':            {'price': 1.50, 'density': 1.00,  'strength': 0.50, 'friction': 0.70, 'restitution': 0.10},
    'glow':             {'price': 1.50, 'density': 1.00,  'strength': 3.00, 'friction': 0.60, 'restitution': 0.10},
    'gold':             {'price': 11.0, 'density': 19.3,  'strength': 7.50, 'friction': 0.50, 'restitution': 0.10},
    'oak':              {'price': 1.00, 'density': 0.60,  'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'pine':             {'price': 1.00, 'density': 0.60,  'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'plastic':          {'price': 1.00, 'density': 1.00,  'strength': 3.00, 'friction': 0.60, 'restitution': 0.10},
    'old wood':         {'price': 0.75, 'density': 0.60,  'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'rubber':           {'price': 1.00, 'density': 1.00,  'strength': 3.00, 'friction': 2.00, 'restitution': 0.10},
    'rusted steel':     {'price': 3.00, 'density': 8.00,  'strength': 10.0, 'friction': 0.50, 'restitution': 0.10},
    'steel':            {'price': 4.00, 'density': 8.00,  'strength': 20.0, 'friction': 0.35, 'restitution': 0.10},
    'tungsten':         {'price': 8.50, 'density': 19.25, 'strength': 30.0, 'friction': 0.20, 'restitution': 0.10} # Damn you it was perfect!
}                                                                                                                  # Made it perfect for you :3




# --------------------------------------------------
# --------------------------------------------------
#
# BRICKS
#
# --------------------------------------------------
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


# --------------------------------------------------
# ACTUATORS [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Actuator_1sx1sx1s_02_Top', 'Actuator_1sx1sx1s_Male', 'Actuator_1sx1sx1s_Top',
                 'Actuator_1sx1sx2s_Top', 'Actuator_1x1x1s_Top', 'Actuator_1x1x1_Top', 'Actuator_1x1x3_Top',
                 'Actuator_1x1x6_Top', 'Actuator_2x1x1s_02_Top', 'Actuator_2x1x1s_Male', 'Actuator_2x1x1s_Top',
                 'Actuator_2x2x1s_Angular_Top', 'Actuator_2x2x1s_Top', 'Actuator_2x2x2_Top', 'Actuator_2x2x15_Top',
                 'Actuator_4x1x1s_Top', 'Actuator_4x4x1s_Top', 'Actuator_6x2x1s_Top', 'Actuator_8x8x1_Top',
                 'Actuator_20x2x1s_Top'],
                br_brick_list['default_brick_data'], True)


append_multiple(br_brick_list,
                ['Actuator_1sx1sx1s_Bottom', 'Actuator_1sx1sx1s_Female', 'Actuator_1sx1sx2s_Bottom',
                 'Actuator_1x1sx1s_Bottom', 'Actuator_1x1x1s_Bottom', 'Actuator_1x1x1_Bottom', 'Actuator_1x1x3_Bottom',
                 'Actuator_1x1x6_Bottom', 'Actuator_2x1sx1s_Bottom', 'Actuator_2x1x1s_02_Bottom',
                 'Actuator_2x1x1s_Bottom', 'Actuator_2x1x1s_Female', 'Actuator_2x2x1s_Angular_Bottom',
                 'Actuator_2x2x1s_Bottom', 'Actuator_2x2x2_Bottom', 'Actuator_2x2x15_Bottom', 'Actuator_4x1x1s_Bottom',
                 'Actuator_4x4x1s_Bottom', 'Actuator_6x2x1s_Bottom', 'Actuator_8x8x1_Bottom',
                 'Actuator_20x2x1s_Bottom'],
                br_brick_list['default_brick_data'] | {
                    'ActuatorMode': 'Accumulated',
                    'InputChannel.InputAxis': BrickInput('Auxiliary', None),
                    'SpeedFactor': 1.0,
                    'MinLimit': 0.0,
                    'MaxLimit': 0.0
                }, True)


# --------------------------------------------------
# AVIATION TODO
# --------------------------------------------------


# BRICKS WITH REGULAR PROEPRTIES
append_multiple(br_brick_list,
                ['BladeHolder_2x1'],
                br_brick_list['default_brick_data'], True)


# BRICKS WITH FLAP PROPERTIES
append_multiple(br_brick_list,
                ['Flap_1x4x1s', 'Flap_2x8x1s'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': True,
                    'InputChannel.InputAxis': BrickInput('None', None),
                    'InputScale': 100.0,
                    'MinAngle': -22.5,
                    'MaxAngle': 22.5,
                    'bAccumulateInput': True
                },
                True)


# BRICKS WITH HELI ENGINE PROPERTIES
append_multiple(br_brick_list,
                ['Turbine_6x2x2'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': True,
                    'PowerInputChannel.InputAxis': BrickInput('OperationMode', None),
                    'AutoHoverInputChannel.InputAxis': BrickInput('DisableSteering', None),
                    'ThrottleInputChannel.InputAxis': BrickInput('ThrottleAlt', None),
                    'PitchInputChannel.InputAxis': BrickInput('ViewPitchAlt', None),
                    'YawInputChannel.InputAxis': BrickInput('SteeringAlt', None),
                    'RollInputChannel.InputAxis': BrickInput('ViewYawAlt', None)
                }, True)


# --------------------------------------------------
# BRICKS TODO
# --------------------------------------------------


# --------------------------------------------------
# CAMERAS TODO
# --------------------------------------------------


# --------------------------------------------------
# COUPLINGS TODO
# --------------------------------------------------


# --------------------------------------------------
# DECORATION TODO
# --------------------------------------------------


# --------------------------------------------------
# FIRE AND WATER TODO
# --------------------------------------------------


# --------------------------------------------------
# GUNS TODO
# --------------------------------------------------


# --------------------------------------------------
# INPUT AND OUTPUT
# --------------------------------------------------


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
                }, True)


# --------------------------------------------------
# LIGHTS TODO
# --------------------------------------------------


# --------------------------------------------------
# PLAYER TODO
# --------------------------------------------------


# --------------------------------------------------
# RAMPS TODO
# --------------------------------------------------


# --------------------------------------------------
# REDIRECTORS TODO
# --------------------------------------------------


# --------------------------------------------------
# RODS TODO
# --------------------------------------------------


# --------------------------------------------------
# ROUND STUFF TODO
# --------------------------------------------------


# --------------------------------------------------
# SCALABLES
# --------------------------------------------------


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


# --------------------------------------------------
# THRUSTERS TODO
# --------------------------------------------------


# --------------------------------------------------
# VEHICLES TODO
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Motor_1x2x5s', 'EMotor_2x2x2', 'Motor_3x2x5s', 'AircraftR4',
                 'Motor_4x2x5s', 'DragV8', 'DieselV12'],
                br_brick_list['default_brick_data'] | {
                    'ThrottleInputChannel.InputAxis': BrickInput('Throttle', None),
                    'GearRatioScale': 1.0,
                    'bTankDrive': False
                }, True)


# --------------------------------------------------
# WINDOWS TODO
# --------------------------------------------------


# --------------------------------------------------
# UNCATEGORIZED TODO
# --------------------------------------------------


# TODO FOLLOWING BRICK. NO DOCUMENTATION ETC. ONLY USED FOR A TEST.
append_multiple(br_brick_list, ['DoubleSiren_1x2x1s'],
                br_brick_list['default_brick_data'] | {
                    'SirenType': 'Car',
                    'HornPitch': 1.0,
                    'InputChannel.InputAxis': BrickInput('Horn', None)
                }, True)


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
