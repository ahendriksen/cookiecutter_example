# -*- coding: utf-8 -*-

"""Main module."""
import astra
import numpy as np

def hello_world():
    """Say hello to world.

    :returns: Nothing
    :rtype: NoneType

    """
    print("Hello world")


def default_projection_geometry():
    """Make a default projection geometry

    The returned projection geometry is a 3D cone beam geometry with
    100 angles, 100x100 pixels with a pixel spacing of 1.0mm.

    :returns: a projection geometry
    :rtype: dict

    """

    spacing = (1.0,1.0)
    shape =(100,100)
    angles = np.linspace(0, 2*np.pi, 100)
    source_distance =1
    detector_distance = 0
    return astra.create_proj_geom(
        "cone",
        *spacing,
        *shape,
        angles,
        source_distance,
        detector_distance,
    )
