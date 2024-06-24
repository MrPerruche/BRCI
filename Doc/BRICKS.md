# BRCI Supported Bricks List

## Default Brick Properties

This is a list of properties all bricks (are supposed to) have.  
NAME: `br_brick_list['default_brick_data']`

- `BrickColor` (`[u8, u8, u8, u8] | int`) (`[0, 0, 127, 255]`)
- `BrickPattern` (`str`) (`Default`)
- `BrickMaterial` (`str`) (`Plastic`)
- `Position` (`[f32, f32, f32]`) (`[0, 0, 0]`)
- `Rotation` (`[f32, f32, f32]`) (`[0, 0, 0]`)

## All Properties

This section includes various data about various bricks' properties which we find counter-intuitive.

### `ActuatorMode`
This defines which mode the actuator is being set to. List :
###### In Brick Rigs 1.7.0b* UI order
```
Accumulated
Seeking
Cycle

PhysicsDriven
Spring
Static
```

### `AmmoType`
This property correspond to the ammo type. It is a single string : `AMMO TYPE (str)`. Input list:
##### Guns:
###### In Brick Rigs 1.7.0b* UI order
```
Standard
Incendiary
HighExplosive
```
##### Launchers (aka. Missiles):
###### In Brick Rigs 1.7.0b* UI order
```
Incendiary
HighExplosive
TargetSeeking
Guided
```

### `bAccumulated`
This property correspond to if the brick accumulate its input
(e.g. for flaps if they conserve their current position upon no longer receiving an input)
It is a single boolean : `ACCUMULATED (bool)`.

### `bAccumulateInput`
This property correspond to if the brick accumulate its input
(e.g. for flaps if they conserve their current position upon no longer receiving an input).
It is a single boolean : `ACCUMULATE (bool)`.

### `bCanDisableSteering`
This property correspond to if the axle can be disabled. It is a single boolean : `CAN DISABLE STEERING (bool)`.

### `bCanInvertSteering`
This property correspond to if the axle's direction can be inverted. It is a single boolean : `CAN INVERT STEERING (bool)`.

### `bDriven`
it is a single boolean : `DRIVEN (bool)`

### `bGenerateLift`
This property correspond to if the bricks has fluid dynamics (aka. aero) enabled.
It is a single boolean : `FLUID DYN (bool)`.

### `bHasBrake`
This property correspond to if the axle can brake. It is a single boolean : `HAS BRAKE (bool)`.

### `bHasHandBrake`
This property correspond to if the axle can hand brake. It is a single boolean : `HAS HAND BRAKE (bool)`.

### `bInvertDrive`
It is a single boolean : `INVERT DRIVE (bool)`.

### `bInvertTankSteering`
It is a single boolean : `INVERT TANK STEER (bool)`.

### `BrakeStrength`
This property correspond to the brake's strength. It is a single float 32 : `BRAKE STRENGTH (f32)`.

### `bReturnToZero`
This property corresponds to if the logic brick will return to zero upon end of the input.
It is a single boolean: `RESET (bool)`

### `BrickColor`
This property correspond to the (main) color assigned to the brick. It is common to all bricks*.
It is a list of 4 elements in the following order : `[HUE (u8), SATURATION (u8), VALUE (u8), ALPHA (u8)]`.
It may also instead be an 8 bytes long integer : `0xHHSSVVAA`.

### `BrickMaterial`
This property correspond to what material the brick is made of. It is common to all bricks*.
It is a single string : `MATERIAL (str)`. Input list:
###### In Brick Rigs 1.7.0b* UI order
```
Aluminium
BrushedAlu
Carbon

ChannelledAlu
Chrome
CloudyGlass

Copper
Foam
Glass

Glow
Gold
LEDMatrix

Oak
Pine
Plastic

RoughWood
Rubber
RustedSteel

Steel
Tungsten
```

### `BrickPattern`
This property correspond to what pattern is applied to the brick, and/or if none is being applied.
It is common to all bricks*. It is a single string : `PATTERN (str)`. Input list:
###### In Brick Rigs 1.7.0b* UI order
```
Default
C_Army
C_Army_Digital

C_Autumn
C_Berlin_2
C_Berlin

C_Berlin_Digital
C_Cristal_Contrast
C_Cristal_Red

C_Dark
C_Desert_2
C_Desert

C_Desert_Digital
C_Flecktarn
C_Heat

C_Navy
C_Sharp
C_Sky

C_Sweden
C_Swirl
C_Tiger

C_Urban
C_Yellow
P_Burnt

P_Fire
P_Hexagon
P_Swirl_Arabica

P_Warning
P_Warning_Red
P_YellowCircles
```

