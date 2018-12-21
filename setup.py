#-------------------------------------------------------------------------
#
#   PyGUI - Distutils Setup Script
#
#-------------------------------------------------------------------------

import os, sys
from glob import glob
from distutils.core import setup
#from distutils.extension import Extension
from distutils.sysconfig import get_python_lib
from distutils_extensions import pygui_build_py

#
#   PyPI Classifiers
#

CLASSIFIERS = """\
Development Status :: 1 - Planning
Environment :: MacOS X :: Cocoa
Environment :: Win32 (MS Windows)
Environment :: X11 Applications :: GTK
Intended Audience :: Developers
Operating System :: MacOS :: MacOS X
Operating System :: POSIX :: Linux
Operating System :: Microsoft :: Windows
Programming Language :: Python
Topic :: Software Development :: User Interfaces
""" #Programming Language :: Python :: 3

#
#   Python 3 Conversion
#

if sys.version_info >= (3,0): #automatically convert to Python 3 syntax while installing
#   #build_py_2to3 now imported in distutils_extensions
#  	try:
#  		from distutils.command.build_py import build_py_2to3 as build_py
#  	except ImportError:
#  		raise ImportError("build_py_2to3 not found in distutils - it is required for Python 3.x")
##		# exclude fixers that break already compatible code
##		from lib2to3.refactor import get_fixers_from_package
##		fixers = get_fixers_from_package('lib2to3.fixes')
##		for skip_fixer in ['import']:
##			fixers.remove('lib2to3.fixes.fix_' + skip_fixer)
##		build_py.fixer_names = fixers
    print('Installing for Python3')
#  else: # install Python 2.x version
#  	from distutils.command.build_py import build_py

#
#   Installation parameters
#

cmd_class = {'build_py': pygui_build_py}
ext_modules = []

version = '<version not found>'
version_file = os.path.join("VXGui", "Version.py") 
# get accurate version sring by running Version.py
exec(compile(open(version_file,'r').read(), version_file, 'exec'))

#
#   Find which implementation to install
#

plat = sys.platform
if plat.startswith("darwin"):
    platdir = "Cocoa"
elif plat.startswith("linux"):
    platdir = "Gtk"
elif plat.startswith("win"):
    platdir = "Win32"
else:
    sys.stderr.write(
        "Don't know which backend to install for platform '%s'.\n"
            % plat)
    sys.exit(1)
    
sys.stdout.write("Installing backend %s\n" % platdir)


#
#   Setup
#

setup(
    cmdclass = cmd_class,
    name = "VXGui",
    version = version,
    description = "Pythonic Cross-Platform GUI Framework",
    author = "Vincent Larkin",
    author_email = "vincent@vincentxii.us",
    url = "https://vxgui.vincentxii.us",
    #download_url=DOWNLOAD_URL,
    long_description = open('README.txt').read(),
    platforms = ["Linux", "MacOS X", "Windows"],
    packages = ["VXGui"],
    package_subdirs = {"VXGui": ["Generic", platdir]},
    package_data = {"VXGui": [os.path.join("Resources", "*", "*")]},
    ext_modules = ext_modules,
    maintainer='Vincent L.',
    maintainer_email='vincent@vincentxii.us',
    keywords = 'GUI Cross-Platform',
    license = 'The Vincent General License'
)
