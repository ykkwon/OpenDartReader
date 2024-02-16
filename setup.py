## setup.py
from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
    name='OpenDartReader',
    version='0.1.0',
    url="https://github.com/ykkwon/OpenDartReader.git",
    packages=find_packages(include=['OpenDartReader']),
    # packages=find_packages(where='src'),
    # package_dir={'': 'src'},
    packages=['OpenDartReader'],
    # author="https://github.com/FinanceData/OpenDartReader",
    # py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    zip_safe=False,
    install_requires=['requests'],
)