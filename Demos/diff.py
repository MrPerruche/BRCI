from typing import Final

import brci

import os
from os import system  # for 'pause'


# This program will show diff for the first brick. It's useful to test properties.


REMOVED_STYLE: Final[str] = brci.FM.CLEAR_ALL + brci.FM.LIGHT_RED + brci.FM.BOLD + brci.FM.STRIKETHROUGH
ADDED_STYLE: Final[str] = brci.FM.CLEAR_ALL + brci.FM.LIGHT_GREEN + brci.FM.BOLD

def halt():
    system('pause')


def print_sep():
    brci.printr("------ ---- -- - -  -    -      -", col=brci.FM.LIGHT_BLACK)


def render_diff(old, new) -> str:
    if old == new:
        return brci.FM.CLEAR_ALL + repr(new)
    return f'{REMOVED_STYLE}{old!r}{brci.FM.CLEAR_ALL} -> {ADDED_STYLE}{new!r}{brci.FM.CLEAR_ALL}'


def diff_col(old, new) -> str:
    return "" if old == new else brci.FM.YELLOW


if __name__ == '__main__':

    brci.printr(f'Diff for the first brick of a creation', col=brci.FM.LIGHT_BLUE)
    print_sep()

    # Get creation name
    creation_name: str = brci.inputr("Creation folder name\n> ")
    while not os.path.exists(os.path.join(brci.ModernCreation.get_brick_rigs_vehicle_folder(), creation_name)) or \
            not os.path.exists(os.path.join(brci.ModernCreation.get_brick_rigs_vehicle_folder(), creation_name, 'Vehicle.brv')):
        brci.printr(f"Creation {creation_name} not found", col=brci.FM.LIGHT_RED)
        creation_name: str = brci.inputr("Creation folder name\n> ")

    # Setup creation
    creation: brci.ModernCreation = brci.Creation14(
        project_name=creation_name,
        project_dir=brci.ModernCreation.get_brick_rigs_vehicle_folder(),
    )
    # First read (ensure there is something)
    creation.read_creation()
    while len(creation.bricks) == 0:
        print_sep()
        brci.printr("Creation is empty.", col=brci.FM.LIGHT_RED)
        halt()
        creation.read_creation()
    brci.printr("Creation found.", col=brci.FM.LIGHT_GREEN)
    halt()

    while True:
        print_sep()

        # Get the old first brick.
        old_brick: brci.Brick = creation.bricks[0]

        # Load updated creation
        creation.bricks = []
        creation.read_creation()

        # Get the new first brick. Ensure there is one
        if len(creation.bricks) == 0:
            brci.printr("Creation is empty.", col=brci.FM.LIGHT_RED)
            halt()
            continue
        new_brick: brci.Brick = creation.bricks[0]

        # Brick type
        brci.printr(f'Brick type: {render_diff(old_brick.get_type(), new_brick.get_type())}',
                    col=diff_col(old_brick.get_type(), new_brick.get_type()))

        # Position and rotation
        brci.printr(f'Position: {render_diff(old_brick.position, new_brick.position)}',
                    col=diff_col(old_brick.position, new_brick.position))  # Will only color "Position: "
        brci.printr(f'Rotation: {render_diff(old_brick.rotation, new_brick.rotation)}',
                    col=diff_col(old_brick.rotation, new_brick.rotation))

        # Properties
        for prop in (old_brick.properties | new_brick.properties).keys():
            if prop not in new_brick.properties:  # Removed property
                brci.printr(f'  _ {prop}: {REMOVED_STYLE}{old_brick.properties[prop]!r}', col=brci.FM.LIGHT_RED)
            elif prop not in old_brick.properties:  # Added property
                brci.printr(f'  _ {prop}: {ADDED_STYLE}{new_brick.properties[prop]!r}', col=brci.FM.LIGHT_GREEN)
            else:  # Unchanged or modified
                brci.printr(f'  _ {prop}: {render_diff(old_brick.properties[prop], new_brick.properties[prop])}',
                            col=diff_col(old_brick.properties[prop], new_brick.properties[prop]))


        halt()