### `BrickSize`
This property correspond to the size of the brick. It is NOT common to all bricks.
It is a list of 3 elements in the following order :
`[WIDTH (cm) (f32), HEIGHT (cm) (f32), DEPTH (cm) (f32)]` (It's in UI order).

### `Brightness`
This property correspond to how light a light is (Ratio, not in percents). It is a single float 32 : `BRIGHTNESS (f32)`

### `bTankDrive`
This property correspond to how the engine will interact with the wheels (Regular / Tank drive).
It is a single boolean : `TANK DRIVE (bool)`

### `ConnectorSpacing`
This property correspond to the brick's connector spacing. It is NOT common to all bricks.
It is a list of 6 elements in the following order: `[UM (u2), BM (u2), UL (u2), BL (u2), UR (u2), BR (u2)]`.
These names correspond to their position in Brick Rigs' UI.
`U` stands for Upper, `B` stands for Bottom. `L` stands for Left, `C` stands for Center, `R` stands for Right.
`0` corresponds to None. `1` corresponds to Default. `2` corresponds for Halves. `3` corresponds to Thirds.

### `CouplingMode`
This property correspond to the coupling mode. It is a single string : `COUPLING MODE (str)`. Input list:
###### In Brick Rigs 1.7.0b* UI order
```
Default
Static
```

### `DisplayColor`
This property correspond to the display's digits color.
It is a list of 3 unsigned 8-bit int values in the following order : `[HUE (u8), SATURATION (u8), VALUE (u8)]`.
It may also instead be a 6 bytes long integer : `0xHHSSVV`.

### `ExitLocation`
This property correspond to custom exit location (if enabled).
It may either be a NoneType (`None`), meaning custom exit location is disabled,
or a list of 3 float 32 values in the following order : `[X (cm) (f32), Y (cm) (f32), Z (cm) (f32)]`.

### `FlashSequence`
This property correspond to the light's flash sequence. It is a single string : `FLASH SEQUENCE (str)`. Input list:
###### In Brick Rigs 1.7.0b* UI order
```
None
Blinker_Sequence
Blinker_Sequence_Inverted

DoubleFlash_Inverted_Sequence
DoubleFlash_Sequence
RunningLight_01_Inverted_Sequence

RunningLight_01_Sequence
RunningLight_02_Inverted_Sequence
RunningLight_02_Sequence

RunningLight_03_Inverted_Sequence
RunningLight_03_Sequence
RunningLight_04_Inverted_Sequence

RunningLight_04_Sequence
Strobe_Sequence
```

### `Font`
This property correspond to what font is applied to the text brick. It is a single string : `FONT (str)`. Input list:
```
BigShouldersStencil
NotoEmoji
Orbitron

PermanentMarker
Roboto
RobotoSerif

Silkscreen
```

### `FontSize`
This property correspond to the font's size. It is a single float 32: `FONT SIZE (f32)`.

### `FuelType`
This property correspond to what fuel is inside the fuel tank. It is a single string : `FUEL TYPE (str)`. Input list:
###### In Brick Rigs 1.7.0b* UI order
```
C4
Nitro
Petrol

RocketFuel
```

### `gbn` (BRCI Component)
This is not a property in Brick Rigs. It is not handled as a property by BRCI.
It is used to indicate BRCI what brick this variable is corresponding to. Example : `AircraftR4`.
Modifying it would cause issues in-game, since properties the BRCI is trying to apply may not correspond to the brick's.
Modification of this element is therefore not recommended.
If BRCI encounters any invalid property, one of the following errors may occur :
BRCI failing to generate the creation; Brick Rigs failing to load the creation, leading to a corrupted file error;
Defined values not corresponding to what's expected.
Modifying this "property" will not in any way update this brick's property list. To change what brick type your variable
is defined to, use `create_brick(brick_type)` again. Be aware this command will clear any previously edited properties

### `GearRatioScale`
This property correspond to the engine's gear ratio. It is a single float 32 : `GEAR RATIO (f32)`

### `HornPitch`
This property correspond to the pitch of the horn. It is a single float 32 : `HORN PITCH (f32)`.

### `IdlerWheels`
This corresponds to what wheels the sprocket will use. It is a list of IDs (Strings or integers) : `WHEELS (int|str)`

### `Image`
This property corresponds to what image is being displayed. It is a single string `IMAGE (str)`. Input list:
###### In Brick Rigs 1.7.0b* UI order
```
Arrow
Biohazard
BRAF

BrickRigs
BrickRigsArms
Caution

Criminals
Crosshair
DesertWorms

Dummy
ElectricHazard
ExplosiveHazard

FireDept
FireHazard

Gauge
Limit80
NoEntrance

OneWay
Phone
Police

Radioactive
Star
Stop

Tank
Virus
```

### `ImageColor`
This property correspond to what color the image is given.
It is a list of 3 unsigned 8-bit int values in the following order : `[HUE (u8), SATURATION (u8), VALUE (u8)]`.
It may also instead be a 6 bytes long integer : `0xHHSSVV`.

### `InputScale`
This property corresponds to what is technically referred as input scale. It is however counterintuitive,
as it refers to various things related to the brick's efficiency (thrust, speed etc.).
It is a single float 32 : `INPUT SCALE (f32)`.

### `LightConeAngle`
This property correspond to a light's cone angle. It is a single float 32 : `LIGHT CONE ANGLE (f32)`

### `LightDirection`
This property correspond to the light's direction. It is a single string : `LIGHT DIRECTION (str)`. Input list:
```
Off
Omnidirectional

X
XNeg

Y
YNeg

Z
ZNeg
```

### `MaxAngle`
This property correspond to the maximum angle (degrees) a brick can actuate to. Please not in some bricks this property
is under the name "MaxLimit". It is a single float 32 : `MAX ANGLE (f32)`.

### `MaxLimit`
This property corresponds to the maximum angle (degrees) or length (centimeters) the actuator can actuate to.
It is a single float 32 : `MAX LIMIT (f32)`.

### `MinAngle`
This property correspond to the minimum angle (degrees) a brick can actuate to. Please not in some bricks this property
is under the name "MinLimit". It is a single float 32 : `MIN ANGLE (f32)`.

### `MinLimit`
This property correspond to the minimum angle (degrees) or length (centimeters) the actuator can actuate to.
It is a single float 32 : `MIN LIMIT (f32)`.

### `NumFractionalDigits`
This property correspond to the number of fractional digits. It is a single float 32 : `DIGITS (f32)`.

### `Operation`
This property correspond to the actuator's operation. It is a single string : `OPERATION (str)`. Input list:
###### In Brick Rigs 1.7.0b* UI order
```
Add
Subtract
Multiply

Divide
Fmod
Power

Greater
Less
Min

Max
Abs
Sign

Round
Ceil
Floor

Sqrt
SinDeg
Sin

AsinDeg
Asin
CosDeg

Cos
AcosDeg
Acos

TanDeg
Tan
AtanDeg

Atan
```

###  `OutlineThickness`
This property correspond to how thick the text's outline is. It is a single float : `OUTLINE (f32)`

### `OutputChannel.MinIn`, `OutputChannel.MaxIn`, `OutputChannel.MinOut`, `OutputChannel.MaxOut` 
These properties correspond to the brick's output channel scaling values.
Each are a single float 32 value : `VALUE (f32)`

### `OwningSeat`
This property correspond to what seat can access that brick. It is a single string corresponding to a brick's name or
a None (Which allows all seats to access it) : `SEAT (str)`

### `Position`
This "property" correspond to the brick's position in centimeters.
Although position is defined as a property in BRCI, it is not a property in Brick Rigs. It is common to all bricks.
It is a list of 3 elements corresponding to the brick's distance from origin in centimeters, in the following order:
`[POS_X (cm) (f32), POS_Y (cm) (f32), POS_Z (cm) (f32)]`.

### `Rotation`
This "property" correspond to the brick's rotation in degrees.
Although rotation is defined as a property in BRCI, it is not a property in Brick Rigs. It is common to all bricks.
It is a list of 3 elements corresponding to the brick's rotation relative to the origin in degrees,
in the following order: `[ROT_Y (deg) (f32), ROT_Z (deg) (f32), ROT_X (deg) (f32)]`.

### `SensorType`
This property correspond to the sensor's type. It is a single string : `SENSOR TYPE (str)`. Input list:
###### In Brick Rigs 1.7.0b UI order
```
Speed
NormalSpeed
Acceleration

NormalAcceleration
AngularSpeed
NormalAngularSpeed

Distance
Time
Proximity

DistanceToGround
Altitude
Pitch

Yaw
Roll
NumSeekingProjectiles

SeekingProjectilesDistance
```

### `SirenType`
This property correspond to what siren is being played. It is a single string : `SIREN (str)`. Input list:
```
Car
EmsUS
FireDeptGerman
PoliceGerman
TruckHorn
```

### `SmokeColor`
This property correspond to the smoke color.
It is a list of 3 elements in the following order: `[HUE (u8), SATURATION (u8), VALUE (u8)]`.
It may also instead be a 6 bytes long integer : `0xHHSSVV`.

### `SpawnScale`
This property correspond to the spawn rate of particles. It is a single float 32 : `SPAWN RATE (f32)`.

### `SpeedFactor`
This property correspond to actuators' speed. It is a single float 32 : `SPEED (f32)`.

### `SteeringAngle`
This property correspond to the maximum angle at which the axle will rotate the wheel.
It is a single float 32 : `STEERING ANGLE (deg) (f32)`.

### `SteeringSpeed`
This property correspond to the speed at which the axle will rotate the wheel.
It is a single float 32 : `STEERING SPEED (f32)`.

### `SuspensionDamping`
This property correspond to the suspension's damping. It is a single float 32 : `SUSPENSION DAMPING (f32)`.

### `SuspensionLength`
This property correspond to the suspension's maximum length. It is a single float 32 : `SUSPENSION LENGTH (f32)`.

### `SuspensionStiffness`
This property correspond to the suspension's stiffness. It is a single float 32 : `SUSPENSION STIFFNESS (f32)`.

### `SwitchName`
This property correspond to the switch's name. It is a single string (supports utf-16) : `TEXT (str)`

### `Text`
This property correspond to the text. It is a single string (supports utf-16) : `TEXT (str)`

### `TextColor`
This property correspond to the text's color.
It is a list of 3 elements in the following order: `[HUE (u8), SATURATION (u8), VALUE (u8)]`.
It may also instead be a 6 bytes long integer : `0xHHSSVV`.

### `TirePressureRatio`
This property correspond to how much pressure is in the tire. It is a single float 32 : `PRESSURE (f32)`

### `TireThickness`
This property correspond to how thick the wheel's tire is. It is a single float 32 : `THICKNESS (f32)`

### `TraceMask`
This property correspond to what mask is applied to a sensor.
It can only be applied to sensors set on the 'Proximity' setting.
It is a single string : `TRACE MASK (str)` Input list:
```
All
Static
Vehicles

OtherVehicles
Pawn
Water
```

### `TrackColor`
This property correspond to what color is assigned to your tracks. It is a list of 4 unsigned 8-bit integers:
`[HUE (u8), SATURATION (u8), VALUE (u8), ALPHA (u8)]`.

### `WheelDiameter`
This property correspond to the wheel's diameter. It is a single float : `DIAMETER (f32)`

### `WheelWidth`
This property corresponds to the wheel's width. It is a single float : `WIDTH (f32)`

### `WinchSpeed`
This property correspond to the winch's speed. 100 corresponds to 1 meter per second (3.6 km/h).
It is a single float 32 : `SPEED (f32)`

### Other :

It may be an input, or a modded property.

If it is an input (They often contain `InputChannel` in their name):

This property corresponds to the brick's input : Either another brick, a constant value, throttle etc.
It has various prefixes depending on the brick (such as `AutoHoverInputChannel` etc.).
It is set to the BrickInput class (custom class) : `INPUT (BrickInput(brick_input_type: str, brick_input: any, prefix: str))`.
Unlike previous versions of BRCI, `BrickInput()` now care about the name of the property it is assigned to.
It has 3 arguments :
`brick_input_type`: the input type;
`brick_input`: may be the input value, or source bricks, or anything else.
`prefix`: this is automatically set by BRCI. You may ignore it or set it to anything.
Input list:
###### In Brick Rigs 1.7.0b UI order
```
BrickInput('None', brick_input, prefix)........... : None (can be anything), prefix
BrickInput('AlwaysOn', brick_input, prefix)....... : Value (f32), prefix
BrickInput('Custom', brick_input, prefix)......... : List of all str brick names (list[str]), prefix

BrickInput('Steering', brick_input, prefix)....... : List of all str brick names (list[str]), prefix
BrickInput('SteeringAlt', brick_input, prefix).... : List of all str brick names (list[str]), prefix
BrickInput('Throttle', brick_input, prefix)....... : List of all str brick names (list[str]), prefix

BrickInput('ThrottleAlt', brick_input, prefix).... : List of all str brick names (list[str]), prefix
BrickInput('Brake', brick_input, prefix).......... : List of all str brick names (list[str]), prefix
BrickInput('BrakeAlt', brick_input, prefix)....... : List of all str brick names (list[str]), prefix

BrickInput('Auxiliary', brick_input, prefix)...... : List of all str brick names (list[str]), prefix
BrickInput('AuxiliaryAlt', brick_input, prefix)... : List of all str brick names (list[str]), prefix
BrickInput('ViewPitch', brick_input, prefix)...... : List of all str brick names (list[str]), prefix

BrickInput('ViewPitchAlt', brick_input, prefix)... : List of all str brick names (list[str]), prefix
BrickInput('ViewYaw', brick_input, prefix)........ : List of all str brick names (list[str]), prefix
BrickInput('ViewYawAlt', brick_input, prefix)..... : List of all str brick names (list[str]), prefix

BrickInput('Horn', brick_input, prefix)........... : List of all str brick names (list[str]), prefix
BrickInput('DisableSteering', brick_input, prefix) : List of all str brick names (list[str]), prefix
BrickInput('InvertSteering', brick_input, prefix). : List of all str brick names (list[str]), prefix

BrickInput('HandBrake', brick_input, prefix)...... : List of all str brick names (list[str]), prefix
BrickInput('OperationMode', brick_input, prefix).. : List of all str brick names (list[str]), prefix
BrickInput('Headlight', brick_input, prefix)...... : List of all str brick names (list[str]), prefix

BrickInput('Beacon', brick_input, prefix)......... : List of all str brick names (list[str]), prefix
BrickInput('WarningLight', brick_input, prefix)... : List of all str brick names (list[str]), prefix
BrickInput('Taillight', brick_input, prefix)...... : List of all str brick names (list[str]), prefix

BrickInput('BrakeLight', brick_input, prefix)..... : List of all str brick names (list[str]), prefix
BrickInput('ReversingLight', brick_input, prefix). : List of all str brick names (list[str]), prefix
BrickInput('Action1', brick_input, prefix)........ : List of all str brick names (list[str]), prefix

BrickInput('Action2', brick_input, prefix)........ : List of all str brick names (list[str]), prefix
BrickInput('Action3', brick_input, prefix)........ : List of all str brick names (list[str]), prefix
BrickInput('Action4', brick_input, prefix)........ : List of all str brick names (list[str]), prefix

BrickInput('Action5', brick_input, prefix)........ : List of all str brick names (list[str]), prefix
BrickInput('Action6', brick_input, prefix)........ : List of all str brick names (list[str]), prefix
BrickInput('Action7', brick_input, prefix)........ : List of all str brick names (list[str]), prefix

BrickInput('Action8', brick_input, prefix)........ : List of all str brick names (list[str]), prefix
```

## Actuators

###### In Brick Rigs 1.7.0b* UI order
```
Actuator_1sx1sx1s_02_Top...... : A
Actuator_1sx1sx1s_Bottom...... : B
Actuator_1sx1sx1s_Female...... : B

Actuator_1sx1sx1s_Male........ : A
Actuator_1sx1sx1s_Top......... : A
Actuator_1sx1sx2s_Bottom...... : B

Actuator_1sx1sx2s_Top......... : A
Actuator_1x1sx1s_Bottom....... : B
Actuator_1x1x1s_Bottom........ : B

Actuator_1x1x1s_Top........... : A
Actuator_1x1x1_Bottom......... : B
Actuator_1x1x1_Top............ : A

Actuator_1x1x3_Bottom......... : B
Actuator_1x1x3_Top............ : A
Actuator_1x1x6_Bottom......... : B

Actuator_1x1x6_Top............ : A
Actuator_2x1sx1s_Bottom....... : B
Actuator_2x1x1s_02_Bottom..... : B

Actuator_2x1x1s_02_Top........ : A
Actuator_2x1x1s_Bottom........ : B
Actuator_2x1x1s_Female........ : B

Actuator_2x1x1s_Male.......... : A
Actuator_2x1x1s_Top........... : A
Actuator_2x2x1s_Angular_Bottom : B

Actuator_2x2x1s_Angular_Top... : A
Actuator_2x2x1s_Bottom........ : B
Actuator_2x2x1s_Top........... : A

Actuator_2x2x2_Bottom......... : B
Actuator_2x2x2_Top............ : A
Actuator_2x2x15_Bottom........ : B

Actuator_2x2x15_Top........... : A
Actuator_4x1x1s_Bottom........ : B
Actuator_4x1x1s_Top........... : A

Actuator_4x4x1s_Bottom........ : B
Actuator_4x4x1s_Top........... : A
Actuator_6x2x1s_Bottom........ : B

Actuator_6x2x1s_Top........... : A
Actuator_8x8x1_Bottom......... : B
Actuator_8x8x1_Top............ : A

Actuator_20x2x1s_Bottom....... : B
Actuator_20x2x1s_Top.......... : A
```

#### Properties : A
- Default Brick Properties

#### Properties : B
- Default Brick Properties
- `ActuatorMode` (`str`) (`'Accumulated'`)
- `InputChannel` (`BrickInput()`) (`BrickInput('Auxiliary', None)`)
- `SpeedFactor` (`f32`) (`1.0`)
- `MinLimit` (`f32`) (`0.0`)
- `MaxLimit` (`f32`) (`0.0`)

## Aviation

###### In Brick Rigs 1.7.0b* UI order

```
BladeHolder_2x1..... : A
Flap_1x4x1s......... : B
Flap_2x8x1s......... : B

Turbine_6x2x2....... : C
Turbine_8x4x2....... : C
Turbine_12x8x5...... : C

Prop_5x1............ : A
Prop_10x1........... : A
Rotor_3x4........... : A

Rotor_4x8........... : A
Blade_20x2.......... : A
Blade_26x2.......... : A

Wing_2x2x1s......... : D
Wing_2x2x1s_L....... : D
Wing_2x2x1s_R....... : D

WingRounded_2x2x1s.. : D
Wing_2x3x1s......... : D
Wing_2x3x1s_L....... : D

Wing_2x3x1s_R....... : D
Wing_2x4x1s_L....... : D
Wing_2x4x1s_R....... : D

Wing_3x3x1s......... : D
Wing_4x8x1s_L....... : D
Wing_4x8x1s_R....... : D

Wing_4x10x1s........ : D
Wing_6x10x1s_L...... : D
Wing_6x10x1s_R...... : D
```

#### Properties : A
- Default Brick Properties

#### Properties : B
- Default Brick Properties
- `bGenerateLift` (`bool`) (`True`)
- `InputChannel` (`BrickInput()`) (`BrickInput('None', None)`)
- `InputScale` (`f32`) (`100.0`)
- `MinAngle` (`f32`) (`-22.5`)
- `MaxAngle` (`f32`) (`22.5`)
- `bAccumulateInput` (`bool`) (`False`)

#### Properties : C
- Default Brick Properties
- `PowerInputChannel` (`BrickInput()`) (`BrickInput('OperationMode', None)`)
- `AutoHoverInputChannel` (`BrickInput()`) (`BrickInput('DisableSteering', None)`)
- `ThrottleInputChannel` (`BrickInput()`) (`BrickInput('ThrottleAlt', None)`)
- `PitchInputChannel` (`BrickInput()`) (`BrickInput('ViewPitchAlt', None)`)
- `YawInputChannel` (`BrickInput()`) (`BrickInput('SteeringAlt', None)`)
- `RollInputChannel` (`BrickInput()`) (`BrickInput('ViewYawAlt', None)`)

#### Properties : D
- Default Brick Properties
- `bGenerateLift` (`bool`) (`True`)

## Bricks

###### In Brick Rigs 1.6.3 UI order
```
[Folder]
[Folder]
[Folder]

[Folder]
[Folder]
[Folder]

[Folder]
Brick_1x1x1s............. : A
Brick_1x1x1s_Flat........ : A

Brick_1x1x1.............. : A
Brick_1x1x3.............. : A
Brick_1x1x4.............. : A

Brick_1x1x6.............. : A
Brick_2x1x1s............. : A
Brick_2x1x1s_Flat........ : A

BrickRounded_2x1x1s...... : A
BrickRounded_2x1x1s_Flat. : A
Brick_2x1x1.............. : A

Brick_2x1x6.............. : A
Brick_2x2x1s............. : A
Brick_2x2x1s_Flat........ : A

BrickRoundedCorner_2x2x1s : A
CornerBrick_2x2x1s....... : A
Brick_2x2x1.............. : A

CornerBrick_2x2x1........ : A
Brick_3x1x1s............. : A
Brick_3x1x1s_Flat........ : A

BrickRounded_3x1x1s...... : A
BrickRounded_3x1x1s_Flat. : A
Brick_3x1x1.............. : A

Brick_3x2x1s............. : A
Brick_3x2x1s_Flat........ : A
Brick_3x2x1.............. : A

Brick_4x1x1s............. : A
Brick_4x1x1s_Flat........ : A
BrickRounded_4x1x1s...... : A

BrickRounded_4x1x1s_Flat. : A
Brick_4x1x1.............. : A
Brick_4x2x1s............. : A

Brick_4x4x1s_Flat........ : A
Brick_5x1x1s............. : A
Brick_5x1x1s_Flat........ : A

BrickRounded_5x1x1s...... : A
BrickRounded_5x1x1s_Flat. : A
Brick_5x1x1.............. : A

Brick_5x2x1s............. : A
Brick_5x2x1s_Flat........ : A
Brick_5x2x1.............. : A

Brick_6x1x1s............. : A
Brick_6x1x1s_Flat........ : A
BrickRounded_6x1x1s...... : A

BrickRounded_6x1x1s_Flat. : A
Brick_6x1x1.............. : A
Brick_6x2x1s............. : A

Brick_6x2x1s_Flat........ : A
Brick_6x2x1.............. : A
Weight_6x2x3............. : A

Brick_6x4x1s............. : A
Brick_6x4x1s_Flat........ : A
Brick_6x6x1s............. : A

Brick_6x6x1s_Flat........ : A
Brick_8x1x1s............. : A
Brick_8x1x1s_Flat........ : A

BrickRounded_8x1x1s...... : A
BrickRounded_8x1x1s_Flat. : A
Brick_8x1x1.............. : A

Brick_8x2x1s............. : A
Brick_8x2x1s_Flat........ : A
Brick_8x2x1.............. : A

Brick_8x4x1s............. : A
Brick_8x4x1s_Flat........ : A
Brick_8x6x1s............. : A

Brick_8x6x1s_Flat........ : A
Brick_8x8x1s............. : A
Brick_8x8x1s_Flat........ : A

Brick_10x1x1s............ : A
Brick_10x1x1............. : A
Brick_10x2x1s............ : A

Brick_10x2x1s_Flat....... : A
Brick_10x2x1............. : A
Brick_10x4x1s............ : A

Brick_10x4x1s_Flat....... : A
Brick_10x6x1s............ : A
Brick_10x6x1s_Flat....... : A

Brick_10x8x1s............ : A
Brick_10x8x1s_Flat....... : A
Brick_12x1x1s............ : A

Brick_12x1x1............. : A
Brick_12x6x1s............ : A
Brick_12x6x1s_Flat....... : A

Brick_12x8x1s............ : A
Brick_12x8x1s_Flat....... : A
Brick_12x12x1............ : A

Brick_16x1x1............. : A
Brick_16x8x1s............ : A
Brick_16x8x1s_Flat....... : A

Brick_20x1x1............. : A
Brick_24x12x1............ : A
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)


## Cameras

###### In Brick Rigs 1.7.0b UI Order

```
Camera_1sx1sx1s.. : A
Camera_2x1x1..... : A
TargetMaker_1x1x1 : A
```

#### Properties : A
- Default Brick Properties
- `OwningSeat` (`str | None`) (`None`) 


## Couplings

###### In Brick Rigs 1.7.0b UI order
```
Coupling_1sx1sx1s_Front_Female : A
Coupling_1sx1sx1s_Front_Male.. : B
Coupling_1x1x1s_Front_Female.. : A

Coupling_1x1x1s_Front_Male.... : B
Coupling_2x2x1s_Female........ : A
Coupling_2x2x1s_Front_Female.. : A

Coupling_2x2x1s_Front_Male.... : B
Coupling_2x2x1s_Male.......... : B
Coupling_4x1x2s_Bottom........ : B

Coupling_4x1x2s_Top........... : A
Coupling_6x2x1s_Male.......... : B
```

#### Properties : A
- Default Brick Properties

#### Properties : B
- Default Brick Properties
- `CouplingMode` (`str`) (`Default`)
- `InputChannel` (`BrickInput()`) (`BrickInput('None', None)`)


## Decoration

###### In Brick Rigs 1.6.3 UI order
```
ImageBrick............ : A
ImageCylinder......... : A
Flag_3x1x2............ : B

TextBrick............. : C
TextCylinder.......... : C
Antenna_1x1x8......... : D

Antenna_2x1x1s........ : D
Bumper_4sx6x2......... : E
Bumper_4sx8x7s........ : E

Door_L_3x1x1.......... : E
Door_R_3x1x1.......... : E
Door_L_3x1x2.......... : E

Door_R_3x1x2.......... : E
WindowedDoor_L_3x1x4.. : E
WindowedDoor_R_3x1x4.. : E

Grid_2x1x1s_02........ : E
Grid_2x1x1s........... : E
GridZylinder_2x2x1s... : E

Handle_1x2x4s......... : D
Handle_4x1x1.......... : D
SteeringWheel_5sx5sx1s : E

SteeringWheel_2x2x1s.. : E
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)
- `BrickSize` (`list[float, float, float]`) (`[6.0, 6.0, 1.0]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 0, 3]`)
- `Image` (`str`) (`'Arrow'`)
- `ImageColor` (`list[int, int, int]`) (`[0, 0, 255]`)

