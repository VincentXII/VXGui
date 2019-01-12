#
#   Python VXGUI - Picture class - Generic
#

from VXGUI import export
from VXGUI.Properties import overridable_property
from VXGUI import View

class Picture(View):

    image = overridable_property('image', "The image to display")
    
    _image = None

    def __init__(self, image = None, file = None, **kwds):
        if file:
            from Images import Image
            image = Image(file)
        View.__init__(self, **kwds)
        if image:
            self.size = image.size
            self._image = image
    
    def get_image(self):
        return self._image
    
    def set_image(self, x):
        self._image = x
        self.invalidate()

    def draw(self, canvas, rect):
        image = self._image
        if image:
            w, h = self.size
            image.draw(canvas, image.bounds, (0, 0, w, h))

export(Picture)
