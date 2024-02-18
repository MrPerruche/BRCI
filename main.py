import os
import struct

# ------------------------------------------------------------
# DEFAULT VARIABLES AND SETUP
# ------------------------------------------------------------

# Setup
interface_version = "B1"
algorithm_version = "A1"

# Important variables
cwd = os.path.dirname(os.path.realpath(__file__))
relative_projects_folder_path = "Projects"
project_folder_path = os.path.join(cwd, relative_projects_folder_path)

# Test variables
brick_list = [["switch"]]
metadata = ["FN", "FD", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]  # [file_name, file_description, brick_count, size_x, size_y, size_z, weight, money]


# ------------------------------------------------------------
# DATA WRITING FUNCTIONS
# ------------------------------------------------------------


# Function to write unsigned integers of any byte length
def unsigned_int(integer, byte_len):
    return (integer & ((1 << (8 * byte_len)) - 1)).to_bytes(byte_len, byteorder='little', signed=False)


# Function to write signed negative integers of any byte length. Used for utf-16 encoding
def signed_neg_int(integer, byte_len):
    max_positive = (1 << (8 * byte_len - 1)) - 1
    min_negative = -(max_positive + 1)
    if integer > max_positive or integer < min_negative:
        raise ValueError("Integer out of range for signed n-byte integer".format(byte_len))
    return (-abs(integer)).to_bytes(byte_len, byteorder='little', signed=True)


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

    with open(destination_path, 'wb') as destination_file:
        destination_file.write(cp_data)


# ------------------------------------------------------------
# METADATA.BRV GENERATOR
# ------------------------------------------------------------


def write_metadata(directory, blank):

    if blank:
        blank_metadata = open(os.path.join(directory, "MetaData.brm"), "x")
        blank_metadata.close()

    else:
        with open(os.path.join(directory, "MetaData.brm"), 'wb') as metadata_file:

            # Writes the amount of data (13 different information)
            metadata_file.write(unsigned_int(13, 1))

            # Write all necessary information for the file name
            line_feed_file_name = (((metadata[0].replace("\\n", "\n")).encode('utf-16')).replace(b'\x0A\x00', b'\x0D\x00\x0A\x00')).decode('utf-16')
            metadata_file.write(signed_neg_int(len(line_feed_file_name), 2))
            metadata_file.write(bin_str(line_feed_file_name)[2:])

            # Write all necessary information for the file description
            watermarked_file_description = f"Created using BR-Logic-API.\n" \
                                           f"Vehicle Generator Version {interface_version},\nOptimization Algorithm Version {algorithm_version}.\n\n" \
                                           f"Description:\n{metadata[1]}\n\nCode:\n"
            watermarked_file_description += str(code)
            watermarked_file_description = (((watermarked_file_description.replace("\\n", "\n")).encode('utf-16')).replace(b'\x0A\x00',b'\x0D\x00\x0A\x00')).decode(
                'utf-16')
            metadata_file.write(signed_neg_int(len(watermarked_file_description), 2))
            metadata_file.write(bin_str(watermarked_file_description)[2:])

            # Write all necessary information for the 4 additional values : Bricks, Size, Weight and Monetary Value
            # [file_name, file_description, brick_count, size_x, size_y, size_z, weight, money]
            metadata_file.write(signed_neg_int(metadata[2], 2))
            metadata_file.write(bin_float(metadata[3], 4))
            metadata_file.write(bin_float(metadata[4], 4))
            metadata_file.write(bin_float(metadata[5], 4))
            metadata_file.write(bin_float(metadata[6], 4))
            metadata_file.write(bin_float(metadata[7], 4))

            # Writes the author. We don't want it to be listed, so we write invalid data.
            metadata_file.write(bytes.fromhex('FFFFFFFFFFFFFFFF'))

            # I have no fucking clue of what I'm writing but hey it's something right?
            metadata_file.write(bytes.fromhex("14686300000000B034B6C7382ADC08E079251F392ADC08"))

            # Writing tags (They don't work gotta fix that AAAAAAAAAAAAAAA)
            metadata_file.write(unsigned_int(3, 1))
            for i in range(3):
                metadata_file.write(unsigned_int(5, 1))
                metadata_file.write(small_bin_str("Other"))


# ------------------------------------------------------------
# PREVIEW.PNG AND CODE.BRC GENERATOR
# ------------------------------------------------------------


# Code.brc
def write_brc(directory):
    brc_write = "setup {"\
               f"\n    file_name = \"{project}\""\
               f"\n    file_description = \"\""\
               f"\n    algorithm_version = \"{algorithm_version}\""\
               f"\n    center_position = [0, 0, 0]"\
               f"\n    center_rotation = [0, 0, 0]"\
               "\n}"
    with open(os.path.join(directory, "Code.brc"), 'w') as brc_file:
        # Write the data to the file
        brc_file.write(brc_write)


# Preview.png
def write_preview(directory):
    copy_file(os.path.join(cwd, "Resources", "icon_compressed_reg.png"), os.path.join(directory, "Preview.png"))


# ------------------------------------------------------------
# VEHICLE.BRV GENERATOR
# ------------------------------------------------------------


def write_brv(directory, blank, bricks):

    if blank:
        fp_vehicle = open(os.path.join(directory, "Vehicle.brv"), "x")
        fp_vehicle.close()

    else:
        print("that one shitty part")


# ------------------------------------------------------------
# RUN ALL GENERATORS
# ------------------------------------------------------------

def write_blank(directory):
    write_metadata(directory, True)
    write_preview(directory)
    write_brc(directory)
    write_brv(directory, True, [])





# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------


# TODO : Replace the project input once we got the UI program.

new_file = False

while True:

    project = input("\nInsert the project's name. It must be in the \"Projects\" folder.\n> ")
    project_in_path = os.path.join(project_folder_path, project)

    # Creating the folder if missing
    if not os.path.exists(os.path.join(project_folder_path, project)):

        new_file = True

        new_project_request = input(f"\nPath not found. Would you like to create the new project \"{project}\"? [Yes/No]\n> ").lower()

        if new_project_request == "yes" or new_project_request == "y":

            # Creating the folder
            os.makedirs(os.path.join(project_folder_path, project))
            project_in_path = os.path.join(project_folder_path, project)

            write_blank(project_in_path)

            break

    else:
        break

# Read the BRCode
with open(os.path.join(project_in_path, "Code.brc"), 'r') as file:
    code = file.read()


# ------------------------------------------------------------
# CONVERT PROGRAM
# ------------------------------------------------------------


# Write stuff
def convert(directory, bricks):
    write_metadata(directory, False)
    write_preview(directory)
    write_brc(directory)
    write_brv(directory, False, bricks)