#
#		Python VXGUI - Images - Generic
#

from VXGUI.Files import FileRef
from VXGUI.Resources import get_resource
from VXGUI import ImageBase

class Image(ImageBase):
    """Class Image represents an RGB or RGBA image.
    
    Constructors:
      Image(file = FileRef or pathname)
    """
    
    def from_resource(cls, name, **kwds):
        return get_resource(cls, name, **kwds)
    
    from_resource = classmethod(from_resource)
    
    def __init__(self, file):
        if isinstance(file, FileRef):
            file = file.path
        self._init_from_file(file)
