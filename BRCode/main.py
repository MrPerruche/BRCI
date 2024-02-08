# Imports
import os
import re  # Regex, ooo spooky!


# Setup Stuff
brvgen_version = f"A6"
alg_version = f"A0 (TODO)"
new_file = False


# Startup Screen
print("████████████═╗  ████████████═╗    ████████████═╗  ████████████═╗  ████████████═╗  ██████████████═╗\
\n████ ╔════████═╗████ ╔════████═╗████ ╔═════════╝████ ╔══════████═╗████ ╔════████═╗████ ╔═════════╝\
\n████████████ ╔═╝████████████ ╔═╝████ ║          ████ ║      ████ ║████ ║    ████ ║██████████═╗\
\n████ ╔════████═╗████ ╔════████═╗████ ║          ████ ║      ████ ║████ ║    ████ ║████ ╔═════╝\
\n████████████ ╔═╝████ ║    ████ ║╚═████████████═╗╚═████████████ ╔═╝████████████ ╔═╝██████████████═╗████═╗\
\n╚════════════╝  ╚════╝    ╚════╝  ╚════════════╝  ╚════════════╝  ╚════════════╝  ╚══════════════╝╚════╝")
print(f"\nVehicle Generator : Version {brvgen_version}. Program Optimizer: Version {alg_version}.\n\n")

# First User Input
while True:

    startup_Input = input(f"\"start\" : Start the program. \"help\" : Show the tutorial. \"credits\" : See credits. \"build\" : Convert to import\n> ")

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

project = input("\nInsert the project's name. It must be in the \"Projects\" folder.\n> ")

# Creating the folder if missing
if not os.path.exists(os.path.join(project_folder_path, project)):

    new_file = True

    while True:
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
                    f"\n    center_rotation = [0, 0, 0]"
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

testnum = 12


def createmetadata(is_new_file):

    watermarked_file_description = f"Created using BR-Logic-API by @destiny_29 and @perru_.\n"\
        f"Vehicle Generator Version {brvgen_version},\nOptimization Algorithm Version {alg_version}\n\n"\
        f"Description:\n{file_description}\n\nCode:\n{BRCode}"

    """
    md_to_write = ""
    md_to_write += "13"  # 8
    md_to_write += len(file_name)  # 16
    md_to_write += file_name
    md_to_write += len(file_description)  # 16
    md_to_write += watermarked_file_description
    """

    # TODO: Finish this

    # print(md_to_write)
    with open(os.path.join(project_in_path, "MetaData.brm"), 'wb') as metadatafile:
        metadatafile.write((len(file_name) & 0xFFFF).to_bytes(2, byteorder='little'))
        metadatafile.write(file_name.encode("utf-8"))


createmetadata(new_file)
