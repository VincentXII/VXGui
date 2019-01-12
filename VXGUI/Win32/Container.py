#--------------------------------------------------------------------
#
#   PyGUI - Container - Win32
#
#--------------------------------------------------------------------

import win32con as wc
from win32api import HIWORD, LOWORD
from VXGUI import export
from VXGUI.Geometry import add_pt, sub_pt
from VXGUI.WinUtils import WinMessageReflector
from VXGUI.GContainers import Container as GContainer

class Container(GContainer, WinMessageReflector):

    def get_content_size(self):
        return sub_pt(self.size, self._win_content_size_adjustment())
    
    def set_content_size(self, size):
        self.size = add_pt(size, self._win_content_size_adjustment())

    def _win_content_size_adjustment(self):
        win = self._win
        wl, wt, wr, wb = win.GetWindowRect()
        cl, ct, cr, cb = win.GetClientRect()
        return ((wr - wl) - (cr - cl), (wb - wt) - (cb - ct))

export(Container)

