from io import open
from setuptools import setup, find_packages
from os.path import join, dirname

# from invertedindex import __version__

__version__ = '1.0'


with open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()
    
with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read()


setup(
    # metadata
    name='invertedindex',
    version=__version__,
    url='https://github.com/lonsofore/invertedindex/',
    author='Lonsofore',
    author_email='lonsofore@yandex.ru',
    license='Apache 2.0',
    description='Inverted index service.',
    long_description=readme,
    keywords='inverted index service',

    # options
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'invertedindex = invertedindex.start:start',
            'invertedindexserver = invertedindexserver.start:start',
            'invertedindexclient = invertedindexclient.start:start',
        ],
    },
)
