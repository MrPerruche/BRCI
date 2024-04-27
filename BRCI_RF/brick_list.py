from .functions import append_multiple, BrickInput

br_brick_materials = {
    'Aluminium': {'price': 2.00, 'density': 2.70,  'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'BrushedAlu': {'price': 2.00, 'density': 2.70,  'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'Carbon': {'price': 6.00, 'density': 1.55,  'strength': 10.0, 'friction': 0.70, 'restitution': 0.10},
    'ChanneledAlu': {'price': 2.00, 'density': 2.70,  'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'Chrome': {'price': 2.00, 'density': 8.00,  'strength': 10.0, 'friction': 0.35, 'restitution': 0.10},
    'CloudyGlass': {'price': 1.50, 'density': 1.00,  'strength': 0.50, 'friction': 0.70, 'restitution': 0.10},
    'Copper': {'price': 3.00, 'density': 9.00,  'strength': 10.0, 'friction': 0.35, 'restitution': 0.10},
    'Foam': {'price': 0.50, 'density': 0.10,  'strength': 0.10, 'friction': 0.70, 'restitution': 0.10},
    'Glass': {'price': 1.50, 'density': 1.00,  'strength': 0.50, 'friction': 0.70, 'restitution': 0.10},
    'Glow': {'price': 1.50, 'density': 1.00,  'strength': 3.00, 'friction': 0.60, 'restitution': 0.10},
    'Gold': {'price': 11.0, 'density': 19.3,  'strength': 7.50, 'friction': 0.50, 'restitution': 0.10},
    'Oak': {'price': 1.00, 'density': 0.60,  'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'Pine': {'price': 1.00, 'density': 0.60,  'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'Plastic': {'price': 1.00, 'density': 1.00,  'strength': 3.00, 'friction': 0.60, 'restitution': 0.10},
    'RoughWood': {'price': 0.75, 'density': 0.60,  'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'Rubber': {'price': 1.00, 'density': 1.00,  'strength': 3.00, 'friction': 2.00, 'restitution': 0.10},
    'RustedSteel': {'price': 3.00, 'density': 8.00,  'strength': 10.0, 'friction': 0.50, 'restitution': 0.10},
    'Steel': {'price': 4.00, 'density': 8.00,  'strength': 20.0, 'friction': 0.35, 'restitution': 0.10},
    'Tungsten': {'price': 8.50, 'density': 19.25, 'strength': 30.0, 'friction': 0.20, 'restitution': 0.10} # Damn you it was perfect!
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
                    'InputChannel.InputAxis': BrickInput('Auxiliary', None, 'InputChannel'),
                    'SpeedFactor': 1.0,
                    'MinLimit': 0.0,
                    'MaxLimit': 0.0
                }, True)


# --------------------------------------------------
# AVIATION [LAST UPDATE: 1.6.3]
# --------------------------------------------------


# BRICKS WITH REGULAR PROPERTIES
append_multiple(br_brick_list,
                ['BladeHolder_2x1', 'Prop_5x1', 'Prop_10x1', 'Rotor_3x4', 'Rotor_4x8', 'Blade_20x2', 'Blade_26x2'],
                br_brick_list['default_brick_data'], True)

# BRICKS WITH REGULAR PROPERTIES + AERO
append_multiple(br_brick_list,
                ['Wing_2x2x1s', 'Wing_2x2x1s_L', 'Wing_2x2x1s_R', 'WingRounded_2x2x1s', 'Wing_2x3x1s',
                 'Wing_2x3x1s_L', 'Wing_2x3x1s_R', 'Wing_2x4x1s_L', 'Wing_2x4x1s_R', 'Wing_3x3x1s', 'Wing_4x8x1s_L',
                 'Wing_4x8x1s_R'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': True
                }, True)


# BRICKS WITH FLAP PROPERTIES
append_multiple(br_brick_list,
                ['Flap_1x4x1s', 'Flap_2x8x1s'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': True,
                    'InputChannel.InputAxis': BrickInput('None', None, 'InputChannel'),
                    'InputScale': 1.0,
                    'MinAngle': -22.5,
                    'MaxAngle': 22.5,
                    'bAccumulateInput': True
                },
                True)


# BRICKS WITH HELI ENGINE PROPERTIES
append_multiple(br_brick_list,
                ['Turbine_6x2x2', 'Turbine_8x4x2', 'Turbine_12x8x5'],
                br_brick_list['default_brick_data'] | {
                    'PowerInputChannel.InputAxis': BrickInput('OperationMode', None, 'PowerInputChannel'),
                    'AutoHoverInputChannel.InputAxis': BrickInput('DisableSteering', None, 'AutoHoverInputChannel'),
                    'ThrottleInputChannel.InputAxis': BrickInput('ThrottleAlt', None, 'ThrottleInputChannel'),
                    'PitchInputChannel.InputAxis': BrickInput('ViewPitchAlt', None, 'PitchInputChannel'),
                    'YawInputChannel.InputAxis': BrickInput('SteeringAlt', None, 'YawInputChannel'),
                    'RollInputChannel.InputAxis': BrickInput('ViewYawAlt', None, 'RollInputChannel')
                }, True)


# --------------------------------------------------
# BRICKS [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list, ['Brick_1x1x1s', 'Brick_1x1x1s_Flat', 'Brick_1x1x1', 'Brick_1x1x3', 'Brick_1x1x4',
                                'Brick_1x1x6', 'Brick_2x1x1s', 'Brick_1x1x1s_Flat', 'BrickRounded_2x1x1s',
                                'BrickRounded_2x1x1s_Flat', 'Brick_2x1x1', 'Brick_2x1x6', 'Brick_2x2x1s',
                                'Brick_2x2x1s_Flat', 'BrickRoundedCorner_2x2x1s', 'CornerBrick_2x2x1s', 'Brick_2x2x1',
                                'CornerBrick_2x2x1', 'Brick_3x1x1s', 'Brick_3x1x1s_Flat', 'BrickRounded_3x1x1s',
                                'BrickRounded_3x1x1s_Flat', 'Brick_3x1x1', 'Brick_3x2x1s', 'Brick_3x2x1s_Flat',
                                'Brick_3x2x1', 'Brick_4x1x1s', 'Brick_4x1x1s_Flat', 'BrickRounded_4x1x1s',
                                'BrickRounded_4x1x1s_Flat', 'Brick_4x1x1', 'Brick_4x2x1s', 'Brick_4x4x1s_Flat',
                                'Brick_5x1x1s', 'Brick_5x1x1s_Flat', 'BrickRounded_5x1x1s', 'BrickRounded_5x1x1s_Flat',
                                'Brick_5x1x1', 'BrickRounded_5x1x1s', 'BrickRounded_5x1x1s_Flat', 'Brick_5x1x1',
                                'Brick_5x2x1s', 'Brick_5x2x1s_Flat', 'Brick_5x2x1', 'Brick_6x1x1s', 'Brick_6x1x1s_Flat',
                                'BrickRounded_6x1x1s', 'BrickRounded_6x1x1s_Flat', 'Brick_6x1x1', 'Brick_6x2x1s',
                                'Brick_6x2x1s_Flat', 'Brick_6x2x1', 'Weight_6x2x3', 'Brick_6x4x1s', 'Brick_6x4x1s_Flat',
                                'Brick_6x6x1s', 'Brick_6x6x1s_Flat', 'Brick_8x1x1s', 'Brick_8x1x1s_Flat',
                                'BrickRounded_8x1x1s', 'BrickRounded_8x1x1s_Flat', 'Brick_8x1x1', 'Brick_8x2x1s',
                                'Brick_8x2x1s_Flat', 'Brick_8x2x1', 'Brick_8x4x1s', 'Brick_8x4x1s_Flat', 'Brick_8x6x1s',
                                'Brick_8x6x1s_Flat', 'Brick_8x8x1s', 'Brick_8x8x1s_Flat', 'Brick_10x1x1s',
                                'Brick_10x1x1s', 'Brick_10x1x1', 'Brick_10x2x1s', 'Brick_10x2x1s_Flat', 'Brick_10x2x1',
                                'Brick_10x4x1s', 'Brick_10x4x1s_Flat', 'Brick_10x6x1s', 'Brick_10x6x1s_Flat',
                                'Brick_10x8x1s', 'Brick_10x8x1s_Flat', 'Brick_12x1x1s', 'Brick_12x1x1', 'Brick_12x6x1s',
                                'Brick_12x6x1s_Flat', 'Brick_12x8x1s', 'Brick_12x8x1s_Flat', 'Brick_12x12x1',
                                'Brick_16x1x1', 'Brick_16x8x1s', 'Brick_16x8x1s_Flat', 'Brick_20x1x1', 'Brick_24x12x1'],
                br_brick_list['default_brick_data'] | {'bGenerateLift': False}, True)


# --------------------------------------------------
# CAMERAS [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Camera_1sx1sx1s', 'Camera_2x1x1', 'TargetMaker_1x1x1'],
                br_brick_list['default_brick_data'] | {
                    'OwningSeat': None
                }, True)


