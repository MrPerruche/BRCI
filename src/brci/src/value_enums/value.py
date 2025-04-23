from abc import ABC, abstractmethod
from typing import Optional

from ..utils import Units


class Value(ABC):

    @staticmethod
    @abstractmethod
    def from_rgb(r: int, g: int, b: int, a: Optional[int] = None):
        """Abstract method to convert from RGB to the implementing color space.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Args:
            r (int): Red component (0-255).
            g (int): Green component (0-255).
            b (int): Blue component (0-255).
            a (Optional[int], optional): Alpha component (0-255).

        Returns:
            Self: The converted color.
        """
        pass


    @staticmethod
    @abstractmethod
    def from_hsv(h: float, s: float, v: float, a: Optional[float] = None):
        """
        Method to convert from HSV to the color space used by the given version of Brick Rigs.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Arguments:
            h (float): Hue component (0.0-360.0).
            s (float): Saturation component (0.0-100.0).
            v (float): Value component (0.0-100.0).
            a (Optional[float], optional): Alpha component (0.0-100.0).

        Returns:
            Self: The converted color.
        """
        pass


    @staticmethod
    @abstractmethod
    def from_hsv_machine(h: float, s: float, v: float, a: Optional[float] = None):
        """
        Method to convert from HSV to the color space used by the given version of Brick Rigs.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Arguments:
            h (float): Hue component (0.0-1.0).
            s (float): Saturation component (0.0-1.0).
            v (float): Value component (0.0-1.0).
            a (Optional[float], optional): Alpha component (0.0-1.0).
        """
        pass


    @staticmethod
    @abstractmethod
    def from_hsl(h: float, s: float, l: float, a: Optional[float] = None):
        """
        Method to convert from HSL to the color space used by the given version of Brick Rigs.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Arguments:
            h (float): Hue component (0.0-360.0).
            s (float): Saturation component (0.0-100.0).
            l (float): Lightness component (0.0-100.0).
            a (Optional[float], optional): Alpha component (0.0-100.0).

        Returns:
            Self: The converted color.
        """
        pass


    @staticmethod
    @abstractmethod
    def from_hsl_machine(h: float, s: float, l: float, a: Optional[float] = None):
        """
        Method to convert from HSL to the color space used by the given version of Brick Rigs.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Arguments:
            h (float): Hue component (0.0-1.0).
            s (float): Saturation component (0.0-1.0).
            l (float): Lightness component (0.0-1.0).
            a (Optional[float], optional): Alpha component (0.0-1.0).

        Returns:
            Self: The converted color.
        """
        pass


    @staticmethod
    @abstractmethod
    def from_cmyk(c: float, m: float, y: float, k: float, a: Optional[float] = None):
        """
        Method to convert from CMYK to the color space used by the given version of Brick Rigs.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Arguments:
            c (float): Cyan component (0.0-100.0).
            m (float): Magenta component (0.0-100.0).
            y (float): Yellow component (0.0-100.0).
            k (float): Black component (0.0-100.0).
            a (Optional[float], optional): Alpha component (0.0-100.0).

        Returns:
            Self: The converted color.
        """


    @staticmethod
    @abstractmethod
    def from_cmyk_machine(c: float, m: float, y: float, k: float, a: Optional[float] = None):
        """
        Method to convert from CMYK to the color space used by the given version of Brick Rigs.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Arguments:
            c (float): Cyan component (0.0-1.0).
            m (float): Magenta component (0.0-1.0).
            y (float): Yellow component (0.0-1.0).
            k (float): Black component (0.0-1.0).
            a (Optional[float], optional): Alpha component (0.0-1.0).

        Returns:
            Self: The converted color.
        """
        pass


    @staticmethod
    @abstractmethod
    def from_oklab(l: float, a: float, b: float, alpha: Optional[float] = None):
        """
        Method to convert from OKLab to the color space used by the given version of Brick Rigs.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Arguments:
            l (float): Lightness component.
            a (float): Alpha (color) component.
            b (float): Beta component.
            alpha (Optional[float], optional): Alpha (transparency) component.
        """
        pass


    @staticmethod
    @abstractmethod
    def from_oklch(l: float, c: float, h: float, a: Optional[float] = None):
        """
        Method to convert from OKLCH to the color space used by the given version of Brick Rigs.
        In versions 14 and older, leaving alpha to None will omit it from the result.
        In versions 15 and newer, leaving alpha to None will set it to its maximum as the game always store it.

        Arguments:
            l (float): Lightness component.
            c (float): Chroma component.
            h (float): Hue component.
            a (Optional[float], optional): Alpha (transparency) component.
        """
        pass


    @staticmethod
    @abstractmethod
    def length(*args: int | float, unit: float | int = Units.METER) -> int | float:
        """
        Outputs the value in this file version representing the given length

        Arguments:
            *args (int | float): Length(s) to convert.
            unit (float | int, optional): Unit of provided values.

        Returns:
            int | float: Length in this file version
        """
        pass


    @staticmethod
    @abstractmethod
    def size(*args: int | float, unit: float | int = Units.METER) -> int | float:
        """
        Outputs the value in this file version representing the given size

        Arguments:
            *args (int | float): Size(s) to convert.
            unit (float | int, optional): Unit of provided values.

        Returns:
            int | float: Size in this file version
        """
        pass


    @staticmethod
    @abstractmethod
    def metadata_size(*args: int | float, unit: float | int = Units.METER) -> int | float:
        """
        Outputs the value in this file version representing the given size

        Arguments:
            *args (int | float): Size(s) to convert.
            unit (float | int, optional): Unit of provided values.

        Returns:
            int | float: Size (to be used for metadata) in this file version
        """
        pass


    @staticmethod
    @abstractmethod
    def distance(*args: int | float, unit: float | int = Units.METER) -> int | float:
        """
        Outputs the value in this file version representing the given distance

        Arguments:
            *args (int | float): Distance(s) to convert.
            unit (float | int, optional): Unit of provided values.

        Returns:
            int | float: Distance in this file version
        """
        pass


    @staticmethod
    @abstractmethod
    def position(*args: int | float, unit: float | int = Units.METER) -> int | float:
        """
        Outputs the value in this file version representing the given position

        Arguments:
            *args (int | float): Position(s) to convert.
            unit (float | int, optional): Unit of provided values.

        Returns:
            int | float: Position in this file version
        """
        pass


    @staticmethod
    @abstractmethod
    def sensor_distance(*args: int | float, unit: float | int = Units.METER) -> int | float:
        """
        Outputs the value in this file version representing the given distance

        Arguments:
            *args (int | float): Distance(s) to convert.
            unit (float | int, optional): Unit of provided values.

        Returns:
            int | float: Distance in this file version
        """
        pass


