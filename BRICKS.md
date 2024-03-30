# BR-API Supported Bricks List

## Default Brick Properties

This is a list of properties all bricks are (supposed to) have.  
NAME: `br_brick_list['default_brick_data']`

- `BrickColor` (`[u8, u8, u8, u8]`) (`[0, 0, 127, 255]`) : Brick color (HSV)
- 

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
- `bGenerateLift` (`bool`) (`False`): Toggle fluid dynamics.
- `BrickSize` (`[u16, u16, u16]`) (`[3, 3, 3]`): Change brick size.
- `ConnectorSpacing` (`[u2, u2, u2, u2, u2, u2]`) (`[3, 3, 3, 3, 3, 3]`): Change connector spacing
  (0 for none; 1 for default; 2 for half; 3 for thirds).