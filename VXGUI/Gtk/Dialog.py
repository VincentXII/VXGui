#
#   Python VXGUI - Dialogs - Gtk
#

from VXGUI import export
from VXGUI.GDialogs import Dialog as GDialog

class Dialog(GDialog):

    _default_keys = ['\r']
    _cancel_keys = ['\x1b']

export(Dialog)
