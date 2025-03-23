REQUIRED FOR RELEASE:
- ~~Implement all bricks (just take a look at BRCI-C:  
copy values into the right function, change inputs (see src.bricks.\_\_init\_\_ for info))~~
- ~~Finish brci.Creation14().write_creation()~~
- ~~Test all serialize / deserializes~~
- ~~Fix colors, read creation~~
- Ensure all functions affecting files work correctly on all supported OS. Improve safety
- ~~Revise some functions to add proper error mitigation. For all errors; use from e if possible~~
- List everything we will have to document in documentation
- ~~Find a convention for docstrings and apply it to all docstrings~~
- Write proper doc & readme
- Fix all TODOs
- ~~Redo main \_\_init\_\_ file to put code that's helpful and won't raise errors~~
- ~~Add brci.Creation14().write_metadata()~~
- ~~Add brci.Creation14().write_preview()~~
- ~~Add brci.Creation14().read_creation()~~ NEEDS TESTING
- ~~Add brci.Creation14().read_metadata()~~ NEEDS TESTING
- Create examples (NEEDS MORE!)
- Make unit tests

TODO:
- Add brci.Creation14().create_preview() and brci.generate_text_bitmap()
- Add function to search/mask bricks
- Add function to search in creation/project folders depending on metadata values (such as name, etc.)


# Brick Rigs Creation Interface 4 documentation

Documentation can be found in the `doc` folder. See `doc/usage.rst` first.

- `brick_rigs.rst`: Relevant technical information about Brick Rigs, its file system and Unreal Engine 4.
- `bricks.rst`: Information about brick classes.
- `bricks14.rst`: List of all bricks in the base game for file version 14 (Brick rigs 1.7 - 1.7.4).
- `color.rst`: Information on how to work with colors with Brick Rigs.
- `units.rst`: Provides information on how to easily work with Brick Rigs' various units.
- `usage.rst`: Essential concepts for BRCI usage, helping you get started and pick up best practices.