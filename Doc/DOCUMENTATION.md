# **Brick Rigs Creation Interface Documentation**

Brick Rigs Creation Interface (a.k.a. BRCI) allows you to
create and edit (not implemented yet) creations (a.k.a. vehicles) in Brick Rigs.

## Setup

First we must import BRCI.  
Here we will use `import BRCI as brci`.

Then, we must initialize BRCI, by creating an instance of the class BRCI.  
Here we will use `data = brci.BRCI()`.

Last, we must edit some variables in order to use it.

Mandatory (Out of order) :  
`data.project_name` (`str`) define what name is given to the file later generated.  
`data.project_folder_directory` (`str`) define where the creation will be created.

Optional (Out of order) :  
`data.project_display_name` (`str`) (`''`) define what name will be displayed in-game.  
`data.file_description` (`str | None`) (`None`) define what description will be displayed in-game.  
`data.visibility` (`int` 0-3) (`2`) define what visibility it is set to; `0` → `Public`, `1` → `Friends Only`, `2` → `Private`, `3` → `Unlisted`.
`data.creation_timestamp` (`int | None`) (`None`) define what timestamp will be displayed in-game as creation time.
None corresponds to timestamp at generation, int corresponds to 100-nanoseconds since 0001-01-01 00:00:00.  
`data.update_timestamp` (`int | None`) (`None`) define what timestamp will be displayed in-game as last update time.
None corresponds to timestamp at generation, int corresponds to 100-nanoseconds since 0001-01-01 00:00:00.  
`data.tags` (`list[str, str, str] | None`) (`None`→`['None', 'None', 'None']`) define what tags will be displayed in-game.
Tags :
- 1st tag : `'None'` / `'Car'` / `'RaceCar'`
// `'Truck'` / `'HeavyMachinery'` / `'Plane'`
// `'Helicopter'` / `'Tank'` / `'Train'`
// `'Trailer'` / `'Prop'` / `'Building'`
// `'Ship'` / `'SpaceCraft'` / `'Bus'`
// `'Motorcycle'`
- 2nd tag : `'None'` / `'_1800s'` / `'_1900s'`
// `'_2000s'` / `'Futuristic'` / `'Ancient'`
// `'WW2'` / `'WW1'`
- 3rd tag : `'None'`/ `'Civil'` / `'Military'`
// `'Police'` / `'FireDepartment'`

`data.logs` (`list[str] | None`) (`None`→`[]`) define what logs will be printed :
- `'time'` will print how long each step takes to generate.
- `'bricks'` will print debug information about bricks.

`data.user_appendix` (`bytes`) (`b''`) define what bytes are hidden in the `Vehicle.brv` file.
This data is cleared when you save it in-game.  
`data.seat_brick` (`str | None`) (`None`) define what brick is the driver seat. If it is set to `None`, it will set all
seats to the "Random" setting, which set the driver seat to the first seat loaded. To set the driver seat, you must use
the brick's name.

Here's an example of how to initialize BRCI:
```python
import BRCI as brci
from os import getcwd

# Initializing BRCI
data = brci.BRCI()
# Configuring BRCI
# Mandatory :
data.project_name = 'my_first_project'
data.project_folder_directory = getcwd()
# Optional :
data.project_display_name = 'My First Project!'
data.file_description = 'My\r\nFirst\r\nCreation'
data.logs = ['time']
data.user_appendix = 'Hello World!'.encode('utf-8')
data.seat_brick = None
```

## Creating Creations

In order to create creations (a.k.a. vehicles), you may use some of the listed functions here to help you.

### Assigning a brick to a variable

#### How to assign a brick to a variable

In order to add a brick, you may use
`data.create_brick()` / `data.cb()`, which will return you a dictionary (`dict[str: any]`) containing all properties and important data.

This function takes 1 mandatory argument and 3 optional arguments:

Mandatory :  
`brick` / `b` (`str`) define which brick you are creating. You must indicate the `.brv` name, not the in-game name.
You may use `BRICKS.md` to easily get their name. Instructions on how to use it down below.

Optional :  
`position` / `pos` (`list[float]`) (`None`→`[0, 0, 0]`) define the position of the brick in centimeters (10cm = 1 third). (It can later be modified with `variable['Position'] = ...`)  
`rotation` / `rot` (`list[float]`) (`None`→`[0, 0, 0]`) define the rotation of the brick in degrees. (It can later be modified with `variable['Rotation'] = ...`)  
`brick_properties` / `p` (`dict | None`) (`None`) define what properties are given to the brick.

