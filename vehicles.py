# Define vehicles here

from BRAPIF import *
from main import _cwd
from main import *

if __name__ == "__main__":
    data = BRAPI()
    data.project_name = 'no_name'
    data.project_display_name = 'no_name'
    data.project_folder_directory = os.path.join(_cwd, 'Projects') # Do not touch
    data.file_description = 'no_description'
    data.debug_logs = ['time']#, 'bricks']
    data.write_blank = False

    def find_missing_gbn(bricks_list: dict, print_missing: bool = True) -> list:
        missing_values: list = []
        for key, value in bricks_list.items():
            if 'gbn' not in value:
                missing_values.append(key)
        if print_missing:
            print(missing_values)
        return missing_values

    def stress_test(bricks: int, size: float = 200.0, generate: bool = True) -> None:
        import random
        data.project_name = f'stress_test_{bricks}'
        data.project_display_name = f'Stress Test ({bricks}b / {size}m)'
        for brick_id_st in range(bricks):
            new_brick_st = create_brick(
                brick=random.choice( list(filter(lambda item: item != 'default_brick_data', br_brick_list.keys())) ),
                position=[random.uniform(0.0, size), random.uniform(0.0, size), random.uniform(0.0, size)],
                rotation=[random.uniform(0.0, 360.0), random.uniform(0.0, 360.0), random.uniform(0.0, 360.0)])

            for property_st in new_brick_st.keys():
                if isinstance(new_brick_st[property_st], float):
                    new_brick_st[property_st] = random.uniform(-1_000_000_000.0, 1_000_000_000.0)

            data.add_brick(str(brick_id_st), new_brick_st)

        if generate:
            data.write_preview()
            data.write_metadata()
            data.write_brv()

    # --------------------------------------------------

    find_missing_gbn(br_brick_list)
    stress_test(10_000)





"""
if __name__ == "__main__":
    # Setting up BR-API
    data = BRAPI()
    data.project_name = 'Wheel-Test'
    data.project_display_name = 'Wheel Test'
    data.project_folder_directory = os.path.join(_cwd, 'Projects') # Do not touch
    data.file_description = 'A test to see if Destiny has properly coded *all* wheels in.'
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

    def thruster_test() -> None:
        properties = {"Position": [0,0,0], "Rotation": [0,0,0], "BrickColor": [0, 255, 255, 255], "InputChannel.InputAxis": "AlwaysOn", "bAccumulated": True}
        thruster = create_brick('Thruster_1sx1sx1s', properties)
        thruster2 = create_brick('Thruster_1x1x1', properties)
        thruster3 = create_brick('Thruster_1x1x3', properties)
        thruster4 = create_brick('Thruster_2x2x4', properties)
        data.add_bricks(["thruster", "thruster2", "thruster3", "thruster4"], [thruster, thruster2, thruster3, thruster4])
    
    def axle_test() -> None:
        properties = {"Position": [0,0,0], "Rotation": [0,0,0]}
        axle = data.create_add_brick('Axle_1sx1sx1s', properties)
        axle2 = data.create_add_brick('Axle_1x1x1s_02', properties | {"Position": [10, 0, 0]})
        axle3 = data.create_add_brick('Axle_1x1x1s', properties | {"Position": [20, 0, 0]})
        axle4 = data.create_add_brick('Axle_1x2x1s', properties | {"Position": [30, 0, 0]})
        axle5 = data.create_add_brick('Axle_2x2x1s', properties | {"Position": [40, 0, 0]})
        axle6 = data.create_add_brick('Axle_2x2x1', properties | {"Position": [50, 0, 0]})
        axle7 = data.create_add_brick('LandingGear_2x2x2', properties | {"Position": [60, 0, 0]})
        axle8 = data.create_add_brick('Axle_2x4x1s', properties | {"Position": [70, 0, 0]})
        axle9 = data.create_add_brick('Axle_2x6x1s', properties | {"Position": [80, 0, 0]})

    def wheel_test() -> None:
        properties = {"Position": [0,0,0], "Rotation": [0,0,0]}
        data.add_bricks(
            ["wheel",
            "wheel2",
            "wheel3",
            "wheel4",
            "wheel5",
            "wheel6",
            "wheel7",
            "wheel8",
            "wheel9",
            "wheel10",
            "wheel11",
            "wheel12",
            "wheel13",
            "wheel14",
            "wheel15",
            "wheel16"
            ], 
            [create_brick('Wheel_2x2s', properties),
             create_brick('RacingWheel_4x2s', properties | {"Position": [10, 0, 0]}),
             create_brick('Wheel_10sx1', properties | {"Position": [20, 0, 0]}),
             create_brick('OffroadWheel_3x4s', properties | {"Position": [30, 0, 0]}),
             create_brick('RacingWheel_3x4s', properties | {"Position": [40, 0, 0]}),
             create_brick('Wheel_3x4s', properties | {"Position": [50, 0, 0]}),
             create_brick('Wheel_7sx2', properties | {"Position": [60, 0, 0]}),
             create_brick('DragWheel_4x2', properties | {"Position": [70, 0, 0]}),
             create_brick('Wheel_4x2', properties | {"Position": [80, 0, 0]}),
             create_brick('OffroadWheel_5x2', properties | {"Position": [90, 0, 0]}),
             create_brick('Wheel_10x4', properties | {"Position": [100, 0, 0]}),
             create_brick('TrainWheel_2x2s', properties | {"Position": [110, 0, 0]}),
             create_brick('TrainWheel_3x2s', properties | {"Position": [120, 0, 0]}),
             create_brick('TrainWheel_4x2s', properties | {"Position": [130, 0, 0]}),
             create_brick('Wheel_1sx1sx1s', properties | {"Position": [140, 0, 0]}),
             create_brick('Wheel_1x1x1', properties | {"Position": [150, 0, 0]})
             ])
    
    data.write_preview()

    #input_channel_test()
    #hornwave_again()    
    #thruster_test()
    #axle_test()
    wheel_test()
    

    print(f"{FM.info} Now generating file.")

    # Writing stuff
    data.write_metadata()
    data.write_brv()
    # data.debug_print(True, False, True) # Prints summary only
    data.debug_print(False, True, False) # Writes all data
    print(f"{FM.success} File successfully generated.")

    "X""
    print(f"\n\n{clr.error} An error occurred.")
    print(f"{clr.warning} Press enter to exit.")
    print(f"{clr.info} Press enter to continue.")
    print(f"{clr.success} File successfully generated.")
    print(f"{clr.debug} print(f'" + "{clr.info} Hello world')")
    print(f"{clr.test} Something\n\n")

    clr.error_with_header("Your creation contains too many bricks.", "Brick Rigs limit all creations to 65,535 bricks (16 bit unsigned integer limit).\nYour creation contains 68,194 bricks. 2,649 bricks were removed.")
    clr.warning_with_header("You suck", "And you will never ever get bitches\nBecause you're gay")=)
    
    input(f'\n\n\nwait')
    "X""
"""