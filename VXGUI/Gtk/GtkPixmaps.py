#
#   Python VXGUI - Gtk - Common pixmap code
#

from gtk import gdk
from VXGUI.StdColors import clear
from VXGUI.GtkImageScaling import gtk_scale_pixbuf
from VXGUI import Canvas

class GtkPixmap:

    def __init__(self, width, height):
        gdk_root = gdk.get_default_root_window()
        self._gdk_pixmap = gdk.Pixmap(gdk_root, width, height)
        #ctx = self._gdk_pixmap.cairo_create()
        #self._gtk_surface = ctx.get_target()

    def _gtk_set_source(self, ctx, x, y):
        ctx.set_source_pixmap(self._gdk_pixmap, x, y)
    
    def get_width(self):
        return self._gdk_pixmap.get_size()[0]

    def get_height(self):
        return self._gdk_pixmap.get_size()[1]

    def get_size(self):
        return self._gdk_pixmap.get_size()
    
    def with_canvas(self, proc):
        canvas = Canvas._from_gdk_drawable(self._gdk_pixmap)
        canvas.backcolor = clear
        proc(canvas)

