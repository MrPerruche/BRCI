import os
# from warnings import warn as raise_warning
from copy import deepcopy
from datetime import datetime
from time import perf_counter
from math import ceil
import re

from .BRCI_RF import *

# Note : every time you see unsigned_int() / signed_int() / bin_float(), byte_len * 8 is the number of bits.

# TODO Calculate vehicle_size, vehicle_weight and vehicle_worth
# TODO Implement Brick Loading (IDEA : Exclusively load user appendix)?
# TODO BRCI_Legacy class for legacy?

# ------------------------------------------------------------
# DEFAULT VARIABLES AND SETUP
# ------------------------------------------------------------


# Setup variables
_version: str = "C51"  # String, This is equivalent to 3.__ fyi

# Important variables
_cwd = os.path.dirname(os.path.realpath(__file__))  # File Path

# Colors

from os import system as os_system

os_system('color')

# ------------------------------------------------------------
# DATA WRITING
# ------------------------------------------------------------


custom_common_properties: dict[str: any] = {}


def create_brick(brick: str, position: list[float] = None, rotation: list[float] = None,
                 brick_properties: dict = None) -> dict:
    if brick_properties is None:
        brick_properties = {}
    if position is None:
        position = [0, 0, 0]
    if rotation is None:
        rotation = [0, 0, 0]
    return deepcopy(br_brick_list[brick]) | {'Position': position,
                                             'Rotation': rotation} | custom_common_properties | brick_properties


def cb(b: str, pos: list[float] = None, rot: list[float] = None, p: dict = None) -> dict:
    return create_brick(b, pos, rot, p)


