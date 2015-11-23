from __future__ import absolute_import

__version__  = '0.1.2'   #(2015.06.22)

from . import data, distributions, geom, prob, random

randn1d      = random.randn1d
multirandn1d = random.multirandn1d

chi2         = distributions.chi2
f            = distributions.f
norm         = distributions.norm
t            = distributions.t
T2           = distributions.T2
