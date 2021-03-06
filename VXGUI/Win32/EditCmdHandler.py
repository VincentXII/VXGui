#
#   VXGUI - Edit command handling - Win32
#

from VXGUI import export
from VXGUI.GEditCmdHandlers import EditCmdHandler as GEditCmdHandler

class EditCmdHandler(GEditCmdHandler):

    def cut_cmd(self):
        self._win.Cut()

    def copy_cmd(self):
        self._win.Copy()

    def paste_cmd(self):
        self._win.Paste()

    def clear_cmd(self):
        self._win.Clear()
    
export(EditCmdHandler)
