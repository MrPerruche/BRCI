import os
# from warnings import warn as raise_warning
from copy import deepcopy

from BRCI_RF import *

# Note : every time you see unsigned_int() / signed_int() / bin_float(), byte_len * 8 is the number of bits.

# TODO Add more jokes in comments because they're pretty annoying.
# TODO Comment each variable to specify their content & classes for rust translation.
# TODO Add all bricks in br_brick_list
# TODO Calculate vehicle_size, vehicle_weight and vehicle_worth
# TODO Find another way to make Brick Inputs. (Perhaps they should work and I'm just an idiot?)
# TODO Finish Appendix System
# TODO Implement Brick Loading (IDEA : Exclusively load user appendix)?

# ------------------------------------------------------------
# DEFAULT VARIABLES AND SETUP
# ------------------------------------------------------------



# Setup variables
version: str = "C31"  # String, This is equivalent to 3.__ fyi

# Important variables
_cwd = os.path.dirname(os.path.realpath(__file__))  # File Path

# Colors

from os import system as os_system
os_system('color')

# ------------------------------------------------------------
# DATA WRITING
# ------------------------------------------------------------


# Return all data about specified brick
#def create_brick(brick: str):
    #return br_brick_list[brick].copy()

# pain

def create_brick(brick: str, position: list[float] = None, rotation: list[float] = None, brick_properties: dict = None) -> dict:
    if brick_properties is None:
        brick_properties = {}
    if position is None:
        position = [0, 0, 0]
    if rotation is None:
        rotation = [0, 0, 0]
    return deepcopy(br_brick_list[brick]) | {'Position': position, 'Rotation': rotation} | brick_properties


