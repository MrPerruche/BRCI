###############################################################################################################
##                                                                                                           ##
##                                                                                                           ##
##                                    Brick Rigs Creation Interface (BRCI)                                   ##
##           Take advantage of Python's dynamic nature to create and edit creations in Brick Rigs.           ##
##                                                                                                           ##
##                                          Originally authored by:                                          ##
##                                        MrPerruche (@perru_, Perru)                                        ##
##                                       Copper (@kitethelunatic, Kite)                                      ##
##                                       ANC (@absolutely_no_context)                                        ##
##                                     Infernia829 (@spectre829, Spectre)                                    ##
##                                   Erzbengel Raziel (@erzbengel_raziel)                                    ##
##                                        TLM (@tlm_gujarati) (M.I.A)                                        ##
##                                                                                                           ##
##                                                                                                           ##
##                         Rewrite authored primarily by MrPerruche (@perru_, Perru)                         ##
##                             With some help from Copper (@kitethelunatic, Kite)                            ##
##                                                                                                           ##
##                      Find BRCI's repository here: https://github.com/MrPerruche/BRCI                      ##
##                                                                                                           ##
###############################################################################################################

"""
Brick Rigs Creation Interface (BRCI)
====================================

Take advantage of Python's dynamic nature to create and edit creations in Brick Rigs.
-------------------------------------------------------------------------------------

BRCI is a package written in python that allows you to create and edit your creations though code.

This gives you quite a lot of freedom as, for example:
- Values of things can be determined at runtime depending on specific variables.
- You can edit an existing vehicle or brick and it's properties.
- You can convert objects in code to bricks in-game.

One of the most useful things BRCI can be used for is recursive tasks, say, a 10x10 grid of switches.

That would take manually placing 100 switches, or instead, take BRCI a few fractions of a second.

Usage
-----

Most functions will have docstrings, as well as BRCI having rst files and a GitHub wiki (soon:tm:).

An example of using BRCI::


  >>> import brci
  ... 
  >>> creation = brci.Creation14("my_creation",  # Name of the folder
  ...                            brci.PROJECT_FOLDER)  # Path of the folder
  ...
  >>> # Some configuration options for the creation...
  >>> creation.name = "My Creation"  # Set display name
  >>> creation.description = "My brand new creation!"
  ...
  >>> # Adding some bricks...
  >>> # Note for BRCI version C users, BRCI now natively includes a whole ton of utilities to help deal with properties!
  >>> creation.add_brick("ScalableBrick", "my_new_brick",
  ...                   properties={
  ...                       "BrickColor": brci.from_rgb(255, 0, 0, 255)
  ...                   }, position=[0, 0, 0], rotation=[0, 0, 0])
  ...
  >>> # You can also add it like this:
  >>> my_brick: brci.Brick = creation.Brick("ScalableBrick", "my_second_brick",
  ...                                       properties={
  ...                                           "BrickColor": brci.from_rgb(255, 255, 0, 255)
  ...                                       }, position=brci.pos([0.1, 0, 0], brci.Units.METER), rotation=[0, 0, 0])
  ...
  >>> creation.bricks.append(my_brick)
  ...
  >>> # Finally, we can save it and put it in our game.
  >>> creation.write_creation()
  >>> creation.write_metadata() # Name can be specified for metadata and vehicle file!
  >>> creation.write_preview(brci.BRCI_THUMBNAIL) # Note: You can specify a custom preview path. Please look at documentation/docstrings!
  >>> creation.bricks = [] # Clear all bricks from the creation, but keep the vehicle file and metadata. Good for reusing the same Creation14 object.
"""

from .src import *