# Brick Rigs Creation Interface Class
class BRCI:

    # Grab values
    def __init__(self,
                 bricks: list[str, dict] | None = None,
                 project_folder_directory: str = '',
                 project_name: str = '',
                 write_blank: bool = False,
                 project_display_name: str = '',
                 file_description: str | None = None,
                 logs: list[str] | None = None,
                 user_appendix: list[bytes] = None,
                 seat_brick: str | None = None,
                 visibility: int = 3,
                 tags: list[str, str, str] | None = None,
                 creation_timestamp: int | None = None,
                 update_timestamp: int | None = None,
                 wip_features: bool = False,
                 custom_description_watermark: str | None = None,
                 backup_directory: str = os.path.join(_cwd, 'Backup')):

        # Set each self.x variable to their __init__ counterparts
        self.project_folder_directory = project_folder_directory  # Path
        self.project_name = project_name  # String
        self.write_blank = write_blank  # Boolean
        self.project_display_name = project_display_name  # String (in-game name (.brm))
        self.file_description = file_description  # String (The description of the file (.brm))
        if bricks is None:  # List (If unspecified, create an empty list)
            bricks = []  # Initialize bricks
        self.bricks = bricks  # List (Of bricks)
        if logs is None:
            logs = []
        if user_appendix is None:
            user_appendix = []
        self.logs = logs  # List of logs to print
        self.user_appendix = user_appendix  # List (User appendix)
        self.seat_brick = seat_brick
        self.visibility = visibility
        if tags is None:
            tags = ['None', 'None', 'None']
        self.tags = tags
        self.creation_timestamp = creation_timestamp
        self.update_timestamp = update_timestamp
        self.wip_features = wip_features
        self.custom_description_watermark = custom_description_watermark
        self.backup_directory = backup_directory

    # Creating more variables
    # In project path
    @property
    def in_project_folder_directory(self) -> str:  # String
        return os.path.join(self.project_folder_directory, self.project_name)

    # Calculate brick count
    @property
    def brick_count(self) -> int:  # 16 Bit integer
        return len(self.bricks)

    # Calculate vehicle size
    @property
    def vehicle_size(self) -> list[float]:  # List of 3 32-bit float
        # TODO : CALCULATE SIZE
        return [100.0, 100.0, 100.0]

    # Calculate vehicle weight
    @property
    def vehicle_weight(self) -> float:  # 32 bit float
        # TODO : CALCULATE WEIGHT
        return 1.0

    # Calculate vehicle worth
    @property
    def vehicle_worth(self) -> float:  # 32 bit float
        # TODO : CALCULATE WORTH
        return 1.0

    # Adding bricks to the brick list
    def add_brick(self, brick_name: str | list[str], brick: dict | list[dict]):
        if isinstance(brick_name, str):
            self.bricks.append([str(brick_name), brick])
        else:
            for add_brick_i in range(len(brick)):
                self.bricks.append([str(brick_name[add_brick_i]), brick[add_brick_i]])

        return self

    def add_new_brick(self, brick_name: str | list[str], brick_type: str | list[str], brick: dict | list[dict] = None,
                      position: list[list[float]] | list[float] = None,
                      rotation: list[list[float]] | list[float] = None):
        if isinstance(brick_type, str):
            self.bricks.append([str(brick_name),
                                create_brick(brick=brick_type, brick_properties=brick, position=position,
                                             rotation=rotation)])
        else:
            for add_new_brick_i in range(len(brick_type)):
                self.bricks.append([str(brick_name[add_new_brick_i]), create_brick(brick=brick_type[add_new_brick_i],
                                                                                   brick_properties=brick[
                                                                                       add_new_brick_i],
                                                                                   position=position[add_new_brick_i],
                                                                                   rotation=rotation[add_new_brick_i])])

        return self

    # Removing bricks from the brick list
    def remove_brick(self, brick_name: str | list[str]):
        for sublist in self.bricks:
            if sublist[0] == brick_name:
                self.bricks.remove(sublist)
                if isinstance(brick_name, str): break

        return self

    # Updating a currently existing brick
    def update_brick(self, brick_name: str | list[str], new_brick: dict | list[dict]):
        for sublist in self.bricks:
            if sublist[0] == brick_name:
                sublist[1] = new_brick
                if isinstance(brick_name, str): break

        return self

    # Retrieving bricks from self.bricks
    def get_brick(self, brick_name: str | list[str]) -> list[dict[str, any]]:
        if isinstance(brick_name, str):
            brick_names: list[dict[str, any]] = [sublist for sublist in self.bricks if sublist[0] == brick_name]
        else:
            brick_names: list[dict[str, any]] = [sublist for sublist in self.bricks if sublist[0] in brick_name]
        return brick_names

    def search_brick(self,
                     names: list[str | int] = None,
                     has_property: list[str] = None,
                     has_value: any = None,
                     has_value_in_range: tuple[int | float] = None,
                     has_item: dict[str, any] = None,
                     has_item_in_range: dict[str, tuple[int | float]] = None,
                     is_brick: list[str] = None,
                     criteria: str = 'and',
                     output_as_dict: bool = False,
                     tolerance_factor: float = 1e-6):

        met_criteria = {key: False for key, value in {
            'names': names,
            'has_property': has_property,
            'has_value': has_value,
            'has_value_in_range': has_value_in_range,
            'has_item': has_item,
            'has_item_in_range': has_item_in_range,
            'is_brick': is_brick
        }.items() if value is not None}

        output_bricks: list[list[dict[str, any]]] = []

        tolerance = 1 + tolerance_factor

        for brick in self.bricks:

            brick_met_criteria = met_criteria.copy()

            # If brick match with a name
            if names is not None and brick[0] in names:
                brick_met_criteria['names'] = True

            # If it is a brick
            if is_brick is not None and brick[1]['gbn'] in is_brick:
                brick_met_criteria['is_brick'] = True

            has_item_mc: int = 0
            has_item_mcir: int = 0

            type_has_value = type(has_value)

            # Checking properties
            for brick_property, brick_value in brick[1].items():

                type_brick_value = type(brick_value)

                # If it has the correct property
                if has_property is not None and brick_property in has_property:
                    brick_met_criteria['has_property'] = True

                # If it has the correct value
                if has_value is not None:
                    if type_has_value in (int, float) and type_brick_value in (int, float):
                        if abs(brick_value - has_value) <= tolerance_factor * has_value:
                            brick_met_criteria['has_value'] = True
                    else:
                        if has_value == brick_value:
                            brick_met_criteria['has_value'] = True

                # If it has a value within a certain range (numbers only)
                if has_value_in_range is not None:
                    if has_value_in_range[0] / tolerance <= brick_value <= has_value_in_range[1] * tolerance:
                        brick_met_criteria['has_value_in_range'] = True

                # If it has the property with the value
                if has_item is not None:

                    if brick_property in has_item.keys():
                        if type(has_item[brick_property]) in (int, float) and type_brick_value in (int, float):
                            has_item_mc += abs(brick_value - has_item[brick_property]) <= tolerance_factor * has_item[
                                brick_property]
                        else:
                            has_item_mc += brick_value == has_item[brick_property]

                # If it has the property with the value being a number in a certain range
                if has_item_in_range is not None:

                    if brick_property in has_item.keys():
                        has_item_mcir += has_item[brick_property][0] / tolerance <= brick_value <= \
                                         has_item[brick_property][0] * tolerance

            # Check if 'has_item' matched
            if has_item is not None and has_item_mc == len(has_item):
                brick_met_criteria['has_item'] = True
            if has_item_in_range is not None and has_item_mcir == len(has_item_in_range):
                brick_met_criteria['has_item_in_range'] = True

            # Outputting our brick if it's correct
            if criteria == 'and' and all(brick_met_criteria.values()):
                output_bricks.append(brick)
            elif criteria == 'or' and any(brick_met_criteria.values()):
                output_bricks.append(brick)
            elif criteria == 'not and' and (not all(brick_met_criteria.values())):
                output_bricks.append(brick)
            elif criteria == 'not or' and (not any(brick_met_criteria.values())):
                output_bricks.append(brick)

        if output_as_dict:
            return {brick[0]: brick[1] for brick in output_bricks}

        return output_bricks

    def get_all_bricks(self, output_as_dict: bool = False):
        if output_as_dict:
            return {brick[0]: brick[1] for brick in self.bricks}

        return self.bricks

    # Deleting all bricks
    def clear_bricks(self):
        self.bricks = []
        return self

    # Add Brick Alias
    def ab(self, n: str | list[str], b: dict | list[dict]):
        return self.add_brick(n, b)

    # Add New Brick Alias
    def anb(self, n: str | list[str], t: str | list[str], b: dict | list[dict] = None, pos: list[float] = None,
            rot: list[float] = None):
        return self.add_new_brick(n, t, b, pos, rot)

    # Remove Brick Alias
    def rb(self, n: str | list[str]):
        return self.remove_brick(n)

    # Update brick Alias
    def ub(self, n: str | list[str], b: dict | list[dict]):
        return self.update_brick(n, b)

    # Get brick Alias
    def gb(self, n: str | list[str]) -> list[dict[str, any]]:
        return self.get_brick(n)

    def ensure_valid_variable_type(self, variable_name: str, occured_when: str) -> None:
        match variable_name:
            case 'write_blank':
                if not isinstance(self.write_blank, bool):
                    FM.warning_with_header("Invalid write_blank type.",
                                           f"Whilst {occured_when}, write_blank was found not to be a boolean, it was instead a {type(self.write_blank).__name__}.\nIt is now set to False.")
                    self.write_blank = False
            case 'bricks_len':
                if len(self.bricks) > 65535:
                    FM.warning_with_header("Too many bricks for BRCI.",
                                           f"Whilst {occured_when}, the length of the list of bricks was found to exceed 65,535.\n"
                                           f"Therefore, the last {len(self.bricks) - 65535 :,} brick(s) were removed. 65,535 bricks left.")
                    self.bricks = self.bricks[:65535]
                if len(self.bricks) > 50000:
                    FM.warning_with_header("Too many bricks for Brick Rigs.",
                                           f"Whilst {occured_when}, the length of the list of bricks was found to exceed 50,000.\n"
                                           f"Although BRCI can generate up to 65,535 bricks; Brick Rigs will only load 50,000 of them.")
            case 'logs':
                logs_whitelist_list: list[str] = ['time', 'bricks']
                invalid_logs_list: list[str] = []
                for log_request_str in self.logs:
                    if not log_request_str in logs_whitelist_list:
                        invalid_logs_list.append(log_request_str)
                if invalid_logs_list:
                    invalid_logs_str: str = ', '.join(invalid_logs_list)
                    logs_whitelist_str: str = ', '.join(logs_whitelist_list)
                    FM.warning_with_header("Unknown log(s) type requested.",
                                           f"Whilst {occured_when}, the following log(s) type requested were found to be invalid: "
                                           f"{invalid_logs_str}.\nYou may instead use the following: {logs_whitelist_str}.")

    # Used to create directory for file generators
    def ensure_project_directory_exists(self) -> None:

        # Verify for invalid inputs
        if not os.path.exists(self.project_folder_directory):
            raise FileNotFoundError(f'Unable to find the project\'s folder ({self.project_folder_directory})')

        os.makedirs(os.path.dirname(os.path.join(self.in_project_folder_directory, self.project_name)), exist_ok=True)

    # Writing preview.png
    def write_preview(self, file_name: str = 'Preview.png') -> None:

        _write_preview_regular_image_path = os.path.join(_cwd, 'Resources', 'BRCI_Preview_Default.png')  # Path

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Verify the image exists.
        if not os.path.exists(_write_preview_regular_image_path):

            FM.warning_with_header("Image not found",
                                   f"Whilst writing preview ({file_name}) we were unable to find BRCI default image. Please retry.")

        # Copy saved image to the project folders.
        else:
            if os.path.exists(os.path.join(self.in_project_folder_directory, file_name)):
                FM.warning_with_header("Preview.png already created",
                                       f"Whilst writing preview ({file_name}), we noticed it was already added.\nThe old Preview.png was therefore replaced.")
                os.remove(os.path.join(self.in_project_folder_directory, file_name))

            copy_file(os.path.join(_write_preview_regular_image_path),
                      os.path.join(self.in_project_folder_directory, file_name))

    # Writing metadata.brm file
    def write_metadata(self, file_name: str = 'MetaData.brm') -> None:

        # Create folder if missing
        self.ensure_project_directory_exists()
        self.ensure_valid_variable_type('write_blank', f'writing {file_name}')
        self.ensure_valid_variable_type('bricks_len', f'writing {file_name}')

        # Write blank file for metadata (if desired)
        if self.write_blank:

            with open(os.path.join(self.in_project_folder_directory, file_name), "x"):
                pass

        # Otherwise write working metadata file
        else:
            with open(os.path.join(self.in_project_folder_directory, file_name), 'wb') as metadata_file:

                # Writes Carriage Return char
                metadata_file.write(unsigned_int(14, 1))

                # Write all necessary information for the file name
                metadata_file.write(signed_int(-len(self.project_display_name), 2))
                metadata_file.write(bin_str(self.project_display_name)[2:])

                # Write all necessary information for the file description
                watermarked_file_description = f"Created using BRCI (Version {_version}).\r\n" \
                                               f"Join our discord for more information : sZXaESzDd9"  # String
                if self.custom_description_watermark is not None:
                    watermarked_file_description += f'\r\n\r\n{self.custom_description_watermark}'
                if self.file_description is not None:
                    watermarked_file_description += f'\r\n\r\nDescription:\r\n{self.file_description}'
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
                metadata_file.write(unsigned_int(16, 1))
                metadata_file.write(b'\x00' * 8)

                # Write time (100 nanosecond Gregorian bigint value)
                # Creation Time
                if self.creation_timestamp is None:
                    metadata_file.write(
                        unsigned_int(int((datetime.now() - datetime(1, 1, 1)).total_seconds() * 1e7), 8))
                else:
                    metadata_file.write(unsigned_int(self.creation_timestamp, 8))
                # Update Time
                if self.update_timestamp is None:
                    metadata_file.write(
                        unsigned_int(int((datetime.now() - datetime(1, 1, 1)).total_seconds() * 1e7), 8))
                else:
                    metadata_file.write(unsigned_int(self.update_timestamp, 8))

                # Write visibility mode
                metadata_file.write(unsigned_int(self.visibility, 1))

                for tag in self.tags:
                    metadata_file.write(unsigned_int(len(tag), 1))
                    metadata_file.write(small_bin_str(tag))

    # Writing the project folder to brick rigs # only works on windows
    def write_to_br(self) -> None:
        import shutil
        # Define the relative path to append to the user's home directory
        relative_path = "AppData/Local/BrickRigs/SavedRemastered/Vehicles"
        # Get the user's home directory and expand the path
        user_home = os.path.expanduser("~")
        # Construct the full path by joining the user's home directory with the relative path
        full_path = os.path.join(user_home, relative_path, self.project_name)

        try:
            # Remove the destination folder if it exists
            if os.path.exists(full_path):
                shutil.rmtree(full_path)
            # Copy the folder
            shutil.copytree(self.in_project_folder_directory, full_path)
        except OSError as e:
            # Failed for some reason -_-
            FM.warning_with_header(f"Failed to clone folder: {e}",
                                   f"This may be because .write_to_br() function was made for Windows.")

    def backup(self, folder_name: str | None = None) -> None:
        import shutil
        use_folder_name = str(int((datetime.now() - datetime(1, 1, 1)).total_seconds() * 1e7)) if folder_name is None else folder_name
        # Define the relative path to append to the user's home directory
        relative_path = os.path.join(os.getenv('LOCALAPPDATA'), 'BrickRigs', 'SavedRemastered', 'Vehicles')
        # Chars known to be safe
        pattern = re.compile(r'^[a-zA-Z0-9_\-]+$')

        try:
            if not os.path.exists(self.backup_directory):

                # This file is part of BRCI but not installed by default. Warning would cause confusing; so we don't.
                if self.backup_directory != os.path.join(_cwd, 'Backup') :
                    FM.warning_with_header("Cannot find specified backup folder",
                                           "Unable to find specified backup folder. The folder has been made for you.")

                os.makedirs(self.backup_directory)

            if os.path.exists(relative_path) and pattern.match(use_folder_name):
                shutil.copytree(relative_path, os.path.join(self.backup_directory, use_folder_name))
            else:
                FM.warning_with_header("Cannot create backup",
                                       "Either your vehicles folder doesn't exist/isn't found (are you on Linux or MacOS?) or the folder name has invalid characters such as emoji.") 
        except OSError as e:
            # Failed for some reason -_-
            FM.warning_with_header(f"Failed to clone folder: {type(e).__name__}: {e}",
                                   f"This may be because .backup() function was made for Windows.")

    # Sharing some variables from writing vehicle.brv to the rest of the class
    bricks_writing = []
    inverted_property_key_table = {}
    id_assigned_property_table = {}
    brci_appendix: list = []

    # Writing Vehicle.brv
    def write_brv(self, file_name: str = 'Vehicle.brv') -> None:

        self.ensure_project_directory_exists()

        # Verify self.write_blank is valid.
        self.ensure_valid_variable_type('write_blank', f'writing {file_name}')

        # Write blank file for vehicle (if desired)
        if self.write_blank:
            blank_brv = open(os.path.join(self.in_project_folder_directory, file_name), "x")
            blank_brv.close()

        # Otherwise write working vehicle file
        else:

            # Show generation time if debug logs
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
                            property_value_mp.prefix = property_key_mp
                            prop_mp_temp = property_value_mp.properties()
                            # If it's incorrect
                            if isinstance(prop_mp_temp, str) and prop_mp_temp == 'invalid_source_bricks':
                                FM.warning_with_header("Invalid type for brick list.",
                                                       f"Whilst writing vehicle ({file_name}),"
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
            self.ensure_valid_variable_type('bricks_len', f'writing {file_name}')
            self.ensure_valid_variable_type('logs', f'writing f{file_name}')

            with (open(os.path.join(self.in_project_folder_directory, file_name), 'wb') as brv_file):

                # --------------------------------------------------
                # SETUP
                # --------------------------------------------------

                self.bricks_writing = deepcopy(self.bricks)

                # Writes Carriage Return char
                brv_file.write(unsigned_int(14, 1))
                # Write brick count
                brv_file.write(unsigned_int(len(self.bricks_writing), 2))

                # --------------------------------------------------
                # MISSING PROPERTIES
                # --------------------------------------------------

                # Add all missing properties, notably inputs.
                add_missing_properties(self.bricks_writing, 'bricks' in self.logs)

                if 'time' in self.logs:
                    print(f'{FM.debug} Time: Missing Properties.. : {perf_counter() - previous_time :.6f} seconds')

                # --------------------------------------------------
                # BRICK TYPES
                # --------------------------------------------------

                # Get the different bricks present in the project
                brick_types = brv_brick_types(self.bricks_writing, 'bricks' in self.logs)  # List

                if 'time' in self.logs:
                    print(f'{FM.debug} Time: Brick Types......... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()
                if 'bricks' in self.logs:
                    print(f'{FM.debug} Brick Types............... : {brick_types}')

                # --------------------------------------------------
                # TEMP IEBL, PROPERTY TABLE, STRING NAME TO ID
                # --------------------------------------------------

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

                if 'time' in self.logs:
                    print(f'{FM.debug} Time: ID Assigning........ : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()
                if 'bricks' in self.logs:
                    print(f'{FM.debug} Identical Excluded Brick L : {temp_iebl}')
                    print(f'{FM.debug} Property Table............ : {property_table}')
                    print(f'{FM.debug} String Name to ID Table... : {string_name_to_id_table}')

                # --------------------------------------------------
                # ID ASSIGNED PROP. TABLE, PROPERTY KEY TABLE, INVERTED PROPERTY KEY TABLE,
                # --------------------------------------------------

                # Setup property ids
                w_current_property_id: int = 0  # 32 bit
                w_property_count: int = 0  # 32 bit
                property_key_table: dict = {}
                w_property_key_num: int = 0

                # Give IDs to all values in var 'id_assigned_property_table'
                for property_value_key, property_value_value in property_table.items():

                    self.id_assigned_property_table = self.id_assigned_property_table | {property_value_key: {}}

                    for pvv_value in property_value_value:
                        self.id_assigned_property_table[property_value_key] = self.id_assigned_property_table[
                                                                                  property_value_key] | {
                                                                                  w_current_property_id: pvv_value}
                        w_current_property_id += 1
                        w_property_count += 1

                    property_key_table = property_key_table | {property_value_key: w_property_key_num}
                    self.inverted_property_key_table = self.inverted_property_key_table | {
                        w_property_key_num: property_value_key}
                    w_property_key_num += 1
                    w_current_property_id = 0

                if 'time' in self.logs:
                    print(f'{FM.debug} Time: Prop. ID Assigning.. : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()
                if 'bricks' in self.logs:
                    print(f'{FM.debug} ID Assigned Property Table : {self.id_assigned_property_table}')
                    print(f'{FM.debug} Property Key Table........ : {property_key_table}')
                    print(f'{FM.debug} Inverted Property Key Tbl. : {self.inverted_property_key_table}')

                # --------------------------------------------------
                # BRICKS WRITING
                # --------------------------------------------------

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

                if 'time' in self.logs:
                    print(f'{FM.debug} Time: Temp Bricks Writing. : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                # Insert n-word here

                # Bricks Writing is ready to be updated!
                self.bricks_writing = deepcopy(temp_bricks_writing)

                if 'time' in self.logs:
                    print(f'{FM.debug} Time: Bricks Writing...... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                # Debug
                if 'bricks' in self.logs:
                    print(f'{FM.debug} Brick Properties Writing.. : {self.bricks_writing}')

                # Write how many properties there are
                brv_file.write(unsigned_int(len(property_table), 2))

                # Write each brick type
                for brick_type in brick_types:
                    brv_file.write(unsigned_int(len(brick_type), 1))
                    brv_file.write(small_bin_str(brick_type))

                if 'time' in self.logs:
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

                    for pt_c_val in property_type_value:

                        temp_pre_spl: bytes = b''

                        if property_type_key in br_property_types.keys():

                            match br_property_types[property_type_key]:

                                case 'bin':

                                    temp_pre_spl += pt_c_val

                                case 'bool':

                                    temp_pre_spl += unsigned_int(int(pt_c_val), 1)

                                case 'brick_id':

                                    temp_pre_spl += unsigned_int(string_name_to_id_table[pt_c_val], 2)

                                case 'custom':

                                    # If it is custom then we expect a function
                                    temp_pre_spl += pt_c_val()

                                case 'float':

                                    temp_pre_spl += bin_float(pt_c_val, 4)

                                case 'list[brick_id]':

                                    temp_pre_spl += unsigned_int(len(pt_c_val), 2)

                                    for pt_c_sub_val in pt_c_val:
                                        temp_pre_spl += unsigned_int(string_name_to_id_table[pt_c_sub_val] + 1, 2)

                                case 'list[3*float]':

                                    temp_pre_spl += bin_float(pt_c_val[0], 4)
                                    temp_pre_spl += bin_float(pt_c_val[1], 4)
                                    temp_pre_spl += bin_float(pt_c_val[2], 4)

                                case 'list[3*uint8]':

                                    if isinstance(pt_c_val, int):
                                        use_pt_c_val = [(pt_c_val >> i) & 0xFF for i in range(16, -1, -8)]
                                    else:
                                        use_pt_c_val = pt_c_val.copy()

                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[0]), 1)
                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[1]), 1)
                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[2]), 1)

                                case 'list[3*uint16]':

                                    if isinstance(pt_c_val, int):
                                        use_pt_c_val = [(pt_c_val >> i) & 0xFFFF for i in range(32, -1, -16)]
                                    else:
                                        use_pt_c_val = pt_c_val.copy()

                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[0]), 2)
                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[1]), 2)
                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[2]), 2)

                                case 'list[4*uint8]':

                                    if isinstance(pt_c_val, int):
                                        use_pt_c_val = [(pt_c_val >> i) & 0xFF for i in range(24, -1, -8)]
                                    else:
                                        use_pt_c_val = pt_c_val.copy()

                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[0]), 1)
                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[1]), 1)
                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[2]), 1)
                                    temp_pre_spl += unsigned_int(round(use_pt_c_val[3]), 1)

                                case 'list[6*uint2]':

                                    if isinstance(pt_c_val, int):
                                        use_pt_c_val = [(pt_c_val >> i) & 0x3 for i in range(12, -1, -2)]
                                    else:
                                        use_pt_c_val = pt_c_val.copy()

                                    temp_w_spl_connector = (
                                                use_pt_c_val[0] + (use_pt_c_val[1] << 2) + (use_pt_c_val[2] << 4) +
                                                (use_pt_c_val[3] << 6) + (use_pt_c_val[4] << 8) + (
                                                            use_pt_c_val[5] << 10))

                                    temp_pre_spl += unsigned_int(temp_w_spl_connector, 2)

                                case 'str8':

                                    temp_pre_spl += signed_int(len(pt_c_val), 1)
                                    temp_pre_spl += small_bin_str(pt_c_val)

                                case 'str16':

                                    temp_pre_spl += signed_int(-len(pt_c_val), 2)
                                    temp_pre_spl += pt_c_val.encode('utf-16')[2:]

                                case 'strany':

                                    try:
                                        # Assume it can be a long str8
                                        temp_pre_spl += signed_int(len(pt_c_val), 2)
                                        temp_pre_spl += small_bin_str(pt_c_val)

                                    except UnicodeEncodeError:
                                        # Assume since it's not a long str8 it must be a long str16
                                        temp_pre_spl += signed_int(-len(pt_c_val), 2)
                                        temp_pre_spl += pt_c_val.encode('utf-16')[2:]

                                case 'uint8':

                                    temp_pre_spl += unsigned_int(int(pt_c_val), 1)


                        elif isinstance(pt_c_val, list) and isinstance(pt_c_val[0],
                                                                       str):  # OR if it doesn't end with .InputAxis

                            temp_pre_spl += unsigned_int(len(pt_c_val), 2)

                            for pt_c_sub_val in pt_c_val:
                                temp_pre_spl += unsigned_int(string_name_to_id_table[pt_c_sub_val] + 1, 2)


                        elif isinstance(pt_c_val, str):  # OR if it ends with .InputAxis

                            temp_pre_spl += unsigned_int(len(pt_c_val), 1)

                            temp_pre_spl += small_bin_str(pt_c_val)

                        elif isinstance(pt_c_val, float) or isinstance(pt_c_val, int):
                            temp_pre_spl += bin_float(pt_c_val, 4)

                        else:

                            raise ValueError(f'Unsupported property type: {pt_c_val}.\n'
                                             f'Consider using bin to implement this property, as explained in Doc/DOCUMENTATION.md')

                        property_length_list.append(len(temp_pre_spl))
                        temp_spl += temp_pre_spl

                    brv_file.write(unsigned_int(len(temp_spl), 4))
                    brv_file.write(temp_spl)

                    # Indicating property length if there's more than one property value.
                    if len(property_length_list) > 1:
                        property_length_set: set = set(property_length_list)
                        if len(property_length_set) > 1:
                            brv_file.write(unsigned_int(0, 2))
                            for property_length in property_length_list:
                                brv_file.write(unsigned_int(property_length, 2))
                        else:
                            brv_file.write(unsigned_int(property_length_list[0], 2))

                    temp_spl: bytes = b''  # Reset

                if 'time' in self.logs:
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
                else:
                    brv_file.write(b'\x00\x00')

                if 'time' in self.logs:
                    print(f'{FM.debug} Time: Write Bricks........ : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                #  BRCI & USER APPENDIX

                # BRCI Appendix

                # Contents
                brv_watermark = f'File written with BRCI. Join our discord to learn more: sZXaESzDd9. Version:'
                self.brci_appendix.append(small_bin_str(brv_watermark))
                self.brci_appendix.append(small_bin_str(_version))

                brick_names_bina: bytes = b''

                # Brick Names
                for brick in self.bricks:
                    name: str = str(brick[0])  # brick[0] = brick name
                    brick_names_bina += unsigned_int(len(name), 2)
                    brick_names_bina += bin_str(name)[2:]

                self.brci_appendix.append(brick_names_bina)

                # Length
                brv_file.write(unsigned_int(len(self.brci_appendix), 4))

                # Writing data
                for brci_individual_appendix in self.brci_appendix:
                    brv_file.write(unsigned_int(len(brci_individual_appendix), 4))
                    brv_file.write(brci_individual_appendix)

                # USER Appendix
                if not isinstance(self.user_appendix, list): user_a_use = [self.user_appendix]
                else: user_a_use = self.user_appendix
                
                # Length
                brv_file.write(unsigned_int(len(self.user_appendix), 4))

                # Data
                for user_individual_appendix in user_a_use:
                    #uia_use: bytearray = bytearray(user_individual_appendix)
                    brv_file.write(unsigned_int(len(user_individual_appendix), 4))
                    brv_file.write(user_individual_appendix)

                if 'time' in self.logs:
                    print(f'{FM.debug} Time: Write Appendix...... : {perf_counter() - previous_time :.6f} seconds')
                    print(f'{FM.debug} Time: Total............... : {perf_counter() - begin_time :.6f} seconds')

    def debug(self, summary_only=False, write=True, print_bricks=False) -> None:

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
        str_to_write += f"DEBUG LOGS: {self.logs}\n"
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
                    true_property_value = self.id_assigned_property_table[string_property][brick_property_value]
                    if callable(true_property_value) and true_property_value.__name__ == '<lambda>':
                        str_to_write += (f"{string_property}: "
                                         f"{true_property_value()}"
                                         f" [ID: {brick_property}, {brick_property_value}]\n")
                    else:
                        str_to_write += (f"{string_property}: "
                                         f"{true_property_value}"
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

    def load_brv(self, load_vehicle: bool = True, load_brci_data: bool = True, load_appendix: bool = True,
                 file_name: str = 'Vehicle.brv'):

        previous_time = perf_counter()
        begin_time = perf_counter()

        self.ensure_project_directory_exists()
        self.ensure_valid_variable_type('logs', f'loading {file_name}')

        with (open(os.path.join(self.in_project_folder_directory, file_name), 'rb') as brv_file_reader):

            brv_file = bytearray(brv_file_reader.read())

        # Removing the first useless byte
        del brv_file[:1]

        # Get brick count and stuff
        brick_count = r_unsigned_int(b_pop(brv_file, 2))

        brick_type_count = r_unsigned_int(b_pop(brv_file, 2))

        property_type_count = r_unsigned_int(b_pop(brv_file, 2))

        if 'time' in self.logs:
            print(f"{FM.debug} Time: Setup & loading..... : {perf_counter() - previous_time :.6f} seconds")
            previous_time = perf_counter()

        # ---------------------------------------------------
        # PART I : BRICK TYPES
        # ---------------------------------------------------

        # Get brick types
        brick_types: list[str] = []

        for _ in range(brick_type_count):
            brick_type_len = r_unsigned_int(b_pop(brv_file, 1))

            brick_types += [r_small_bin_str(b_pop(brv_file, brick_type_len))]

        if 'time' in self.logs:
            print(f"{FM.debug} Time: Brick Types......... : {perf_counter() - previous_time :.6f} seconds")
            # LENGTH OF TEXT : Time: ....................
            previous_time = perf_counter()

        if 'bricks' in self.logs:
            print(f"{FM.debug} Brick Types............... : {brick_types}")
            # LENGTH OF TEXT : ..........................

        # ---------------------------------------------------
        # PART II : PRE-LOAD BRICK PROPERTIES
        # ---------------------------------------------------

        # Get property types
        # bin_properties: dict[str, list[int, int, bytes, list[int]]] = {}

        p_id_to_p: dict[int: str] = {}
        p_val_id_to_val: dict[int: dict[int: any]] = {}

        for r_property in range(property_type_count):

            # Getting property name len
            property_type_icon_len = r_unsigned_int(b_pop(brv_file, 1))

            # Getting property & its data
            property_name = r_small_bin_str(b_pop(brv_file, property_type_icon_len))
            property_count = r_unsigned_int(b_pop(brv_file, 2))
            property_byte_len = r_unsigned_int(b_pop(brv_file, 4))

            # Assigning property name id and more
            p_id_to_p |= {r_property: property_name}
            p_val_id_to_val |= {property_name: {}}

            property_content: bytes = b_pop(brv_file, property_byte_len)

            # Getting all properties length
            if property_count > 1:
                properties_len: list[int] | int = r_unsigned_int(b_pop(brv_file, 2))
                if properties_len == 0:

                    properties_len: list[int] = []

                    for _ in range(property_count):
                        properties_len.append(r_unsigned_int(b_pop(brv_file, 2)))
            else:
                properties_len: list[int] = [property_byte_len]

            # Get all different properties in a list
            if load_vehicle:

                properties_byte: list[bytes] = []  # REMINDER AS I GET CONFUSED: THIS IS ALL VALUES FOR THE PROPERTY

                # If length is variable
                if isinstance(properties_len, list):

                    for i in properties_len:
                        properties_byte.append(b_pop(property_content, i))

                # If length is constant
                else:

                    for _ in range(len(property_content) // properties_len):
                        properties_byte.append(b_pop(property_content, properties_len))

                # Convert bytes data

                if property_name in br_property_types:

                    for i, property_bin in enumerate(properties_byte):

                        # Binary was already extracted in properties_byte
                        match br_property_types[property_name]:

                            case 'bin' | 'custom':

                                p_val_id_to_val[property_name] |= {i: property_bin}

                            case 'bool':

                                p_val_id_to_val[property_name] |= {i: bool(r_unsigned_int(property_bin))}

                            case 'brick_id':

                                # SIEVE THOUGH ALL PROPERTIES AGAIN TO CONVERT IDS ONCE BRICKS ARE LOADED
                                p_val_id_to_val[property_name] |= {i: r_unsigned_int(property_bin)}

                            case 'float':

                                p_val_id_to_val[property_name] |= {i: r_bin_float(property_bin)}

                            case 'list[brick_id]':

                                brick_id_list: list[int] = []

                                for _ in range(r_unsigned_int(b_pop(property_bin, 1))):
                                    brick_id_list.append(r_unsigned_int(b_pop(property_bin, 2)))

                                p_val_id_to_val[property_name] |= {i: brick_id_list.copy()}

                            case 'list[3*float]':

                                p_val_id_to_val[property_name] |= {i:
                                                                       [r_bin_float(property_bin[j:j + 4]) for j in
                                                                        range(0, len(property_bin), 4)]
                                                                   }

                            case 'list[3*uint8]':

                                p_val_id_to_val[property_name] |= {i:
                                                                       [property_bin[j] for j in
                                                                        range(len(property_bin))]
                                                                   }

                            case 'list[3*uint16]':

                                p_val_id_to_val[property_name] |= {i:
                                                                       [r_unsigned_int(property_bin[j:j + 2]) for j in
                                                                        range(0, len(property_bin), 2)]
                                                                   }

                            case 'list[4*uint8]':

                                p_val_id_to_val[property_name] |= {i:
                                                                       [property_bin[j] for j in
                                                                        range(len(property_bin))]
                                                                   # For some reason this outputs little endian?
                                                                   }

                            case 'list[6*uint2]':

                                p_val_id_to_val[property_name] |= {
                                    i: [(r_unsigned_int(property_bin) >> j) & 0x3 for j in range(12, -1, -2)]}

                            case 'str8':

                                p_val_id_to_val[property_name] |= {i: r_small_bin_str(property_bin[1:])}

                            case 'str16':

                                p_val_id_to_val[property_name] |= {i: r_small_bin_str(b'\xFF\xFE' + property_bin[2:])}

                            case 'strany':

                                if r_signed_int(property_bin[:2]) < 0:
                                    # It's UTF-16
                                    # It looks like some 2IQ move is going on here but no we're getting rid of
                                    # the property length
                                    p_val_id_to_val[property_name] |= {i: r_bin_str(b'\xFF\xFE') + property_bin[2:]}
                                else:
                                    # It's UTF-8
                                    p_val_id_to_val[property_name] |= {i: r_small_bin_str(property_bin)}

                            case 'uint8':

                                p_val_id_to_val[property_name] |= {i: r_unsigned_int(property_bin)}

                elif property_name.endswith('.InputAxis'):  # Presuming it's an input channel's type

                    for i, property_bin in enumerate(properties_byte):
                        p_val_id_to_val[property_name] |= {i: r_small_bin_str(property_bin[1:])}

                elif property_name.endswith('.Value'):  # Presuming it's an input channel's value

                    for i, property_bin in enumerate(properties_byte):
                        p_val_id_to_val[property_name] |= {i: r_bin_float(property_bin)}

                elif property_name.endswith('.SourceBricks'):  # Presuming it's a list of brick inputs

                    for i, property_bin in enumerate(properties_byte):
                        # SIEVE THROUGH ALL PROPERTIES AGAIN TO CONVERT THEM
                        p_val_id_to_val[property_name] |= {i: property_bin}

                else:

                    FM.warning_with_header("Unknown property type",
                                           f"The vehicle file you're attempting to load contains the property {property_name}.\n"
                                           f"This property is unknown, and was ignored by BRCI. It's contents weren't loaded.")

        # Debug Logs
        if 'time' in self.logs:
            print(f"{FM.debug} Time: Properties (1)...... : {perf_counter() - previous_time :.6f} seconds")
            # LENGTH OF TEXT : Time: ....................
            previous_time = perf_counter()

        if 'bricks' in self.logs:
            print(f'{FM.debug} Property ID to Property... : {p_id_to_p}')
            print(f"{FM.debug} P. Value ID to Value (1).. : {p_val_id_to_val}")

        # Reading all bricks
        for r_brick in range(brick_count):

            # Retrieving the brick type
            brick_type: str = brick_types[r_unsigned_int(b_pop(brv_file, 2))]

            # Reading properties
            # Length of the property list in bytes (unneeded so just get rids of it)
            b_pop(brv_file, 4)
            # Reading the number of properties
            properties_num: int = r_unsigned_int(b_pop(brv_file, 1))
            # Saving each property
            properties_id: list[tuple[int, int]] = []
            for _ in range(properties_num):
                property_type_id: int = r_unsigned_int(b_pop(brv_file, 2))
                property_value_id: int = r_unsigned_int(b_pop(brv_file, 2))
                properties_id += [(property_type_id, property_value_id)]

            # Reading position and rotation
            brick_px: float = r_bin_float(b_pop(brv_file, 4))
            brick_py: float = r_bin_float(b_pop(brv_file, 4))
            brick_pz: float = r_bin_float(b_pop(brv_file, 4))
            brick_ry: float = r_bin_float(b_pop(brv_file, 4))
            brick_rz: float = r_bin_float(b_pop(brv_file, 4))
            brick_rx: float = r_bin_float(b_pop(brv_file, 4))

            # Converting properties to dictionary
            if load_vehicle:
                properties: dict = {
                    'gbn': brick_type,
                    'Position': [brick_px, brick_py, brick_pz],
                    'Rotation': [brick_rx, brick_ry, brick_rz]
                }
                for property_id in properties_id:
                    property_type = p_id_to_p[property_id[0]]
                    property_value = p_val_id_to_val[property_type][property_id[1]]
                    properties[property_type] = property_value

                self.bricks.append([r_brick, properties])

        # Seats
        seat = r_unsigned_int(b_pop(brv_file, 2))
        if load_vehicle:
            if seat == 0:
                self.seat_brick = None
            else:
                self.seat_brick = seat

        # Debug Logs
        if 'time' in self.logs:
            print(f"{FM.debug} Time: Bricks (1).......... : {perf_counter() - previous_time :.6f} seconds")
            # LENGTH OF TEXT : Time: ....................
            previous_time = perf_counter()

        if 'bricks' in self.logs:
            print(f'{FM.debug} Bricks (1)................ : {self.bricks}')

        # Is used later to convert. Don't worry about it not being filled ;)
        brick_id_to_name_table: dict[int: str] = {}

        # Loading additional data (names)
        if load_brci_data and brv_file != '':

            brci_data_elements = r_unsigned_int(b_pop(brv_file, 4))

            # Get rid of the description
            b_pop(brv_file, r_unsigned_int(b_pop(brv_file, 4)))
            brci_data_elements -= 1

            file_version: str = r_small_bin_str(b_pop(brv_file, r_unsigned_int(b_pop(brv_file, 4))))
            brci_data_elements -= 1

            f_maj_vers, f_min_vers = file_version[0], file_version[1:]
            f_maj_vers = ord(f_maj_vers) - ord('A') + 1
            c_maj_vers, c_min_vers = _version[0], _version[1:]
            c_maj_vers = ord(c_maj_vers) - ord('A') + 1

            # Too old version of BRCI warning
            if c_maj_vers < f_maj_vers or (c_maj_vers == f_maj_vers and c_min_vers < f_min_vers):
                FM.warning_with_header("BRCI is outdated.",
                                       "It appears the file you're attempting to load was made in a later version\n"
                                       f"than this version of BRCI (BRCI: {_version}. File: {file_version}).\n"
                                       f"Expect unexpected results.")

            if int(f_min_vers) <= 44 and f_maj_vers <= c_maj_vers:

                raise NotImplementedError(f"BRCI {_version} no longer support BRCI data of files generated before C45.")

            elif int(f_min_vers) <= int(c_min_vers) and f_maj_vers <= c_maj_vers:

                # BRCI C45 BRCI DATA VERSION:

                b_pop(brv_file, 4)

                for i in range(brick_count):

                    brick_name = r_bin_str(b'\xFF\xFE' + b_pop(brv_file, r_unsigned_int(b_pop(brv_file, 2)) * 2))
                    if load_vehicle:
                        self.bricks[i][0] = brick_name
                    brick_id_to_name_table |= {i: brick_name}

                brci_data_elements -= 1

            # Clear any remaining data
            while brci_data_elements > 0:
                b_pop(brv_file, r_unsigned_int(b_pop(brv_file, 4)))
                brci_data_elements -= 1

        if 'time' in self.logs:
            print(f"{FM.debug} Time: Load BRCI Data...... : {perf_counter() - previous_time :.6f} seconds")
            # LENGTH OF TEXT : Time: ....................
            previous_time = perf_counter()

        if 'bricks' in self.logs:
            print(f'{FM.debug} BRCI Data / Id to Name.... : {brick_id_to_name_table}')

        if load_appendix and brv_file != '':

            # Getting rid of brci data if required
            if not load_brci_data:
                brci_data_elements: int = r_unsigned_int(b_pop(brv_file, 4))

                while brci_data_elements > 0:
                    b_pop(brv_file, r_unsigned_int(b_pop(brv_file, 4)))
                    brci_data_elements -= 1

            self.user_appendix = []

            user_appendix_len: int = r_unsigned_int(b_pop(brv_file, 4))

            for _ in range(user_appendix_len):
                self.user_appendix.append(b_pop(brv_file, r_unsigned_int(b_pop(brv_file, 4))))

        if 'time' in self.logs:
            print(f"{FM.debug} Time: Load User Appendix.. : {perf_counter() - previous_time :.6f} seconds")
            # LENGTH OF TEXT : Time: ....................
            previous_time = perf_counter()

        if 'bricks' in self.logs:
            print(f'{FM.debug} User Appendix............. : {self.user_appendix}')

        # Fixing brick ids now that we have all bricks & their name (I want to sleep)
        if load_vehicle:

            for brick in self.bricks:

                brick[1] = create_brick(brick[1]['gbn']) | brick[1]  # We don't do the |= thing since order matters

                # brick[1] = brick properties

                properties_to_update: dict[str, any] = {}
                properties_to_create: dict[str, any] = {}
                properties_to_delete: set[str] = set()

                for b_prop_k, b_prop_v in brick[1].items():

                    if b_prop_k in br_property_types:
                        if br_property_types[b_prop_k] == 'brick_id' and len(brick_id_to_name_table) > 0:

                            properties_to_update |= {b_prop_k: brick_id_to_name_table[b_prop_v]}

                        elif br_property_types[b_prop_k] == 'list[brick_id]' and len(brick_id_to_name_table) > 0:

                            brick_str_id_list: list[str] = []

                            for i in range(len(b_prop_v)):
                                brick_str_id_list.append(brick_id_to_name_table[b_prop_v[i]])

                            properties_to_update |= {b_prop_k: brick_str_id_list}  # Todo

                    elif (b_prop_k.endswith('.InputAxis')
                          or b_prop_k.endswith('.SourceBricks')
                          or b_prop_k.endswith('.Value')):

                        pre_dot_name, post_dot_name = b_prop_k.split('.')[:2]

                        if pre_dot_name not in properties_to_create.keys():
                            properties_to_create[pre_dot_name] = BrickInput('None', None)

                        if post_dot_name == 'InputAxis':

                            properties_to_create[pre_dot_name].brick_input_type = b_prop_v

                        elif post_dot_name == 'Value':

                            properties_to_create[pre_dot_name].brick_input = b_prop_v

                        else:  # Assuming its .SourceBricks

                            brick_input_list: list[int | str] = [r_unsigned_int(b_prop_v[i:i + 2]) for i in
                                                                 range(0, len(b_prop_v), 2)]

                            if len(brick_id_to_name_table) > 0:
                                brick_input_list = [brick_id_to_name_table[j - 1] for j in brick_input_list]

                            properties_to_create[pre_dot_name].brick_input = brick_input_list

                        properties_to_delete.add(b_prop_k)

                brick[1].update(properties_to_update)

                for property_to_delete in properties_to_delete:
                    del brick[1][property_to_delete]

                brick[1] |= properties_to_create

        if 'time' in self.logs:
            print(f"{FM.debug} Time: Bricks (2).......... : {perf_counter() - previous_time :.6f} seconds")
            print(f"{FM.debug} Time: Total............... : {perf_counter() - begin_time :.6f} seconds")
            # LENGTH OF TEXT : Time: ....................

        if 'bricks' in self.logs:
            print(f'{FM.debug} Bricks (2)................ : {self.bricks}')

        return self

    # Load metadata
    def load_metadata(self, load_display_name: bool = True, load_description: bool = True, load_creation_time: bool = True,
                      load_update_time: bool = False, load_visibility: bool = True, load_tags: bool = True,
                      file_name: str = "MetaData.brm"):

        if not self.wip_features:
            FM.warning_with_header('WIP Features not enabled!', 'You are attempting to use .load_metadata().\n'
                                                                'This feature is still WIP. Set .wip_features to True\n'
                                                                'In order to access WIP features.')

            with open(os.path.join(self.in_project_folder_directory, file_name), 'wb') as metadata_file_reader:

                metadata_file = bytearray(metadata_file_reader.read())

            del metadata_file[:1]

            name_len: int = r_signed_int(b_pop(metadata_file, 2))
            if name_len >= 0:
                # UTF-8
                name: str = r_small_bin_str(b_pop(metadata_file, name_len))
            else:
                # UTF-16
                name: str = r_bin_str(b_pop(metadata_file, -name_len*2))
            if load_display_name:
                self.project_display_name = name

            description_len: int = r_signed_int(b_pop(metadata_file, 2))
            if description_len >= 0:
                # UTF-8
                description: str = r_small_bin_str(b_pop(metadata_file, description_len))
            else:
                # UTF-16
                description: str = r_bin_str(b_pop(metadata_file, -description_len*2))
            if load_description:
                self.file_description = description

            # Get rid of brick count, vehicle size, weight & worth (we don't need that)
            b_pop(metadata_file, 22)

            # Get rid of the author
            author_len = r_unsigned_int(b_pop(metadata_file, 1))
            b_pop(metadata_file, ceil(author_len / 2))

            # Creation time
            creation_timestamp = r_unsigned_int(b_pop(metadata_file, 8))
            last_update_timestamp = r_unsigned_int(b_pop(metadata_file, 8))
            if load_creation_time:
                self.creation_timestamp = creation_timestamp
            if load_update_time:
                self.update_timestamp = last_update_timestamp

            visibility: int = r_unsigned_int(b_pop(metadata_file, 1))

            if load_visibility:
                self.visibility = visibility

            tags: list[str] = []
            for _ in range(3):
                if metadata_file: # If there's still something to take
                    tag_len = r_unsigned_int(b_pop(metadata_file, 1))
                    tag = r_small_bin_str(b_pop(metadata_file, tag_len))
                    tags.append(tag)
            if load_tags:
                self.tags = tags.copy()


    @staticmethod
    def get_missing_gbn_keys(print_missing: bool = False) -> list:
        missing_values: list = []
        for key, value in br_brick_list.items():
            if 'gbn' not in value:
                missing_values.append(key)
        if print_missing:
            print(missing_values)
        return missing_values


    @staticmethod
    def get_missing_properties(print_missing: bool = False):
        missing_values: set = set()
        for bricks in br_brick_list.values():
            for brick_property, brick_p_item in bricks.items():
                if (brick_property not in br_property_types.keys()
                        and not isinstance(brick_p_item, BrickInput)
                        and not brick_property in ['Position', 'Rotation', 'gbn']):
                    missing_values.update({str(brick_property)})
        if print_missing:
            print(missing_values)
        return missing_values


# --------------------------------------------------