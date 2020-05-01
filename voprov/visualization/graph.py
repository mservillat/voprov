from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from prov.graph import *
from voprov.models.constants import *
from voprov.models.voprovDescriptions import *

__author__ = 'Jean-François Sornay'
__email__ = 'jean-francois.sornay@etu.umontpellier.fr'


INFERRED_ELEMENT_CLASS.update({
    VOPROV_ATTR_DESCRIPTOR: VOProvActivityDescription,
})