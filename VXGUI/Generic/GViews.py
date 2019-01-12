#
#		Python VXGUI - Views - Generic
#

from VXGUI.Properties import overridable_property
from VXGUI.Geometry import add_pt, sub_pt, rect_sized
from VXGUI import DrawableContainer

class View(DrawableContainer):
    """A View is a 2D drawing area having its own coordinate
    system and clipping area."""

    _default_size = (100, 100)

