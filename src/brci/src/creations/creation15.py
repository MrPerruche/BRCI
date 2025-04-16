from collections.abc import Callable
from typing import Optional, Final, Any, Self
from shutil import copytree as _shutil_copytree
from time import perf_counter
import os

from .modern_creation import ModernCreation
from ..brick import *
from ..constants import *
from ..utils import *
from ..write_utils import *
from ..value_enums import Value15

# TODO: Get rid of this terrible function system
from ..write_utils import _get_property_data, _convert_brick_types, _convert_brick_names_to_id, _get_prop_bin



class Creation15(ModernCreation):

    def __init__(self, project_name: str, project_dir: str,
                 name: str = '', description: str = '', appendix: bytes | bytearray = bytearray(),
                 tags: list[str] | None = None, visibility: Visibility = Visibility.PUBLIC,
                 creation_time: Optional[int] = None, update_time: Optional[int] = None,
                 size: Optional[list[float]] = None, weight: float = 0.0, price: float = 0.0,
                 author: int = 0) -> None:
        """
        Project creation class for version 15 (Brick Rigs 1.8.0).

        Arguments:
            project_name (str): Name of the folder in which all Brick Rigs file (Vehicle.brv etc.) will be stored.
            project_dir (str): Directory where these folders will go in.
            name (str, optional): Name of the project displayed in-game.
            description (str, optional): Description of the project displayed in-game.
            appendix (bytes | bytearray, optional): Hidden binary data in files.
            tags (list[str] | None, optional): List of tags for the project.
            visibility (Visibility, optional): Visibility of the project, set to Visibility.PUBLIC, Visibility.FRIENDS, Visibility.PRIVATE or Visibility.HIDDEN.
            creation_time (Optional[int], optional): Time the project was created (in 100s of nanoseconds since 0001-01-01 00:00:00 UTC).
            update_time (Optional[int], optional): Time the project was last updated (in 100s of nanoseconds since 0001-01-01 00:00:00 UTC).
            size (Optional[list[float]], optional): Size of the project (in meters).
            weight (float, optional): Weight of the project (in kilograms).
            price (float, optional): Price of the project (in dollars).
            author (int, optional): Author of the creation.
        """

        self.bricks: list[Brick15] = []  # Correct type hinting

        super().__init__(15, Value15, project_name, project_dir,
                         name, description, appendix,
                         tags, visibility,
                         None,
                         creation_time, update_time,
                         size, weight, price, author)


    @staticmethod
    def get_property_types_dict() -> dict[str, Type[BinaryType]]:
        return property_types15


    @staticmethod
    def get_bricks_dict() -> dict[str, Brick]:
        return bricks15


    @staticmethod
    def Brick(brick_type: str, name: str | int, position: Optional[list[float]] = None,
              rotation: Optional[list[float]] = None, properties: Optional[dict[str, Any]] = None):
        return Brick15(brick_type, name, position, rotation, properties)


    def deserialize_creation(self, file: bytearray) -> Self:
        # -------------------- PART 1: HEADER INFO -------------------- #

        file_version: int = get_unsigned_int(extract_bytes(file, 1))

        # Version check:
        if file_version != self.get_file_version():
            raise NotImplementedError(f"Version {file_version} mismatch, {self.get_file_version()})")

        # The next two bytes are the number of bricks in the creation. (uint16)
        num_bricks: int = get_unsigned_int(extract_bytes(file, 2))

        # The next two bytes are the number of unique brick types.
        num_brick_types: int = get_unsigned_int(extract_bytes(file, 2))
        # And the next two, the number of unique properties:
        num_properties: int = get_unsigned_int(extract_bytes(file, 2))

        # logwrap("debug", "Creation14::read_creation || Buffer -> Header info completed...")

        # -------------------- PART 2: BRICK TYPES  -------------------- #

        brick_types: set = set()
        for _ in range(num_brick_types):
            brick_types.add(extract_str8(file))
        brick_types_tuple = tuple(brick_types)

        # logwrap("debug", "Creation14::read_creation || Buffer -> Brick types completed...")

        # -------------------- PART 3: PROPERTIES -------------------- #

        properties: dict[str, list[Any]] = {}

        for _ in range(num_properties):

            prop_name: str = extract_str8(file)
            num_values: int = get_unsigned_int(extract_bytes(file, 2))
            bin_len: int = get_unsigned_int(extract_bytes(file, 4))
            bin_properties: bytearray = extract_bytes(file, bin_len)

            bin_values: list[bytearray] = []
            values: list[any] = []

            first_len: int = 0  # TODO: Is this fine? (here to get rid of potentially unused variable warning)

            if num_values > 1:
                first_len = get_unsigned_int(extract_bytes(file, 2))

                if first_len == 0:
                    for _ in range(num_values):
                        bin_values.append(extract_bytes(bin_properties, get_unsigned_int(extract_bytes(file, 2))))

                else:  # if num_values > 1:
                    bin_values = [extract_bytes(bin_properties, first_len) for _ in range(num_values - 1)]

            else:
                bin_values = [bin_properties]

            for bin_value in bin_values:
                # Deserialize values
                values.append(self.get_property_types_dict()[prop_name].deserialize(bin_value, settings['numpy']))

            properties.update({prop_name: values})

        # logwrap("debug", "Creation14::read_creation || Buffer -> Properties completed...")

        # -------------------- PART 4: BRICKS -------------------- #

        # DEBUGPRINT print(f'{FM.MAGENTA}FIRST: {file}{FM.CLEAR_ALL}')

        # Setting up stuff
        property_type_names: tuple[str, ...] = tuple(properties.keys())

        for brick in range(num_bricks):

            # Get type of the brick
            brick_type: str = brick_types_tuple[get_unsigned_int(extract_bytes(file, 2))]

            # Property list len in bytes (useless here)
            extract_bytes(file, 4)

            # PROPERTIES
            # Get number of properties
            num_brick_properties: int = get_unsigned_int(extract_bytes(file, 1))

            # DEBUGPRINT print(f'{FM.LIGHT_GREEN}{FM.BOLD}FOR {brick}: {file}{FM.CLEAR_ALL}')
            # DEBUGPRINT print(f'{FM.LIGHT_BLUE}{properties=}{FM.CLEAR_ALL}')

            # Get properties
            brick_properties: dict = {}
            for _ in range(num_brick_properties):
                # Retrieve IDs
                prop_id: int = get_unsigned_int(extract_bytes(file, 2))
                val_id: int = get_unsigned_int(extract_bytes(file, 2))

                # DEBUGPRINT print(f'{FM.LIGHT_GREEN}{prop_id=}, {val_id=}\n{brick_properties=}\n{property_type_names[prop_id]=}\n{properties[property_type_names[prop_id]]=}{FM.CLEAR_ALL}')

                # Obtain value from IDs and append them to already collected properties
                brick_properties.update({
                    property_type_names[prop_id]: properties[property_type_names[prop_id]][val_id]
                })

                # DEBUGPRINT print(f'{FM.LIGHT_GREEN}NEW {brick_properties=}\n===================================================={FM.CLEAR_ALL}')

            # Get position and rotation
            position: list[float] = [get_sp_float(extract_bytes(file, 4)) for _ in range(3)]
            rotation: list[float] = [get_sp_float(extract_bytes(file, 4)) for _ in range(3)]
            rotation = [rotation[2], rotation[0], rotation[1]]  # (Y Z X) -> (X Y Z)

            # Done. Add the brick to the list
            self.add_brick(brick_type=brick_type,
                           name=brick,
                           position=position,
                           rotation=rotation,
                           properties=brick_properties
                           )

        # -------------------- PART 5: FOOTER --------------------

        seat_id: int = get_unsigned_int(extract_bytes(file, 2))

        # if seat_id != 0:
        #     self.seat = seat_id - 1

        self.appendix = file

        # DEBUGPRINT end_t = perf_counter()
        # DEBUGPRINT print(f"time (reading excluded): {end_t - start_t:,.6f}")

        return self


    def deserialize_metadata(self, file: bytearray, load_last_update: bool = False) -> Self:


        # if not is_valid_folder_name(os.path.join(self.project_dir, self.project_name, file_name), os.name == 'nt'):
        #     raise OSError(f"Invalid path {os.path.join(self.project_dir, self.project_name, file_name)}")

        # #################### WRITING ####################

        # logwrap("info", f"Creation14::write_metadata || Instantiating buffer, writing basic details...")

        # Initializing stuff
        # with open(os.path.join(self.project_dir, self.project_name, file_name), 'rb') as f:
        #     buffer: bytearray = bytearray(f.read())
        # Version number
        version: int = get_unsigned_int(extract_bytes(file, 1))
        if version != self.get_file_version():
            raise NotImplementedError(f"Invalid version number {version}, expected {self.get_file_version()}")

        # File name
        self.name = extract_str16(file)

        # Description:
        self.description = extract_str16(file)

        # Brick Count ignored
        extract_bytes(file, 2)

        # logwrap("info", "Creation14::write_metadata || Basic details -> Buffer completed...")

        # Vehicle Size
        self.size = [None, None, None]
        for i in range(3):
            self.size[i] = get_sp_float(extract_bytes(file, 4))

        # Weight
        self.weight = get_sp_float(extract_bytes(file, 4))

        # Price
        self.price = get_sp_float(extract_bytes(file, 4))

        # Remove the 0x1D (29). Steam
        extract_bytes(file, 1)

        # Get author
        author_coded: list[int] = [x for x in extract_bytes(file, get_unsigned_int(extract_bytes(file, 1)))]
        author_str: list[str] = [f'{x:02x}' for x in author_coded]
        self.author = int(''.join(author_str))

        # No clue
        extract_bytes(file, 4)

        # Write time (100 nanosecond Gregorian bigint value)
        self.creation_time = get_unsigned_int(extract_bytes(file, 8))

        # logwrap("info", "Creation14::write_metadata || Extended details -> Buffer completed...")

        # Update time
        if load_last_update:
            self.update_time = get_unsigned_int(extract_bytes(file, 8))
        else:
            extract_bytes(file, 8)

        """

        # Visibility mode
        print(buffer)
        self.visibility = Visibility(get_unsigned_int(extract_bytes(buffer, 1)))

        # Tags
        self.tags = []
        lim = 3
        while buffer and lim > 0:
            self.tags.append(get_utf8(buffer))
            lim -= 1
        """

        # logwrap("info", "Creation14::write_metadata || All details -> Buffer completed. Writing file...")

        # logwrap("info", "Creation14::write_metadata || Metadata writing successful.")

        return self

    def serialize_creation(self) -> bytearray:

        # #################### TREATMENT ####################

        # Bricks
        num_bricks: int = len(self.bricks)
        # Brick Types
        brick_types: set[str] = {brick.get_type() for brick in self.bricks}
        brick_types_to_index: dict[str, int] = {brick_type: i for i, brick_type in enumerate(brick_types)}
        num_brick_types: int = len(brick_types)

        # printr(f'{FM.YELLOW}BRICK TYPES [{num_brick_types}]: {brick_types_to_index}')  # DEBUGPRINT DBU

        # Properties
        prop_id_t__val_id_t_val: dict[int, dict[int, Any]]
        prop_id_t__val_t_val_id: dict[int, dict[int, int]]
        # prop_id_t_type, prop_type_t_id, prop_id_t__val_id_t_val, prop_id_t__val_t_val_id = _get_property_data(
        #     self.bricks, bricks14)

        # I pray id(value) works
        # it works

        # Init variables
        prop_id_t_type: dict[int, str] = {}  # Property and their id
        prop_type_t_id: dict[str, int] = {}  # Property id and their property
        prop_id_t__val_id_t_val: dict[int, dict[int, Any]] = {}  # Property id and their values: id -> value

        default_properties: dict[str, Any] = self.get_bricks_dict()

        for brick in self.bricks:
            brick_type_defaults: dict[str, Any] = default_properties[brick.get_type()]

            for property_, value in brick.properties.items():
                if brick_type_defaults[property_] == value or value is None:
                    continue

                # Get or assign property ID
                property_id = prop_type_t_id.get(property_)
                if property_id is None:
                    property_id = len(prop_type_t_id)
                    prop_id_t_type[property_id] = property_
                    prop_type_t_id[property_] = property_id
                    prop_id_t__val_id_t_val[property_id] = {}

                # Instead of using id(), iterate to check for an existing equal value.
                value_id = None
                for existing_id, stored_value in prop_id_t__val_id_t_val[property_id].items():
                    if stored_value == value:
                        value_id = existing_id
                        break

                # If no equal value is found, store it with a new ID.
                if value_id is None:
                    value_id = len(prop_id_t__val_id_t_val[property_id])
                    prop_id_t__val_id_t_val[property_id][value_id] = value

                # printr(f'{FM.LIGHT_GREEN}BRICK [{brick.name}] PROPERTY [{property_}] VALUE_ID [{value_id}] VALUE [{value}]')  # DEBUGPRINT

        # logwrap("debug", "Creation14::write_creation || Calculated header properties, instantiating buffer...")

        # #################### GENERATION ####################

        buffer: bytearray = bytearray()

        # -------------------- PART 1: HEADER --------------------

        # Version
        buffer.extend(unsigned_int(self.get_file_version(), 1))

        # Bricks, unique bricks, unique properties
        buffer.extend(unsigned_int(num_bricks, 2))
        buffer.extend(unsigned_int(num_brick_types, 2))
        buffer.extend(unsigned_int(len(prop_id_t_type), 2))  # number of properties, could be another var

        # Brick types
        buffer.extend(_convert_brick_types(brick_types))

        # logwrap("debug", "Creation14::write_creation || Header properties -> Buffer completed...")

        # -------------------- PART 2: BRICK TYPES --------------------

        # for brick_t in brick_types:
        #     buffer.extend(unsigned_int(len(brick_t), 1))  # Str len
        #     buffer.extend(utf8(brick_t))  # Str

        # -------------------- PART 3: PROPERTIES --------------------

        # Get all brick IDs
        brick_id_table: dict[str | int, int] = _convert_brick_names_to_id(self.bricks)

        """printr(f'{FM.LIGHT_CYAN}'
               f'{prop_id_t_type=}\n'
               f'{prop_type_t_id=}\n'
               f'{prop_id_t__val_id_t_val=}\n'
               f'{brick_id_table=}\n'
               # f'{prop_id_t__val_t_val_id=}\n'
               f'================================================')  # DEBUGPRINT DBU """

        for type_, id_ in prop_type_t_id.items():
            # Property name
            buffer.extend(unsigned_int(len(type_), 1))
            buffer.extend(utf8(type_))

            # Number of properties
            buffer.extend(unsigned_int(len(set(prop_id_t__val_id_t_val[id_])), 2))

            # Convert all properties of this type to binary
            properties_binary, properties_binary_addon = _get_prop_bin(self.get_property_types_dict()[type_], id_,
                                                                       prop_id_t__val_id_t_val, brick_id_table)

            # DEBUGPRINT printr(f'{FM.CYAN}{properties_binary=}\n{properties_binary_addon=}\n=============')

            # Write all that
            buffer.extend(unsigned_int(len(properties_binary), 4))
            buffer.extend(properties_binary)
            buffer.extend(properties_binary_addon)

            # printr(f'{FM.LIGHT_BLUE}BIN_PROPERTY: TYPE [{type_}] ID [{id_}] LEN [{len(properties_binary)}] BIN_PROPERTY [{properties_binary}] BIN_ADDON [{properties_binary_addon}]')  # DEBUGPRINT

        # logwrap("debug", "Creation14::write_creation || Brick Properties -> Buffer completed...")

        # -------------------- PART 4: BRICKS --------------------

        for brick in self.bricks:

            property_bin: bytearray = bytearray()

            # Write brick id
            buffer.extend(unsigned_int(brick_types_to_index[brick.get_type()], 2))

            # Write number of non-default properties
            brick_properties: dict[str, Any] = {prop: val for prop, val in brick.properties.items()
                                                if bricks15[brick.get_type()][prop] != val}

            # Write property ids
            property_bin.extend(unsigned_int(len(brick_properties), 1))  # Number of non-default properties
            for prop, val in brick_properties.items():
                prop_id: int = prop_type_t_id[prop]
                property_bin.extend(unsigned_int(prop_id, 2))  # id of the property type
                value_id = None
                for existing_id, stored_value in prop_id_t__val_id_t_val[prop_id].items():
                    if stored_value == val:
                        property_bin.extend(unsigned_int(existing_id, 2))
                        break
                # property_bin.extend(unsigned_int(prop_id_t__val_t_val_id[prop_id][id(val)], 2))  # id of the value

            # Position (X, Y, Z)
            property_bin.extend(sp_float(brick.position[0]))
            property_bin.extend(sp_float(brick.position[1]))
            property_bin.extend(sp_float(brick.position[2]))
            # Rotation (Y, Z, X / Pitch, Yaw, Roll)
            property_bin.extend(sp_float(brick.rotation[1]))
            property_bin.extend(sp_float(brick.rotation[2]))
            property_bin.extend(sp_float(brick.rotation[0]))

            # Write changes
            buffer.extend(unsigned_int(len(property_bin), 4))
            buffer.extend(property_bin)

        # logwrap("debug", "Creation14::write_creation || Bricks -> Buffer completed...")

        # -------------------- PART 5: FOOTER AND APPENDIX --------------------

        # Footer
        # if self.seat is None:
        #     buffer.extend(b'\x00\x00')
        # else:
        #     buffer.extend(unsigned_int(brick_id_table[self.seat], 2))

        buffer.extend(self.appendix)

        # logwrap("debug", "Creation14::write_creation || Footer/Appendix -> Buffer completed. Writing file...")

        return buffer

    def serialize_metadata(self) -> bytearray:

        # #################### WRITING ####################

        # logwrap("info", f"Creation14::write_metadata || Instantiating buffer, writing basic details...")

        # Initializing stuff
        buffer: bytearray = bytearray()

        # Version number
        buffer.extend(unsigned_int(self.get_file_version(), 1))

        # File name
        buffer.extend(signed_int(-len(self.name), 2))
        buffer.extend(utf16(self.name)[2:])

        # Description:
        buffer.extend(signed_int(-len(self.description), 2))
        buffer.extend(utf16(self.description)[2:])

        # Brick Count
        buffer.extend(unsigned_int(len(self.bricks), 2))

        # logwrap("info", "Creation14::write_metadata || Basic details -> Buffer completed...")

        # Vehicle Size
        for axis_size in self.size:
            buffer.extend(sp_float(axis_size))

        # Weight
        buffer.extend(sp_float(self.weight))

        # Price
        buffer.extend(sp_float(self.price))

        # Add the 0x1D (29). Steam
        buffer.extend(b'\x1D')

        # Get author
        # Pretty long. basically 1234567 -> ['7', '65', '43', '21']
        author_str: list[str] = [str(self.author)[i:i + 2][::-1] for i in range(0, len(str(self.author)), 2)][::-1]
        author_coded: int = 0
        for i, seg in enumerate(author_str):
            if len(seg) == 2:
                author_coded += ((int(seg[1]) << 4) + int(seg[0])) << (i * 8)
            else:
                author_coded += int(seg[0]) << (i * 8 + 4)
        if len(str(self.author)) % 2 == 1:
            author_coded //= 0x10
        buffer.extend(unsigned_int(author_coded, len(author_str)))

        # No clue.
        buffer.extend(b'\x00\x00\x00\x00')

        # Write time (100 nanosecond Gregorian bigint value)
        # Creation time
        if self.creation_time is None:
            buffer.extend(unsigned_int(get_time_100ns(), 8))
        else:
            buffer.extend(unsigned_int(self.creation_time, 8))

        # logwrap("info", "Creation14::write_metadata || Extended details -> Buffer completed...")

        # Update time
        if self.update_time is None:
            buffer.extend(unsigned_int(get_time_100ns(), 8))
        else:
            buffer.extend(unsigned_int(self.update_time, 8))

        # Visibility mode
        buffer.extend(unsigned_int(self.visibility.value, 1))

        # Tags
        buffer.extend(unsigned_int(len(self.tags), 2))
        for tag in self.tags:
            buffer.extend(unsigned_int(len(tag), 1))
            buffer.extend(utf8(tag))

        # logwrap("info", "Creation14::write_metadata || All details -> Buffer completed. Writing file...")

        # logwrap("info", "Creation14::write_metadata || Metadata writing successful.")

        return buffer