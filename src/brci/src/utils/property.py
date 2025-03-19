from typing import Optional, Iterable

from ..constants import Units, ColorSpace, Connection



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




def convert_len(value: float | int | list[float | int], old_unit: float | int, new_unit: float | int) -> float | list[float]:

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
                  has_alpha: Optional[bool] = None,
                  maximum: float = 255,
                  new_maximum: Optional[float] = None,
                  return_int: bool = True) -> list[float | int]:

    """
    Will convert a list of integers or floats corresponding to a color from one color space to another.

    Arguments:
        color (list[int | float]): A list of integers or floats (of length depending on the color space) corresponding to the color to convert.
        old_space (ColorSpace): The color space of the color to convert.
        new_space (ColorSpace): The color space to convert the color to.
        has_alpha (Optional[bool]): Whether the color has an alpha channel. Leave none to determine automatically.
        maximum (float): The maximum value of each color channel.
        new_maximum (Optional[float]): If set, it is the maximum value of each color channel in the new color space.
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
    old_colorspace_length: int = len(old_space.name)

    alpha = has_alpha
    if has_alpha is None:
        alpha = old_colorspace_length == len(color) - 1

    if new_maximum is None:
        new_maximum = maximum

    # print(f'{len(color)=}\n{old_colorspace_length=}\n{alpha=}\n{maximum=}\n{new_maximum=}\n{old_space=}\n{new_space=}\n{has_alpha=}\n')

    if not (old_colorspace_length <= len(color) <= old_colorspace_length + int(alpha)):
        if has_alpha is None:
            raise ValueError(f"Color has an invalid amount of elements: expected {old_colorspace_length} or"
                             f" {old_colorspace_length+1} elements")
        # else:
        raise ValueError(f"Color has an invalid amount of elements: expected {old_colorspace_length}" +
                         (f" or {old_colorspace_length+1} elements" if has_alpha else " elements"))

    # Get RGB color
    scaled_color: list[float] = [col / maximum for col in color]
    rgb_color: list[float] = [0.0] * (len(old_space.name) + int(alpha))

    if old_space is ColorSpace.RGB:
        rgb_color = scaled_color
    elif old_space is ColorSpace.HSV or old_space is ColorSpace.HSL:
        h, s, v = scaled_color[:3]
        if old_space is ColorSpace.HSV:
            c = v * s
            m = v - c
        else:  # HSL
            c = (1 - abs(2 * v - 1)) * s
            m = v - c / 2
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
        rgb_color[0] = r + m
        rgb_color[1] = g + m
        rgb_color[2] = b + m
    elif old_space is ColorSpace.CMYK:
        c, m, y, k = scaled_color[:4]
        rgb_color[0] = (1 - c) * (1 - k)
        rgb_color[1] = (1 - m) * (1 - k)
        rgb_color[2] = (1 - y) * (1 - k)
    else:
        raise AttributeError(f"Color space {old_space} is not supported.")

    r, g, b = rgb_color[:3]
    new_color = rgb_color  # Mutability! Careful when using. Here for readability

    if new_space is ColorSpace.RGB:
        pass
    elif new_space is ColorSpace.HSV or new_space is ColorSpace.HSL:
        mx = max(r, g, b)  # rgb_color contains alpha. I'm fairly confident this is faster than rgb_color[:3]
        mn = min(r, g, b)
        diff = mx - mn
        new_color[2] = (mx + mn) / 2
        if diff == 0:
            new_color[0] = 0
        else:
            if mx == r:
                new_color[0] = (60 * ((g - b) / diff) + 360) % 360
            elif mx == g:
                new_color[0] = (60 * ((b - r) / diff) + 120) % 360
            else:
                new_color[0] = (60 * ((r - g) / diff) + 240) % 360
        new_color[0] /= 360
        if new_space == ColorSpace.HSV:
            new_color[1] = 0 if mx == 0 else (diff / mx)
            new_color[2] = mx
        else:  # HSL
            if new_color[2] == 0 or new_color[2] == 1:
                new_color[1] = 0
            else:
                new_color[1] = (mx - mn) / (1 - abs(2 * new_color[2] - 1))
    elif new_space is ColorSpace.CMYK:
        mx = max(r, g, b)
        new_color.insert(3, k := 1 - mx)  # Adds an extra slot for key (at the 3rd index -> cmyk(a))
        if mx == 0:  # Check for pure black to avoid zero division errors
            new_color = [0, 0, 0, 1, rgb_color[-1]] if alpha else [0, 0, 0, 1]
        else:
            new_color[0] = (1 - r - k) / (1 - k)
            new_color[1] = (1 - g - k) / (1 - k)
            new_color[2] = (1 - b - k) / (1 - k)
    else:
        raise AttributeError(f"Color space {new_space} is not supported.")

    return [int(col * new_maximum) for col in new_color] if return_int else [col * new_maximum for col in new_color]





def convert_byte_color(color: list[int | float] | tuple[int | float, ...],
                  old_space: ColorSpace,
                  new_space: ColorSpace,
                  has_alpha: Optional[bool] = None):

    """
    Will convert a list of integers or floats corresponding to a color from one color space to another;
    both color spaces must be within the byte range [0, 255].
    It will always return a list of integers.

    Arguments:
        color (list[int | float]): A list of integers corresponding to the color to convert.
        old_space (ColorSpace): The color space of the color to convert.
        new_space (ColorSpace): The color space to convert the color to.
        has_alpha (Optional[bool]): Whether the color has an alpha channel. Leave none to determine automatically.

    Returns:
        A list of integers corresponding to the converted color.

    Exceptions:
        AttributeError: If old_space or new_space are not of the ColorSpace enum type.
        TypeError: One of the provided arguments is of an invalid type.
        ValueError: If the color space or new color space is not supported or one of the lists are of incorrect length.
        ValueError: One of the value arguments has an invalid value.
    """

    return convert_color(color, old_space=old_space, new_space=new_space, has_alpha=has_alpha, maximum=255, new_maximum=255, return_int=True)  # return_int=True is not necessary but useful for clarity

def convert_float_color(color: list[int | float] | tuple[int | float, ...],
                  old_space: ColorSpace,
                  new_space: ColorSpace,
                  has_alpha: Optional[bool] = None):

    """
    Will convert a list of integers or floats corresponding to a color from one color space to another;
    both color spaces must be within [0.0, 1.0].
    It will always return a list of floats.

    Arguments:
        color (list[int | float]): A list of integers or floats (of length depending on the color space) corresponding to the color to convert.
        old_space (ColorSpace): The color space of the color to convert.
        new_space (ColorSpace): The color space to convert the color to.
        has_alpha (Optional[bool]): Whether the color has an alpha channel. Leave none to determine automatically.

    Returns:
        A list of floats corresponding to the converted color.

    Exceptions:
        AttributeError: If old_space or new_space are not of the ColorSpace enum type.
        TypeError: One of the provided arguments is of an invalid type.
        ValueError: If the color space or new color space is not supported or one of the lists are of incorrect length.
        ValueError: One of the value arguments has an invalid value.
    """

    return convert_color(color, old_space=old_space, new_space=new_space, has_alpha=has_alpha, maximum=1.0, new_maximum=1.0, return_int=False)

def from_rgb(r: int, g: int, b: int, a: Optional[int] = None) -> list[int]:

    """
    Will convert RGB color to HSV in BR's ranges

    Arguments:
        r (int): Red channel [0, 255]
        g (int): Green channel [0, 255]
        b (int): Blue channel [0, 255]
        a (Optional[int]): Alpha channel [0, 255]

    Returns:
        A list of 3 or 4 integers (depending on if alpha is provided or not) in HSV with each value ranging from 0 to 255

    Exceptions:
        AttributeError: If old_space or new_space are not of the ColorSpace enum type.
        TypeError: One of the provided arguments is of an invalid type.
        ValueError: If the color space or new color space is not supported or one of the lists are of incorrect length.
        ValueError: One of the value arguments has an invalid value.
    """

    color = [r, g, b] if a is None else [r, g, b, a]
    return convert_byte_color(color, old_space=ColorSpace.RGB, new_space=ColorSpace.HSV)

def from_hsv(h: float, s: float, v: float, a: Optional[float] = None) -> list[int]:

    """
    Will convert HSV color to HSV in BR's ranges

    Arguments:
        h (float): Hue channel [0, 360]
        s (float): Saturation channel [0, 100]
        v (float): Value channel [0, 100]
        a (Optional[float]): Alpha channel [0, 100]

    Returns:
        A list of 3 or 4 integers (depending on if alpha is provided or not) in HSV with each value ranging from 0 to 255

    Exceptions:
        AttributeError: If old_space or new_space are not of the ColorSpace enum type.
        TypeError: One of the provided arguments is of an invalid type.
        ValueError: If the color space or new color space is not supported or one of the lists are of incorrect length.
        ValueError: One of the value arguments has an invalid value.
    """

    if a is None:
        return [int(h/360*255), int(s/100*255), int(v/100*255)]
    else:
        return [int(h/360*255), int(s/100*255), int(v/100*255), int(a/100*255)]

def from_hsl(h: float, s: float, l: float, a: Optional[float] = None) -> list[int]:

    """
    Will convert HSL color to HSL in BR's ranges

    Arguments:
        h (float): Hue channel [0, 360]
        s (float): Saturation channel [0, 100]
        l (float): Lightness channel [0, 100]
        a (Optional[float]): Alpha channel [0, 100]

    Returns:
        A list of 3 or 4 integers (depending on if alpha is provided or not) in HSL with each value ranging from 0 to 255

    Exceptions:
        AttributeError: If old_space or new_space are not of the ColorSpace enum type.
        TypeError: One of the provided arguments is of an invalid type.
        ValueError: If the color space or new color space is not supported or one of the lists are of incorrect length.
        ValueError: One of the value arguments has an invalid value.
    """

    color = [h/360, s/100, l/100] if a is None else [h/360, s/100, l/100, a/100]
    return convert_color(color, ColorSpace.HSL, ColorSpace.HSV, maximum=1.0, new_maximum=255.0, return_int=True)

def from_cmyk(c: float, m: float, y: float, k: float, a: Optional[float] = None) -> list[int]:

    """
    Will convert CMYK color to CMYK in BR's ranges

    Arguments:
        c (float): Cyan channel [0, 100]
        m (float): Magenta channel [0, 100]
        y (float): Yellow channel [0, 100]
        k (float): Black channel [0, 100]
        a (Optional[float]): Alpha channel [0, 100]

    Returns:
        A list of 3 or 4 integers (depending on if alpha is provided or not) in CMYK with each value ranging from 0 to 255

    Exceptions:
        AttributeError: If old_space or new_space are not of the ColorSpace enum type.
        TypeError: One of the provided arguments is of an invalid type.
        ValueError: If the color space or new color space is not supported or one of the lists are of incorrect length.
        ValueError: One of the value arguments has an invalid value.
    """

    color = [c/100, m/100, y/100, k/100] if a is None else [c/100, m/100, y/100, k/100, a/100]
    return convert_color(color, ColorSpace.CMYK, ColorSpace.HSV, maximum=1.0, new_maximum=255.0, return_int=True)


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

