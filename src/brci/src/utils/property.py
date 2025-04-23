from typing import Optional, Iterable
import math

from ..constants import Units, ColorSpace, Connection
from .misc import clamp



class ConnectorSpacing(Iterable[Connection]):

    def __init__(self, tl: int | Connection, tm: int | Connection, tr: int | Connection,
                       bl: int | Connection, bm: int | Connection, br: int | Connection):

        self._tl = Connection.from_int(tl)
        self._tm = Connection.from_int(tm)
        self._tr = Connection.from_int(tr)
        self._bl = Connection.from_int(bl)
        self._bm = Connection.from_int(bm)
        self._br = Connection.from_int(br)

    def get_tl(self) -> Connection:
        return self._tl

    def get_x_pos(self) -> Connection:
        return self._tl

    def set_tl(self, value: int | Connection):
        self._tl = Connection.from_int(value)

    def set_x_pos(self, value: int | Connection):
        self._tl = Connection.from_int(value)

    def get_tm(self) -> Connection:
        return self._tm

    def get_y_pos(self) -> Connection:
        return self._tm

    def set_tm(self, value: int | Connection):
        self._tm = Connection.from_int(value)

    def set_y_pos(self, value: int | Connection):
        self._tm = Connection.from_int(value)

    def get_tr(self) -> Connection:
        return self._tr

    def get_z_pos(self) -> Connection:
        return self._tr

    def set_tr(self, value: int | Connection):
        self._tr = Connection.from_int(value)

    def set_z_pos(self, value: int | Connection):
        self._tr = Connection.from_int(value)

    def get_bl(self) -> Connection:
        return self._bl

    def get_x_neg(self) -> Connection:
        return self._bl

    def set_bl(self, value: int | Connection):
        self._bl = Connection.from_int(value)

    def set_x_neg(self, value: int | Connection):
        self._bl = Connection.from_int(value)

    def get_bm(self) -> Connection:
        return self._bm

    def get_y_neg(self) -> Connection:
        return self._bm

    def set_bm(self, value: int | Connection):
        self._bm = Connection.from_int(value)

    def set_y_neg(self, value: int | Connection):
        self._bm = Connection.from_int(value)

    def get_br(self) -> Connection:
        return self._br

    def get_z_neg(self) -> Connection:
        return self._br

    def set_br(self, value: int | Connection):
        self._br = Connection.from_int(value)

    def set_z_neg(self, value: int | Connection):
        self._br = Connection.from_int(value)

    def __iter__(self):

        """
        Returns an iter of values in the following order: X- X+ Y- Y+ Z- Z+
        :return:
        """

        return iter((self.get_x_neg(), self.get_x_pos(),
                self.get_y_neg(), self.get_y_pos(),
                self.get_z_neg(), self.get_z_pos()))



def srgb_to_linear(*args: int | float, maximum: int | float | list[int | float] = 255,
                   new_maximum: Optional[int | float | list[int | float]] = None, return_int: bool = True) -> list[int | float]:
    """
    Will correct colors from sRGB to linear, typically resulting in darker outputs

    Arguments:
        *args (int | float): Integers or floats corresponding to the color to convert.
        maximum (int | float | list[int | float], optional): Maximum value of the color.
        new_maximum (int | float | list[int | float], optional): New maximum value of the color.

    Returns:
        list[int | float]: Corrected color.
    """
    if isinstance(maximum, (int, float)):
        maximum = [maximum] * len(args)
    elif len(args) != len(maximum):
        raise ValueError(f"Maximum has an invalid amount of elements")

    if new_maximum is None:
        new_maximum = maximum
    elif isinstance(new_maximum, (int, float)):
        new_maximum = [new_maximum] * len(args)
    elif len(args) != len(new_maximum):
        raise ValueError(f"New maximum has an invalid amount of elements")

    args = [c / m for c, m in zip(args, maximum)]
    result = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in args]
    return [int(c * m) for c, m in zip(result, new_maximum)] if return_int else [c * m for c, m in zip(result, new_maximum)]


