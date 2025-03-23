import brci
from os import system  # For pause


# Function to get pitch based on index in the loop
def get_pitch(note: int, num_notes: int):
    assert num_notes != 1, "Division by zero."
    return 2 - (1.5 * note / (num_notes - 1))  # Intentionally in reverse order to be in the right order in-game.


if __name__ == '__main__':

    # Get user input
    notes: int = int(input("How many notes would you like?\n> "))
    assert notes > 2, "There must be at least 2 notes."  # Cannot allow 1. It would cause zero division errors.
    assert notes * 2 + 1 <= brci.Limits.BR_BRICK_LIMIT, "Too many notes. You can only create up to 24,999 notes."  # Brick Rigs only loads 50,000 bricks.
    brci.printr(f"Valid input. Generating {notes} notes...", col=brci.FM.LIGHT_GREEN)

    # Initialize a BRCI creation instance
    creation: brci.Creation = brci.Creation14(
        f'demo_piano_{notes}',
        brci.BRICK_RIGS_FOLDER[0],
        name=f"Demo piano with {notes} notes",
        description=f"Demo of a piano created using brci-{brci.BRCI_VERSION}.",
        author=76561199095329086,  # SteamID 64 of Raized
        size=brci.metadata_size([max(0.6, notes / 10), 0.4, 0.436], brci.Units.METER)  # 0.336: Exact size of a horn
    )

    # Add the base block to connect all switches and sirens
    creation.add_brick('ScalableBrick', 'base',
                       position=brci.pos([max(30, notes * 5), 20, 0], brci.Units.CENTIMETER),
                       properties={
                           'BrickColor': brci.from_rgb(0, 0, 0, 0),
                           'BrickMaterial': 'Oak',
                           'BrickSize': brci.size([max(60, notes * 10), 40, 10], brci.Units.CENTIMETER),
                       })

    for i in range(notes):

        # Create the switch for user input
        creation.add_brick('Switch_1sx1sx1s', f'note{i}.input',
                           position=brci.pos([i * 10 + 5, 5, 5], brci.Units.CENTIMETER),
                           properties={
                               'BrickColor': brci.from_rgb(0, 0, 0, 0),
                               'BrickMaterial': 'Oak',
                               'OutputChannel.MinIn': 0.0,
                               'OutputChannel.MaxIn': 1.0,
                               'OutputChannel.MinOut': 0.0,
                               'OutputChannel.MaxOut': 1.0,
                               'SwitchName': f"Note {notes - i} (Pitch: {round(get_pitch(i, notes)*100, 1)}%)",
                           })

        creation.add_brick('DoubleSiren_1x2x1s', f'note{i}.siren',
                           position=brci.pos([30, 25, 5], brci.Units.CENTIMETER),
                           rotation=[0, 0, 90],
                           properties={
                               'BrickColor': brci.from_rgb(0, 0, 0, 0),
                               'BrickMaterial': 'Oak',
                               'InputChannel.InputAxis': 'Custom',
                               'InputChannel.SourceBricks': [f'note{i}.input'],
                               'HornPitch': get_pitch(i, notes)
                           })


    creation.write_creation(exist_ok=True),
    creation.write_metadata(exist_ok=True),
    creation.write_preview(brci.BRCI_THUMBNAIL)

    brci.printr("Piano created successfully.", col=brci.FM.LIGHT_GREEN)
    system('pause')