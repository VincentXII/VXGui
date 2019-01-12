#--------------------------------------------------------------------
#
#   VXGUI - Event - Win32
#
#--------------------------------------------------------------------

from VXGUI import export
from VXGUI.GEvents import Event as GEvent

class Event(GEvent):

    def _platform_modifiers_str(self):
        return ""

export(Event)
