from setuptools import find_packages
from setuptools import setup

install_requires = [
    'pyramid>=1.9',
    'PyYAML>=3.12',
    'morfdict>=0.4.6',
]

if __name__ == '__main__':
    setup(
        name='sapp',
        version='0.5.0',
        packages=find_packages(),
        install_requires=install_requires,
        license='Apache License 2.0',
    )