#### Properties : B
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)
- `BrickSize` (`list[float, float, float]`) (`[6.0, 1.0, 6.0]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 0, 3]`)
- `Image` (`str`) (`'Arrow'`)
- `ImageColor` (`list[int, int, int]`) (`[0, 0, 255]`)

#### Properties : C
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)
- `BrickSize` (`list[float, float, float]`) (`[6.0, 6.0, 1.0]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 0, 3]`)

#### Properties : D
- Default Brick Properties

#### Properties : E
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

## Fire and Water

###### In Brick Rigs 1.6.3 UI order
```
Float............. : A
Detonator_1x1x1s.. : B
PumpZylinder_2x2x2 : C

Tank_1x1x1........ : D
Tank_2x2x1........ : D
Tank_2x2x4........ : D
```

#### Properties : A
- Default Brick Properties
- `BrickSize` (`[u16, u16, u16]`) (`[3, 3, 3]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 3, 3]`)

#### Properties : B
- Default Brick Properties
- `InputChannel` (`BrickInput()`) (`BrickInput('Action1', None)`)

#### Properties : C
- Default Brick Properties
- `InputChannel` (`BrickInput()`) (`BrickInput('None', None)`)

#### Properties : D
- Default Brick Properties
- `FuelType` (`str`) (`'Petrol'`)

