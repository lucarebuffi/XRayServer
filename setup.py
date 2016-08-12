#! /usr/bin/env python3

import os

from setuptools import find_packages, setup

NAME = 'OASYS-XRayServer'
VERSION = '1.0.1'
ISRELEASED = True

DESCRIPTION = 'X-Ray Server: Sergey Stepanov\'s X-Ray Server on OASYS'
README_FILE = os.path.join(os.path.dirname(__file__), 'README.txt')
LONG_DESCRIPTION = open(README_FILE).read()
AUTHOR = 'Luca Rebuffi'
AUTHOR_EMAIL = 'luca.rebuffi@elettra.eu'
URL = 'https://github.com/lucarebuffi/XRayServer'
DOWNLOAD_URL = 'https://github.com/lucarebuffi/XRayServer'
LICENSE = 'GPLv3'

KEYWORDS = (
    'X-ray optics',
    'simulator',
    'oasys',
)

CLASSIFIERS = (
    'Development Status :: 4 - Beta',
    'Environment :: X11 Applications :: Qt',
    'Environment :: Console',
    'Environment :: Plugins',
    'Programming Language :: Python :: 3',
    'Intended Audience :: Science/Research',
)

SETUP_REQUIRES = (
    'setuptools',
)

INSTALL_REQUIRES = (
    'setuptools',
    'numpy',
    'scipy',
    'matplotlib==1.4.3',
    'srxraylib>=0.0.9',
    'orange-widget-core>=0.0.2',
    'oasys>=0.1.9',
)

PACKAGES = find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests'))

PACKAGE_DATA = {
    "orangecontrib.xrayserver.widgets.xrayserver":["icons/*.png", "icons/*.jpg", "misc/*.*"],
}

NAMESPACE_PACAKGES = ["orangecontrib", "orangecontrib.xrayserver", "orangecontrib.xrayserver.widgets"]

ENTRY_POINTS = {
    'oasys.addons' : ("xrayserver = orangecontrib.xrayserver", ),
    'oasys.widgets' : (
        "X-Ray Server = orangecontrib.xrayserver.widgets.xrayserver",
    )
}

import site, shutil, sys

if __name__ == '__main__':
    setup(
          name = NAME,
          version = VERSION,
          description = DESCRIPTION,
          long_description = LONG_DESCRIPTION,
          author = AUTHOR,
          author_email = AUTHOR_EMAIL,
          url = URL,
          download_url = DOWNLOAD_URL,
          license = LICENSE,
          keywords = KEYWORDS,
          classifiers = CLASSIFIERS,
          packages = PACKAGES,
          package_data = PACKAGE_DATA,
          setup_requires = SETUP_REQUIRES,
          install_requires = INSTALL_REQUIRES,
          entry_points = ENTRY_POINTS,
          namespace_packages=NAMESPACE_PACAKGES,
          include_package_data = True,
          zip_safe = False,
          )