from setuptools import setup, find_packages

setup(
    name="nyapythonpkg",
    version="1.2.0",
    author="aayush-jha",
    description="built right now",
    packages=find_packages(),
    install_requires=[
        'pandas',
        # List dependencies, e.g., 'numpy', 'pandas'
    ],
)