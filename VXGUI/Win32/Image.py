#--------------------------------------------------------------------
#
#   PyGUI - Image - Win32
#
#--------------------------------------------------------------------

import GDIPlus as gdi
from VXGUI import export
from VXGUI.GImages import Image as GImage

class Image(GImage):

    def _init_from_file(self, path):
        self._win_image = gdi.Bitmap.from_file(path)

export(Image)
