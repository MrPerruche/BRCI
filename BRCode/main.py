# Imports
import os
from sys import exit
import re

# Setup Stuff
brvgen_version = f"A3"
alg_version = f"A0 (TODO)"

# Startup Screen
print("████████████═╗  ████████████═╗    ████████████═╗  ████████████═╗  ████████████═╗  ██████████████═╗\
\n████╔═════████═╗████╔═════████═╗████ ╔═════════╝████ ╔══════████═╗████ ╔════████═╗████ ╔═════════╝\
\n████████████ ╔═╝████████████ ╔═╝████ ║          ████ ║      ████ ║████ ║    ████ ║██████████═╗\
\n████╔═════████═╗████ ╔════████═╗████ ║          ████ ║      ████ ║████ ║    ████ ║████ ╔═════╝\
\n████████████ ╔═╝████ ║    ████ ║╚═████████████═╗╚═████████████ ╔═╝████████████ ╔═╝██████████████═╗████═╗\
\n╚════════════╝  ╚════╝    ╚════╝  ╚════════════╝  ╚════════════╝  ╚════════════╝  ╚══════════════╝╚════╝")
print(f"\nVehicle Generator : Version {brvgen_version}. Program Optimizer: Version {alg_version}.\n\n")

# First User Input
while True:

    startupInput = input(f"\"start\" : Start the program. \"help\" : Show the tutorial. \"credits\" : See credits.\n> ")

    if startupInput == "help":
        print("\nThis is debug help. You're welcome.\n")

    elif startupInput == "credits":
        print("\nCredits :\n"
              "- Destiny @destiny_29 : Programming, Creator\n"
              "- Perru @perru_ : Programming\n"
              "- Fluppi393 @fluppi393 : Game developer, shared game's code.\n")

    elif startupInput == "start":
        break

    else:
        print("\nInvalid input. Retry.\n")

# Get the current working directory of the script
cwd = os.path.dirname(os.path.realpath(__file__))

# Define the relative path to the Projects folder from the script's location
# Start the relative path directly from the "Projects" folder
relative_projects_folder_path = "Projects"

# Combine the script's current working directory with the relative path to the Projects folder
projectFolderPath = os.path.join(cwd, relative_projects_folder_path)

project = input("\nInsert the project's name. It must be in the \"Projects\" folder.\n> ")

# Creating the folder if missing
if not os.path.exists(os.path.join(projectFolderPath, project)):
    while True:
        newProjectRequest = input(f"\nPath not found. Would you like to create the new project \"{project}\"? [Yes/No]\n> ").lower()

        if newProjectRequest == "yes" or newProjectRequest == "y":
            try:
                # Creating the folder
                os.makedirs(os.path.join(projectFolderPath, project))
                projectInPath = os.path.join(projectFolderPath, project)

                # Creating the Metadata.brm file (Blank)
                fpMetadata = open(os.path.join(projectInPath, "Metadata.brm"), "x")
                fpMetadata.close()

                # Creating the Vehicle.brv file (Blank)
                fpVehicle = open(os.path.join(projectInPath, "Vehicle.brv"), "x")
                fpVehicle.close()

                # Creating the BRCode.txt file (Blank)
                fpBRCode = open(os.path.join(projectInPath, "BRCode.txt"), "x")
                fpBRCode.close()

                # Setup the BRCode.txt file (Blank)
                BRCodeWrite = "setup {"\
                              f"\n    fileName = \"{project}\""\
                              f"\n    fileDescription = \"\""\
                              f"\n    codeVersion = \"{brvgen_version}\""\
                              "\n    centerPosition = [0, 0, 0]"\
                              "\n    centerRotation = [0, 0, 0]\n}"
                with open(os.path.join(projectInPath, "BRCode.txt"), 'w') as file:
                    # Write the data to the file
                    file.write(BRCodeWrite)

                input("\nThe file was successfully create. Please write your code in BRCode.txt and rerun the program to generate Vehicle.brv. Press enter tp end")
                exit()

            except Exception as e:
                print(f"An error occurred: {e}")

projectInPath = os.path.join(projectFolderPath, project)

# Writing metadata


# Declare all variables at the start of your script
fileName = None
fileDescription = None
codeVersion = None
centerPosition = None
centerRotation = None


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
with open(os.path.join(projectInPath, "BRCode.txt"), 'r') as file:
    file_content = file.read()

# Parse the setup block and update the variables
parse_setup_block(file_content)

# Now you can access the variables directly
print(fileName)  # Should output: testDoNotDelete
print(centerPosition)  # Should output: [0,  0,  0]