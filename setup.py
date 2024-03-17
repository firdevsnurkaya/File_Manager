from setuptools import setup

setup(
    name='myPackage',
    version='0.1',
    author='Firdevs',
    author_email='firdevsnurkaya@gmail.com',
    description='A simple Python package attempt',
    packages=['myPackage', 'myPackage.file_manager', 'myPackage.time_utils'],
    install_requires=[],  
)


