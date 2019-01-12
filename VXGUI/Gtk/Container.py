#
#   Python VXGUI - Containers - Gtk version
#

from gtk import gdk
from VXGUI import export
from VXGUI.Geometry import inset_rect
from VXGUI.GContainers import Container as GContainer

class Container(GContainer):
    #  Subclasses must set the inner widget to be a Fixed or Layout
    #  widget.

    def _add(self, comp):
        GContainer._add(self, comp)
        x, y = comp._position
        self._gtk_inner_widget.put(comp._gtk_outer_widget, int(x), int(y))

    def _remove(self, comp):
        self._gtk_inner_widget.remove(comp._gtk_outer_widget)
        GContainer._remove(self, comp)

export(Container)
