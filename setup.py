import sys
from setuptools import setup, find_packages

name='essence'
version='0.0.1'
author='Hector Dearman'
author_email='hector.dearman@gmail.com'
url='https://github.com/chromy/essence.git'
license='MIT'
description=''
long_description=open('README.rst').read()

install_requires = [
    'sortedcontainers',
    'total_ordering',
]

tests_require = [
    'pytest',
    'tox',
    'check-manifest>=0.25',
]

extra_requires = {
    'test': tests_require,
}


setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    description=description,
    long_description=long_description,

    packages=find_packages('src'),
    package_dir={'':'src'},
    scripts=[],

    install_requires=install_requires,
    tests_require=tests_require,
    extra_requires=extra_requires,

    classifiers=[
        # Status
        'Development Status :: 3 - Alpha',

        # Audience
        'Intended Audience :: Developers',

        # License
        'License :: OSI Approved :: MIT License',

        # Python version support
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