Additionally, you may use `brci.custom_common_properties` (`dict[str: any]`) to add / overwrite properties
that are returned whenever you use this function. Keep in mind `brick_properties` has priority over this variable.

Here's an example on how to use `data.create_brick()` / `data.cb()`:

```python
# Initializing BRCI
import BRCI as brci
from os import getcwd

data = brci.BRCI()
data.project_name = 'my_first_project'
data.project_folder_directory = getcwd()

# Overwriting properties returned by default by brci.create_brick()
brci.custom_common_properties = {
    'BrickPattern': 'P_Swirl_Arabica',
    'BrickColor': [120, 255, 212, 255]
}
# Creating our new brick
my_brick = data.create_brick('Switch_1sx1sx1s', [10, 0, 0], [0, 180, 0], {'BrickPattern': 'C_Flecktarn'})
my_brick['BrickMaterial'] = 'ChannelledAlu'

print(my_brick)

"""
This script will print (With new lines added):
{
    'BrickColor': [120, 255, 212, 255],
    'BrickPattern': 'C_Flecktarn',
    'BrickMaterial': 'ChannelledAlu',
    'Position': [10.0, 0.0, 0.0],
    'Rotation': [0.0, 180.0, 0.0],
    'OutputChannel.MinIn': -1.0,
    'OutputChannel.MaxIn': 1.0,
    'OutputChannel.MinOut': -1.0,
    'OutputChannel.MaxOut': 1.0,
    'InputChannel': BrickInput('None', None),
    'bReturnToZero': True,
    'SwitchName': ''
    'gbn': 'Switch_1sx1sx1s'
}
Note : 'gbn' indicates which brick it is. We recommend you not to modify it.
"""
```

#### How `BRICKS.md` is structured

This file helps you find brick names and information about brick names & properties.

It is divided in two parts:

##### Every property in-game
This part list every property in Brick Rigs. It explains what's their type, how to use them, since many properties such as `ExitLocation`
and `BrickColor` are fairly counter-intuitive at first, and more.
Additionally, it explains what we mean by "Default Brick Properties" at the beginning

##### Every brick in-game
This part list every brick and what property are assigned to them. It is sorted as such:
It is separated by categories, and then listed one by one in UI order, skipping a line every time UI changes line.
We ignore folders. For each brick a letter is assigned to them after many dots.  
This letter define what properties this brick has. It can be seen at the bottom of the list, along with
their default value and type (in order to avoid constantly scrolling back up)

### Get a brick ready for generation

In order to make a brick you've created using the previously demonstrated method,
you must use `data.add_brick()` / `data.ab()` which will return self.

It has 2 mandatory arguments :

Mandatory :  
`brick_name` / `n` (`str | list[str]`) define what name you want to give your brick, in order to interact with it in various
ways such as deleting / editing it, using it as an input for some bricks, etc.  
`brick` / `b` (`dict[str: any] | list[dict[str: any]]`) define what properties are given to the brick (What is returned
by `data.create_brick()` / `data.cb()`).

If the arguments are provided as a list, then all arguments must be in list form to affect multiple bricks concurrently.
Additionally, all lists must be of the same length.

Here's an example on how to use `data.add_brick()` / `data.ab()`:

```python
# Initializing BRCI
import BRCI as brci
from os import getcwd

data = brci.BRCI()
data.project_name = 'my_first_project'
data.project_folder_directory = getcwd()

# Creating our new brick
my_brick = data.add_brick('Switch_1sx1sx1s', [10, 0, 0], [0, 180, 0], {'BrickPattern': 'C_Flecktarn'})
my_brick['BrickMaterial'] = 'ChannelledAlu'

# Adding our brick to the list of bricks that will be generated
data.add_brick('my_brick', my_brick)
```

### Creating a new brick already ready for generation

You may do the two previous steps (`data.cb()` + `data.ab()`) in one line using `data.add_new_brick()` / `data.anb()`,
which returns self.

It has 2 mandatory arguments and 3 optional arguments :

Mandatory :
`brick_name` / `n` (`str | list[str]`) define what name you want to give your brick, in order to interact with it in various
ways such as deleting / editing it, using it as an input for some bricks, etc.  
`brick_type` / `t` (`str | list[str]`) define what type of brick you want to create. 

