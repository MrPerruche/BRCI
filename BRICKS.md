# BR-API Supported Bricks List

## Default Brick Properties

This is a list of properties all bricks are (supposed to) have.  
NAME: `br_brick_list['default_brick_data']`

- `BrickColor` (`[u8, u8, u8, u8]`) (`[0, 0, 127, 255]`)
- `BrickPattern` (`str`) (`Default`)
- `BrickMaterial` (`str`) (`Plastic`)
- `Position` (`[f32, f32, f32]`) (`[0, 0, 0]`)
- `Rotation` (`[f32, f32, f32]`) (`[0, 0, 0]`)

## All Properties

This section includes various data about various bricks' properties which we find counter-intuitive.

### `ActuatorMode`
This define which mode the actuator is being set to. List :
###### In Brick Rigs 1.6.3 UI order
## <span style="color: lime;">TODO</span>
```
Accumulated
```

### `BrickColor`
This property correspond to the (main) color assigned to the brick. It is common to all bricks*.
It is a list of 4 elements in the following order :  
`[HUE (u8), SATURATION (u8), VALUE (u8), ALPHA (u8)]`

### `BrickMaterial`
This property correspond to what material the brick is made of. It is common to all bricks*.
It is a single string : `str`. Input list:
###### In Brick Rigs 1.6.3 UI order
## <span style="color: lime;">TODO</span>
```
Plastic
```

### `BrickPattern`
This property correspond to what pattern is applied to the brick, and/or if none is being applied.
It is common to all bricks. It is a single string : `str`. Input list:
###### In Brick Rigs 1.6.3 UI order
## <span style="color: lime;">TODO</span>
```
Default
```

### `gbn` (BR-API Component)
This is not a property in Brick Rigs. It is not handled as a property.
It is used to indicate the API what brick this variable is corresponding to.
Example : `AircraftR4`. As modifying it may cause issues in-game, such as properties being set to invalid values or
reset to their default value, or the brick or entire creation not loading, it is not recommended to edit it.
Modifying this "property" will not in any way update this brick's property list. To change what brick type your variable
is defined to, use `create_brick(brick_type)` again.

### `InputChannel.InputAxis`
This property corresponds to the brick's input : Either another brick, a constant value, throttle etc.
It has various names depending on the brick (such as `AutoHoverInputChannel.InputAxis` etc.).
It is set to the BrickInput class (custom class) : `BrickInput(brick_input_type, brick_input)`. Input list:
###### In Brick Rigs 1.6.3 UI order
## <span style="color: lime;">TODO</span>
```
BrickInput('AlwaysOn', brick_input).. : Value, (f32)
```

### `Position`
This "property" correspond to the brick's position in centimeters.
Although position is defined as a property in BR-API, it is not a property in Brick Rigs. It is common to all bricks.
It is a list of 3 elements corresponding to the brick's distance from origin in centimeters, in the following order:
`[POS_X (cm) (f32), POS_Y (cm) (f32), POS_Z (cm) (f32)]`

### `Rotation`
This "property" correspond to the brick's rotation in degrees.
Although rotation is defined as a property in BR-API, it is not a property in Brick Rigs. It is common to all bricks.
It is a list of 3 elements corresponding to the brick's rotation relative to the origin in degrees, in the following order:
`[ROT_Y (deg) (f32), ROT_Z (deg) (f32), ROT_X (deg) (f32)]`

### `SpeedFactor`
This property corresponds to actuators' speed. It is a single float 32 : `f32`.

## Actuators

###### In Brick Rigs 1.6.3 UI order
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
- ## <span style="color: lime;">TODO</span>
- `ActuatorMode` (`str`) (`'Accumulated'`)
- `InputChannel.InputAxis` (`BrickInput()`) (`BrickInput('Auxiliary', None)`)
- `SpeedFactor` (`f32`) (`1.0`) : Actuator speed (factor)
- `MinLimit` (`f32`) (`0.0`) : Actuator minimum (angle (°) / length (cm) / ...) limit
- `MaxLimit` (`f32`) (`0.0`) : Actuator maximum (angle (°) / length (cm) / ...) limit

## Aviation

###### In Brick Rigs 1.6.3 UI order

## <span style="color: lime;">TODO</span>
```
BladeHolder_2x1 : A
Flap_1x4x1s.... : B
Flap_2x8x1s.... : B

Turbine_6x2x2.. : C
```

#### Properties : A
- Default Brick Properties

#### Properties : B
- Default Brick Properties
- ## <span style="color: lime;">TODO</span>
- `bGenerateLift` (`bool`) (`True`): Toggle fluid dynamics
- `InputChannel.InputAxis` (`BrickInput()`) (`BrickInput('None', None)`) : Change brick input(s)
- `InputScale` (`f32`) (`100.0`) : Change input scale
- `MinAngle` (`f32`) (`-22.5`) : Set flap's minimum angle
- `MaxAngle` (`f32`) (`22.5`) : Set flap's maximum angle
- `bAccumulateInput` (`bool`) (`False`) : Toggle input accumulation

#### Properties : C

## Scalable Bricks

###### TODO: NOT IN ORDER

```
ScalableBrick............... : A
ScalableCone................ : A
ScalableConeRounded......... : A
ScalableZylinder............ : A
ScalableCylinder90R0........ : A
ScalableCylinder90R1........ : A
ScalableHalfCone............ : A
ScalableHalfCylinder........ : A
ScalableHemisphere.......... : A
ScalablePyramid............. : A
ScalableQuarterSphere....... : A
ScalableRamp................ : A
ScalableRampRounded......... : A
ScalableRampRoundedN........ : A
ScalableWedge............... : A
ScalableWedgeCorner......... : A

ScalableCorner.............. : B
ScalableCornerN............. : B
ScalableCornerRounded....... : B
ScalableCornerRoundedN...... : B
ScalableQuarterCone......... : B
ScalablePyramidCorner....... : B
ScalablePyramidCornerRounded : B
```

#### Properties : A
- Default Brick Properties
- ## <span style="color: lime;">TODO</span>
- `bGenerateLift` (`bool`) (`False`): Toggle fluid dynamics.
- `BrickSize` (`[u16, u16, u16]`) (`[3, 3, 3]`): Change brick size. (`[X, Y, Z]`)
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 3, 3]`): Change connector spacing
  (0: None, 1: Default, 2: Half, 3: Third). (`[FR, FL, MR, ML, BR, BL]`)