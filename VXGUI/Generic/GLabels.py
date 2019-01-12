#
#   Python VXGUI - Labels - Generic
#

from VXGUI.Properties import overridable_property
from VXGUI import Control

class Label(Control):
    """A piece of static text for labelling items in a window."""
    
    _default_tab_stop = False
    
    text = overridable_property('text')
    