# Brick Rigs API Class
class BRCI:

    # Grab values
    def __init__(self,
                 bricks=None,
                 project_folder_directory='',
                 project_name='',
                 write_blank=False,
                 project_display_name='',
                 file_description='',
                 debug_logs=None,
                 user_appendix=b'',
                 seat_brick=None):

        # Set each self.x variable to their __init__ counterparts
        self.project_folder_directory = project_folder_directory  # Path
        self.project_name = project_name  # String
        self.write_blank = write_blank  # Boolean
        self.project_display_name = project_display_name  # String (in-game name (.brm))
        self.file_description = file_description  # String (The description of the file (.brm))
        if bricks is None:  # List (If unspecified, create an empty list)
            bricks = [] # Initialize bricks
        self.bricks = bricks # List (Of bricks)
        if debug_logs is None:
            debug_logs = []
        self.debug_logs = debug_logs # List of logs to print
        self.user_appendix = user_appendix # List (User appendix)
        self.seat_brick = seat_brick


    # Creating more variables
    # In project path
    @property
    def in_project_folder_directory(self): # String
        return os.path.join(self.project_folder_directory, self.project_name)

    # Calculate brick count
    @property
    def brick_count(self): # 16 Bit integer
        return len(self.bricks)

    # Calculate vehicle size
    @property
    def vehicle_size(self): # List of 3 32-bit float
        # TODO : CALCULATE SIZE
        return [1, 2, 3]

    # Calculate vehicle weight
    @property
    def vehicle_weight(self): # 32 bit float
        # TODO : CALCULATE WEIGHT
        return 0.1

    # Calculate vehicle worth
    @property
    def vehicle_worth(self): # 32 bit float
        # TODO : CALCULATE WORTH
        return 0.2 # I wonder if this will make it 0.2 in-game? Or does BR calculate the price itself?


    # Adding bricks to the brick list
    def add_brick(self, brick_name: str | list[dict], brick: dict | list[dict]):
        if isinstance(brick_name, str):
            self.bricks.append([str(brick_name), brick])
        else:
            for add_brick_i in range(len(brick)):
                self.bricks.append([str(brick_name[add_brick_i]), brick[add_brick_i]])

        return self


    def add_new_brick(self, brick_name: str | list[str], brick_type: str | list[str], brick: dict | list[dict]):
        if isinstance(brick_type, str):
            self.bricks.append([str(brick_name), create_brick(brick=brick_type, brick_properties=brick)])
        else:
            for add_new_brick_i in range(len(brick_type)):
                self.bricks.append([str(brick_name[add_new_brick_i]), create_brick(brick=brick_type[add_new_brick_i], brick_properties=brick[add_new_brick_i])])

    
    def add_all_bricks(self, local_variables: list[dict]):

        iteration_count = len(self.bricks)
        for var in local_variables:
            # Check if it is a dict
            if isinstance(var, dict):
                # Check if it is from create_brick()
                if 'default_brick_data' in var:
                    iteration_count += 1; self.add_brick(str(iteration_count), var)


    # Removing bricks from the brick list
    def remove_brick(self, brick_name: str):

        self.bricks = [sublist for sublist in self.bricks if sublist[0] != str(brick_name)]

        return self


    # Updating a currently existing brick
    def update_brick(self, brick_name: str, new_brick: dict):
        self.remove_brick(brick_name)
        self.add_brick(brick_name, new_brick)

        return self


    def ensure_valid_variable_type(self, variable_name: str, occured_when: str) -> None:
        match variable_name:
            case 'write_blank':
                if not isinstance(self.write_blank, bool):
                    FM.error_with_header("Invalid write_blank type.", f"Whilst {occured_when}, write_blank was found not to be a boolean, it was instead a {type(self.write_blank).__name__}.\nIt is now set to False.")
                    self.write_blank = False
            case 'bricks_len':
                if len(self.bricks) > 65535:
                    FM.error_with_header("Too many bricks.",
                        f"Whilst {occured_when}, the length of the list of bricks was found to exceed 65,535.\n"
                        f"Therefore, the last {len(self.bricks)-65535 :,} brick(s) were removed. 65,535 bricks left.")
                    self.bricks = self.bricks[:65535]
            case 'logs':
                logs_whitelist_list: list[str] = ['time', 'bricks']
                invalid_logs_list: list[str] = []
                for log_request_str in self.debug_logs:
                    if not log_request_str in logs_whitelist_list:
                        invalid_logs_list.append(log_request_str)
                if invalid_logs_list:
                    invalid_logs_str: str =  ', '.join(invalid_logs_list)
                    logs_whitelist_str: str = ', '.join(logs_whitelist_list)
                    FM.warning_with_header("Unknown log(s) type requested.",
                        f"Whilst {occured_when}, the following log(s) type requested were found to be invalid: "
                        f"{invalid_logs_str}.\nYou may instead use the following: {logs_whitelist_str}.")



    # Used to create directory for file generators
    def ensure_project_directory_exists(self):

        # Verify for invalid inputs
        if not os.path.exists(self.project_folder_directory):

            raise FileNotFoundError(f'Unable to find the project\'s folder ({self.project_folder_directory})')

        os.makedirs(os.path.dirname(os.path.join(self.in_project_folder_directory, self.project_name)), exist_ok=True)


    # Writing preview.png
    def write_preview(self):

        _write_preview_regular_image_path = os.path.join(_cwd, 'Resources', 'icon_beta.png') # Path

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Verify the image exists.
        if not os.path.exists(_write_preview_regular_image_path):

            FM.error_with_header("Image not found", "Whilst writing Preview.png, we were unable to find BR-API default image. Please retry.")

        # Copy saved image to the project folders.
        else:
            if os.path.exists(os.path.join(self.in_project_folder_directory, "Preview.png")):
                FM.warning_with_header("Preview.png already created", "Whilst writing Preview.png, we noticed it was already added.\nThe old Preview.png was therefore replaced.")
                os.remove(os.path.join(self.in_project_folder_directory, "Preview.png"))

            copy_file(os.path.join(_write_preview_regular_image_path),
                os.path.join(self.in_project_folder_directory, "Preview.png"))

    # Writing metadata.brm file
    def write_metadata(self):

        # Create folder if missing
        self.ensure_project_directory_exists()
        self.ensure_valid_variable_type('write_blank', 'writing MetaData.brm')
        self.ensure_valid_variable_type('bricks_len', 'writing MetaData.brm')

        # Write blank file for metadata (if desired)
        if self.write_blank:

            with open(os.path.join(self.in_project_folder_directory, "MetaData.brm"), "x"):
                pass

        # Otherwise write working metadata file
        else:
            with open(os.path.join(self.in_project_folder_directory, "MetaData.brm"), 'wb') as metadata_file:

                # Writes Carriage Return char
                metadata_file.write(unsigned_int(13, 1))

                # Write all necessary information for the file name
                metadata_file.write(signed_int(-len(self.project_display_name), 2))
                metadata_file.write(bin_str(self.project_display_name)[2:])

                # Write all necessary information for the file description
                watermarked_file_description = f"Created using BR-API (Version {version}).\n" \
                                               f"Join our discord for more information : [INVITE LINK]\n\n" # String
                if self.file_description is not None:
                    watermarked_file_description += f'Description:\n{self.file_description}.'
                metadata_file.write(signed_int(-len(watermarked_file_description), 2))
                metadata_file.write(bin_str(watermarked_file_description)[2:])

                # Write all necessary information for the 4 additional values : Bricks, Size, Weight and Monetary Value
                metadata_file.write(unsigned_int(self.brick_count, 2))
                metadata_file.write(bin_float(self.vehicle_size[0], 4))
                metadata_file.write(bin_float(self.vehicle_size[1], 4))
                metadata_file.write(bin_float(self.vehicle_size[2], 4))
                metadata_file.write(bin_float(self.vehicle_weight, 4))
                metadata_file.write(bin_float(self.vehicle_worth, 4))

                # Writes the author. We don't want it to be listed, so we write invalid data.
                metadata_file.write(bytes.fromhex('FFFFFFFFFFFFFFFF')) # What if a steam ID someday reaches this limit? Never!

                # I have no fucking clue of what I'm writing but hey it's something right?
                metadata_file.write(bytes.fromhex("14686300000000B034B6C7382ADC08E079251F392ADC08")) # Peak programming. TODO Figure out what the fuck we're writing here


                # Write a function for a very specific and stupid purpose
                def write_tags_to_file(tag1: str = "Other", tag2: str = "Other", tag3: str = "Other"):
                    metadata_file.write(unsigned_int(3, 1))
                    for i in range(3):
                        metadata_file.write(unsigned_int(5, 1))
                        metadata_file.write(small_bin_str(locals()[f"tag{i+1}"])) # "locals()" returns the dict of all variables in the current scope
                        # Trying to modify said dict will actually add a new variable or change an existing one. I don't know why, since it is returning the *current* variables.


                # Writing tags                                                                                          FIXME
                write_tags_to_file() # TODO: Add a way to input tags. For now, they are all "Other"



    # Sharing some variables from writing vehicle.brv to the rest of the class
    bricks_writing = []
    inverted_property_key_table = {}
    id_assigned_property_table = {}
    brapi_appendix: list = []



    # Writing Vehicle.brv
    def write_brv(self):

        self.ensure_project_directory_exists()

        # Verify self.write_blank is valid.
        self.ensure_valid_variable_type('write_blank', 'writing Vehicle.brv')

        # Write blank file for vehicle (if desired)
        if self.write_blank:
            blank_brv = open(os.path.join(self.in_project_folder_directory, "Vehicle.brv"), "x")
            blank_brv.close()

        # Otherwise write working vehicle file
        else:

            # Show generation time if debug logs
            from time import perf_counter
            previous_time = perf_counter()
            begin_time = perf_counter()

            def brv_brick_types(bricks: list, debug: bool = False) -> list:
                brick_types_f = list(set(item[1]['gbn'] for item in bricks))
                if debug:
                    print(f'{FM.debug} Brick Types......... : {brick_types_f}')
                return brick_types_f


            # Add missing properties. Only made for BrickInput() but there may be more stuff later on
            def add_missing_properties(bricks: list, debug: bool = False) -> None:
                # For each brick
                for brick_mp in bricks:
                    # Initialising required variables
                    properties_to_add: dict = {}
                    properties_to_remove: list = []
                    # For each property
                    for property_key_mp, property_value_mp in brick_mp[1].items():
                        # If it's set to the BrickInput class
                        if isinstance(property_value_mp, BrickInput):
                            # Get the right property list
                            prop_mp_temp = property_value_mp.properties()
                            # If it's incorrect
                            if isinstance(prop_mp_temp, str) and prop_mp_temp == 'invalid_source_bricks':
                                FM.error_with_header("Invalid type for brick list.",f"Whilst writing Vehicle.brv,"
                                    f"we noticed {property_key_mp} (from brick {brick_mp[0]!r}) was not set to a list."
                                    f"\nIt was set to type {type(property_value_mp).__name__}. It is now set to None, corresponding to no inputs.")
                                property_value_mp.brick_input = []
                                prop_mp_temp = property_value_mp.properties()
                            # Get rid of the old, put the new instead
                            properties_to_add.update(prop_mp_temp)
                            properties_to_remove.append(property_key_mp)
                    for property_to_remove in properties_to_remove:
                        del brick_mp[1][property_to_remove]
                    brick_mp[1].update(properties_to_add)
                if debug:
                    print(f'{FM.debug} Modified Brick List. : {bricks}')


            # Verify if there are too many bricks
            self.ensure_valid_variable_type('bricks_len', 'writing Vehicle.brv')
            self.ensure_valid_variable_type('logs', 'writing Vehicle.brv')

            with (open(os.path.join(self.in_project_folder_directory, "Vehicle.brv"), 'wb') as brv_file):


                self.bricks_writing = self.bricks.copy()

                # Writes Carriage Return char
                brv_file.write(unsigned_int(13, 1))
                # Write brick count
                brv_file.write(unsigned_int(len(self.bricks_writing), 2))

                # Add all missing properties, notably inputs.
                add_missing_properties(self.bricks_writing, 'bricks' in self.debug_logs)

                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Missing Properties.. : {perf_counter() - previous_time :.6f} seconds')

                # Get the different bricks present in the project
                brick_types = brv_brick_types(self.bricks_writing, 'bricks' in self.debug_logs) # List

                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Brick Types......... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                # Write the number of different brick types
                brv_file.write(unsigned_int(len(brick_types), 2))

                # [ Getting rid of all properties that are set to the default value for each brick ]
                # Brick list filtering variables
                temp_iebl = []  # List of lists containing an integer and a list containing a dictionary and integers
                safe_property_list: list[str] = ['gbn', 'Position', 'Rotation']

                # Defining bricks
                w_current_brick_id = 0  # 16 bit
                string_name_to_id_table = {}
                property_table = {}

                # List Properties
                for current_brick in self.bricks_writing:
                    # Add all bricks without including data
                    temp_iebl.append([w_current_brick_id, [{}, {}]])
                    string_name_to_id_table[current_brick[0]] = w_current_brick_id
                    w_current_brick_id += 1

                    # For each data for each brick
                    for p_del_current_key, p_del_current_value in current_brick[1].items():

                        # Accept if it's in the safe list (list which gets whitelisted even if default value is identical)
                        if p_del_current_key in safe_property_list:
                            temp_iebl[-1][1][0][p_del_current_key] = p_del_current_value
                        # Otherwise regular process: if not default, get rid of it
                        elif p_del_current_key not in br_brick_list[current_brick[1]['gbn']]:

                            # THE SAME THING AS DOWN BELOW

                            temp_iebl[-1][1][1][p_del_current_key] = p_del_current_value
                            # Make sure key in the dict exists
                            property_table.setdefault(p_del_current_key, [])
                            # Setup property table
                            if p_del_current_value not in property_table[p_del_current_key]:
                                property_table[p_del_current_key].append(p_del_current_value)

                        elif p_del_current_value != br_brick_list[current_brick[1]['gbn']][p_del_current_key]:

                            temp_iebl[-1][1][1][p_del_current_key] = p_del_current_value
                            # Make sure key in the dict exists
                            property_table.setdefault(p_del_current_key, [])
                            # Setup property table
                            if p_del_current_value not in property_table[p_del_current_key]:
                                property_table[p_del_current_key].append(p_del_current_value)


                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: ID Assigning........ : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()


                # Setup property ids
                w_current_property_id: int = 0  # 32 bit
                w_property_count: int = 0 # 32 bit
                property_key_table: dict = {}
                w_property_key_num: int = 0

                # Give IDs to all values in var 'id_assigned_property_table'
                for property_value_key, property_value_value in property_table.items():

                    self.id_assigned_property_table = self.id_assigned_property_table | {property_value_key: {}}

                    for pvv_value in property_value_value:

                        self.id_assigned_property_table[property_value_key] = self.id_assigned_property_table[property_value_key] | {w_current_property_id: pvv_value}
                        w_current_property_id += 1
                        w_property_count += 1

                    property_key_table = property_key_table | {property_value_key: w_property_key_num}
                    self.inverted_property_key_table = self.inverted_property_key_table | {w_property_key_num: property_value_key}
                    w_property_key_num += 1
                    w_current_property_id = 0


                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Prop. ID Assigning.. : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                # Give IDs
                temp_bricks_writing: list = []

                for current_brick in range(len(self.bricks_writing)):

                    temp_bricks_writing += [[temp_iebl[current_brick][0], [temp_iebl[current_brick][1][0], []]]]

                    # Give Property IDs, Brick Type IDs
                    for current_property, current_property_value in temp_iebl[current_brick][1][1].items():

                        # Find what the id is
                        for key, value in self.id_assigned_property_table[current_property].items():
                            if value == current_property_value:
                                found_key: int = int(key)

                        # Giving IDs
                        temp_bricks_writing[-1][1][1].append([property_key_table[current_property], found_key])

                    # Giving Brick Type IDs
                    temp_bricks_writing[-1][1][0]['gbn'] = brick_types.index(temp_bricks_writing[-1][1][0]['gbn'])

                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Temp Bricks Writing. : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                # Insert n-word here

                # Bricks Writing is ready to be updated!
                self.bricks_writing = temp_bricks_writing.copy()

                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Bricks Writing...... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()


                # Debug
                if 'bricks' in self.debug_logs:
                    print(f'{FM.debug} Identical Excluded Brick L : {temp_iebl}')
                    print(f'{FM.debug} Property Table............ : {property_table}')
                    print(f'{FM.debug} ID Assigned Property Table : {self.id_assigned_property_table}')
                    print(f'{FM.debug} Brick Properties Writing.. : {self.bricks_writing}')
                    print(f'{FM.debug} String Name to ID Table... : {string_name_to_id_table}')
                    print(f'{FM.debug} Brick Types............... : {brick_types}')
                    print(f'{FM.debug} Property Key Table........ : {property_key_table}')
                    print(f'{FM.debug} Inverted Property Key Tbl. : {self.inverted_property_key_table}')

                # Write how many properties there are
                brv_file.write(unsigned_int(len(property_table), 2))


                # Write each brick type
                for brick_type in brick_types:
                    brv_file.write(unsigned_int(len(brick_type), 1))
                    brv_file.write(small_bin_str(brick_type))

                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Write Brick Types... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                temp_spl: bytes = b''

                # Write properties
                for property_type_key, property_type_value in property_table.items():
                    property_length_list: list[int] = []
                    # Writing keys
                    brv_file.write(unsigned_int(len(property_type_key), 1))
                    brv_file.write(small_bin_str(property_type_key))
                    # Number of values
                    brv_file.write(unsigned_int(len(property_type_value), 2))

                    # Summing values
                    for pt_c_val in property_type_value:  # property_table_current_value

                        temp_pre_spl: bytes = b''

                        if property_type_key not in br_special_property_instance_list:

                            # If it's an integer (uint 16 bit by default)
                            if type(pt_c_val) == int:  # This is because it fucks around when its bool as bool is a subtype of int
                                pt_c_val = float(pt_c_val)

                            # If it's a float (float 32 bit by default)
                            if isinstance(pt_c_val, float):
                                temp_pre_spl += bin_float(pt_c_val, 4)

                            # If it's a bool
                            elif isinstance(pt_c_val, bool):
                                temp_pre_spl += unsigned_int(int(pt_c_val), 1)

                            # If it's a string (converting to utf-8)
                            elif isinstance(pt_c_val, str):
                                temp_pre_spl += signed_int(len(pt_c_val), 1)
                                temp_pre_spl += small_bin_str(pt_c_val)

                            # If it's a list of strings (=> generally list of bricks)
                            elif isinstance(pt_c_val, list) and isinstance(pt_c_val[0], str):
                                temp_pre_spl += unsigned_int(len(pt_c_val), 2) # TODO UNSURE: *2?
                                for pt_c_sub_val in pt_c_val:
                                    temp_pre_spl += unsigned_int(string_name_to_id_table[pt_c_sub_val]+1, 2)


                        else:
                            match br_special_property_instance_list[property_type_key]:
                                case 'INT8':
                                    temp_pre_spl += unsigned_int(pt_c_val, 1)
                                case '6xINT2':
                                    temp_w_spl_connector = pt_c_val[0] + (pt_c_val[1] << 2) + (pt_c_val[2] << 4) + (
                                                pt_c_val[3] << 6) + (pt_c_val[4] << 8) + (pt_c_val[5] << 10)
                                    temp_pre_spl += unsigned_int(temp_w_spl_connector, 2)
                                case '3xINT16':
                                    temp_pre_spl += unsigned_int(pt_c_val[0], 2)
                                    temp_pre_spl += unsigned_int(pt_c_val[1], 2)
                                    temp_pre_spl += unsigned_int(pt_c_val[2], 2)
                                case '3xINT8':
                                    temp_pre_spl += unsigned_int(pt_c_val[0], 1)
                                    temp_pre_spl += unsigned_int(pt_c_val[1], 1)
                                    temp_pre_spl += unsigned_int(pt_c_val[2], 1)
                                case '4xINT8':
                                    temp_pre_spl += unsigned_int(pt_c_val[0], 1)
                                    temp_pre_spl += unsigned_int(pt_c_val[1], 1)
                                    temp_pre_spl += unsigned_int(pt_c_val[2], 1)
                                    temp_pre_spl += unsigned_int(pt_c_val[3], 1)
                                case '3xFLOAT32/None':
                                    temp_pre_spl += bin_float(pt_c_val[0], 4)
                                    temp_pre_spl += bin_float(pt_c_val[1], 4)
                                    temp_pre_spl += bin_float(pt_c_val[2], 4)
                                case 'UTF-16':
                                    raise NotImplementedError('UTF-16 not implemented yet.')

                        property_length_list.append(len(temp_pre_spl))
                        temp_spl += temp_pre_spl


                    brv_file.write(unsigned_int(len(temp_spl), 4))
                    brv_file.write(temp_spl)

                    # Indicating property length if there's more than one property value.
                    if len(property_length_list) > 1:
                        property_length_set: set = set(property_length_list)
                        if len(property_length_set) > 1:
                            brv_file.write(unsigned_int(0, 2))
                        for property_length in property_length_set:
                            brv_file.write(unsigned_int(property_length, 2))

                    temp_spl: bytes = b''  # Reset

                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Write Properties.... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()


                # WRITING BRICKS
                brick_data_writing: bytes = b''


                for current_brick in self.bricks_writing:

                    # Writing Brick Type
                    brv_file.write(unsigned_int(current_brick[1][0]['gbn'], 2))
                    # Getting ready to list properties
                    brick_data_writing += unsigned_int(len(current_brick[1][1]), 1)
                    for current_property in current_brick[1][1]:
                        brick_data_writing += unsigned_int(current_property[0], 2)
                        brick_data_writing += unsigned_int(current_property[1], 2)
                    # Getting ready to write position and rotation
                    brick_data_writing += bin_float(float(current_brick[1][0]['Position'][0]), 4)
                    brick_data_writing += bin_float(float(current_brick[1][0]['Position'][1]), 4)
                    brick_data_writing += bin_float(float(current_brick[1][0]['Position'][2]), 4)
                    # Note sure why its out of order in the brv. Whatever
                    brick_data_writing += bin_float(float(current_brick[1][0]['Rotation'][1]), 4)
                    brick_data_writing += bin_float(float(current_brick[1][0]['Rotation'][2]), 4)
                    brick_data_writing += bin_float(float(current_brick[1][0]['Rotation'][0]), 4)

                    # Writing
                    brv_file.write(unsigned_int(len(brick_data_writing), 4))
                    brv_file.write(brick_data_writing)

                    # Reset
                    brick_data_writing = b''

                if self.seat_brick is not None:
                    brv_file.write(unsigned_int(string_name_to_id_table[self.seat_brick], 2))
                else: brv_file.write(b'\x00\x00')

                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Write Bricks........ : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()


                #  BR-API & USER APPENDIX


                brv_watermark = f'File written with BR-API version {version}. Join our discord to learn more: sZXaESzDd9'
                self.brapi_appendix.append(small_bin_str(brv_watermark))


                for brapi_individual_appendix in self.brapi_appendix:
                    brv_file.write(unsigned_int(len(brapi_individual_appendix), 4))
                    brv_file.write(brapi_individual_appendix)

                if 'time' in self.debug_logs:
                    print(f'{FM.debug} Time: Write Appendix...... : {perf_counter() - previous_time :.6f} seconds')
                    print(f'{FM.debug} Time: Total............... : {perf_counter() - begin_time :.6f} seconds')

    def debug(self, summary_only=False, write=True, print_bricks=False):

        def named_spacer(name: str):
            return '=== ' + name + ' ' + '=' * (95 - len(name))

        spacer = '█' * 100

        str_to_write = ''

        # PRINTING GENERAL INFORMATION
        str_to_write += spacer + '\n'
        str_to_write += named_spacer("PROJECT INFORMATION") + '\n'
        str_to_write += f"PROJECT FOLDER: {self.in_project_folder_directory}\n"
        str_to_write += f"PROJECT NAME: {self.project_display_name!r} [ID: {self.project_name}]\n"
        str_to_write += f"FILE DESCRIPTION: {self.file_description!r}\n"
        str_to_write += f"DEBUG LOGS: {self.debug_logs}\n"
        str_to_write += named_spacer("CREATION INFORMATION") + '\n'
        str_to_write += f"BRICK COUNT: {self.brick_count}\n"
        str_to_write += f"VEHICLE SIZE [X,Y,Z] (CM): {self.vehicle_size}\n"
        str_to_write += f"VEHICLE WEIGHT (KG): {self.vehicle_weight}\n"
        str_to_write += f"VEHICLE WORTH: {self.vehicle_worth}\n"

        # PRINTING BRICKS

        if not summary_only:
            for current_brick in range(len(self.bricks)):

                str_to_write += spacer + '\n'

                # BRICK INFORMATION

                str_to_write += named_spacer('BRICK INFORMATION') + '\n'
                str_to_write += f'BRICK NAME: {self.bricks[current_brick][0]} [ID:{self.bricks_writing[current_brick][0]}]\n'
                str_to_write += (f"BRICK TYPE: {self.bricks[current_brick][1]['gbn']} "
                                 f"[ID: {self.bricks_writing[current_brick][1][0]['gbn']}]\n")
                str_to_write += f"BRICK POS.: {self.bricks[current_brick][1]['Position']}\n"
                str_to_write += f"BRICK ROT.: {self.bricks[current_brick][1]['Rotation']}\n"

                # BRICK PROPERTIES
                str_to_write += named_spacer('BRICK PROPERTIES') + '\n'
                no_properties = True
                for brick_property, brick_property_value in self.bricks_writing[current_brick][1][1]:
                    string_property = self.inverted_property_key_table[brick_property]
                    str_to_write += (f"{string_property}: "
                                     f"{self.id_assigned_property_table[string_property][brick_property_value]}"
                                     f" [ID: {brick_property}, {brick_property_value}]\n")
                    no_properties = False
                if no_properties:
                    str_to_write += "No properties found.\n"

            str_to_write += spacer

        if write:
            with open(os.path.join(self.in_project_folder_directory, "debug_logs.txt"), 'w', encoding='utf-16') as file:
                file.write('DEBUG LOGS\n')
                file.write(str_to_write)

        if print_bricks: print(str_to_write)


# --------------------------------------------------