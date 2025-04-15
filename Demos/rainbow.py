import brci

from os import system

if __name__ == '__main__':

    user_input: int = int(input("How many bricks do you like?\n> "))
    assert user_input > 0, "There must be at least 1 brick."
    assert user_input <= brci.Limits.BR_BRICK_LIMIT, "Too many bricks. You can only create up to 50,000 bricks."

    brci.printr(f"{brci.FM.LIGHT_GREEN}Valid input. Generating {user_input} rainbow brick(s).")

    creation: brci.ModernCreation = brci.Creation14(
        f'demo_rainbow_{user_input}',
        brci.ModernCreation.get_brick_rigs_vehicle_folder(),
        name=f"Demo {user_input} rainbow brick(s)",
        description=f"Demo of {user_input} rainbow brick(s) going in a straight line. Created using brci-{brci.BRCI_VERSION}.",
        author=76561198882119759,  # SteamID 64 of kal
        size=brci.metadata_size([0.3 * user_input, 0.3, 0.1], brci.Units.METER)
    )

    for i in range(user_input):
        creation.add_brick(
            'ScalableBrick',
            f'rainbow.brick{i}',
            brci.pos([i*0.3, 0, 0], brci.Units.METER),
            [0, 0, 0],
            {
                "BrickSize": brci.size([0.3, 0.3, 0.1], brci.Units.METER),
                "BrickColor": brci.from_hsv(int((i/user_input)*360), 100, 100, 100),
                "BrickMaterial": brci.Value.Material.GLOW
            }
        )

    creation.write_creation(exist_ok=True)
    creation.write_metadata(exist_ok=True)
    creation.write_preview(brci.BRCI_THUMBNAIL)

    brci.printr("Rainbow created successfully.", col=brci.FM.LIGHT_GREEN)
    system('pause')