# --------------------------------------------------
# COUPLINGS [LAST UPDATE: 1.6.3]
# --------------------------------------------------

# Female
append_multiple(br_brick_list,
                ['Coupling_1sx1sx1s_Front_Female', 'Coupling_1x1x1s_Front_Female', 'Coupling_2x2x1s_Female',
                 'Coupling_2x2x1s_Front_Female', 'Coupling_4x1x2s_Top'],
                br_brick_list['default_brick_data'], True)

# Male
append_multiple(br_brick_list,
                ['Coupling_1sx1sx1s_Front_Male', 'Coupling_1x1x1s_Front_Male', 'Coupling_2x2x1s_Front_Male',
                 'Coupling_2x2x1s_Male', 'Coupling_4x1x2s_Bottom', 'Coupling_6x2x1s_Male'],
                br_brick_list['default_brick_data'] | {
                    'CouplingMode': 'Static',
                    'InputChannel.InputAxis': BrickInput('None', None, 'InputChannel')
                }, True)

# --------------------------------------------------
# DECORATION [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Antenna_1x1x8', 'Antenna_2x1x1s', 'Handle_1x2x4s', 'Handle_4x1x1'],
                br_brick_list['default_brick_data'], True)


append_multiple(br_brick_list,
                ['Bumper_4sx6x2', 'Bumper_4sx8x7s', 'Door_L_3x1x1', 'Door_R_3x1x1', 'Door_L_3x1x2',
                 'Door_R_3x1x2', 'WindowedDoor_3x1x2', 'WindowedDoor_R_3x1x4', 'Grid_2x1x1s_02', 'Grid_2x1x1s',
                 'GridZylinder_2x2x1s', 'SteeringWheel_5sx5sx1s', 'SteeringWheel_2x2x1s'],
                br_brick_list['default_brick_data'], True)

