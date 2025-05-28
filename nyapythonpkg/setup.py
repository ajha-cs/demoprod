import os
from setuptools import setup, find_packages

# Get the version from an environment variable, default to '0.0.1' if not set
VERSION = os.getenv('PACKAGE_VERSION', '0.0.1')

setup(
    name='nyapythonpkg',
    version=VERSION,
    author="aayush-jha",
    description="built right now",
    packages=find_packages(),
    install_requires=[
        'pandas',
        # List dependencies, e.g., 'numpy', 'pandas'
    ],
)