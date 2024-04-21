from BRCI_RF import append_multiple, BrickInput

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
# BRICKS TODO
# --------------------------------------------------


# --------------------------------------------------
# CAMERAS TODO
# --------------------------------------------------


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
# DECORATION TODO
# --------------------------------------------------


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
                    'EnabledInputChannel.InputAxis': BrickInput('AlwaysOn', 1.0, 'EnabledInputChannel'), # TODO
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
# WINDOWS TODO
# --------------------------------------------------


# --------------------------------------------------
# UNCATEGORIZED [LAST UPDATE: 1.6.3]
# --------------------------------------------------

# Archs, Ledges and more
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

append_multiple(br_brick_list, ['Winch_3x2x1'],
                br_brick_list['default_brick_data'] | {
                    'InputChannel.InputAxis': BrickInput('Auxiliary', None, 'InputChannel'),
                    'WinchSpeed': 100.0 # 100 = 1 meter/s
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
    'SmokeColor': '3xINT8',
    'SwitchName': 'UTF-16',
    'NumFractionalDigits': 'INT8',
    'ExitLocation': '3xFLOAT32/None'
}