append_multiple(br_brick_list,
                ['Imageplate_1x1x0', 'Imageplate_1x1x1s', 'ImageZylinder_1x1x1s', 'Imageplate_2x2x1s',
                 'ImageZylinder_2x2x1s', 'Flag_3x1x2', 'Imageplate_4x4x1s'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False,
                    'Image': 'Caution',
                    'ImageColor': [0, 0, 255]
                }, True)


append_multiple(br_brick_list,
                ['Nameplate_1sx1sx1s', 'Nameplate_1x1sx1s', 'Nameplate_2x1sx1s'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False,
                    'Text': 'Text',
                    'TextColor': [0, 0, 0],
                    'FontSize': 10
                }, True)

append_multiple(br_brick_list,
                ['Nameplate_1x1x1s', 'NameZylinder_1x1x1s', 'Nameplate_2x1x1s', 'Nameplate_4x1x1s',
                 'Nameplate_6x1x1s', 'Nameplate_8x1x1s'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False,
                    'Text': 'Text',
                    'TextColor': [0, 0, 0],
                    'FontSize': 30
                }, True)

append_multiple(br_brick_list,
                ['Nameplate_2x2x1s', 'NameZylinder_2x2x1s', 'Nameplate_4x2x1s', 'Nameplate_6x2x1s',
                 'Nameplate_8x2x1s'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False,
                    'Text': 'Text',
                    'TextColor': [0, 0, 0],
                    'FontSize': 60
                }, True)


