# **Brick Rigs API Documentation**

Brick Rigs API is an API which allows you to create or edit creations (also known as vehicles) in Brick Rigs.

Our first step is to create a variable with the WriteData class,
which will allow us to, among other, convert our code to a creation. To do this, write the following:  
`data = BRAPI()`  
Then we will assign it a few necessary values :  
    - `data.project_folder_directory` : The folder `(str)`  
    - `data.project_name` : Creation's folder name `(str)`  
    - `data.project_display_name` : Creation's in-game name `(str)`  
    - `data.file_description` : Creation's in-game description `(str)`

We'll soon cover how to create and edit bricks. For now,
to initialize it, write the following :  
`my_brick = create_brick('Switch_1sx1sx1s')`

## Adding new bricks

To add new bricks with BR-API, you must use the following function:  
`data.add_brick(brick_name, new_brick)`  
    - `brick_name` correspond to the brick's name. Here `'my_brick'`. It indicates the program what name you want to
give this brick. It's used to edit and remove bricks, as well as handle inputs etc.  
    - `new_brick` correspond to the current brick. Here `my_brick`. It's input must be of the Brick class.
It's here to give the program all info necessary to add this new brick.  
    - `data` corresponds to the variable we established earlier, which is set to the WriteData() class.  
```
# Exemple : Adding bricks

# Handle BR Files
data = BRAPI(project_folder_directory='D:\Exemples',
             project_name='adding bricks', 
             project_display_name='Adding Bricks Tutorial',
             file_description='...')
                 
# Create our first brick
my_brick = create_brick('Switch_1sx1sx1s')
# Add my_brick as 'original_name' brick
data.add_brick('original_name', my_brick)
```

## Updating bricks

To edit currently existing bricks with BR-API, it works just like with adding new bricks, except that instead
it uses the function `data.update_brick(brick_name, new_brick)`. It'll replace the brick indicated by `brick_name` with
`new_brick` in `data`. It'll however conserve the old name.
```
# Exemple : Updating bricks

# Handle BR Files
data = BRAPI(project_folder_directory='D:\Exemples',
             project_name='updating bricks', 
             project_display_name='Updating Bricks Tutorial',
             file_description='...')
                 
# Create and add our first brick
my_brick = create_brick('Switch_1x1x1s')
data.add_brick('original_name', my_brick)

# Create a new variable for a brick with different properties
my_updated_brick = my_brick
my_updated_brick['SwitchName'] = 'Hello World!'

# Update 'original_name' brick, to no longer be my_brick but my_updated_brick
# Note : you don't have to declare a new variable or have a different name.
data.update_brick('original_name', my_updated_brick)
```

## Removing bricks

To remove any currently existing bricks with BR-API, you must use the function
`data.remove_brick(brick_name)`  
This function will remove the brick with the name defined by `brick_name` from `data`
```
# Exemple : Removing bricks

# Handle BR Files
data = BRAPI(project_folder_directory='D:\Exemples',
             project_name='removing bricks', 
             project_display_name='Remove Bricks Tutorial',
             file_description='...')
                 
# Create and add our first brick
my_brick = create_brick('Switch_1sx1sx1s')
data.add_brick('original_name', my_brick)

# Remove 'original_name' brick
data.remove_brick('original_name')
```

## Writing files

### Preview.png

To write `Preview.png` files, you can use the following function :  
`data.write_preview()`

### Metadata.brm

To write `Metadata.brm` files, you can use the following function :  
`data.write_metadata()`

Note : You can use `\n` to create a new line.

### Vehicle.brv

To write `Vehicle.brv` files, you can use the following function :
`data.write_brv()`

### Exemple

```
# Example : Creating a creation

# Handle BR Files
data = BRAPI(project_folder_directory='D:\Exemples',
             project_name='creating a creation', 
             project_display_name='Creating A Creation Tutorial',
             file_description='...')
                 
# Adding a brick for the program to generate
my_brick = create_brick('Switch_1sx1sx1s')
my_brick['bReturnToZero'] = False
data.add_brick('my_brick', my_brick)

# Creating the creation
data.write_preview()
data.write_metadata()
data.write_brv()
```

## Bricks

Bricks and properties use the name given to them by the BRV file,
not the display name.

### Creating a brick

To create a brick, you may use the function `create_brick(brick)`.

`brick` (`str`): Indicate which brick you are creating.

```
# Exemple :

my_brick = create_brick('Switch_1sx1sx1s')  # 'Switch_1sx1sx1s' corresponds to a small switch.
```

### Editing a brick

Brick info is stored as a dictionary. You can edit the dictionary directly.

```
# Exemple :

my_brick = create_brick('Switch_1sx1sx1s')
my_brick['OutputChannel.MinIn'] = 0
```

### Main settings

This sections contains settings common to all bricks.

`gbn` (`str`): This indicates the program which brick you're using.
It is set to the first argument, it is set by the function create_brick()  
Avoid changing `gbn`. 'gbn' stands for 'Game Brick Name'.

`BrickColor` (list `[int, int, int, int]`): You can use this to change the bricks' color.
Elements in the list correspond to (in order) `[HUE, VALUE, SATURATION, ALPHA]`.
Integers must range between 0 and 255.

`BrickPattern` (`str`): You can use this to change the bricks' pattern.

`BrickMaterial` (`str`): You can use this to change the bricks' material.

`Position` (list `[float, float, float]`): You can use this to change the bricks' position.
(Same order as in Brick Rigs)

`Rotation` (list `[float, float, float]`): You can use this to change the bricks' rotation.
(Same order as in Brick Rigs)

### Common settings

This section contains all frequently occurring settings for bricks.

`bGenerateLift` (`bool`): Toggle fluid dynamics.

TODO


### Modded bricks

Some bricks (modded or recently added bricks) may not be available in the brick list
(accessible in the br_brick_list variable).

If you're already using the latest version of BR-API,
you may use `append_multiple(var, keys, value, gbn)` function to add them to your list of bricks:

`var` : Set it to `br_brick_list`.

`keys` : Set it to the list of bricks you want to be created with these potential properties.

`value` : Set it to `br_brick_list['default_brick_data'] | {...}`,
replace `{...}` with the potential properties list.

`gbn` : Set it to `True`.


```
# Exemple : Adding a new brick to the brick list
# Warning : This part is still under active development and is guarenteed to change as it contains several flaws.

append_multiple(br_brick_list, ['ModdedBrick1', 'ModdedBrick2'],
                br_brick_list['default_brick_data'] | {
                    'bGenerateLift': True,
                    'ConnectorSpacing': signed_sub_byte_int([3, 3, 2, 3, 0, 0], 6, 2)}, True)  # Subject to changes.
```