## Guns
```
Barrel_1sx1sx3..... : A
Barrel_1x1x4....... : A
Barrel_1x1x4_Flat.. : A

Flamethrower_2x2x2. : B
Gun_2x1x1.......... : C
Gun_2x2x2_Ballistic : C

Gun_2x2x2.......... : C
Gun_4x2x2.......... : C
```

#### Properties : A
- Default Brick Properties

#### Properties : B
- Default Brick Properties
- `InputChannel` (`BrickInput()`) (`BrickInput('Action1', None)`)

#### Properties : C
- Default Brick Properties
- `InputChannel` (`BrickInput()`) (`BrickInput('Action2', None)`)
- `AmmoType` (`str`) (`Standard`)

## Input and Output

###### In Brick Rigs 1.6.3 UI order
```
DisplayBrick...... : A
MathBrick_1sx1sx1s : B
Sensor_1sx1sx1s... : C

Sensor_1x1x1s..... : C
Switch_1sx1sx1s... : D
Switch_1x1x1s..... : D
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)
- `BrickSize` (`[u16, u16, u16]`) (`[6, 3, 1]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 3, 0]`)
- `InputChannel` (`BrickInput()`) (`BrickInput('Custom', None)`)
- `NumFractionalDigits` (`u8`) (`1`)
- `DisplayColor` (`[u8, u8, u8] | int`) (`[0, 204, 128]`)

#### Properties : B
- Default Brick Properties
- `Operation`: (`str`) (`Add`)
- `InputChannelA`: (`BrickInput()`) (`BrickInput('Custom', None)`)
- `InputChannelB`: (`BrickInput()`) (`BrickInput('AlwaysOn', 1.0)`)

#### Properties : C
- Default Brick Properties
- `OutputChannel.MinIn` (`f32`) (`-1.0`)
- `OutputChannel.MaxIn` (`f32`) (`1.0`)
- `OutputChannel.MinOut` (`f32`) (`-1.0`)
- `OutputChannel.MaxOut` (`f32`) (`1.0`)
- `EnabledInputChannel` (`BrickInput()`) (`BrickInput('AlwaysOn', 1.0)`)
- `SensorType` (`str`) (`'Speed'`)
- `TraceMask` (`str`) (`'All'`)
- `bReturnToZero` (`bool`) (`False`)

#### Properties : D
- Default Brick Properties
- `OutputChannel.MinIn` (`f32`) (`-1.0`)
- `OutputChannel.MaxIn` (`f32`) (`1.0`)
- `OutputChannel.MinOut` (`f32`) (`-1.0`)
- `OutputChannel.MaxOut` (`f32`) (`1.0`)
- `InputChannel` (`BrickInput()`) (`BrickInput('None', None)`),
- `bReturnToZero` (`bool`) (`True`)
- `SwitchName` (`str`) (`''`)

## Light

###### In Brick Rigs 1.6.3 UI order
```
LightBrick....... : A
LightCone........ : A
LightConeFlat.... : A

