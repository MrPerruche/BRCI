# **Brick Rigs Creation Interface Documentation**

Brick Rigs Creation Interface (a.k.a. BRCI) allows you to
create and edit (not implemented yet) creations (a.k.a. vehicles) in Brick Rigs.

## Setup


Naturally, depending on if you're working in main.py or elsewhere, you may need to import BRCI.
First things first, we must set up BRCI. To do so, we must write the following: `data = brci.BRCI()`.

Then, we must declare a few variables:
- `data.project_name` (`str`) : This corresponds to the folder's name.
- `data.project_display_name` (`str`) : This corresponds to the creation's in-game name.
- `data.project_folder_directory` (`str`) : It must be set to the path in which the creation's folder will be created.
It must already exist.

Additionally, we may declare a few more variables.
- `data.file_description` (`str` | `NoneType`) (`None`) : It corresponds to the creation's in-game description.
- `data.debug_logs` (`list[str]` | `NoneType`) (`None`): Allows you to print certain types of debug logs. Currently available types:
  - `'time'` : Prints the time it takes to generate the creation.
  - `'bricks'` : Print debug information about bricks.
- `data.user_appendix` (`bytes`) (`b''`) : This corresponds to data hidden in the .brv file you can write.
Keep in mind once saving in-game, this data will be cleared!
- `data.seat_brick` (`str` | `NoneType`) (`None`) : You must here insert what brick is the driver seat.
If set to None, all seats will have the "Random" setting selected, meaning the first seat brick rigs load will be the
driver seat.

At the end, it may look something like this:
```
# Supposing we are working in example.py
import BRCI as brci
_cwd = os.path.dirname(os.path.realpath(__file__))

# Mandatory :
data = brci.BRCI()
data.project_name = 'my_project'
data.project_display_name = 'My Project'
data.project_folder_directory = os.path.join(_cwd, 'Projects')  # To create it in the Projects folder.
data.file_description = None
# Optional :
data.debug_logs = ['time']
data.user_appendix = 'Hello World!'.encode('utf-8')
data.seat_brick = None
```

### Additional Information
For strings, you may use `\r\n` to create a new line.

## Bricks

BRCI was made to create creations though code. That's what we're here for.
Creations are made of bricks, so lets see how it works:

