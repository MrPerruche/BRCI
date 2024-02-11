# Imports
import os
import re  # Regex, ooo spooky!
import struct
import numpy as np


# Setup Stuff
brvgen_version = f"A7"
alg_version = f"A0 (TODO)"
new_file = False
brick_count = 123
monetary_value = 456
weight_kg = 7.89
size_x = 1011.12
size_y = 13.1415
size_z = 0.161718


# Functions

# -Changing int size
def setuintsize(integer, byte_len):
    return (integer & (1 << (8 * byte_len) - 1)).to_bytes(byte_len, byteorder='little')


# -Changing int size, outputs negative signed int
def setnintsize(integer, byte_len):
    max_positive = (1 << (8 * byte_len - 1)) - 1
    min_negative = -(max_positive + 1)
    if integer > max_positive or integer < min_negative:
        raise ValueError("Integer out of range for signed n-byte integer".format(byte_len))
    return (-abs(integer)).to_bytes(byte_len, byteorder='little', signed=True)


# -Changing float size
def setfloatsize(float_number, byte_len):
    # Convert the float to the appropriate precision
    if byte_len == 2:
        # Half-precision float (not natively supported, using numpy)
        float_bytes = np.float16(float_number).tobytes()
    elif byte_len == 4:
        # Single-precision float
        float_bytes = struct.pack('!f', float_number)
    elif byte_len == 8:
        # Double-precision float
        float_bytes = struct.pack('!d', float_number)
    else:
        raise ValueError("Invalid byte length for float")

    # Ensure the bytes are the correct length, padding with zeros if necessary
    padded_bytes = float_bytes.ljust(byte_len, b'\x00')[:byte_len]

    return padded_bytes


# -Writing string with utf-16 (unicode) encoding
def bstr(string):
    return string.encode('utf-16')


def sbstr(string):
    return string.encode('utf-8')