def linear_to_srgb(*args: int | float, maximum: int | float | list[int | float] = 255,
                   new_maximum: Optional[int | float | list[int | float]] = None, return_int: bool = True) -> list[int | float]:
    """
    Will correct colors from linear to sRGB, typically resulting in brighter outputs

    Arguments:
        *args (int | float): Integers or floats corresponding to the color to convert.
        maximum (int | float | list[int | float], optional): Maximum value of the color.
        new_maximum (int | float | list[int | float], optional): New maximum value of the color.

    Returns:
        list[int | float]: Corrected color.
    """
    if isinstance(maximum, (int, float)):
        maximum = [maximum] * len(args)
    elif len(args) != len(maximum):
        raise ValueError(f"Maximum has an invalid amount of elements")

    if new_maximum is None:
        new_maximum = maximum
    elif isinstance(new_maximum, (int, float)):
        new_maximum = [new_maximum] * len(args)
    elif len(args) != len(new_maximum):
        raise ValueError(f"New maximum has an invalid amount of elements")

    args = [c / m for c, m in zip(args, maximum)]
    result = [12.92 * c if c <= 0.00304 else 1.055 * c ** (1 / 2.4) - 0.055 for c in args]
    return [int(c * m) for c, m in zip(result, new_maximum)] if return_int else [c * m for c, m in zip(result, new_maximum)]


def convert_len(value: float | int | list[float | int] | tuple[float | int, ...], old_unit: float | int, new_unit: float | int) -> float | list[float]:

    """
    Convert a value or list of values from one unit to another. Both unit arguments must be use the same unit.

    Arguments:
        value: Value or list of values to convert.
        old_unit: Old unit.
        new_unit: New unit.

    Returns:
        float | int | list[float | int]: Converted value(s)

    Exceptions:
        TypeError: If one of the arguments is of an unexpected type.
    """


    # Need to import it each time to update it

    if (type(value) in (list, tuple, set, frozenset)) and ({type(v) for v in value} - {float, int} != set()):
        # raise TypeError("Value must be a float, int or list of floats and ints.")
        pass

    elif not type(value) in (float, int):

        # raise TypeError("Value must be a float, int or list of floats and ints.")
        pass

    if not type(old_unit) in (float, int):

        raise TypeError("Old unit must be a float or int.")

    if not type(new_unit) in (float, int):

        raise TypeError("New unit must be a float or int.")


    # If it's a value we convert it to the new unit
    if isinstance(value, (float, int)):
        return value / new_unit * old_unit

    # Else if it's a list we convert each value to the new unit
    elif isinstance(value, (list, tuple, set, frozenset)):
        return [v / new_unit * old_unit for v in value]

    # else:
    raise TypeError("Converting provided value(s) failed unexpectedly.")


# Function to calculate position of a brick from any unit
def position(value: float | int | list[float | int], unit: float | int = Units.METER) -> float | list[float]:

    """
    Function to convert position or distance (not length, see size function) of a brick from any unit to the unit Brick Rigs use.
    Aliases: `brci.distance()`, `brci.dist()`, `brci.pos()`, `brci.metadata_size()`

    Arguments:
        value: Value or list of values to convert.
        unit: Unit of provided values.

    Returns:
        Converted value.

    Exceptions:
        TypeError: If one of the arguments is of an unexpected type.
    """

    return convert_len(value, unit, Units.UE_UNIT)

# Aliases
metadata_size = distance = dist = pos = position


# Function to calculate size of a brick from any unit
def size(brick_size: float | int | list[float | int], unit: float | int = Units.METER) -> float | list[float]:

    """
    Function to convert size or length (not distance, see pos function) of a brick from any unit to the unit Brick Rigs use.
    Aliases: `brci.length()`

    Arguments:
        brick_size: Value or list of values to convert.
        unit: Unit of provided values.

    Returns:
        Converted value.

    Exceptions:
        TypeError: If one of the arguments is of an unexpected type.
    """

    return convert_len(brick_size, unit, Units.THIRD)