LightCylinder.... : A
LightHemisphere.. : A
LightRamp........ : A

LightRampRounded. : A
LightRampRoundedN : A
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)
- `BrickSize` (`[f32, f32, f32]`) (`[3.0, 3.0, 3.0]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 3, 3]`)
- `InputChannel` (`BrickInput()`) (`BrickInput('Headlight', None)`)
- `Brightness` (`f32`) (`0.5`)
- `FlashSequence` (`str`) (`'None'`)
- `LightDirection` (`str`) (`'Off'`)
- `LightConeAngle` (`f32`) (`45.0`)

## Player

###### In Brick Rigs 1.6.3 UI order
```
RemoteController_2x1x1s : A
Seat_2x2x7s............ : B
Seat_3x2x2............. : B

Seat_5x2x1s............ : B
SteeringWheel_5sx5sx1s. : C
SteeringWheel_2x2x1s... : C
```

#### Properties : A
- Default Brick Properties

#### Properties : B
- Default Brick Properties
- `ExitLocation` (`None` or `[f32, f32, f32]`) (`None`)

#### Properties : C
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

## Ramps

###### In Brick Rigs 1.6.3 UI order
```
[Folder]
[Folder]
[Folder]

[Folder]
Ramp_1x1x2s........... : B
RampRounded_1x1x2s.... : B

CornerRamp_1x1x1...... : A
CornerRounded_1x1x1... : A
Ramp_1x1x1............ : B

RampN_1x1x1........... : B
RampRounded_1x1x1..... : B
RampRoundedN_1x1x1.... : A

Ramp_1x2x2s........... : B
RampRounded_1x2x2s.... : B
Ramp_1x2x1............ : B

RampRounded_1x2x1..... : B
Ramp_1x4x2s........... : B
RampRounded_1x4x2s.... : B

Ramp_1x4x1............ : B
RampRounded_1x4x1..... : B
Ramp_2x1x1_02......... : B

Ramp_2x1x1............ : B
RampN_2x1x1........... : B
RampRounded_2x1x1..... : B

Trapezoid_2x1x1....... : B
Ramp_2x1x2............ : B
RampN_2x1x2........... : B

RampRoundedN_2x1x2.... : B
Ramp_2x1x3............ : B
RampN_2x1x3........... : B

Ramp_2x1x4............ : B
RampN_2x1x4........... : B
CornerRamp_2x2x1_02... : A

CornerRamp_2x2x1...... : A
CornerRampN_2x2x1..... : A
CornerRounded_2x2x1_02 : A

CornerRounded_2x2x1... : B
Ramp_2x2x1............ : B
RampN_2x2x1........... : B

Ramp_2x4x1............ : B
RampN_2x4x1........... : B
RampRounded_3x1x2s.... : B

DoubleRamp_3x1x1...... : B
DoubleRampN_3x1x1..... : B
Ramp_3x1x1_02......... : B

Ramp_3x1x1............ : B
RampN_3x1x1........... : B
CornerRamp_3x2x1_L.... : A

CornerRamp_3x2x1_R.... : A
Ramp_3x2x1............ : B
RampN_3x2x1........... : B

CornerRamp_3x3x1...... : B
Ramp_3x4x1............ : B
RampN_3x4x1........... : B

RampRounded_4x1x2s.... : B
RampRoundedN_4x2x4.... : B
CornerRamp_4x3x1_L.... : B

CornerRamp_4x3x1_R.... : B
CornerRamp_4x4x1...... : B
CornerRamp_5x3x1_L.... : B

CornerRamp_5x3x1_R.... : B
```

