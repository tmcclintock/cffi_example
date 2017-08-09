"""
The setup file is where the c code will get compiled.

All of this can be copied, you just need an identical
directory structure for your project, or you can mess with
that if you want.

Many, many thanks to Mike Jarvis, who implemented this
technique for Treecorr and Coord.
https://github.com/rmjarvis/TreeCorr
https://github.com/LSSTDESC/Coord/tree/master/coord

Check out those projects to see how you can
facilitate requirements and more dependencies.
"""
from __future__ import print_function
import sys, os, glob
import setuptools
from setuptools import setup, Extension

#Create the symlink. If this is run more than once
#then it throws an error that can't be suppressed,
#hence the message below.
os.system('ln -s ../include mycffi/include')
print("If you see 'ln: failed...' ignore it. It's OK.")

#Specify the sources
sources = glob.glob(os.path.join('src','*.c'))
print('sources = ',sources)
#and the header files.
headers = glob.glob(os.path.join('include','*.h'))
print('headers = ',headers)
#Create the extension.
ext=Extension("mycffi._mycffi", sources, depends=headers, include_dirs=['include'])

#Create the distribution.
dist = setup(name="mycffi",
             author="Tom McClintock",
             author_email="tmcclintock89@gmail.com",
             description="A usage example for cffi that I couldn't fine elsewhere.",
             license="MIT License",
             url="https://github.com/tmcclintock/cffi_example",
             packages=['mycffi'],
             package_data={'mycffi' : headers },
             ext_modules=[ext])

#setup.py doesn't put the .so file in the mycffi directory, 
#so this bit makes it possible to
#import mycffi from the root directory.  
#Not really advisable, but everyone does it at some
#point, so might as well facilitate it.
build_lib = glob.glob(os.path.join('build','*','mycffi','_mycffi*.so'))
if len(build_lib) >= 1:
    lib = os.path.join('mycffi','_mycffi.so')
    if os.path.lexists(lib): os.unlink(lib)
    os.link(build_lib[0], lib)
