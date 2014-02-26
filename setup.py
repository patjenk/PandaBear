#!/usr/bin/env python
# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
Setup script for pandabear
'''

import os
from setuptools import Command, setup

# Ensure we are in pandabear source dir
setup_dirname = os.path.dirname(__file__)
if setup_dirname != '':
    os.chdir(setup_dirname)

pandabear_version = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                 'pandabear',
                                                 'version.py')
pandabear_reqs = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                              'requirements.txt')

exec(compile(open(pandabear_version).read(), pandabear_version, 'exec'))

with open(pandabear_reqs) as f:
    lines = f.read().split('\n')
    requirements = [line for line in lines if line]


class CleanSDist(Command):
    description = "Remove traces of setup.py sdist"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import glob
        import shutil
        shutil.rmtree('dist', True)
        for eidir in glob.glob(os.path.join('pandabear', '*egg*info*')):
            shutil.rmtree(eidir, True)


setup_kwargs = {'name': 'pandabear',
                'version': __version__,
                'url': '',
                'license': 'ISC',
                'description': 'Infinitely Scalable Database',
                'author': 'Patrick Jenkins',
                'author_email': '',
                'classifiers': ['Programming Language :: Python',
                                'Programming Language :: Python :: 2.7',
                                'Development Status :: 1 - Planning',
                                'Intended Audience :: Developers',
                                'Operating System :: POSIX :: Linux',
                                ],
                'packages': ['pandabear'],
                'package_data': {},
                'data_files': [],
                'install_requires': requirements,
                'zip_safe': False,
                'cmdclass': {'clean_sdist': CleanSDist},
                }

if __name__ == '__main__':
    setup(**setup_kwargs)