#### Properties : A
- Default Brick Properties

#### Properties : B
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

## Redirectors

###### In Brick Rigs 1.6.3 UI order

```
Redirector_1x1x0............ : A
CornerBrick_1x1x1s_Flat..... : A
Redirector_1x1x1s_02........ : A

Redirector_1x1x1s........... : A
RedirectorZylinder_1x1x1s_02 : A
RedirectorZylinder_1x1x1s... : A

Redirector_1x1x1_02......... : A
Redirector_1x1x1_03......... : A
Redirecotr_1x1x1_04......... : A

Redirector_1x1x1............ : A
Redirector_4sx1x1........... : A
Redirector_4sx1x4s.......... : A

Redirector_4sx4x1........... : A
Redirector_4sx6x1........... : A
Redirector_2x1x1s_02........ : A

Redirector_2x1x1s_03........ : A
Redirector_2x1x1s_04........ : A
Redirector_2x1x1s........... : A

RedirectorZylinder_2x2x1s_02 : A
RedirectorZylinder_2x2x1s... : A
Octagon_2x4x4s.............. : A

Redirector_3x2x1s_02........ : A
Redirector_3x2x1s........... : A
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

## Rods

###### In Brick Rigs 1.6.3 UI order
```
Rod_1x1x1. : A
Rod_1x1x2. : A
Rod_1x1x3. : A