Optional :
`brick` / `b` (`dict[str: any] | list[dict[str: any]]`) define what properties are given to the brick.  
`position` / `pos` (`list[float] | list[list[float]]`) define where the brick will be placed.  
`rotation` / `rot` (`list[float] | list[list[float]]`) define how the brick will be rotated.

If the arguments are provided as a list, then all arguments must be in list form to affect multiple bricks concurrently.
Additionally, all lists must be of the same length.

Here's an example on how to use `data.add_new_brick()` / `data.anb()`:

```python
# Initializing BRCI
import BRCI as brci
from os import getcwd

data = brci.BRCI()
data.project_name = 'my_first_project'
data.project_folder_directory = getcwd()

# Adding a newly created brick
data.add_new_brick('my_brick', 'Switch_1sx1sx1s', {
    'BrickColor': [120, 255, 212, 255],
    'BrickPattern': 'C_Flecktarn',
    'BrickMaterial': 'ChannelledAlu'
}, [10, 0, 0], [0, 180, 0])
```

### Modifying an already added brick

You may need to modify an already implemented brick. In this case, use `data.update_brick()` / `data.ub()` which returns self.

It has 2 mandatory arguments :

Mandatory :  
`brick_name` (`str | list[str]`) define what brick you're editing (use its name, not its type)
`new_brick` (`dict | list[dict]`) define what values are being set, instead of the old ones.

If the arguments are provided as a list, then all arguments must be in list form to affect multiple bricks concurrently.
Additionally, all lists must be of the same length.

Here's an example on how to use `data.update_brick()` / `data.ub()`:

```python
# Initializing BRCI
import BRCI as brci
from os import getcwd

data = brci.BRCI()
data.project_name = 'my_first_project'
data.project_folder_directory = getcwd()

# Creating our new brick
my_brick = brci.cb('Switch_1sx1sx1s', [10, 0, 0], [0, 180, 0], {'BrickPattern': 'C_Flecktarn'})

# Adding our brick to the list of bricks that will be generated
data.ab('my_brick', my_brick)

# Modifying our brick & applying changes
my_brick['BrickColor'] = [0, 127, 255, 255]
data.update_brick('my_brick', my_brick)
```

### Deleting an already added brick

You may need to delete an already implemented brick. In this case, use `data.remove_brick()` / `data.rb()` which returns self.

It has 1 mandatory argument :

Mandatory :  
`brick_name` / `n` (`str | list[str]`) define what brick you're going to delete (use its name, not its type).

If the argument is provided as a list, it'll delete multiple bricks simultaneously.

Here's an example on how to use `data.remove_brick()` / `data.rb()`:

```python
# Initializing BRCI
import BRCI as brci
from os import getcwd

data = brci.BRCI()
data.project_name = 'my_first_project'
data.project_folder_directory = getcwd()

# Creating our new brick
my_brick = brci.cb('Switch_1sx1sx1s', [10, 0, 0], [0, 180, 0], {'BrickPattern': 'C_Flecktarn'})

# Adding our brick to the list of bricks that will be generated
data.ab('my_brick', my_brick)

# Deleting our brick
data.remove_brick('my_brick')
```

### Deleting all already added bricks

You may need to clear all implemented bricks. In this case, you may use `data.clear_bricks()`, which returns self.

It takes no arguments.

Here's an example on how to use `data.clear_bricks()` :
```python
# Initializing BRCI
import BRCI as brci
from os import getcwd

data = brci.BRCI()
data.project_name = 'my_first_project'
data.project_folder_directory = getcwd()

# Creating some bricks
data.anb('first', 'Switch_1sx1sx1s')
data.anb('second', 'DisplayBrick')
data.anb('third', 'ScalableBrick')
data.anb('last', 'Wing_4x8x1s_L')

# Clearing all bricks
data.clear_bricks()

# No bricks left. Generating .brv will generate an empty creation.
```

## Loading and modifying existing creations

### Loading creations

To load existing creations in BRCI, you may use `data.load_brv()` which returns self.

It has 4 optional arguments:

Optional:  
`load_vehicle` (`bool`) (`True`) define if bricks will be loaded  
`load_brci_data` (`bool`) (`True`) define if brick names will be loaded 
(only works if it was generated by BRCI and not modified by the game)  
`load_appendix` (`bool`) (`True`) define if appendix data will be loaded  
`file_name` (`str`) (`'Vehicle.brv'`) define how the loaded file is named

