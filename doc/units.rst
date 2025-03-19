==========================
WORKING WITH UNITS IN BRCI
==========================


**It is advised to read** ``brick_rigs.rst`` **before reading this**

TLDR;
"""""

Brick Rigs use a variety of units. For example, length is typically expressed in either centimeters (UE units),
decimeters (thirds) or meters.

-----

BRCI provides a few features to help deal with these units.

The ``brci.Units`` class store values of the length of 43 units (mostly metric and imperial) in meters, as well as the
24 metric prefixes (KILO, MEGA, GIGA,..).