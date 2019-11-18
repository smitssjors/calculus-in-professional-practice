from setuptools import setup, find_packages

setup(
    name='cpp',
    packages=find_packages(),
    extras_require={
        'dev': ['PyQt5==5.13.2', 'numpy==1.17.4', 'matplotlib==3.1.1', 'graphviz==0.13.2'],
        'test': ['pytest==5.2.2']
    })