# Aliases
length = size



# -------------------------


def convert_color(color: list[int | float] | tuple[int | float, ...],
                  old_space: ColorSpace,
                  new_space: ColorSpace,
                  return_alpha: Optional[bool] = None,
                  maximum: float | int | list[float | int] = 255,
                  new_maximum: Optional[float | int | list[float | int]] = None,
                  return_int: bool = True) -> list[float | int]:

    """
    Will convert a list of integers or floats corresponding to a color from one color space to another.
    Maximum and new_maximum may be "ignored" by some channels if dealing with perceptual color spaces like OKLab or OKLCH.

    Arguments:
        color (list[int | float]): A list of integers or floats (of length depending on the color space) corresponding to the color to convert.
        old_space (ColorSpace): The color space of the color to convert.
        new_space (ColorSpace): The color space to convert the color to.
        return_alpha (Optional[bool]): Whether the output color has an alpha channel. Leave none to determine automatically from the input.
        maximum (float | int | list[float | int]): The maximum value of each color channel.
        new_maximum (Optional[float | int | list[float | int]]): If set, it is the maximum value of each color channel in the new color space.
        return_int (bool): Whether to return the color as integers or floats.

    Returns:
        A list of integers or floats (of length depending on the color space) corresponding to the converted color.

    Exceptions:
        AttributeError: If old_space or new_space are not of the ColorSpace enum type.
        TypeError: One of the provided arguments is of an invalid type.
        ValueError: If the color space or new color space is not supported or one of the lists are of incorrect length.
        ValueError: One of the value arguments has an invalid value.
        ZeroDivisionError: If maximum is 0.
    """


    # Ensure color validity
    if {isinstance(col, (int, float)) for col in color} != {True}:
        raise ValueError("Color must be a list or tuple of ints and/or floats")

    # Ensure color / color space validity
    old_colorspace_length: int = ColorSpace.get_len_of(old_space)

    input_has_alpha = len(color) == old_colorspace_length + 1
    if return_alpha is None:
        return_alpha = input_has_alpha

    if isinstance(maximum, (int, float)):
        maximum = [maximum] * len(color)
    elif len(color) != len(maximum):
        raise ValueError(f"Maximum has an invalid amount of elements")

    if new_maximum is None:
        new_maximum = maximum
    elif isinstance(new_maximum, (int, float)):
        new_maximum = [new_maximum] * len(color)
    elif len(color) != len(new_maximum):
        raise ValueError(f"New maximum has an invalid amount of elements")


    # print(f'{len(color)=}\n{old_colorspace_length=}\n{alpha=}\n{maximum=}\n{new_maximum=}\n{old_space=}\n{new_space=}\n{has_alpha=}\n')

    if len(color) != old_colorspace_length + int(input_has_alpha):
        raise ValueError(f"Color has an invalid amount of elements")

    # Get RGB color
    if ColorSpace.is_perceptual(old_space):
        normalized_color: list[float] = (color[ :-1] + [color[-1] / maximum[-1]]) if input_has_alpha else color
    else:
        normalized_color: list[float] = [c / m for c, m in zip(color, maximum)]
    r, g, b, a = 0.0, 0.0, 0.0, normalized_color[-1] if input_has_alpha else 1.0


    if old_space is ColorSpace.RGB:
        r, g, b = normalized_color[ :3]

    elif old_space is ColorSpace.HSV:
        h, s, v = normalized_color[:3]
        c = v * s
        m = v - c
        x = c * (1 - abs((h * 6) % 2 - 1))

        if 0 <= h < 1 / 6:
            r, g, b = c, x, 0
        elif 1 / 6 <= h < 2 / 6:
            r, g, b = x, c, 0
        elif 2 / 6 <= h < 3 / 6:
            r, g, b = 0, c, x
        elif 3 / 6 <= h < 4 / 6:
            r, g, b = 0, x, c
        elif 4 / 6 <= h < 5 / 6:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        r += m
        g += m
        b += m

    elif old_space is ColorSpace.HSL:
        h, s, l = normalized_color[ :3]
        c = (1 - abs(2 * l - 1)) * s
        m = l - c / 2
        x = c * (1 - abs((h * 6) % 2 - 1))

        if 0 <= h < 1 / 6:
            r, g, b = c, x, 0
        elif 1 / 6 <= h < 2 / 6:
            r, g, b = x, c, 0
        elif 2 / 6 <= h < 3 / 6:
            r, g, b = 0, c, x
        elif 3 / 6 <= h < 4 / 6:
            r, g, b = 0, x, c
        elif 4 / 6 <= h < 5 / 6:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        r += m
        g += m
        b += m

    elif old_space is ColorSpace.CMYK:
        c, m, y, k = normalized_color[ :4]
        r = (1 - c) * (1 - k)
        g = (1 - m) * (1 - k)
        b = (1 - y) * (1 - k)

    elif old_space in (ColorSpace.OKLAB, ColorSpace.OKLCH):
        if old_space is ColorSpace.OKLCH:
            L, C, H = normalized_color[ :3]
            a_ = C * math.cos(H / 360 * 2 * math.pi)
            b_ = C * math.sin(H / 360 * 2 * math.pi)
        else:
            L, a_, b_ = normalized_color[ :3]

        l_ = L + 0.3963377774 * a_ + 0.2158037573 * b_
        m_ = L - 0.1055613458 * a_ - 0.0638541728 * b_
        s_ = L - 0.0894841775 * a_ - 1.2914855480 * b_

        l = l_ ** 3
        m = m_ ** 3
        s = s_ ** 3

        r =  4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
        g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
        b = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s

    else:
        raise AttributeError(f"Color space {old_space} is not supported.")

    if not ColorSpace.is_perceptual(new_space):
         r, g, b = clamp(0, r, 1), clamp(0, g, 1), clamp(0, b, 1)
    # if perceptual, will not clamp so r, g, b = r, g, b.
    new_color = ([0.0] * ColorSpace.get_len_of(new_space)) + ([a] if input_has_alpha else [])


    if new_space is ColorSpace.RGB:
        new_color[ :3] = r, g, b

    elif new_space is ColorSpace.HSV:
        mx = max(r, g, b)
        mn = min(r, g, b)
        diff = mx - mn
        if diff == 0:
            h = 0
        elif mx == r:
            h = (60 * ((g - b) / diff) + 360) % 360
        elif mx == g:
            h = (60 * ((b - r) / diff) + 120) % 360
        else:
            h = (60 * ((r - g) / diff) + 240) % 360
        s = 0 if mx == 0 else diff / mx
        v = mx
        new_color[:3] = h / 360, s, v

    elif new_space is ColorSpace.HSL:
        mx = max(r, g, b)
        mn = min(r, g, b)
        diff = mx - mn
        l = (mx + mn) / 2
        if diff == 0:
            h = 0
        elif mx == r:
            h = (60 * ((g - b) / diff) + 360) % 360
        elif mx == g:
            h = (60 * ((b - r) / diff) + 120) % 360
        else:
            h = (60 * ((r - g) / diff) + 240) % 360
        if l == 0 or l == 1:
            s = 0
        else:
            s = diff / (1 - abs(2 * l - 1))

        new_color[:3] = h / 360, s, l

    elif new_space is ColorSpace.CMYK:
        mx = max(r, g, b)
        k = 1 - mx
        if mx == 0:  # Check for pure black to avoid zero division errors
            new_color[ :4] = [0, 0, 0, 1]
        else:
            new_color[0] = (1 - r - k) / (1 - k)
            new_color[1] = (1 - g - k) / (1 - k)
            new_color[2] = (1 - b - k) / (1 - k)

    elif new_space in (ColorSpace.OKLAB, ColorSpace.OKLCH):
        l_linear = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
        m_linear = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
        s_linear = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b

        l_ = l_linear ** (1 / 3)
        m_ = m_linear ** (1 / 3)
        s_ = s_linear ** (1 / 3)

        L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
        a_ = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
        b_ = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_

        if new_space is ColorSpace.OKLAB:
            new_color[:3] = L, a_, b_
        else:
            C = math.sqrt(a_ * a_ + b_ * b_)
            H = ((math.atan2(b_, a_) / (2 * math.pi)) % 1.0) * 360.0
            new_color[:3] = L, C, H

    else:
        raise AttributeError(f"Color space {new_space} is not supported.")

    if ColorSpace.is_perceptual(new_space):
        return [int(c) for c in new_color] if return_int else new_color
    else:
        return [int(clamp(0, c, 1) * m) for c, m in zip(new_color, new_maximum)] if return_int \
                else [clamp(0, c, 1) * m for c, m in zip(new_color, new_maximum)]


