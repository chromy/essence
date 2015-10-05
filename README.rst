===
essence
===

.. image:: https://travis-ci.org/chromy/essence.svg
    :target: https://travis-ci.org/chromy/essence

Essence is an entity component system framework for Python.

An example::

    >>> import ecs
    >>> world = ecs.World()
    >>> alice = ecs.new_entity()
    >>> position = PositionComponent(3, 4)
    >>> alice.add(position)
    >>> print alice.get(Position)
    <PositionComponent(3, 4)>
