#
#   Python VXGUI - Pixmap - Gtk
#

from gtk import gdk
from VXGUI import export
from VXGUI.GtkPixmaps import GtkPixmap
from VXGUI.GPixmaps import Pixmap as GPixmap

class Pixmap(GtkPixmap, GPixmap):

    def __init__(self, width, height):
        GtkPixmap.__init__(self, width, height)

export(Pixmap)
