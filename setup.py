""" Basissets for Variational Approach for conformation dynamics (VAC)

This package provides basis sets for molecular dynamics (MD), 
and in particular protein dynamics. See [1] for a first approach in this direction.

References
----------

[1] Vitalini, F., Noe, F. and Keller, B. (2015): A basis set for peptides for the
    variational approach to conformational kinetics. (In review).

"""
from __future__ import print_function
import os
import versioneer
from setuptools import setup, Extension, find_packages
from os.path import relpath, join

DOCLINES = __doc__.split("\n")

CLASSIFIERS = """\
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: Open BSD clause 2 (OpenBSD)
Programming Language :: Python
Topic :: Scientific/Engineering :: Bio-Informatics
Topic :: Scientific/Engineering :: Chemistry
Topic :: Scientific/Engineering :: Physics
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

metadata=dict(
    name = 'basissets',
    author = 'Frank Noe, Fabian Paul and Feliks Nueske',
    author_email = 'frank.noe@fu-berlin.de',
    description = DOCLINES[0],
    long_description = "\n".join(DOCLINES[2:]),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='OpenBSD',
    url='https://github.com/markovmodel/basissets',
    platforms=['Linux', 'Mac OS-X', 'Unix', 'Windows'],
    classifiers=CLASSIFIERS.splitlines(),
    packages=find_packages(),
    package_data={'basissets':['ResiduesEigenvectors/*']
                  },
    zip_safe=False,
    install_requires=[
        'numpy',
        'scipy',
        'six',
        ],
        )

setup(**metadata)