Rod_1x1x4. : A
Rod_1x1x6. : A
Rod_1x1x8. : A

Rod_1x1x10 : A
Rod_1x1x12 : A
Rod_1x1x16 : A

Rod_1x1x20 : A
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

## Round Stuff

###### In Brick Rigs 1.6.3 UI order
```
Cone_1x1x1.......... : A
Cone_2x2x2.......... : A
Cone_4x4x4.......... : A

Zylinder_1x1x1s..... : A
Zylinder_1x1x1s_Flat : A
Zylinder_1x1x1...... : A

Zylinder_2x2x1s..... : A
Zylinder_2x2x1s_Flat : A
Zylinder_2x2x1...... : A

Zylinder_2x2x4s..... : A
HalfZylinder_4x2x4.. : A
HalfSphere_1x1...... : A

HalfSphere_2x2x1.... : A
HalfSphere_4x4x2.... : A
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

## Scalable Bricks

###### In Brick Rigs 1.6.3 UI order

```
ScalableBrick............... : A
ScalableCone................ : A
ScalableConeRounded......... : A

ScalableConeFlat............ : A
ScalableCorner.............. : B
ScalableCornerN............. : B
ScalableCornerRounded....... : B

ScalableCornerRoundedN...... : B
ScalableZylinder............ : A
ScalableCylinder90R0........ : A

ScalableCylinder90R1........ : A
ScalableHalfCone............ : A
ScalableHalfCylinder........ : A

ScalableHemisphere.......... : A
ScalablePyramid............. : A
ScalablePyramidCorner....... : B

ScalablePyramidCornerRounded : B
ScalableQuarterCone......... : B
ScalableQuarterSphere....... : A

ScalableRamp................ : A
ScalableRampRounded......... : A
ScalableRampRoundedN........ : A

ScalableWedge............... : A
ScalableWedgeCorner......... : A

```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)
- `BrickSize` (`[f32, f32, f32]`) (`[3.0, 3.0, 3.0]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 3, 3]`)

#### Properties : B
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`) Note: Cannot always be enabled.
- `BrickSize` (`[f32, f32, f32]`) (`[3.0, 3.0, 3.0]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 3, 3]`)

## Thrusters

###### In Brick Rigs 1.6.3 UI order

```
Thruster_1sx1sx1s : A
Thruster_1x1x1... : A
Thruster_1x1x3... : A

Thruster_2x2x4... : A
Tank_1x1x1....... : B
Tank_2x2x1....... : B

Tank_2x2x4....... : B
```

#### Properties : A
- Default Brick Properties
- `InputChannel` (`BrickInput()`) (`BrickInput('Throttle', None)`)
- `InputScale` (`f32`) (`1.0`)
- `bAccumulated` (`bool`) (`False`)

#### Properties : B
- Default Brick Properties
- `FuelType` (`str`) (`Petrol`)

## Vehicle

###### In Brick Rigs 1.7.0b UI order