# --------------------------------------------------
# FIRE AND WATER [LAST UPDATE: 1.6.3]
# --------------------------------------------------

# Float
append_multiple(br_brick_list, ['Float'], br_brick_list['default_brick_data'] | {
    'BrickSize': [3, 3, 3],
    'ConnectorSpacing': [3, 3, 3, 3, 3, 3]
}, True)

# Detonator
append_multiple(br_brick_list, ['Detonator_1x1x1s'], br_brick_list['default_brick_data'] | {
    'InputChannel.InputAxis': BrickInput('Action1', None, 'InputChannel')
}, True)

# Pumps
append_multiple(br_brick_list, ['PumpZylinder_2x2x2'], br_brick_list['default_brick_data'] | {
    'InputChannel.InputAxis': BrickInput('None', None, 'InputChannel')
}, True)

# FUEL TANKS IN VEHICLE CATEGORY

# --------------------------------------------------
# GUNS [LAST UPDATE: 1.6.3]
# --------------------------------------------------

# Barrels
append_multiple(br_brick_list,
                ['Barrel_1sx1sx3', 'Barrel_1x1x4', 'Barrel_1x1x4_Flat'],
                br_brick_list['default_brick_data'], True)

# Flamethrower
append_multiple(br_brick_list, ['Flamethrower_2x2x2'], br_brick_list['default_brick_data'] | {
    'InputChannel.InputAxis': BrickInput('Action1', None, 'InputChannel')
}, True)

# Guns
append_multiple(br_brick_list, ['Gun_2x1x1', 'Gun_2x2x2_Ballistic', 'Gun_2x2x2', 'Gun_4x2x2'],
                br_brick_list['default_brick_data'] | {
                    'InputChannel.InputAxis': BrickInput('Action1', None, 'InputChannel'),
                    'AmmoType': 'Standard'
}, True)

# Launchers
append_multiple(br_brick_list,
                ['Launcher_2x1sx1s', 'Launcher_4x2sx2s', 'Launcher_6x1x1'],
                br_brick_list['default_brick_data'] | {
                    'InputChannel.InputAxis': BrickInput('Action1', None, 'InputChannel'),
                    'AmmoType': 'HighExplosive'
                }, True)


# --------------------------------------------------
# INPUT AND OUTPUT [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list, ['Switch_1sx1sx1s', 'Switch_1x1x1s'],
                br_brick_list['default_brick_data'] | {
                    'OutputChannel.MinIn': -1.0,
                    'OutputChannel.MaxIn': 1.0,
                    'OutputChannel.MinOut': -1.0,
                    'OutputChannel.MaxOut': 1.0,
                    'InputChannel.InputAxis': BrickInput('None', None, 'InputChannel'),
                    'bReturnToZero': True,
                    'SwitchName': ''}, True)

append_multiple(br_brick_list, ['DisplayBrick'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False,
                    'BrickSize': [6, 3, 1],
                    'ConnectorSpacing': [3, 3, 3, 3, 3, 0],
                    'InputChannel.InputAxis': BrickInput('Custom', None, 'InputChannel'),
                    'NumFractionalDigits': 1,
                    'DisplayColor': [0, 204, 128]
                }, True)

append_multiple(br_brick_list, ['Sensor_1sx1sx1s', 'Sensor_1x1x1s'],
                br_brick_list['default_brick_data'] | {
                    'OutputChannel.MinIn': -1.0,
                    'OutputChannel.MaxIn': 1.0,
                    'OutputChannel.MinOut': -1.0,
                    'OutputChannel.MaxOut': 1.0,
                    'EnabledInputChannel.InputAxis': BrickInput('AlwaysOn', 1.0, 'EnabledInputChannel'),
                    'SensorType': 'Speed',
                    'TraceMask': 'All',
                    'bReturnToZero': False
                }, True)

append_multiple(br_brick_list, ['MathBrick_1sx1sx1s'],
                br_brick_list['default_brick_data'] | {
                    'Operation': 'Add',
                    'InputChannelA.InputAxis': BrickInput('Custom', None, 'InputChannelA'),
                    'InputChannelB.InputAxis': BrickInput('AlwaysOn', 1.0, 'InputChannelB')
                }, True)


