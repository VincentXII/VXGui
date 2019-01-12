#
#		Python VXGUI - Frames - Gtk
#

from gtk import Fixed
from VXGUI import export
from VXGUI.GFrames import Frame as GFrame

class Frame(GFrame):

    def __init__(self, **kwds):
        gtk_widget = Fixed()
        gtk_widget.show()
        GFrame.__init__(self, _gtk_outer = gtk_widget)

export(Frame)
