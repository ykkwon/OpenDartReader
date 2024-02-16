## setup.py
from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
    name='OpenDartReader',
    version='0.1',
    url="https://github.com/ykkwon/OpenDartReader.git",
    packages=find_packages(),
    # packages=find_packages(where='src'),
    # package_dir={'': 'src'},
    author="https://github.com/FinanceData/OpenDartReader"
    # py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=['requests'],
)