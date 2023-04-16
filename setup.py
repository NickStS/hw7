from setuptools import setup, find_packages

setup(
    name='clean-folder',
    version='1.0.0',
    description='A program for clean files by type',
    packages=find_packages(),
    install_requires=[
        'pathlib',
        ],
    entry_points={
        'console_scripts': [
            'clean-folder=main:main',
        ],
    },
)
