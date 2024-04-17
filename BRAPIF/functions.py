import struct
from dataclasses import dataclass


class FM:
    reset = '\x1b[0m' # Reset code
    red = '\x1b[31m'
    blue = '\x1b[34m'
    green = '\x1b[32m'
    yellow = '\x1b[33m'
    purple = '\x1b[35m'
    cyan = '\x1b[36m'
    white = '\x1b[37m'
    black = '\x1b[30m'
    light_blue = '\x1b[94m'
    light_green = '\x1b[92m'
    light_red = '\x1b[91m'
    light_purple = '\x1b[95m'
    light_white = '\x1b[97m'
    light_black = '\x1b[90m'
    light_cyan = '\x1b[96m'
    light_yellow = '\x1b[93m'
    bold = '\x1b[1m'
    underline = '\x1b[4m'
    italic = '\x1b[3m'
    reverse = '\x1b[7m'
    strikethrough = '\x1b[9m'
    remove_color = '\x1b[39m'
    remove_bold = '\x1b[22m'
    remove_underline = '\x1b[24m'
    remove_italic = '\x1b[23m'
    remove_reverse = '\x1b[27m'
    remove_strikethrough = '\x1b[29m'
    bg_red = '\x1b[41m'
    bg_green = '\x1b[42m'
    bg_blue = '\x1b[44m'
    bg_yellow = '\x1b[43m'
    bg_black = '\x1b[40m'
    bg_white = '\x1b[47m'
    bg_light_red = '\x1b[101m'
    bg_light_green = '\x1b[102m'
    bg_light_blue = '\x1b[104m'
    bg_light_yellow = '\x1b[103m'
    bg_light_black = '\x1b[100m'
    bg_light_white = '\x1b[107m'
    bg_purple = '\x1b[45m'
    bg_light_purple = '\x1b[105m'
    bg_cyan = '\x1b[46m'
    bg_light_cyan = '\x1b[106m'
    info = f'{reverse}{light_blue}[INFO]{remove_reverse}'
    success = f'{reverse}{light_green}[SUCCESS]{remove_reverse}'
    error = f'{reverse}{light_red}[ERROR]'
    warning = f'{reverse}{yellow}[WARNING]'
    debug = f'{reverse}{light_purple}[DEBUG]{remove_reverse}'
    test = f'{reverse}{light_cyan}[TEST]{remove_reverse}'

    @staticmethod
    def error_with_header(header, text):
        print(f"{FM.error} {header}{FM.remove_reverse} \n{text}")

    @staticmethod
    def warning_with_header(header, text):
        print(f"{FM.warning} {header}{FM.remove_reverse} \n{text}")


def unsigned_int(integer, byte_len):

    if integer >= 2**(byte_len*8):
        raise OverflowError(f'Input is greater than {byte_len*8} bit limit of unsigned integer.')

    if integer < 0:
        raise OverflowError(f'Negative input. {integer} is less than 0.')

    return (integer & ((1 << (8 * byte_len)) - 1)).to_bytes(byte_len, byteorder='little', signed=False)


# Function to write signed negative integers of any byte length. Used for utf-16 encoding
def signed_int(integer, byte_len):
    return integer.to_bytes(byte_len, byteorder='little', signed=True)


# Function to write half, single and double precision float number
def bin_float(float_number, byte_len):

    if byte_len == 2:
        # Convert the float to a  32-bit integer representation
        float_bits = struct.unpack('<I', struct.pack('<f', float_number))[0]

        # Extract the sign, exponent, and mantissa from the float bits
        sign = (float_bits >> 16) & 0x8000
        exponent = (float_bits >> 23) & 0xFF
        mantissa = float_bits & 0x7FFFFF

        # Handle special cases
        if exponent == 255:
            # Infinity or NaN
            if mantissa:
                # NaN, return a half-precision NaN
                return struct.pack('<H', 0x7C00 | (mantissa >> 13))
            else:
                # Infinity, return a half-precision infinity
                return struct.pack('<H', sign | 0x7C00)

        # Subtract the bias from the exponent
        exponent -= 127

        # Check for overflow or underflow
        if exponent < -24:
            # Underflow, return zero
            return struct.pack('<H', sign)
        elif exponent > 15:
            # Overflow, return infinity
            return struct.pack('<H', sign | 0x7C00)

        # Normalize the mantissa and adjust the exponent
        mantissa >>= 13
        exponent += 15

        # Combine the sign, exponent, and mantissa into a half-precision float
        half_float_bits = (sign << 15) | (exponent << 10) | mantissa

        # Pack the half-precision float bits into a  16-bit binary string
        return struct.pack('<H', half_float_bits)

    elif byte_len == 4:  # Single-precision float
        float_bytes = struct.pack('<f', float_number)
    elif byte_len == 8:  # Double-precision float
        float_bytes = struct.pack('<d', float_number)
    else:
        raise ValueError("Invalid byte length for float")

    padded_bytes = float_bytes.ljust(byte_len, b'\x00')[:byte_len]

    return padded_bytes


# Function to write with utf-16 encoding (Neg. length excluded)
def bin_str(string):
    return string.encode('utf-16')


# Function to write with utf-8 encoding (Length excluded)
def small_bin_str(string):
    return string.encode('utf-8')


# Function to copy existing files into new directories
def copy_file(source_path, destination_path):
    with open(source_path, 'rb') as src_file:
        cp_data = src_file.read()

    _blank_preview = open(destination_path, "x")
    _blank_preview.close()

    with open(destination_path, 'wb') as destination_file:
        destination_file.write(cp_data)


def append_multiple(var, keys, value, gbn=False):
    for key in keys:

        var[key] = value.copy()

        if gbn:
            var[key]['gbn'] = key





@dataclass
class BrickInput:

    brick_input_type: str
    brick_input: any
    prefix: str
    last_chance: bool = False


    def properties(self):

        match self.brick_input_type:

            # For Always On (Constant Value)
            case 'AlwaysOn':
                # If its valid
                if isinstance(self.brick_input, (float, int)):
                    # If it's not the default value
                    if float(self.brick_input) != 1.0:
                        # Return both properties
                        return {
                            f'{self.prefix}.InputAxis': self.brick_input_type,
                            f'{self.prefix}.Value': float(self.brick_input)
                        }
                    # If it's the default value
                    # Return type only
                    else: return { f'{self.prefix}.InputAxis': self.brick_input_type }
                # Or if its invalid
                # Return type only
                else: return { f'{self.prefix}.InputAxis': self.brick_input_type }

            # Anything having as an input multiple bricks
            case 'Custom':
                if self.brick_input is None:
                    self.brick_input: list = []
                if isinstance(self.brick_input, list):
                    if self.brick_input: return {
                        f'{self.prefix}.InputAxis': self.brick_input_type,
                        f'{self.prefix}.SourceBricks': self.brick_input
                    }
                    else: return { f'{self.prefix}.InputAxis': self.brick_input_type }
                else: return 'invalid_source_bricks'
