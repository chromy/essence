import sys
from subprocess import call
from setuptools import setup
from setuptools.command.test import test as TestCommand

class EssenceTest(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tox(self):
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        return errno

    def run_check_manifest(self):
        return call(['check-manifest'])

    def run_tests(self):
        errno = self.run_check_manifest()
        if errno != 0:
            return sys.exit(errno)
        errno = self.run_tox()
        if errno != 0:
            return sys.exit(errno)


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
        'check-manifest>=0.25',
    ],

    cmdclass = {
        'test': EssenceTest
    },

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
