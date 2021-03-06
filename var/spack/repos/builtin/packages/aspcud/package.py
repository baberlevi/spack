# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Aspcud(CMakePackage):
    """Aspcud: Package dependency solver

       Aspcud is a solver for package dependencies. A package universe
       and a request to install, remove, or upgrade packages have to
       be encoded in the CUDF format. Such a CUDF document can then be
       passed to aspcud along with an optimization criteria to obtain
       a solution to the given package problem."""

    homepage = "https://potassco.org/aspcud"
    url      = "https://github.com/potassco/aspcud/archive/v1.9.4.tar.gz"

    version('1.9.4', '35e5c663a25912e4bdc94f168e827ed2')

    depends_on('boost', type=('build'))
    depends_on('cmake', type=('build'))
    depends_on('re2c', type=('build'))
    depends_on('clingo')

    def cmake_args(self):
        spec = self.spec
        gringo_path = join_path(spec['clingo'].prefix.bin, 'gringo')
        clasp_path = join_path(spec['clingo'].prefix.bin, 'clasp')
        args = ['-DASPCUD_GRINGO_PATH={0}'.format(gringo_path),
                '-DASPCUD_CLASP_PATH={0}'.format(clasp_path)]
        return args
