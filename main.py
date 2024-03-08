import os

from BRAPIF import *

# ------------------------------------------------------------
# DEFAULT VARIABLES AND SETUP
# ------------------------------------------------------------

# Setup variables
version = "C2"

# Important variables
_cwd = os.path.dirname(os.path.realpath(__file__))

# Temporary Variables
# No Temporary Variables.


# ------------------------------------------------------------
# DATA WRITING
# ------------------------------------------------------------


# Return all data about specified brick
def create_brick(brick: str):
    return br_brick_list[brick]


# What am I supposed to comment here?
class BRAPI:

    # Getting all values. Do I have to comment that too?
    def __init__(self,
                 bricks=None,
                 project_folder_directory='',
                 project_name='',
                 write_blank=False,
                 project_display_name='',
                 file_description=''):

        # I'm not commenting this either.
        self.project_folder_directory = project_folder_directory
        self.project_name = project_name
        self.write_blank = write_blank
        self.project_display_name = project_display_name
        self.file_description = file_description
        if bricks is None:
            bricks = []
        self.bricks = bricks


    # Creating more variables
    # In project path
    @property
    def in_project_folder_directory(self):
        return os.path.join(self.project_folder_directory, self.project_name)

    # Calculate brick count
    @property
    def brick_count(self):
        return len(self.bricks)

    # Calculate vehicle size
    @property
    def vehicle_size(self):
        # TODO : CALCULATE SIZE
        return [1, 2, 3]

    # Calculate vehicle weight
    @property
    def vehicle_weight(self):
        # TODO : CALCULATE WEIGHT
        return 0.1

    # Calculate vehicle worth
    @property
    def vehicle_worth(self):
        # TODO : CALCULATE WORTH
        return 0.2

    # Adding bricks to the brick list
    def add_brick(self, brick_name, new_brick):
        self.bricks.append([str(brick_name), new_brick])


    # Removing bricks from the brick list
    def remove_brick(self, brick_name):

        self.bricks = [sublist for sublist in self.bricks if sublist[0] != str(brick_name)]


    # Updating a currently existing brick
    def update_brick(self, brick_name, new_brick):
        self.remove_brick(brick_name)
        self.add_brick(brick_name, new_brick)


    # Used to create directory for file generators
    def ensure_project_directory_exists(self):

        # Verify for invalid inputs
        if not os.path.exists(self.project_folder_directory):

            raise FileNotFoundError(f'Unable to find the project\'s folder ({self.project_folder_directory})')

        os.makedirs(os.path.dirname(os.path.join(self.in_project_folder_directory, self.project_name)), exist_ok=True)


    # Writing preview.png
    def write_preview(self):

        _write_preview_regular_image_path = os.path.join(_cwd, 'Resources', 'icon_compressed_reg.png')

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Verify the image exists.
        if not os.path.exists(_write_preview_regular_image_path):

            raise FileNotFoundError('Unable to create preview, original image not found.')

        # Copy saved image to the project folders.
        copy_file(os.path.join(_write_preview_regular_image_path),
                  os.path.join(self.in_project_folder_directory, "Preview.png"))


    # Writing metadata.brm file
    def write_metadata(self):

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Verify self.write_blank is valid.
        if not isinstance(self.write_blank, bool):

            raise TypeError('Invalid write_blank type. Expected bool.')

        # Write blank file for metadata (if desired)
        if self.write_blank:

            blank_metadata = open(os.path.join(self.in_project_folder_directory, "MetaData.brm"), "x")
            blank_metadata.close()

        # Otherwise write working metadata file
        else:
            with open(os.path.join(self.in_project_folder_directory, "MetaData.brm"), 'wb') as metadata_file:

                # Writes Carriage Return char
                metadata_file.write(unsigned_int(13, 1))

                # Write all necessary information for the file name
                line_feed_file_name = (((self.project_name.replace("\\n", "\n")).encode('utf-16'))
                                       .replace(b'\x0A\x00',b'\x0D\x00\x0A\x00')).decode('utf-16')
                metadata_file.write(signed_int(-len(line_feed_file_name), 2))
                metadata_file.write(bin_str(line_feed_file_name)[2:])

                # Write all necessary information for the file description
                watermarked_file_description = f"Created using BR-API.\n" \
                                               f"BR-API Version {version}.\n\n" \
                                               f"Description:\n{self.file_description}."
                watermarked_file_description = (
                    ((watermarked_file_description.replace("\\n", "\n")).encode('utf-16'))
                    .replace(b'\x0A\x00',b'\x0D\x00\x0A\x00')).decode('utf-16')
                metadata_file.write(signed_int(-len(watermarked_file_description), 2))
                metadata_file.write(bin_str(watermarked_file_description)[2:])

                # Write all necessary information for the 4 additional values : Bricks, Size, Weight and Monetary Value
                metadata_file.write(signed_int(self.brick_count, 2))
                metadata_file.write(bin_float(self.vehicle_size[0], 4))
                metadata_file.write(bin_float(self.vehicle_size[1], 4))
                metadata_file.write(bin_float(self.vehicle_size[2], 4))
                metadata_file.write(bin_float(self.vehicle_weight, 4))
                metadata_file.write(bin_float(self.vehicle_worth, 4))

                # Writes the author. We don't want it to be listed, so we write invalid data.
                metadata_file.write(bytes.fromhex('FFFFFFFFFFFFFFFF'))

                # I have no fucking clue of what I'm writing but hey it's something right?
                metadata_file.write(bytes.fromhex("14686300000000B034B6C7382ADC08E079251F392ADC08"))

                # Writing tags                                                                                          TODO Broken
                metadata_file.write(unsigned_int(3, 1))
                for i in range(3):
                    metadata_file.write(unsigned_int(5, 1))
                    metadata_file.write(small_bin_str("Other"))


    # Writing Vehicle.brv
    def write_brv(self):

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Verify self.write_blank is valid.
        if not isinstance(self.write_blank, bool):

            raise TypeError('Invalid write_blank type. Expected bool.')

        # Write blank file for vehicle (if desired)
        if self.write_blank:
            blank_brv = open(os.path.join(self.in_project_folder_directory, "Vehicle.brv"), "x")
            blank_brv.close()

        # Otherwise write working vehicle file
        else:
            with open(os.path.join(self.in_project_folder_directory, "Vehicle.brv"), 'wb') as brv_file:

                # Writes Carriage Return char
                brv_file.write(unsigned_int(13, 1))
                # Write brick count
                brv_file.write(unsigned_int(self.brick_count, 2))

                # Get the different bricks present in the project
                brick_types = list(set(item[1]['gbn'] for item in self.bricks))

                print('Verify input', self.bricks)

                print('br_brick_list:', br_brick_list)


                """
                Destiny here's your home work:
                
                Structure:

                self.bricks is a list with sublists. Each sublist has two items: the brick's name (not important) and a
                dictionary with all the brick's data, including position, rotation, and 'gbn' (which is the brick type
                for the BRV).
                br_brick_list is a dictionary where each key is a brick type, and the value is a dictionary with default
                data for that brick type.

                Goal:

                Remove any data from each brick that matches the default values listed in br_brick_list.
                """

                print('verify output', self.bricks)

                # Write each brick type
                for brick_type in brick_types:
                    brv_file.write(unsigned_int(len(brick_type), 1))
                    brv_file.write(small_bin_str(brick_type))

                brv_file.write(unsigned_int(len(brick_types), 2))



# Try it out
data = BRAPI()
data.project_name = 'test project b'
data.project_display_name = 'My Project'
data.project_folder_directory = os.path.join(_cwd, 'Projects')
data.file_description = 'My first project.'

print(data.project_folder_directory)

first_brick = create_brick('Switch_1sx1sx1s')
second_brick = create_brick('DisplayBrick')
third_brick = create_brick('Switch_1sx1sx1s')

first_brick['bReturnToZero'] = False
first_brick['OutputChannel.MinIn'] = 12
third_brick['OutputChannel.MaxOut'] = -12

data.add_brick('first_brick', first_brick)
data.add_brick('second_brick', second_brick)
data.add_brick('third_brick', third_brick)

print(first_brick['gbn'])

data.write_preview()
data.write_metadata()
data.write_brv()


"""
# Doesnt matter.
my_test_brick = create_brick('Switch_1sx1sx1s')
data.add_brick('my_test_brick', my_test_brick)
print(my_test_brick)
print(data.bricks)
"""