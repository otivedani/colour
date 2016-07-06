#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CRT Displays RGB Primaries
==========================

Defines *CRT* displays *RGB* primaries tri-spectral power distributions.

Each *CRT* display data is in the form of a *dict* of
:class:`colour.colorimetry.spectrum.TriSpectralPowerDistribution` classes as
follows::

    {'name': TriSpectralPowerDistribution,
    ...,
    'name': TriSpectralPowerDistribution}

The following *CRT* displays are available:

-   Typical CRT Brainard 1997

See Also
--------
`Displays IPython Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/characterisation/displays.ipynb>`_

References
----------
.. [1]  Machado, G. (2010). A model for simulation of color vision deficiency
        and a color contrast enhancement technique for dichromats. Retrieved
        from http://www.lume.ufrgs.br/handle/10183/26950
"""

from __future__ import division, unicode_literals

from colour.characterisation import RGB_DisplayPrimaries
from colour.utilities import CaseInsensitiveMapping

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['CRT_DISPLAYS_RGB_PRIMARIES_DATA',
           'CRT_DISPLAYS_RGB_PRIMARIES']

CRT_DISPLAYS_RGB_PRIMARIES_DATA = {
    'Typical CRT Brainard 1997': {
        'red': {
            380.0: 0.0025,
            385.0: 0.0017,
            390.0: 0.0017,
            395.0: 0.0011,
            400.0: 0.0017,
            405.0: 0.0028,
            410.0: 0.0037,
            415.0: 0.0046,
            420.0: 0.0064,
            425.0: 0.0079,
            430.0: 0.0094,
            435.0: 0.0105,
            440.0: 0.0113,
            445.0: 0.0115,
            450.0: 0.0113,
            455.0: 0.0113,
            460.0: 0.0115,
            465.0: 0.0164,
            470.0: 0.0162,
            475.0: 0.0120,
            480.0: 0.0091,
            485.0: 0.0119,
            490.0: 0.0174,
            495.0: 0.0218,
            500.0: 0.0130,
            505.0: 0.0123,
            510.0: 0.0260,
            515.0: 0.0242,
            520.0: 0.0125,
            525.0: 0.0119,
            530.0: 0.0201,
            535.0: 0.0596,
            540.0: 0.0647,
            545.0: 0.0251,
            550.0: 0.0248,
            555.0: 0.0325,
            560.0: 0.0199,
            565.0: 0.0161,
            570.0: 0.0128,
            575.0: 0.0217,
            580.0: 0.0693,
            585.0: 0.1220,
            590.0: 0.1861,
            595.0: 0.2173,
            600.0: 0.0777,
            605.0: 0.0531,
            610.0: 0.2434,
            615.0: 0.5812,
            620.0: 0.9354,
            625.0: 1.6054,
            630.0: 0.6464,
            635.0: 0.1100,
            640.0: 0.0322,
            645.0: 0.0207,
            650.0: 0.0194,
            655.0: 0.0196,
            660.0: 0.0166,
            665.0: 0.0173,
            670.0: 0.0220,
            675.0: 0.0186,
            680.0: 0.0377,
            685.0: 0.0782,
            690.0: 0.0642,
            695.0: 0.1214,
            700.0: 0.7169,
            705.0: 1.1098,
            710.0: 0.3106,
            715.0: 0.0241,
            720.0: 0.0180,
            725.0: 0.0149,
            730.0: 0.0108,
            735.0: 0.0097,
            740.0: 0.0091,
            745.0: 0.0093,
            750.0: 0.0083,
            755.0: 0.0073,
            760.0: 0.0081,
            765.0: 0.0067,
            770.0: 0.0070,
            775.0: 0.0073,
            780.0: 0.0066},
        'green': {
            380.0: 0.0018,
            385.0: 0.0016,
            390.0: 0.0020,
            395.0: 0.0021,
            400.0: 0.0025,
            405.0: 0.0030,
            410.0: 0.0043,
            415.0: 0.0059,
            420.0: 0.0079,
            425.0: 0.0104,
            430.0: 0.0126,
            435.0: 0.0147,
            440.0: 0.0170,
            445.0: 0.0191,
            450.0: 0.0220,
            455.0: 0.0267,
            460.0: 0.0340,
            465.0: 0.0462,
            470.0: 0.0649,
            475.0: 0.0936,
            480.0: 0.1345,
            485.0: 0.1862,
            490.0: 0.2485,
            495.0: 0.3190,
            500.0: 0.3964,
            505.0: 0.4691,
            510.0: 0.5305,
            515.0: 0.5826,
            520.0: 0.6195,
            525.0: 0.6386,
            530.0: 0.6414,
            535.0: 0.6348,
            540.0: 0.6189,
            545.0: 0.5932,
            550.0: 0.5562,
            555.0: 0.5143,
            560.0: 0.4606,
            565.0: 0.3993,
            570.0: 0.3297,
            575.0: 0.2719,
            580.0: 0.2214,
            585.0: 0.1769,
            590.0: 0.1407,
            595.0: 0.1155,
            600.0: 0.0938,
            605.0: 0.0759,
            610.0: 0.0614,
            615.0: 0.0522,
            620.0: 0.0455,
            625.0: 0.0437,
            630.0: 0.0278,
            635.0: 0.0180,
            640.0: 0.0136,
            645.0: 0.0107,
            650.0: 0.0085,
            655.0: 0.0067,
            660.0: 0.0055,
            665.0: 0.0044,
            670.0: 0.0039,
            675.0: 0.0033,
            680.0: 0.0030,
            685.0: 0.0028,
            690.0: 0.0023,
            695.0: 0.0028,
            700.0: 0.0078,
            705.0: 0.0113,
            710.0: 0.0039,
            715.0: 0.0011,
            720.0: 0.0009,
            725.0: 0.0008,
            730.0: 0.0009,
            735.0: 0.0011,
            740.0: 0.0009,
            745.0: 0.0010,
            750.0: 0.0011,
            755.0: 0.0013,
            760.0: 0.0015,
            765.0: 0.0018,
            770.0: 0.0021,
            775.0: 0.0015,
            780.0: 0.0018},
        'blue': {
            380.0: 0.0219,
            385.0: 0.0336,
            390.0: 0.0524,
            395.0: 0.0785,
            400.0: 0.1130,
            405.0: 0.1624,
            410.0: 0.2312,
            415.0: 0.3214,
            420.0: 0.4263,
            425.0: 0.5365,
            430.0: 0.6296,
            435.0: 0.6994,
            440.0: 0.7470,
            445.0: 0.7654,
            450.0: 0.7519,
            455.0: 0.7151,
            460.0: 0.6619,
            465.0: 0.5955,
            470.0: 0.5177,
            475.0: 0.4327,
            480.0: 0.3507,
            485.0: 0.2849,
            490.0: 0.2278,
            495.0: 0.1809,
            500.0: 0.1408,
            505.0: 0.1084,
            510.0: 0.0855,
            515.0: 0.0676,
            520.0: 0.0537,
            525.0: 0.0422,
            530.0: 0.0341,
            535.0: 0.0284,
            540.0: 0.0238,
            545.0: 0.0197,
            550.0: 0.0165,
            555.0: 0.0143,
            560.0: 0.0119,
            565.0: 0.0099,
            570.0: 0.0079,
            575.0: 0.0065,
            580.0: 0.0057,
            585.0: 0.0051,
            590.0: 0.0047,
            595.0: 0.0043,
            600.0: 0.0029,
            605.0: 0.0023,
            610.0: 0.0036,
            615.0: 0.0061,
            620.0: 0.0088,
            625.0: 0.0141,
            630.0: 0.0060,
            635.0: 0.0015,
            640.0: 0.0008,
            645.0: 0.0006,
            650.0: 0.0006,
            655.0: 0.0007,
            660.0: 0.0006,
            665.0: 0.0005,
            670.0: 0.0006,
            675.0: 0.0005,
            680.0: 0.0007,
            685.0: 0.0010,
            690.0: 0.0010,
            695.0: 0.0016,
            700.0: 0.0060,
            705.0: 0.0094,
            710.0: 0.0030,
            715.0: 0.0007,
            720.0: 0.0009,
            725.0: 0.0008,
            730.0: 0.0011,
            735.0: 0.0010,
            740.0: 0.0010,
            745.0: 0.0012,
            750.0: 0.0013,
            755.0: 0.0012,
            760.0: 0.0016,
            765.0: 0.0015,
            770.0: 0.0028,
            775.0: 0.0046,
            780.0: 0.0058}}}

CRT_DISPLAYS_RGB_PRIMARIES = CaseInsensitiveMapping(
    {'Typical CRT Brainard 1997': RGB_DisplayPrimaries(
        'Typical CRT Brainard 1997',
        CRT_DISPLAYS_RGB_PRIMARIES_DATA.get('Typical CRT Brainard 1997'))})
"""
*CRT* displays *RGB* primaries tri-spectral power distributions.

CRT_DISPLAYS_RGB_PRIMARIES : CaseInsensitiveMapping
    {'Typical CRT Brainard 1997'}
"""
