from .creation15 import Creation15
from .modern_creation import ModernCreation

from ..brick import *
from ..constants import *
from ..utils import *
from ..write_utils import *

from typing import Optional, Final, Any, Self


class Subassembly15(Creation15):
    def __init__(self, directory_to_read: str, vehicles_directory: str, origin_point: Optional[list[float]] = [0, 0, 0], no_vehicle_read: Optional[bool] = False) -> None:
        # TODO argument documentation and names could use some fixing
        """A special wrapper around brci.Creation15 for the specific purpose of managing groups of bricks easier.

        WILL AUTOMATICALLY ATTEMPT TO READ THE SPECIFIED VEHICLE.

        Args:
            directory_to_read (str): The directory containing the vehicle (.brv) to read.
            vehicles_directory (str): The directory containing directory_to_read.
            origin_point (list[float], optional): The center of the subassembly. Good if you need to specify, say, the corner of a block as the origin. Defaults to [0, 0, 0].
            no_vehicle_read (bool, optional): Whether to skip reading the vehicle, if you for some reason need this functionality. Defaults to False.
        """

        super().__init__(directory_to_read, vehicles_directory,
                         'Subassembly', 'You should not see this. Please do not write subassemblies.', bytearray(),
                         None, Visibility.PUBLIC,
                         None, None,
                         None, 0.0, 0.0)

        self.origin_point: list[float] = origin_point
        self.no_vehicle_read: bool = no_vehicle_read

        if not self.no_vehicle_read:
            self.read_creation()


    def serialize_creation(self):
        raise SerializationError("Subassemblies do not permit being written back to the filesystem. If you need this functionality, make a new Creation15 object and transfer the bricks " \
        "to it.")


    def write_creation(self, file_name = 'Vehicle.brv', exist_ok = True):
        raise SerializationError("Subassemblies do not permit being written back to the filesystem. If you need this functionality, make a new Creation15 object and transfer the bricks " \
        "to it.")


    def __call__(self, target_creation: ModernCreation, brick_name_prefix: str, position: Optional[list[float]] = None, rotation: Optional[list[float]] = None,
                 naming_scheme: Optional[str] = "<i>_<name>_<brick>"):
        # Subassemblies are callable like a function.
        """Merge a subassembly into a target creation at the specified coordinates.

        Args:
            target_creation (ModernCreation): The creation to add the bricks to.
            brick_name_prefix (str): The prefix to apply to the names of the subassembly's bricks. If the prefix is '1', the subassembly's directory_to_read is '2',
                and the brci name of the current brick being added is '3', then the final name ends up being "1_2_3" by default.
            position (list[float], optional): The position to insert the bricks at. Revolves around the origin point. Defaults to None.
            rotation (list[float], optional): The rotation to insert the bricks at. Defaults to None.
            naming_scheme (str, optional): See brick_name_prefix. \<i\> = prefix, \<name\> = directory_to_read, \<brick\> = brci name of the current brick.
                Defaults to "\<i\>\_\<name\>\_\<brick\>".
        """

        self.place(target_creation, brick_name_prefix, position, rotation, naming_scheme)


    def place(self, target_creation: ModernCreation, brick_name_prefix: str, position: Optional[list[float]] = None, rotation: Optional[list[float]] = None,
              naming_scheme: Optional[str] = "<i>_<name>_<brick>"):
        """Merge a subassembly into a target creation at the specified coordinates.

        Args:
            target_creation (ModernCreation): The creation to add the bricks to.
            brick_name_prefix (str): The prefix to apply to the names of the subassembly's bricks. If the prefix is '1', the subassembly's directory_to_read is '2',
                and the brci name of the current brick being added is '3', then the final name ends up being "1_2_3" by default.
            position (list[float], optional): The position to insert the bricks at. Revolves around the origin point. Defaults to None.
            rotation (list[float], optional): The rotation to insert the bricks at. Defaults to None.
            naming_scheme (str, optional): See brick_name_prefix. \<i\> = prefix, \<name\> = directory_to_read, \<brick\> = brci name of the current brick.
                Defaults to "\<i\>\_\<name\>\_\<brick\>".
        """

        # This is the method that __call__ will call.

        brick_name_prefix = brick_name_prefix or "Subassembly"
        naming_scheme = naming_scheme or "<i>_<name>_<brick>"

        if "<i>" not in naming_scheme:
            naming_scheme = f"<i>{naming_scheme}"

        if position == None:
            position = [0, 0, 0] # preserve origin point!

        if rotation == None:
            rotation = [0, 0, 0]

        replicated_bricks = deepcopy(self.bricks)

        for brick in replicated_bricks:
            if isinstance(brick, Brick15):
                brick.name = naming_scheme.replace("<i>", self.name).replace("<name>", self.directory_to_read).replace("<brick>", str(brick.name))
                brick.position = [
                    (brick.position[0] - self.origin_point[0]) + position[0],
                    (brick.position[1] - self.origin_point[1]) + position[1],
                    (brick.position[2] - self.origin_point[2]) + position[2]
                ]
                # TODO rotation since i dont think brci 4 has the old rotation functions yet so multibrick rotation and around an origin stuff is off the table for now


        target_creation.bricks.extend(replicated_bricks)
