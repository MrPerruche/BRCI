from json import loads as json_load
from zlib import crc32 as zlib_crc32
import os

from .data import BRCI_CWD
from ..exceptions import *


# Soon:tm:

"""

fonts: dict[ str, dict[str, list[list[ list[int] ]] ] ] = {}
font_colors: dict[str, dict[str, list[int]]] = {}

def load_font(json_font_path: str, font_name: str) -> None:

    \"""
    Will load a font from a json file. The json file must have the following structure:
    {
        "colors": {
            " ": [<color for empty>],
            "<character to replace>": [<r>, <g>, <b>],
            ...
        },
        "none": [
            "<pixels as characters for each line. They will be replaced with the color assigned to it in colors dict>",
            ...
        ],
        "<glyph>": [
            "<pixels as characters for each line. They will be replaced with the color assigned to it in colors dict>",
            ...
        ],
        ...
    }

    Arguments:
        json_font_path (str): Path to the json file.
        font_name (str): Name of the font.

    Exceptions:
        JSONDecodeError: json file is invalid
        FontError: If the json files' structure is invalid

    \"""

    global fonts, font_colors

    with open(json_font_path, 'r') as f:
        _current_font = json_load(f.read())

    if 'colors' not in _current_font.keys():
        raise FontError(f"Color mappings for json font not found when loading {font_name}.")

    if 'none' not in _current_font.keys():
        raise FontError(f"No glyph for unknown characters found when loading {font_name}.")

    font_colors.update({font_name: _current_font.pop('colors')})
    fonts.update({font_name: {k: [[ font_colors[font_name][char] for char in s] for s in a] for k, a in _current_font.items()}})


load_font(os.path.join(BRCI_CWD, 'resources', 'font.json'), 'default')



def generate_text_bitmap(text: str, size_x: int = 256, size_y: int = 256, scale: int = 3, background: Optional[list[int]] = None, font: str = 'default') -> list[list[ list[int] ]]:

    \"""
    Will convert text to a grid of RGBA values.
    \"""

    used_font: dict[str, list[list[ list[int] ]]] = fonts[font]
    used_colors = {char: col.copy() for char, col in font_colors[font].items()}  # faster than deepcopy
    if background is None:
        background_col = font_colors[font][' ']
    else:
        background_col = background
        used_colors[' '] = background
    position: int = 2 * scale
    text_height: int = len(used_font['none']) * scale
    lines: list[list[ list[int] ]] = [[background_col] * position for _ in range(text_height)]
    right_padding: int = position  # = 2 * padding. micro optimisation goes brrr
    is_auto_new_line: bool = False
    for char in text:
        if is_auto_new_line and char == ' ':
            continue
        else:
            is_auto_new_line = False
        printed_char: list[list[ list[int] ]] = [[pixel for pixel in line for _ in range(scale)] for line in used_font[char] for _ in range(scale)] if char in used_font else used_font['none']
        if char == '\n' or position + len(printed_char[0]) > size_x - right_padding:
            for i in range(text_height):
                lines[-text_height + i].extend([background_col] * (size_x - len(lines[-text_height + i])))
            position = 2 * scale
            lines.extend([[background_col] * position for _ in range(text_height)])
            if char == ' ':
                is_auto_new_line = True
                continue
            if char == '\n':
                continue
        for i, line in enumerate(printed_char):
            lines[-text_height + i].extend(line)
        position += len(printed_char[0])
    for i in range(text_height):
        lines[-text_height + i].extend([background_col] * (size_x - len(lines[-text_height + i])))

    if len(lines) > size_y:
        return lines[:size_y]
    # else:
    lines.extend([[background_col] * size_x] * (size_y - len(lines)))
    return lines

def crc32(data):
    return zlib_crc32(data) & 0xffffffff

"""
