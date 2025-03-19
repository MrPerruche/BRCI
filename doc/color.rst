===============
COLOR UTILITIES
===============

BRCI makes available plenty functions to make working with color in-game easier.

BRCI identifies the different color spaces it supports with the ``brci.ColorSpace`` enum. It has the following values:

- ``brci.ColorSpace.RGB = 1``
- ``brci.ColorSpace.HSV = 2``
- ``brci.ColorSpace.HSL = 3``
- ``brci.ColorSpace.CMYK = 4``

Conversion between color spaces
-------------------------------

To convert from a color space to another, the ``brci.convert_color()`` function can be used. Note all functions
here will first convert to RGB (float) before converting and returning the color in the new color space. It has 7
arguments, the first 3 are required:

- ``color (list[int | float])``: A list of integers or floats (of length depending on the color space) corresponding to the color to convert.
- ``old_space (ColorSpace)``: The color space of the color to convert.
- ``new_space (ColorSpace)``: The color space to convert the color to.
- ``has_alpha (Optional[bool])``: Whether the color has an alpha channel. Leave None to determine automatically.
- ``maximum (float)``: The maximum value of each color channel.
- ``new_maximum (Optional[float])``: If set, it is the maximum value of each color channel in the new color space.
- ``return_int (bool)``: Whether to return the color as integers or floats.

Simplified conversion functions
-------------------------------

There are also two functions duplicates of ``brci.convert_color()`` with less arguments to simplify usage:

- ``brci.convert_byte_color(color, old_space, new_space, has_alpha)`` which returns
  ``convert_color(color, old_space=old_space, new_space=new_space, has_alpha=has_alpha, maximum=255, new_maximum=255, return_int=True)``
- ``brci.convert_float_color(color, old_space, new_space, has_alpha)`` which returns
  ``convert_color(color, old_space=old_space, new_space=new_space, has_alpha=has_alpha, maximum=1.0, new_maximum=1.0, return_int=False)``

Color creation functions
------------------------

Finally, the functions ``brci.from_rgb(r, g, b, a)``, ``brci.from_hsv(h, s, v, a)``, ``brci.from_hsl(h, s, l, a)``,
``brci.from_cmyk(c, m, y, k, a)`` all return the same color in the HSV color space with each channel in the [0, 255]
range, which is used for ``BrickColor`` properties. All values must be expressed in their typical range ([0, 255] for
rgb, [0, 360] for hue, [0, 100] (percents) for other channels).