# coding=utf-8
from setuptools import setup, find_packages

description = 'Dummy client/server app'

setup(
    name='dummy-app',
    version='0.0.1',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    description=description,
    long_description=description,
    url='http://github.com/karmab/dummy-app',
    author='Karim Boumedhel',
    author_email='karimboumedhel@gmail.com',
    license='ASL',
    entry_points='''
        [console_scripts]
        kdummy=dummy.main:run
    ''',
)
