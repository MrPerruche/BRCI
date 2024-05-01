# **Brick Rigs Creation Interface Documentation**

Brick Rigs Creation Interface (a.k.a. BRCI) allows you to
create and edit (not implemented yet) creations (a.k.a. vehicles) in Brick Rigs.

## Setup

First we must import BRCI.  
Here we will use `import BRCI as brci`.

Then, we must initialize BRCI, by creating an instance of the class BRCI.  
Here we will use `data = brci.BRCI()`.

Last, we must edit some variables in order to use it.

Mandatory :  
`data.project_name` (`str`) define what name is given to the file later generated.  
`data.project_folder_directory` (`str`) define where the creation will be created.

Optional :  
`data.project_display_name` (`str`) (`''`) define what name will be displayed in-game.  
`data.file_description` (`str | None`) (`None`) define what description will be displayed in-game.  
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

It has 3 mandatory arguments and 2 optional arguments :

Mandatory :

`brick_name` / `n` (`str | list[str]`) define what name you want to give your brick, in order to interact with it in various
ways such as deleting / editing it, using it as an input for some bricks, etc.  
`brick_type` / `t` (`str | list[str]`) define what type of brick you want to create.  
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

### Modifying an already implemented brick

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

### Deleting an already implemented brick

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

## Generating files

Note that if any file already exists with the same name, BRCI will crash. This will be resolved once
we will implement file editing.
BRCI give you 4 functions to generate files and get debug information:

### `data.write_preview()`

Calling this function will generate a temporary image : `Preview.png`.

### `data.write_metadata()`

Calling this function will generate metadata : `MetaData.brm`. It does NOT matter if metadata is incorrect. However,
metadata is required!

### `data.write_brv()`

Calling this function will generate the creation : `Vehicle.brv`.
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

`BrickInput()` is a custom class that is used to specify what inputs are given to a brick. Learn more in `BRICKS.md`.


## Tips
- You can use `\r\n` to create a new line. Only using `\n` will not work.