You will need the help of `BRICKS.md` to continue.
In this file, in the first part you may see every property in-game, and potentially some useful information about them,
such as what input they can take etc.
In the second part you will see all bricks' technical names (as BRCI don't use display names you can see in-game).
They are sorted by category (In Brick Rigs' order), then placed in the same order as in-game.
Next to them is a letter. This letter corresponds to what set of properties this brick has (see at the end of the list
for what letter corresponds to what set of properties).

### Creating and adding bricks

### `brci.create_brick()`

Alias : `brci.cb(b, pos, rot, p)`

We must first get a brick's information.
To do so, we may use the `brci.create_brick(brick, position, rotation, brick_properties)` function.
It comes with 4 arguments :
- `brick` (`str`) (Mandatory) : What brick you want to create.
- `position` (`list[float] | None`) (`None`) (Optional) :
A list of 3 floats corresponding to the brick's position IN CENTIMETERS.
None corresponds to position [0, 0, 0]. It may be changed later using `variable['Position'] = [X (cm) (f32), Y (cm) (f32), Z (cm) (f32)]`.
- `rotation` (`list[float] | None`) (`None`) (Optional) :
A list of 3 floats corresponding to the brick's rotation IN DEGREES.
None corresponds to rotation [0, 0, 0]. It may be changed later using `variable['Rotation'] = [X (deg) (f32), Y (deg) (f32), Z (deg) (f32)]`.
- `brick_properties` (`dict | None`) (`None`) (Optional) : If you wish to save lines, you can already edit some properties with this property.

It may look like this, using all arguments :

```
# Setting up BRCI is not required to use this function.

my_brick = brci.create_brick('SteeringWheel_2x2x1s', [10, 0, 120], [0, 90, 0], {'bGenerateLift': True})
```

`brci.create_brick()` will return a dictionary, containing all properties. You may edit these properties. Let's take a scalable for example:

```
# Setting up BRCI is not required to use this function.

my_brick = brci.create_brick('SteeringWheel_2x2x1s', [10, 0, 120], [0, 90, 0], {'bGenerateLift': True})
my_brick['BrickColor'] = [16, 191, 127, 231]
print(my_brick)

"""
Output (Separated into multiple lines) :
{
    'BrickColor': [16, 191, 127, 231],
    'BrickPattern': 'Default',
    'BrickMaterial': 'Plastic',
    'Position': [0.0, 0.0, 0.0],
    'Rotation': [0.0, 0.0, 0.0],
    'bGenerateLift': True,
    'gbn': 'SteeringWheel_2x2x1s'
} 
Tip : Do NOT modify 'gbn' in order to avoid any issues with invalid bricks or properties. Learn more in BRICKS.md
"""
```

### `data.add_brick()`

Alias : `data.ab(n, b)`

After creating a brick, you must add it to the list of bricks that will be generated.
To do so, you may use `data.add_brick(brick_name, brick)`.
It comes with 2 arguments:
- `brick_name` (`str | list[str]`) (Mandatory) : This corresponds to how you want to name your brick, to interact with it later.
We highly recommend you putting in the same name as your variable's name.
You may use a list of strings in order to add multiple bricks simultaneously, if other inputs are also list of their respective types.
- `brick` (`dict | list[dict]`) (Mandatory) :
You must put here the dict (which you may modify in order to use non-default values) returned by `create_brick()`.
You may use a list of strings in order to add multiple bricks simultaneously, if other inputs are also list of their respective types.


It may look like this, using all arguments:
```
# Supposing BRCI is already setup

my_brick = brci.create_brick('SteeringWheel_2x2x1s', [10, 0, 120], [0, 90, 0], {'bGenerateLift': True})
data.add_brick('my_brick', my_brick)
```

`data.add_brick()` will return self.

### `data.add_new_brick()`

Alias : `data.anb(n, t, b)`

As doing `create_brick()` then `data.add_brick()` may be too long, we decided to create this function to create a
brick in a single line
This function works just like `data.add_brick()`, except it takes a third argument, in between the 2 already established, determining what kind of brick you're creating:
- `brick_name` (`str | list[str]`) (Mandatory) : This corresponds to how you want to name your brick, to interact with it later.
We highly recommend you putting in the same name as your variable's name.
You may use a list of strings in order to create multiple bricks simultaneously, if other inputs are also list of their respective types.
- `brick_type` (`str | list[str]`) (Mandatory) : This corresponds to the type of brick you want to create.
You may use a list of strings in order to create multiple bricks simultaneously, if other inputs are also list of their respective types.
- `brick` (`dict | list[dict]`) (Mandatory) : Here you must put all non-default properties for your brick.
You may use a list of dictionaries in order to create multiple bricks simultaneously, if other inputs are also list of their respective types.

It may look something like this, using all arguments:
```
# Supposing BRCI is already setup

data.add_new_brick(['first_brick', 'second_brick'],
                   ['MathBrick_1sx1sx1s', 'Switch_1x1x1s'],
                   [{}, {'bReturnToZero: False', 'Position': [10, 0, 2.5]}])
```

`data.add_new_brick()` will return self.


### `data.update_brick()`

Alias : `data.ub(n, b)`

If you have to modify an already added brick, you may use the function `data.update_brick(brick_name, new_brick)`.
It takes 2 arguments:
- `brick_name` (`str | list[str]`) (Mandatory) : The name of the brick you want to modify.
You may use a list of strings in order to add multiple bricks simultaneously, if other inputs are also list of their respective types.
- `new_brick` (`dict | list[dict]`) (Mandatory) : The new values for the properties of the brick.
You may use a list of strings in order to create multiple bricks simultaneously, if other inputs are also list of their respective types.

It may look like this:
```
# Supposing BRCI is already setup

my_brick = brci.create_brick('Switch_1sx1sx1s')
data.add_brick('my_brick', my_brick)

my_brick['bReturnToZero'] = False
data.update_brick('my_brick', my_brick)
```

`data.update_brick()` will return self.

### `data.remove_brick()`

Alias : `data.rb(n)`

If you want to remove an already added brick, you may use the function `data.remove_brick(brick_name)`.
It takes 1 argument:
- `brick_name` (`str | list[str]`) (Mandatory) : The name of the brick you want to remove.
You may use a list of strings in order to remove multiple bricks simultaneously.

It may look like this:
```
# Supposing BRCI is already setup

my_brick = brci.create_brick('Switch_1sx1sx1s')
data.add_brick('my_brick', my_brick)

data.remove_brick('my_brick')
```

### Generating files

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

`data.debug(summary_only, write, print_bricks)` has 3 arguments:
- `summary_only` (`bool`) (`False`) (Optional) : If true, it will only get essential information on the build :
Name, Amount of bricks, etc. Otherwise, it will also print all generated bricks and debug information to help troubleshooting.
- `write` (`bool`) (`True`) (Optional) : If true, it will write everything in `debug_logs.txt`. Brick Rigs will ignore this file.
- `print_bricks` (`bool`) (`False`) (Optional) : If true, it will print all generated bricks to the console.

### `data.get_missing_gbn_keys()`
`data.get_missing_gbn_keys()` is a function that returns all missing 'gbn' keys. It is used to find a common error
when adding bricks to the brick list : leaving argument `gbn` to false whilst using `append_multiple()`. This function
has 1 argument:
- `print_missing` (`bool`) (`False`) (Optional) : If true, it will not only return all missing `gbn` keys but
also print them.

If there is no issue, `['default_brick_data']` will be returned.
Note: `'default_brick_data'` is not a brick and using it will cause an error as no `gbn` key is given to it.
Even if it had one, which would no longer cause an error with BRCI, Brick Rigs would not be able to load this brick.


### Brick Inputs

