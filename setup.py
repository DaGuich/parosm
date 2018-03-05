from setuptools import setup, find_packages


with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='parosm',
    version='0.1',
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
            'osm2sql = parosm.prog.osm2sql.__init__:main'
        ]
    },
    test_suite='tests',
    python_requires='>=3.0.0'
)