# --------------------------------------------------
# LIGHTS [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Light_1sx1sx1s', 'Light_1x1x0', 'Light_1x1x1s', 'Light_1x1x1s_Flat', 'LightZylinder_1x1x1s',
                 'LightZylinder_1x1x1s_Flat', 'LightCone_1x1x1', 'LightHalfSphere_1x1', 'LightRamp_1x1x1',
                 'LightRampRounded_1x1x1', 'LightZylinder_1x1x1', 'Light_2x1x1s', 'LightZylinder_2x2x1s_Flat'],
                br_brick_list['default_brick_data'] | {
                    'InputChannel.InputAxis': BrickInput('Headlight', None, 'InputChannel'),
                    'Brightness': 0.5,
                    'FlashSequence': 'None',
                    'LightDirection': 'Off',
                    'LightConeAngle': 45.0
                }, True)


# --------------------------------------------------
# PLAYER [LAST UPDATE: 1.6.3]
# --------------------------------------------------

# RC Receiver
append_multiple(br_brick_list, ['RemoteController_2x1x1s'], br_brick_list['default_brick_data'], True)

# Seats
append_multiple(br_brick_list, ['Seat_2x2x7s', 'Seat_3x2x2', 'Seat_5x2x1s'],
                br_brick_list['default_brick_data'] | {
                    'ExitLocation': None
                }, True)

append_multiple(br_brick_list, ['SteeringWheel_5sx5sx1s', 'SteeringWheel_5x5x1s'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False
                }, True)

# --------------------------------------------------
# RAMPS [LAST UPDATE: 1.6.3]
# --------------------------------------------------

# NO Fluid Dynamics
append_multiple(br_brick_list,
                ['CornerRamp_1x1x1', 'CornerRounded_1x1x1', 'RampRoundedN_1x1x1', 'CornerRamp_2x2x1_02',
                 'CornerRamp_2x2x1', 'CornerRampN_2x2x1', 'CornerRounded_2x2x1_02', 'CornerRamp_3x2x1_L',
                 'CornerRamp_3x2x1_R'],
                br_brick_list['default_brick_data'], True)


append_multiple(br_brick_list,
                ['Ramp_1x1x2s', 'RampRounded_1x1x2s', 'Ramp_1x1x1', 'RampN_1x1x1', 'RampRounded_1x1x1',
                 'Ramp_1x2x2s', 'RampRounded_1x2x2s', 'Ramp_1x2x1', 'RampRounded_1x2x1', 'Ramp_1x4x2s',
                 'RampRounded_1x4x2s', 'Ramp_1x4x1', 'RampRounded_1x4x1', 'Ramp_2x1x1_02', 'Ramp_2x1x1', 'RampN_2x1x1',
                 'RampRounded_2x1x1', 'Trapezoid_2x1x1', 'Ramp_2x1x2', 'RampN_2x1x2', 'RampRoundedN_2x1x2',
                 'Ramp_2x1x3', 'RampN_2x1x3', 'Ramp_2x1x4', 'RampN_2x1x4', 'CornerRounded_2x2x1', 'Ramp_2x2x1',
                 'RampN_2x2x1', 'Ramp_2x4x1', 'Ramp_2x4x1', 'RampN_2x4x1', 'RampRounded_3x1x2s', 'DoubleRamp_3x1x1',
                 'DoubleRampN_3x1x1', 'Ramp_3x1x1_02', 'Ramp_3x1x1', 'RampN_3x1x1', 'Ramp_3x2x1', 'RampN_3x2x1',
                 'CornerRamp_3x3x1', 'Ramp_3x4x1', 'RampN_3x4x1', 'RampRounded_4x1x2s', 'RampRoundedN_4x2x4',
                 'CornerRamp_4x3x1_L', 'CornerRamp_4x3x1_R', 'CornerRamp_4x4x1', 'CornerRamp_5x3x1_L',
                 'CornerRamp_5x3x1_R'],
                br_brick_list['default_brick_data'] | {'bGenerateLift': False}, True)


