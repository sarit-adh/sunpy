"""
The following colormaps are provided by this module.

.. plot::

    import matplotlib.pyplot as plt
    import sunpy.visualization.colormaps as cm
    cm.show_colormaps()


"""
from sunpy.visualization.colormaps.cm import *  # noqa

for cmname in cmlist.keys():  # noqa
    __doc__ += f"\n* '`~sunpy.visualisation.colormaps.{cmname}`'\n"
