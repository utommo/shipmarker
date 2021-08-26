from matplotlib.path import Path
from matplotlib import transforms
from matplotlib.markers import MarkerStyle

import numpy as np

class UnsizedMarker(MarkerStyle):
    def _set_custom_marker(self, path):
        self._transform = transforms.IdentityTransform()
        self._path = path

def shipmarker(x,y,psi):
    """
        x,y location of marker
        heading with 0 degree north
    """
    ship = Path([[-1.,-2.], [1., -2.], [1., 1.1], [0., 2.], [-1., 1.1], [0.,0.]], 
                [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY,])
        
    R = transforms.Affine2D().rotate_deg(360 - np.round(psi))
    triangle2 = ship.transformed(R)
    m = UnsizedMarker(triangle2)    
    return x,y,m