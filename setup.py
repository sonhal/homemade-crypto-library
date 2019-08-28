from setuptools import setup, find_packages

setup(
    name='homemade_crypto',
    version='0.0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/sonhal/homemade-crypto-library',
    license='MIT',
    author='sondre',
    author_email='',
    description='A homemade cryptography library made for educational purposes'
)
