from setuptools import setup, find_packages


setup(
    name='lnkr',
    version='0.1',
    description="Short link creator",
    author='Jacob Cook',
    author_email='jacob@peakwinter.net',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['lnkr = lnkr.commands:main'],
    }
)
