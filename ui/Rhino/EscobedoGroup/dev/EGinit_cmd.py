from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import scriptcontext as sc  # type: ignore

import compas_rhino


__commandname__ = "EGinit"


HERE = compas_rhino.get_document_dirname()
HOME = os.path.expanduser('~')
CWD = HERE or HOME


def RunCommand(is_interactive):

    sc.sticky["EG"] = {}
    compas_rhino.display_message("EscobedoGroup UI loaded.")


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
