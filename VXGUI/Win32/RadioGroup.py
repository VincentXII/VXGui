#--------------------------------------------------------------------
#
#   VXGUI - RadioGroup - Win32
#
#--------------------------------------------------------------------

from VXGUI import export
from VXGUI.GRadioGroups import RadioGroup as GRadioGroup

class RadioGroup(GRadioGroup):

    def _item_added(self, item):
        item._win_update()
    
    def _item_removed(self, item):
        item._win_update()
    
    def _value_changed(self):
        for item in self._items:
            item._win_update()

export(RadioGroup)
