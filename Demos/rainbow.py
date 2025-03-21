import sys, os

# written by kal
# TODO this could be cleaner

dirpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dirpath, '..', 'src'))

import brci # raises a warning in some IDEs (vscode)
print(brci.__file__) # verify correct path

if __name__ == '__main__':

    user_input = None

    while user_input == None:
        try:
            user_input = input("How many bricks do you want to generate? Enter a whole number/integer, at least 1...\n> ")
            if user_input == "": continue
            
            brick_count = int(user_input)
            if brick_count < 1:
                raise ValueError
            
            break
        
        except:
            brci.printr(f"{brci.FM.LIGHT_RED}Invalid input. Please try again.")
            continue

    brci.printr(f"{brci.FM.LIGHT_GREEN}Got it! Generating {brick_count} rainbow brick{'s' if brick_count > 1 else ''}...")

    data = brci.Creation14("rainbow", brci.PROJECT_FOLDER, f"Rainbow Brick{'s' if brick_count > 1 else ''}",
                           f"{brick_count} rainbow brick{'s' if brick_count > 1 else ''} with a rainbow hue. Goes in a straight line.")

    for i in range(brick_count):
        data.add_brick(
            "ScalableBrick",
            str(i),
            brci.pos([i*0.3, 0, 0]),
            [0, 0, 0],
            {
                "BrickSize": brci.size([0.3, 0.3, 0.1]),
                "BrickColor": brci.from_hsv(int((i/brick_count)*360), 100, 100, 100),
                "BrickMaterial": "Glow"
            }
        )

    data.write_preview(brci.BRCI_THUMBNAIL)
    data.write_metadata()
    data.write_creation()

    brci.printr(f"{brci.FM.LIGHT_GREEN}Done! You can find the project in `{os.path.join(brci.PROJECT_FOLDER, data.project_name)}`.")