# Startup Screen
print(
    "█████████╗ █████████╗       ███╗        █████████╗  █████████╗ ███╗ █████████╗       ████████╗ ████████╗ ███╗\n"
    "███╔═══███╗███╔═══███╗      ███║       ███╔════███╗███╔══════╝ ███║███╔══════╝      ███╔═══███╗███╔══███╗███║\n"
    "█████████╔╝█████████╔╝█████╗███║       ███║    ███║███║  █████╗███║███║       █████╗██████████║████████╔╝███║\n"
    "███╔═══███╗███╔═══███╗╚════╝███║       ███║    ███║███║  ╚═███║███║███║       ╚════╝███╔═══███║███╔════╝ ███║\n"
    "█████████╔╝███║   ███║      ██████████╗╚█████████╔╝╚█████████╔╝███║╚█████████╗      ███║   ███║███║      ███║\n"
    "╚════════╝ ╚══╝   ╚══╝      ╚═════════╝ ╚════════╝  ╚════════╝ ╚══╝ ╚════════╝      ╚══╝   ╚══╝╚══╝      ╚══╝\n"
    "████████████████████████████████████████████████████████████████████████████████████████████████████████████╗\n"
    "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
print(f"Vehicle Generator : Version {brvgen_version}. Program Optimizer: Version {alg_version}.\n\n")


# First User Input
while True:

    startup_Input = input(f"\"start\"   : Create a new project or convert an existing project into BrickRigs.\n\"help\"    : Explain in detail how the BR-Logic-API works.\n\"credits\" : List everyone involved in this program.\n\"build\"   : Convert any program to a module (importable program)\n> ")

    if startup_Input == "help":
        print("\nThis is debug help. You're welcome.\n")

    elif startup_Input == "credits":
        print("\nCredits :\n"
              "- Destiny @destiny_29 : Programming, Creator\n"
              "- Perru @perru_ : Programming\n"
              "- Fluppi393 @fluppi393 : Game developer, shared game's code.\n")

    elif startup_Input == "start":
        break

    else:
        print("\nInvalid input. Retry.\n")

# Get the current working directory of the script
cwd = os.path.dirname(os.path.realpath(__file__))

# Define the relative path to the Projects folder from the script's location
# Start the relative path directly from the "Projects" folder
relative_projects_folder_path = "Projects"

# Combine the script's current working directory with the relative path to the Projects folder
project_folder_path = os.path.join(cwd, relative_projects_folder_path)

while True:

    project = input("\nInsert the project's name. It must be in the \"Projects\" folder.\n> ")

    # Creating the folder if missing
    if not os.path.exists(os.path.join(project_folder_path, project)):

        new_file = True

        new_project_request = input(f"\nPath not found. Would you like to create the new project \"{project}\"? [Yes/No]\n> ").lower()

        if new_project_request == "yes" or new_project_request == "y":
            try:
                # Creating the folder
                os.makedirs(os.path.join(project_folder_path, project))
                project_in_path = os.path.join(project_folder_path, project)

                # Creating the Metadata.brm file (Blank)
                fp_metadata = open(os.path.join(project_in_path, "MetaData.brm"), "x")
                fp_metadata.close()

                # Creating the Vehicle.brv file (Blank)
                fp_vehicle = open(os.path.join(project_in_path, "Vehicle.brv"), "x")
                fp_vehicle.close()

                # Creating the BRCode.txt file (Blank)
                fp_BRCode = open(os.path.join(project_in_path, "BRCode.txt"), "x")
                fp_BRCode.close()

                # Setup the BRCode.txt file (Blank)
                BRCode_write = "setup {"\
                    f"\n    file_name = \"{project}\""\
                    f"\n    file_description = \"\""\
                    f"\n    code_version = \"{brvgen_version}\""\
                    f"\n    center_position = [0, 0, 0]"\
                    f"\n    center_rotation = [0, 0, 0]"\
                    "\n}"
                with open(os.path.join(project_in_path, "BRCode.txt"), 'w') as file:
                    # Write the data to the file
                    file.write(BRCode_write)

                input("\nThe file was successfully created. Please write your code in BRCode.txt.\nPress enter to continue or quit the program.")
                break

            except Exception as e:
                print(f"An error occurred: {e}")

project_in_path = os.path.join(project_folder_path, project)

# Writing metadata


# Declare all variables at the start of your script
file_name = "unknown"
file_description = "unknown"
code_version = "unknown"
center_position = [0, 0, 0]
center_rotation = [0, 0, 0]


# Function to parse the setup block and extract variables
def parse_setup_block(thefilescontent):
    # Regular expression pattern to match the setup block
    setup_pattern = r"setup\s*\{\n((?:.*\n)+?)\}"

    # Find the setup block using regex
    setup_match = re.search(setup_pattern, thefilescontent, re.MULTILINE | re.DOTALL)

    # If the setup block is found
    if setup_match:
        # Extract the content inside the setup block
        setup_content = setup_match.group(1).strip()

        # Split the content into lines
        setup_lines = setup_content.split('\n')

        # Process each line in the setup block
        for line in setup_lines:
            # Remove any leading or trailing whitespace
            line = line.strip()

            # Check if the line contains an assignment
            if '=' in line:
                # Split the line into key and value
                key, value = line.split('=', 1)

                # Strip any whitespace around the key and value
                key = key.strip()
                value = value.strip()

                # Remove quotes from string literals
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]

                # Update the global variable with the value
                globals()[key] = value


# Read the contents of the custom code file
with open(os.path.join(project_in_path, "BRCode.txt"), 'r') as file:
    BRCode = file.read()

# Parse the setup block and update the variables
parse_setup_block(BRCode)


def createmetadata(is_new_file):

    # TODO: Finish this

    with open(os.path.join(project_in_path, "MetaData.brm"), 'wb') as metadatafile:

        # Writes 13 in 8ubit. Not sure what it is for, its just there.
        metadatafile.write(setuintsize(13, 1))

        # Write all necessary information for the file name
        metadatafile.write(setnintsize(len(file_name), 2))
        metadatafile.write(bstr(file_name))

        # Write all necessary information for the file description
        watermarked_file_description = f"Created using BR-Logic-API by @destiny_29 and @perru_.\n" \
                                       f"Vehicle Generator Version {brvgen_version},\nOptimization Algorithm Version {alg_version}\n\n" \
                                       f"Description:\n{file_description}\n\nCode:\n{BRCode}"
        metadatafile.write(setnintsize(len(watermarked_file_description), 2))
        metadatafile.write(bstr(watermarked_file_description))

        # Write all necessary information for the 4 additional values : Bricks, Size, Weight and Monetary Value
        metadatafile.write(setuintsize(brick_count, 2))
        metadatafile.write(setfloatsize(size_x, 4))
        metadatafile.write(setfloatsize(size_y, 4))
        metadatafile.write(setfloatsize(size_z, 4))
        metadatafile.write(setfloatsize(weight_kg, 4))
        metadatafile.write(setfloatsize(monetary_value, 4))

        # Writes the author. We don't want it to be listed so we write invalid data.
        metadatafile.write(sbstr("NoAuthor"))
        metadatafile.write()


createmetadata(new_file)
