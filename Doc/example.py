import BRCI as brci
import os


if __name__ == "__main__":
    data = brci.BRCI()
    data.project_name = 'no_name'
    data.project_display_name = 'no name'
    data.project_folder_directory = os.path.join(os.getcwd(), 'Projects')
    data.logs = ['time']
    data.file_description = 'no\r\ndescription'
    data.write_blank = False


    # This function creates plenty of commonly used bricks
    def stress_test(bricks: int, size: float = 20_000.0, generate: bool = True) -> None:
        import random

        # Giving our project a name
        data.project_name = f'stress_test_{bricks}'
        # Giving our project a name to show in-game
        data.project_display_name = f'Stress Test ({bricks}b / {size}m)'
        # For each brick
        for brick_id_st in range(bricks):
            # Create a new brick
            new_brick_st = brci.create_brick(
                brick=random.choice(brci.br_brick_list.keys().remove('default_brick_data')),  # Select a random (valid) brick
                position=[random.uniform(0.0, size), random.uniform(0.0, size), random.uniform(0.0, size)],
                rotation=[random.uniform(0.0, 360.0), random.uniform(0.0, 360.0), random.uniform(0.0, 360.0)])

            # Pick a random property, if it's a float, set it to a random value between -1bil and +1bil.
            for property_st in new_brick_st.keys():
                if isinstance(new_brick_st[property_st], float):
                    new_brick_st[property_st] = random.uniform(-1_000_000_000.0, 1_000_000_000.0)

            data.add_brick(str(brick_id_st), new_brick_st)

        # If we want to generate a file now
        if generate:
            data.write_preview()
            data.write_metadata()
            data.write_brv()
            data.write_to_br()
            data.clear_bricks()


    def horn_wave(min_pitch: float, max_pitch: float, pitch_step: float, generate: bool = True) -> None:

        def float_range(start: float, stop: float, step: float):
            while start <= stop:
                yield start
                start += step

        def limit_loop(val: float, min_v: float, max_v: float):
            dif = max_v - min_v
            return min_v + ((val - min_v) % dif)

        data.project_name = 'horn_wave'
        data.project_display_name = f'Horn Wave ({min_pitch}%-{max_pitch}% / {pitch_step}% steps)'

        support_size = 0

        for pitch in float_range(min_pitch, max_pitch, pitch_step):
            support_size += 3

            data.anb(str(pitch), 'DoubleSiren_1x2x1s', {
                'BrickColor': [limit_loop(support_size*2, 0, 256), 255, 255, 255],
                'HornPitch': pitch/100
            }, [support_size*10, 0, 5])

        data.anb('support', 'ScalableBrick', {
            'BrickColor': [150, 100, 25, 255],
            'BrickSize': [support_size, 6, 1]
        }, [support_size*5, 0, -5])

        if generate:
            data.write_preview()
            data.write_metadata()
            data.write_brv()
            data.write_to_br()
            data.clear_bricks()


    # --------------------------------------------------

    """
    List of functions:
    
    stress_test(bricks, float, generate)
        bricks: int, Mandatory.
        size: float = 20_000.0 (in centimeters)
        generate: bool = True (executes write_preview(), write_metadata(), write_brv(), write_to_br(), clear_bricks())
        
    horn_wave(min_pitch, max_pitch, pitch_step, generate)
        min_pitch: float, Mandatory. (in percents)
        max_pitch: float, Mandatory. (in percents)
        pitch_step: float, Mandatory. (in percents)
        generate: bool = True (executes write_preview(), write_metadata(), write_brv(), write_to_br(), clear_bricks())
    """

    # stress_test(1_000)

    # horn_wave(40, 50, 0.5)

