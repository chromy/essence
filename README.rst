=======
essence
=======

.. image:: https://readthedocs.org/projects/essence/badge/?version=latest
    :target: http://essence.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://travis-ci.org/chromy/essence.svg
    :target: https://travis-ci.org/chromy/essence
.. image:: https://img.shields.io/pypi/v/essence.svg
    :target: https://crate.io/packages/essence/
    :alt: Latest PyPI version
.. image:: https://img.shields.io/pypi/dm/essence.svg
    :target: https://crate.io/packages/essence/
    :alt: Number of PyPI downloads
.. image:: https://img.shields.io/pypi/pyversions/essence.svg
    :target: https://crate.io/packages/essence/
    :alt: Supported Python Versions

Essence is an 'entity, component, system' framework for Python.

An example

.. code-block:: python

    >>> import essence
    >>> world = essence.World()
    >>> alice = essence.new_entity()
    >>> position = PositionComponent(3, 4)
    >>> alice.add(position)
    >>> print alice.get(Position)
    <PositionComponent(3, 4)>


Tests
-----

You can use :code:`py.test` to run the tests for just the current Python
environment or :code:`tox` to perform more comprehensive testing.
