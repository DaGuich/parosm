from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call as call
import shlex
import os


class BuildPBFClasses(install):
    def run(self):
        call(' '.join(shlex.split(
            'protoc -I proto/ --python_out=./parosm/parse/ proto/fileformat.proto proto/osmformat.proto'
        )), shell=True)
        install.run(self)


if __name__ == '__main__':
    with open('README.rst', 'r') as f:
        long_description = f.read()

    setup(
        name='parosm',
        version='0.1b1',
        description='OpenStreetMap Parser',
        long_description=long_description,
        url='https://github.com/DaGuich/parosm.git',
        keywords=[
            'parser',
            'osm',
            'openstreetmap'
        ],
        license='GPL Version 3',
        classifiers=[
            'Programming Language :: Python :: 3'
        ],
        packages=find_packages(exclude=['tests']),
        entry_points={
            'console_scripts': [
                'osm2sql = parosm.prog.osm2sql.__init__:main',
                'osminfo = parosm.prog.osminfo.__init__:main'
            ]
        },
        test_suite='tests',
        python_requires='>=3.0.0',
        cmdclass={
            'install': BuildPBFClasses,
        }
    )
