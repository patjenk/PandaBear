# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
pandabear.version
===============

Get version of pandabear
'''

from distutils.version import StrictVersion
__version__ = str(StrictVersion('0.0b0'))
del StrictVersion

if __name__ == '__main__':
    print(__version__)