WARNING: Set `load_brci_data` to `False` if the file you're attempting to load was made before version C45!

Here's an example on how to use `data.load_brv()` :

```python
# Initializing BRCI
import BRCI as brci
import os

cwd = os.path.dirname(os.path.realpath(__file__))

data = brci.BRCI()

data.project_name = 'my_first_project'
data.project_folder_directory = cwd

# Loading vehicle file
data.load_brv()
```

### Retrieving bricks

You may need to retrieve bricks. In this case; you have a variety of functions:

#### Retrieving all bricks

To retrieve all bricks, you may use `data.get_all_bricks()` which returns all bricks; in a format depending on specified arguments

It has 1 optional argument:

Optional:  
`output_as_dict` (`bool`) (`False`) define if the output will be a dictionary will a brick names and their properties or
a list of lists containing as the first (0) element their name and the second (1) element their properties.

Here's an example on how to use `data.get_all_bricks()` :

```python
# Initializing BRCI
import BRCI as brci
import os

cwd = os.path.dirname(os.path.realpath(__file__))

data = brci.BRCI()

data.project_name = 'my_first_project'
data.project_folder_directory = cwd

# Loading vehicle file
data.load_brv()

# Printing its bricks
print(data.get_all_bricks(True))
```

#### Retrieving bricks with (a) given name(s)

To retrieve bricks with (a) given name(s), you may use `data.get_brick()` which returns the requested bricks (without their name).

It has 1 mandatory argument:

Mandatory:  
`brick_name` (`str | list[str]`) define what brick(s) BRCI will retrieve.  

It's outcome depends on bricks currently loaded. Here's an example on how to use `data.get_brick()` :
```python
# Initializing BRCI
import BRCI as brci
import os

cwd = os.path.dirname(os.path.realpath(__file__))

data = brci.BRCI()

data.project_name = 'my_first_project'
data.project_folder_directory = cwd

# Loading vehicle file
data.load_brv()

# Printing its bricks
# In order to retrieve brick names, you must load brci data too.
# If it is not loaded, you must use IDs. Here IDs may be [0, 2].
print(data.get_brick(['my_first_brick', 'my_third_brick']))
```

### Retrieving unknown bricks

To retrieve bricks using data other than their names/ID, you may use `data.search_brick()`.
Keep in mind this function is extremely expensive.
All arguments set to `None` will be ignored in the sorting.

It has 10 optional arguments:

Optional:  
`names` (`list[str | int]`) (`None`) define what names BRCI will look for. This can also be done with `data.get_brick()`.  
`has_property` (`list[str]`) (`None`) will include all bricks that has one of the specified properties.  
`has_value` (`any`) (`None`) will include all properties with the specified value. You cannot sort by a list of value.  
`has_value_in_range` (`tuple[int | float]`) (`None`) will take 2 numbers and include all properties of which their assigned values are a number in their range.
Make sure numbers are in the right order.  
`has_item` (`dict[str, any]`) (`None`) will include all bricks that have the specified properties and value  
`has_item_in_range` (`dict[str, tuple[int | float]]`) (`None`) will take 2 numbers and include all bricks that have the specified properties and value in their range
Make sure numbers are in the right order.  
`is_brick` (`list[str]`) (`None`) will include all bricks of which their type is in the specified list.  
`criteria` (`str`) (`'and'`) define what bricks BRCI will return depending on how these conditions are met.
It may be set to either `'and'`, `'or'`, `'not and'` or `'not or'`.  
`output_as_dict` (`bool`) (`False`) define if the output will be a dictionary will a brick names and their properties or
a list of lists containing as the first (0) element their name and the second (1) element their properties.  
`tolerance_factor` (`float`) (`1e-6`) define the tolerance factor for numbers (tolerance adjusted based on the value, allowing proportional deviation to counter floating point accuracy issues)


Here's an example on how to use `data.search_brick()` :
```python
# Initializing BRCI
import BRCI as brci
import os

cwd = os.path.dirname(os.path.realpath(__file__))

data = brci.BRCI()

data.project_name = 'my_first_project'
data.project_folder_directory = cwd

# Loading vehicle file
data.load_brv()

# Searching for a brick
# 'not or' = If it is not ... or ... => If it is none of these
print(data.search_brick(names=[0, 1, 2, 20, 3, 8, 5], is_brick=['Switch_1sx1sx1s', 'Switch_1x1x1s'], criteria='not or'))
```


## Generating files

