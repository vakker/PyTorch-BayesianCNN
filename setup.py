from setuptools import find_packages, setup

setup(
    name='bbb',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'torch>=1.2.0',
    ],
)
