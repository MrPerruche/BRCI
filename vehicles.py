# Define vehicles here

from BRAPIF import *
from main import _cwd
from main import *

if __name__ == "__main__":
    # Setting up BR-API
    data = BRAPI()
    data.project_name = 'Proper-Hornwave'
    data.project_display_name = 'Hornwave'
    data.project_folder_directory = os.path.join(_cwd, 'Projects') # Do not touch
    data.file_description = 'An impressive display of BR-API and a flex that it works.'
    data.debug_logs = ['time']#, 'bricks']
    data.write_blank = None

    def stress_test_run() -> None:
        import random
        for brick_number in range(100_000):
            try:
                test_brick = create_brick(random.choice(list(br_brick_list.keys())))
                temp_test_selected_property = random.choice(list(test_brick.keys()))
                if isinstance(test_brick[temp_test_selected_property], float):
                    test_brick[temp_test_selected_property] = random.uniform(0.0, 1000.0)
                test_brick['Position'] = [random.uniform(0.0, 25000.0), random.uniform(0.0, 25000.0), random.uniform(0.0, 25000.0)]
                test_brick['Rotation'] = [random.uniform(0.0, 360.0), random.uniform(0.0, 360.0), random.uniform(0.0, 360.0)]
                if 'gbn' in test_brick:
                    data.add_brick(str(brick_number), test_brick)
            except KeyError:
                raise KeyError(f'GBN INVALID BRICK')

    def horn_pitch_test() -> None:
        test_pitch = 0.5
        position_x = 0
        hue = 0
        for brick_number_b in range(20):
            test_pitch -= 0.025
            position_x += 10
            hue += 10
            test_current_brick_w = create_brick('DoubleSiren_1x2x1s')
            test_current_brick_w['HornPitch'] = test_pitch
            test_current_brick_w['Position'] = [position_x, 0, 0]
            test_current_brick_w['BrickColor'] = [hue, 255, 255, 255]
            data.add_brick(str(brick_number_b), test_current_brick_w)


    def destiny_s_test() -> None:
        properties = {"Position": [0,0,0], "Rotation": [0,0,0], "BrickColor": [0, 255, 255, 255]}
        switch1 = create_brick('Switch_1sx1sx1s', properties)
        data.add_brick("Switch1", switch1)


    def input_channel_test():
        my_scalable = create_brick('ScalableBrick')
        data.add_brick('my_scalable', my_scalable)
        my_math_brick = create_brick('MathBrick_1sx1sx1s')
        my_math_brick['InputChannelA.InputAxis'] = BrickInput('AlwaysOn', -2_000_000.0, 'InputChannelA')
        my_math_brick['InputChannelB.InputAxis'] = BrickInput('Custom', ['my_math_brick'], 'InputChannelB')
        data.add_brick("my_math_brick", my_math_brick)

    def hornwave_again() -> None:
        loop = 11 # 70-71%
        start = 0.70 # 70%
        current = start
        hue = 0
        pos_x = 0
        for i in range(loop):
            if i >= 1: pos_x += 10; hue += 10; current += 0.001
            curbrick = create_brick('DoubleSiren_1x2x1s', {'HornPitch': current, 'BrickColor': [hue, 255, 255, 255], 'Position': [pos_x, 0, 0]})
            data.add_brick(str(i), curbrick)
        base_scalable = create_brick('ScalableBrick', {'Position': [50, 0, -5], 'BrickColor': [hue+10, 255, 255, 255], 'BrickSize': [13, 6, 1]}) # 1 stud = 3 of these
        data.add_brick("base_scalable", base_scalable)

    data.write_preview()

    #input_channel_test()
    hornwave_again()    
    

    print(f"{FM.info} Now generating file.")

    # Writing stuff
    data.write_metadata()
    data.write_brv()
    # data.debug_print(True, False, True) # Prints summary only
    data.debug_print(False, True, False) # Writes all data
    print(f"{FM.success} File successfully generated.")

    """
    print(f"\n\n{clr.error} An error occurred.")
    print(f"{clr.warning} Press enter to exit.")
    print(f"{clr.info} Press enter to continue.")
    print(f"{clr.success} File successfully generated.")
    print(f"{clr.debug} print(f'" + "{clr.info} Hello world')")
    print(f"{clr.test} Something\n\n")

    clr.error_with_header("Your creation contains too many bricks.", "Brick Rigs limit all creations to 65,535 bricks (16 bit unsigned integer limit).\nYour creation contains 68,194 bricks. 2,649 bricks were removed.")
    clr.warning_with_header("You suck", "And you will never ever get bitches\nBecause you're gay")=)
    
    input(f'\n\n\nwait')
    """