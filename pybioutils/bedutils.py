"""
Functions used to manipulate bed files

Written by Wayne Doyle unless otherwise noted

(C) 2019 Wayne Doyle GPLv2

"""

import logging
import matplotlib.pyplot as plt
from . import helpers

# Start log
bed_log = logging.getLogger(__name__)


def venn_bed(a,
             b,
             c=None,
             colors=None,
             labels=None,
             ax=None):
    """
    Makes a proportional Venn diagram of the intersection between 2-3 bed files

    Inspired by code from github.com/daler/pybedtools/tree/master/pybedtools/scripts/venn_mpl.py

    Args:
        a (BedTool object): bed file imported into the environment by BedTool
        b (BedTool object): bed file imported into the environment by BedTool
        c (BedTool object): optional bed file imported into the environment
            if provided will make a Venn intersecting all three, if not provided Venn is for a and b
        colors (list): colors for each bed file circle
        labels (list): labels for each ed file circle
        ax (object): plot Venn on specified axis
    """
    if c is None:
        from matplotlib_venn import venn2
        if colors is None:
            colors = ['forestgreen', 'orchid']
        if labels is None:
            labels = ['a', 'b']
        helpers.check_param_num(param=colors,
                                expected=2)
        helpers.check_param_num(param=labels,
                                expected=2)
        venn2(subsets=((a - b).count(),
                       (b - a).count(),
                       (a + b).count()),
              set_labels=labels,
              set_colors=colors,
              ax=ax)

    else:
        from matplotlib_venn import venn3
        if colors is None:
            colors = ['forestgreen', 'orchid']
        if labels is None:
            labels = ['a', 'b']
        helpers.check_param_num(param=colors,
                                expected=3)
        helpers.check_param_num(param=labels,
                                expected=3)
        venn3(subsets=((a - b - c).count(),  # unique to a
                       (b - a - c).count(),  # unique to b
                       (a + b - c).count(),  # a and b, not c
                       (c - a - b).count(),  # unique to c
                       (a + c - b).count(),  # a and c, not b
                       (b + c - a).count(),  # b and c, not a
                       (a + b + c).count()),  # all
              set_labels=labels,
              set_colors=colors,
              ax=ax)
    if ax is None:
        plt.show()
