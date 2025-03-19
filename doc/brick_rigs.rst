==================================
INNER WORKINGS OF BRICK RIGS FILES
==================================

This document contains relevant technical information about Brick Rigs and it's file system as well as Unreal Engine 4.

Different types of data
-----------------------

Brick Rigs is written in C++. C++ is a lot less flexible than Python. Whilst using the library, you will often notice
restrictions over the data, such as values being limited to a specific range (typically 0 - 255 for integers) or
floating point numbers being less precise than in Python.

This part of the document where you will encounter the different types and what are their limitations. Keep them in mind
as they may result in silent errors!

**Integers**

Integers are typically used for values unrelated to positions, sizes and math, like fractional digits property on
displays or the colors. Whilst integers ranging up to quintillions exist, Brick Rigs mostly use unsigned 8-bit integers
(aka. uint8 or u8). These integers are limited to the [0, 255] range.

**Floating point values**

Brick Rigs typically use floating point values for positions, sizes and math. Since Brick Rigs run on Unreal Engine 4,
it relies on 32-bit floating point numbers (aka. single precision floats or float32). These numbers range between
[-3.402823466e+38, 3.402823466e+38] (with support for +Infinity, -Infinity and NaN although Brick Rigs rarely handle
these correctly). They have roughly 7 digits of precision (log_2(2^23) ~= 6.9237).

Python on the other hand use double-precision floating points number, which are much more accurate and can support
wider ranges. BRCI will therefore convert the two, which may result in small inaccuracies.

**BRCI's custom classes**

BRCI features custom classes to handle numbers, like the Visibility enum for metadata writing or the ConnectorSpacing
class for the property of the same name. These classes are meant to make working with data easier and less error-prone.


Brick Rigs' units
-----------------

Brick Rigs stores and work with data in uncommon units. They can sometimes be confusing to work with.

**Length**

Length is typically expressed in three units:

.. list-table::
    :widths: 10 40 40 40

    * - Unit
      - Thirds (aka. Stud, Decameter)
      - Centimeters (aka. Units)
      - Meters
    * - Size
      - ``0.1 cm`` / ``~3.9in``
      - ``0.01m`` / ``~0.39in``
      - ``100cm`` / ``~39in``
    * - Use
      - Typically used for the length, width or depth of bricks
      - Typically used for positions and sizes
      - Typically used for sensor outputs
    * - Info
      - This unit comes from earlier versions when size was stored as 16-bit integers. Brick sizes were limited to
        multiples of 10 centimeters.
      - Centimeters (or Unreal Engine Units) is the unit used by default in Unreal Engine.
      - Meters are used for elements exposed to players.


**Angles**

TODO


**Colors**

Colors are stored as 3 or 4 unsigned 8-bit integers despite Brick Rigs showing floats. This is why colors are so
imprecise in-game. Colors are stored in the HSV(A) format, where the integers of each channel correspond to a 0 to 360
degrees hue or 0 to 100% saturation, value or alpha.

BRCI contains a few functions to help dealing with the confusing color space: ``brci.from_rgb(r, g, b, a)``,
``brci.from_hsv(h, s, v, a)``, ``brci.from_hsl(h, s, l, a)``, ``brci.from_cmyk(c, m, y, k, a)``, all converting to HSV
as 8-bit integers.