```
ExhaustBrick..... : A
ExhaustCylinder.. : A
Axle_1sx1sx1s.... : B

Axle_1x1x1s_02... : B
Axle_1x1x1s...... : B
Axle_1x2x1s...... : B

Axle_2x2x1s...... : B
Axle_2x2x1....... : B
LandingGear_2x2x2 : B

Axle_2x4x1s...... : B
Axle_2x6x1s...... : B
Compressor_4x1x4s : C

Motor_1x2x5s..... : D
EMotor_2x2x2..... : D
Motor_3x2x5s..... : D

AircraftR4....... : D
Motor_4x2x5s..... : D
DragV8........... : D

DieselV12........ : D
Mudguard_2x1sx3.. : C
Mudguard_2x1x1s.. : C

Mudguard_2x2x2s.. : C
Mudguard_4x2x5s.. : C
Tank_1x1x1....... : F

Tank_2x2x1....... : F
Tank_2x2x4....... : F
Wheel_2x2s....... : G

RacingWheel_4x2s. : H
Wheel_7sx2....... : I
Wheel_10sx1...... : J

OffroadWheel_3x4s : K
RacingWheel_3x4s. : T
Wheel_3x4s....... : U

DragWheel_4x2.... : L
Wheel_4x2........ : V
OffroadWheel_5x2. : M

Wheel_10x4....... : N
IdlerWheel....... : O
SprocketWheel.... : P

TrainWheel_2x2s.. : Q
TrainWheel_3x2s.. : R
TrainWheel_4x2s.. : S

Wheel_1sx1sx1s... : E
Wheel_1x1x1...... : E
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)
- `BrickSize` (`[f32, f32, f32]`) (`[3.0, 3.0, 3.0]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 3, 3]`)
- `InputChannel` (`BrickInput()`) (`BrickInput('None', None)`)
- `SmokeColor` (`[u8, u8, u8]`) (`[0, 0, 0]`)
- `SpawnScale` (`f32`) (`1.0`) 

#### Properties : B
- Default Brick Properties
- `SteeringAngle` (`float`) (`0.0`)
- `SteeringSpeed` (`float`) (`1.0`)
- `SuspensionLength` (`float`) (`0.0`)
- `SuspensionStiffness` (`float`) (`2.0`)
- `SuspensionDamping` (`float`) (`1.0`)
- `bDriven` (`bool`) (`True`)
- `bInvertDrive` (`bool`) (`False`)
- `bHasBrake` (`bool`) (`True`)
- `bHasHandBrake` (`bool`) (`True`)
- `BrakeStrength` (`float`) (`1.0`)
- `SteeringInputChannel` (`BrickInput()`) (`BrickInput('Steering', None)`)
- `BrakeInputChannel` (`BrickInput()`) (`BrickInput('Brake', None)`)
- `bCanDisableSteering` (`bool`) (`False`)
- `bCanInvertSteering` (`bool`) (`False`)

#### Properties : C
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

#### Properties : D
- Default Brick Properties
- `ThrottleInputChannel` (`BrickInput()`) (`BrickInput('Throttle', None)`)
- `GearRatioScale` (`float`) (`1.0`)
- `bTankDrive` (`bool`) (`False`)

#### Properties : E
- Default Brick Properties

#### Properties : F
- Default Brick Properties
- `FuelType` (`str`) (`'Petrol'`)

#### Properties : G
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`6.0`)
- `WheelWidth` (`float`) (`2.0`)
- `TireThickness` (`float`) (`1.2`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : H
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`9.0`)
- `WheelWidth` (`float`) (`2.0`)
- `TireThickness` (`float`) (`1.0`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : I
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`7.0`)
- `WheelWidth` (`float`) (`3.0`)
- `TireThickness` (`float`) (`1.25`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : J
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`10.0`)
- `WheelWidth` (`float`) (`3.0`)
- `TireThickness` (`float`) (`2.2`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : K
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`8.2`)
- `WheelWidth` (`float`) (`4.0`)
- `TireThickness` (`float`) (`1.85`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : L
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`12.0`)
- `WheelWidth` (`float`) (`6.0`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : M
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`15.0`)
- `WheelWidth` (`float`) (`6.0`)
- `TireThickness` (`float`) (`4.5`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : N
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`30.0`)
- `WheelWidth` (`float`) (`12.0`)
- `TireThickness ` (`float`) (`9.0`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : O
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`9.0`)
- `WheelWidth` (`float`) (`3.0`)

#### Properties : P
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`9.0`)
- `WheelWidth` (`float`) (`3.0`)
- `IdlerWheels` (`list[int]`) (`[]`)
- `TrackColor` (`[u8, u8, u8, u8]`) (`[0, 0, 26, 255]`)

#### Properties : Q
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`6.0`)
- `WheelWidth` (`float`) (`2.0`)

#### Properties : R
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`9.0`)
- `WheelWidth` (`float`) (`2.0`)

#### Properties : S
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`12.0`)
- `WheelWidth` (`float`) (`2.0`)

#### Properties : T
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`9.0`)
- `WheelWidth` (`float`) (`4.0`)
- `TireThickness` (`float`) (`1.0`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : U
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`8.1`)
- `WheelWidth` (`float`) (`4.0`)
- `TireThickness` (`float`) (`1.8`)
- `TirePressureRatio` (`float`) (`0.8`)

#### Properties : V
- Default Brick Properties
- `bInvertTankSteering` (`bool`) (`False`)
- `WheelDiameter` (`float`) (`12.0`)
- `WheelWidth` (`float`) (`6.0`)
- `TireThickness` (`float`) (`2.65`)
- `TirePressureRatio` (`float`) (`0.8`)

## Windows

###### In Brick Rigs 1.6.3 UI order
```
Panel_1x2x4....... : A
Panel_1x4x4....... : A
Panel_1x6x6....... : A

Windscreen_2x4x2.. : A
Windscreen_2x4x3.. : A
Windscreen_2x6x2.. : A

Windscreen_2x6x3.. : A
Windscreen_2x8x3.. : A
Windscreen_4x6x3.. : A
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

## Uncategorized

###### In Brick Rigs 1.7.0b UI order

```
Arch_2x1x2......... : A
Arch_4x1x4......... : A
Arch_6x1x1......... : A

Arch_8x1x8......... : A
FlareGun_1x1x1..... : D
CornerLedge_1x1x1.. : A

Ledge_1x1x1........ : A
Ledge_1x2x1........ : A
Ledge_1x4x1........ : A

DoubleSiren_1x2x1s. : B
PlaneTail_10x10x16. : A
CraneSupport_6x6x20 : A

Winch_3x2x1s....... : C
```

#### Properties : A
- Default Brick Properties
- `bGenerateLift` (`bool`) (`False`)

#### Properties : B
- Default Brick Properties
- `SirenType` (`str`) (`'Car'`)
- `HornPitch` (`f32`) (`1.0`)
- `InputChannel` (`BrickInput()`) (`BrickInput('Horn', None)`)

#### Properties : C
- Default Brick Properties
- `InputChannel` (`BrickInput()`) (`BrickInput('Auxiliary', None)`)
- `WinchSpeed` (`f32`) (`100.0`)

#### Properties : D
- Default Brick Properties
- `InputChannel` (`BrickInput()`) (`BrickInput('Action1', None)`)