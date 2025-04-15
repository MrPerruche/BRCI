from .bricks14 import *
from .bricks15 import *

# Input channels:
# InputChannel.InputAxis     -> BrickInput(<this>, ...)
# InputChannel.Value         -> BrickInput('AlwaysOn', <this (int / float)>)
# InputChannel.SourceBricks  -> BrickInput('Custom'/'Taillight'/..., <this (list[brick_id]>)
