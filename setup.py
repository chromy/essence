from setuptools import setup

setup(
    name='essence',
    version='0.0.1',
    author='Hector Dearman',
    author_email='hector.dearman@gmail.com',
    packages=['essence'],
    scripts=[],
    url='https://github.com/chromy/essence.git',
    license='MIT',
    description='',
    long_description=open('README.rst').read(),

    install_requires=[
        'sortedcontainers',
        'total_ordering',
    ],

    tests_require = [
        'pytest',
        'tox',
    ],

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