# --------------------------------------------------
# REDIRECTORS [LAST UPDATE:  1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Redirector_1x1x0', 'CornerBrick_1x1x1s_Flat', 'Redirector_1x1x1s_02', 'Redirector_1x1x1s',
                 'RedirectorZylinder_1x1x1s_02', 'RedirectorZylinder_1x1x1s', 'Redirector_1x1x1_02',
                 'Redirector_1x1x1_03', 'Redirector_1x1x1_04', 'Redirector_1x1x1', 'Redirector_4sx1x1',
                 'Redirector_4sx1x4s', 'Redirector_4sx4x1', 'Redirector_4sx6x1', 'Redirector_2x1x1s_02',
                 'Redirector_2x1x1s_03', 'Redirector_2x1x1s_04', 'Redirector_2x1x1s', 'RedirectorZylider_2x2x1s_02',
                 'RedirectorZylinder_2x2x1s', 'Octagon_2x4x4', 'Redirector_3x2x1s_02', 'Redirector_3x2x1s'],
                br_brick_list['default_brick_data'] | {'bGenerateLift': False}, True)



# --------------------------------------------------
# RODS [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Rod_1x1x1', 'Rod_1x1x2', 'Rod_1x1x3', 'Rod_1x1x4', 'Rod_1x1x6', 'Rod_1x1x8', 'Rod_1x1x10',
                 'Rod_1x1x12', 'Rod_1x1x16', 'Rod_1x1x20'],
                br_brick_list['default_brick_data'] | {'bGenerateLift': False}, True)


# --------------------------------------------------
# ROUND STUFF [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Cone_1x1x1', 'Cone_2x2x2', 'Cone_4x4x4', 'Zylinder_1x1x1s', 'Zylinder_1x1x1s_Flat',
                 'Zylinder_1x1x1', 'Zylinder_2x2x1s', 'Zylinder_2x2x1s_Flat', 'Zylinder_2x2x1', 'Zylinder_2x2x4',
                 'HalfSphere_1x1', 'HalfSphere_2x2x1', 'HalfSphere_4x4x2', 'HalfZylinder_4x2x4'],
                br_brick_list['default_brick_data'] | {'bGenerateLift': False}, True)


# --------------------------------------------------
# SCALABLES [LAST UPDATE: 1.6.3]
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
# THRUSTERS [LAST UPDATE: 1.6.3]
# --------------------------------------------------

append_multiple(br_brick_list,
                ['Thruster_1sx1sx1s', 'Thruster_1x1x1', 'Thruster_1x1x3', 'Thruster_2x2x4'],
                br_brick_list['default_brick_data'] | {
                    'InputChannel.InputAxis': BrickInput('Throttle', None, 'InputChannel'),
                    'InputScale' : 1.0,
                    'bAccumulated': False
                }, True)

# FUEL TANKS IN VEHICLE CATEGORY


# --------------------------------------------------
# VEHICLES [LAST UPDATE: 1.6.3]
# --------------------------------------------------

# Axles
append_multiple(br_brick_list,
                ['Axle_1sx1sx1s', 'Axle_1x1x1s_02', 'Axle_1x1x1s', 'Axle_1x2x1s',
                 'Axle_2x2x1s', 'Axle_2x2x1', 'LandingGear_2x2x2', 'Axle_2x4x1s', 'Axle_2x6x1s'],
                br_brick_list['default_brick_data'] | {
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
                    'SteeringInputChannel.InputAxis': BrickInput('Steering', None, 'SteeringInputChannel'),
                    'BrakeInputChannel.InputAxis': BrickInput('Brake', None, 'BrakeInputChannel'),
                    'bCanDisableSteering': False,
                    'bCanInvertSteering': False
                }, True)

# Compressor and exhaust
append_multiple(br_brick_list,
                ['Compressor_4x1x4s', 'Mudguard_2x1sx3', 'Mudguard_2x1x1s', 'Mudguard_2x2x2s', 'Mudguard_4x2x5s'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False
                }, True)

append_multiple(br_brick_list, ['Exhaust_1x1x1'],
                br_brick_list['default_brick_data'] | {
                    'InputChannel.InputAxis': BrickInput('None', None, 'InputChannel'),
                    'SmokeColor': [0, 0, 255],
                    'SpawnScale': 1.0
                }, True)