Note that if any file already exists with the same name, BRCI will crash. This will be resolved once
we will implement file editing.
BRCI give you 4 functions to generate files and get debug information:

### `data.write_preview()`

Calling this function will generate a "temporary" BRCI image : `Preview.png`.

It has 1 optional argument:

Optional:  
`file_name` (`bool`) (`'Vehicle.brv'`) define how will the generated file be named (Brick rigs will not load it if you don't set it to the default value)


### `data.write_metadata()`

Calling this function will generate metadata : `MetaData.brm`. It does NOT matter if metadata is incorrect. However,
metadata is required!

It has 1 optional argument:

Optional:  
`file_name` (`bool`) (`'Vehicle.brv'`) define how will the generated file be named (Brick rigs will not load it if you don't set it to the default value)


### `data.write_brv()`

Calling this function will generate the creation : `Vehicle.brv`.

It has 1 optional argument:

Optional:  
`file_name` (`bool`) (`'Vehicle.brv'`) define how will the generated file be named (Brick rigs will not load it if you don't set it to the default value)

As you may have guessed, it is necessary.

### `data.write_to_br()`

Calling this function will duplicate everything generated so far in Brick Rigs' folder. It only works for Windows users.
If the project is already in Brick Rigs' vehicle folder, it will replace the previous one without causing an error.

### Other functions

### `data.debug()`

`data.debug(summary_only, write, print_bricks)` has 3 optional arguments:

Optional :  
`summary_only` (`bool`) (`False`), if true, will make it only get essential information on the build :
Name, Amount of bricks, etc. Otherwise, it will also include all generated bricks and debug information to help troubleshooting.  
`write` (`bool`) (`True`), if true, will make it write everything in `debug_logs.txt`. Brick Rigs will ignore this file.  
`print_bricks` (`bool`) (`False`), if true, will make it print all generated bricks to the console.

### `data.get_missing_gbn_keys()`
`data.get_missing_gbn_keys()` is a function that returns all missing 'gbn' keys. It is used to find a common error
when adding bricks to the brick list : leaving argument `gbn` to false whilst using `append_multiple()`. This function
has 1 argument:  

`print_missing` (`bool`) (`False`) (Optional) : If true, it will not only return all missing `gbn` keys but
also print them.

If there is no issue, `['default_brick_data']` will be returned.
Note: `'default_brick_data'` is not a brick and using it will cause an error as no `gbn` key is given to it.
Even if it had one, which would no longer cause an error with BRCI, Brick Rigs would not be able to load this brick.


## Brick Inputs

`BrickInput()` is a custom class that is used to specify what inputs are given to a brick. Learn more in `BRICKS.md`
(check last property listed).


## Implementing Modded/Missing bricks

You may encounter some issues using BRCI regarding modded or newly added bricks.

Note : If newly added bricks are missing, make sure to update BRCI to the latest version!

In order to implement missing bricks, you must use `brci.append_multiple()`. Before explaining how to use it to
implement missing bricks, let's check how it works:

`var` (`dict`) defines is which dictionary will be modified  
`keys` (`list`) defines which keys are going to be appended  
`value` (`dict`) defines what is going to be appended to it  
`gbn` (`bool`) defines if we're implementing missing bricks

Now that we're familiar with this function, let's use it to create bricks:
- `var` must be set to `brci.br_brick_list`.
- `keys` must be a list of a brick names (names in the `.brv` file, not in-game). There may only be 1 element in this list.
- `value` must be set to `brci.br_brick_list['default_brick_data'] | {...}`.
Replace `...` with the list of properties, other than `Position`, `Rotation`, `BrickColor`, `BrickPattern`, `BrickMaterial`.
`gbn` is defined with the last argument. Naturally, property names must also correspond to names in the `.brv` file, not in-game.
If there are no other properties to add, you may remove `| {}`.
- `gbn` must be set to `True` in order to add `gbn` keys for each. We recommend you doing it using this argument instead
of `value`, not only to make the code harder to read but also because `gbn` must be unique to each key.

Here's an example on how to use `brci.append_multiple()` to implement missing bricks:
```python
import BRCI as brci

# Adding our new brick
brci.append_multiple(brci.br_brick_list, ['NewFancyBrick', 'MyModdedBrick'],
                     brci.br_brick_list['default_brick_data'] | {
                         'ThisNewFancyProperty': 1.0,
                         'YetAnotherNewProperty': brci.BrickInput('Custom', None),
                         'BinaryProperty': b'Abcd',
                         'CustomProperty': ['say_hello', 'James']
                     }, True)

# Note that this will now work. Here's why : (See documentation below)
```

If your new brick(s) involve new properties, you must add to the `brci.br_property_types` dictionary every single new
property and their type. It may be one of these :
- `bin` (Later discussed).
- `bool` : Boolean.
- `brick_id` : A single brick (string).
- `custom` : (Later discussed).
- `float` : Single precision float.
- `list[brick_id]` : A list of bricks.
- `list[3*float]` : A list of 3 single precision float values.
- `list[3*uint8]` : A list of 3 unsigned 8-bit integer values. Also accept a single unsigned 24-bit integer value (e.g. `0x7AD608`).
- `list[3*uint16]` : A list of 3 unsigned 16-bit integer values. Also accept a single unsigned 48-bit integer value (e.g. `0x7AD608CF0072`).
- `list[4*uint8]` : A list of 4 unsigned 8-bit integer values. Also accept a single unsigned 32-bit integer value (e.g. `0x7AD608CF`).
- `list[6*uint2]` : A list of 6 unsigned 2-bit integer values. Also accept a single unsigned 12-bit integer value (e.g. `0xAD6`).
- `str8` : A utf-8 string (maximum length: 255).
- `str16` : A utf-16 string (maximum length: 32767).
- `strany`: A string that may either be utf-8 (maximum length: 32767) or utf-16 (maximum length: 32767).
- `uint8` : Single unsigned 8-bit integer.

Concerning `bin` :
This type will directly write binary data to your `brv` file.
It is only made available for mods, and is not used by default by BRCI.

Concerning `custom` :
This will take a lambda function that will be executed and is expected to return a bytes object.
(e.g. `'CustomProperty': lambda: say_hello('world')`)
When attempting to load a custom property, it'll load it as if it was a binary property.

Here's an example on how to use `brci.append_multiple()`, as-well as setup required info.
```python
import BRCI as brci

brci.br_property_types += {'ThisNewFancyProperty': 'float'}
# Since YetAnotherNewProperty is using the BrickInput() type, we do not add it to the dict.
brci.br_property_types += {'BinaryProperty': 'bin'}
brci.br_property_types += {'CustomProperty': 'custom'}

def say_hello(name):
    text = f'Hello, {name}!'
    return brci.unsigned_int(len(text), 1) + brci.small_bin_str(text)

# Adding our new brick
brci.append_multiple(brci.br_brick_list, ['NewFancyBrick', 'MyModdedBrick'],
                     brci.br_brick_list['default_brick_data'] | {
                         'ThisNewFancyProperty': 1.0,
                         'YetAnotherNewProperty': brci.BrickInput('Custom', ['MyFunction', 'MyArgument']),
                         'BinaryProperty': b'Abcd',
                         'CustomProperty': lambda: say_hello('world')
                     }, True)
```

As you may have seen, you have a few functions to your disposition to convert to binary:
- `brci.unsigned_int(integer, byte_len)` will convert to an unsigned little endian integer of the specified byte length.
(e.g. `brci.unsigned_int(1234, 2)` will return the 16-bit unsigned integer `0x4D2`).
- `brci.signed_int(integer, byte_len)` will convert to a signed little endian integer of the specified byte length.
(e.g. `brci.signed_int(-1234, 2)` will return the 16-bit signed integer `0x2EFB`).
- `brci.bin_float(float_number, byte_len)` will convert to a little endian float of the specified byte length.
It only supports single precision (`byte_len=4`) and double precision (`byte_len=8`) floating point numbers.
(e.g. `brci.bin_float(1234.5, 4)` will return the 32-bit little endian float `0x00509A44`).
- `brci.bin_str(string)` will convert to an utf-16 string. It was only made for better readability.
- `brci.small_bin_str(string)` will convert to an utf-8 string. It was only made for better readability.
- All the previously mentioned functions in this will also have a duplicate with the `r_` prefix, standing for reverse.
(e.g. `brci.r_bin_float(brci.bin_float(1234.5, 2))` will return float `1234.5`).


## Tips
- You can use `\r\n` to create a new line. Only using `\n` will not work.
- `brci.br_brick_list` is a dict containing all bricks and their properties. You may use it to get the list of (known)
bricks. Keep in mind this dict also contains the element `'default_brick_data'`, which is not a brick.

