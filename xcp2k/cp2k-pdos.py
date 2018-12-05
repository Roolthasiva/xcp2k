#!/usr/bin/env python
# vim: set fileencoding=utf-8 ts=8 sw=4 tw=0 :

"""
Convert the discrete CP2K PDOS points to a smoothed curve using convoluted gaussians.

Also shifts the energies by the Fermi energy (so the Fermi energy will afterwards be at 0),
and normalizes by the number of atoms of this kind.
"""

# Copyright (c) 2017 Tiziano Müller <tiziano.mueller@chem.uzh.ch>,
# based on a Fortran tool written by Marcella Iannuzzi <marcella.iannuzzi@chem.uzh.ch>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from __future__ import print_function

import re
import argparse
import contextlib

import numpy as np


def cp2k_pdos(fpdos = None, natoms=None, sigma = 0.01, de=0.001, total_sum = False, pheader=False, output='smear.dat'):
    '''
    'fpdos':   the PDOS file generated by CP2K
    'natoms':         the total number of atoms of this kind in the structure
    'sigma':          sigma for the gaussian distribution (default: 0.02)
    'de': '-d':       integration step size (default: 0.001)
    'total-sum':      calculate and print the total sum for each orbital (default: no)
    'no-header':      do not print a header (default: print header)
    'output':         write output to specified file (default: write to standard output)
    '''
    HEADER_MATCH = re.compile(
    r'\# Projected DOS for atomic kind (?P<element>\w+) at iteration step i = \d+, E\(Fermi\) = [ \t]* (?P<Efermi>[^\t ]+) a\.u\.')
    fhandle = open(fpdos, 'r')
    header = HEADER_MATCH.match(fhandle.readline().rstrip())
    efermi = float(header.group('Efermi'))
    # header is originally: ['#', 'MO', 'Eigenvalue', '[a.u.]', 'Occupation', 's', 'py', ...]
    header = fhandle.readline().rstrip().split()[1:]  # remove the comment directly
    header[1:3] = [' '.join(header[1:3])]  # rejoin "Eigenvalue" and its unit
    data = np.loadtxt(fhandle)  # load the rest directly with numpy

    npnts, ncols = data.shape
    ncols -= 3  # ignore energy, occupation and #MO for mesh

    emin = min(data[:, 1]) - 0.2 # energies are in the second column
    emax = max(data[:, 1]) + 0.2
    nmesh = int((emax-emin)/de)+1

    # reproduce exactly the previous Fortran-based code
    xmesh = np.array([emin+i*de for i in range(1, nmesh+1)])
    ymesh = np.zeros((nmesh, ncols))

    fact = de/(sigma*np.sqrt(2.0*np.pi))
    for mpnt in range(nmesh):
        func = np.exp(-(xmesh[mpnt]-data[:, 1])**2/(2.0*sigma**2))*fact
        ymesh[mpnt, :] = func.dot(data[:, 3:])

    xmesh -= efermi  # put the Fermi energy at 0
    xmesh *= 27.211384  # convert to eV
    ymesh /= natoms  # normalize

    with smart_open(output) as fhandle:
        if pheader:
            print(("#{:>16}" + " {:>16}"*ncols).format("Energy_[eV]", *header[3:]), file=fhandle)
        for mpnt in range(nmesh):
            print(("{:16.8f}" + " {:16.8f}"*ncols).format(xmesh[mpnt], *ymesh[mpnt, :]), file=fhandle)
    return xmesh, ymesh

if __name__ == '__main__':
    pass
    cp2k_pdos(fpdos='ptoxcoy-co-ALPHA_k1-1.pdos', natoms=2, total_sum = True)