# Engines
append_multiple(br_brick_list,
                ['Motor_1x2x5s', 'EMotor_2x2x2', 'Motor_3x2x5s', 'AircraftR4',
                 'Motor_4x2x5s', 'DragV8', 'DieselV12'],
                br_brick_list['default_brick_data'] | {
                    'ThrottleInputChannel.InputAxis': BrickInput('Throttle', None, 'ThrottleInputChannel'),
                    'GearRatioScale': 1.0,
                    'bTankDrive': False
                }, True)

# Fuel
append_multiple(br_brick_list,
                ['Tank_1x1x1', 'Tank_2x2x1', 'Tank_2x2x4'],
                br_brick_list['default_brick_data'] | {
                    'FuelType': 'Petrol'
                }, True)

# Wheels
append_multiple(br_brick_list,
                ['Wheel_2x2s', 'RacingWheel_4x2s', 'Wheel_10sx1', 'OffroadWheel_3x4s', 'RacingWheel_3x4s',
                 'Wheel_3x4s', 'Wheel_7sx2', 'DragWheel_4x2', 'Wheel_4x2', 'OffroadWheel_5x2', 'Wheel_10x4'],
                br_brick_list['default_brick_data'] | {
                    'bInvertTankSteering': False,
                    'TirePressureRatio': 0.8
                }, True)

append_multiple(br_brick_list,['TrainWheel_2x2s', 'TrainWheel_3x2s', 'TrainWheel_4x2s'],
                br_brick_list['default_brick_data'] | {
                    'bInvertTankSteering': True
                }, True)

append_multiple(br_brick_list, ['Wheel_1sx1sx1s', 'Wheel_1x1x1'], br_brick_list['default_brick_data'], True)


# --------------------------------------------------
# WINDOWS [LAST UPDATE: 1.6.3]
# --------------------------------------------------


append_multiple(br_brick_list,
                ['Panel_1x2x4', 'Panel_1x4x4', 'Panel_1x6x6', 'Windscreen_2x4x2', 'Windscreen_2x4x3',
                 'Windscreen_2x6x2', 'Windscreen_2x6x3', 'Windscreen_2x8x3', 'Windscreen_4x6x3'],
                br_brick_list['default_brick_data'] | {'bGenerateLift': False}, True)


# --------------------------------------------------
# UNCATEGORIZED [LAST UPDATE: 1.6.3]
# --------------------------------------------------

# Arch, Ledges and more
append_multiple(br_brick_list, ['Arch_2x1x2', 'Arch_4x1x2', 'Arch_6x1x1', 'Arch_8x1x8', 'CornerLedge_1x1x1',
                                'Ledge_1x1x1', 'Ledge_1x2x1', 'Ledge_1x4x1', 'PlaneTail_10x10x6'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': False
                }, True)

# Horn
append_multiple(br_brick_list, ['DoubleSiren_1x2x1s'],
                br_brick_list['default_brick_data'] | {
                    'SirenType': 'Car',
                    'HornPitch': 1.0,
                    'InputChannel.InputAxis': BrickInput('Horn', None, 'InputChannel')
                }, True)

# Winch
append_multiple(br_brick_list, ['Winch_3x2x1'],
                br_brick_list['default_brick_data'] | {
                    'InputChannel.InputAxis': BrickInput('Auxiliary', None, 'InputChannel'),
                    'WinchSpeed': 100.0 # 100 = 1 meter/s
                }, True)


# -------------------------------------------------
# PROPERTIES
# --------------------------------------------------

"""
Order for Connector Spacing in UI: [1.6.3]
    [1] [0]
    [3] [2]
    [5] [4]
"""

br_special_property_instance_list = {
    'BrickColor': '4xINT8_r',
    'BrickSize': '3xINT16_r',
    'ConnectorSpacing': '6xINT2',
    'DisplayColor': '3xINT8_r',
    'SmokeColor': '3xINT8_r',
    'SwitchName': 'UTF-16',
    'NumFractionalDigits': 'INT8',
    'ExitLocation': '3xFLOAT32/None',
    'OwningSeat': '1BrickID',
    'ImageColor': '3xINT8_r',
    'Text': 'UTF-16',
    'TextColor': '3xINT8_r'
}