def rgb_to_oklab(r: int | float, g: int | float, b: int | float, a: Optional[int | float] = None) -> list[float]:
    """
    Convers RGB to OKLAB. Exceptionally included to make working with gradients easier.

    Arguments:
        r (int | float): Red value.
        g (int | float): Green value.
        b (int | float): Blue value.
        a (Optional[int | float], optional): Alpha value.

    Returns:
        list[float]: OKLAB values.
    """
    return convert_color([r, g, b] + ([] if a is None else [a]), ColorSpace.RGB, ColorSpace.OKLAB, maximum=255, return_int=False)


def rgb_to_oklch(r: int | float, g: int | float, b: int | float, a: Optional[int | float] = None) -> list[float]:
    """
    Convers RGB to OKLCH. Exceptionally included to make working with gradients easier.

    Arguments:
        r (int | float): Red value.
        g (int | float): Green value.
        b (int | float): Blue value.
        a (Optional[int | float], optional): Alpha value.

    Returns:
        list[float]: OKLCH values.
    """
    return convert_color([r, g, b] + ([] if a is None else [a]), ColorSpace.RGB, ColorSpace.OKLCH, maximum=255, return_int=False)


def brick_input14(prop_name: str, input_type: str, value: float | int = 1.0, source_bricks: Optional[list[str]] = None) -> dict[str, float | int | list[str]]:

    """
    Converts a list of arguments into a list of properties corresponding to brick inputs to provide similarity with BRCI-C.
    Aliases: `brci.BrickInput14()`

    Arguments:
        prop_name (str): Name of the property. e.g. `'EnabledInputChannel'`
        input_type (str): Type of the input.
        value (float | int): Value of the input.
        source_bricks (list[str]): List of source bricks.

    Returns:
        dict[str, float | int | list[str]]: List of properties.
    """

    return {
        f'{prop_name}.InputAxis': input_type,
        f'{prop_name}.SourceBricks': [] if source_bricks is None else source_bricks,
        f'{prop_name}.Value': value
    }


BrickInput14 = brick_input14


def brick_input15(prop_name: str, input_type: str, value: float | int = 1.0, source_bricks: Optional[list[str]] = None) -> dict[str, float | int | list[str]]:

    """
    Converts a list of arguments into a list of properties corresponding to brick inputs to provide similarity with BRCI-C.
    Aliases: `brci.BrickInput15()`

    Arguments:
        prop_name (str): Name of the property. e.g. `'EnabledInputChannel'`
        input_type (str): Type of the input.
        value (float | int): Value of the input.
        source_bricks (list[str]): List of source bricks.

    Returns:
        dict[str, float | int | list[str]]: List of properties.
    """

    return {
        f'{prop_name}.InputAxis': input_type,
        f'{prop_name}.SourceBricks': [] if source_bricks is None else source_bricks,
        f'{prop_name}.Value': value
    }


BrickInput15 = brick_input15

