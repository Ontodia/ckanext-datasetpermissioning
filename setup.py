#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-datasetpermissioning',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.datasetpermissioning'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        datasetpermissioning = ckanext.datasetpermissioning.plugins:DatasetPermissioning
    """
)
