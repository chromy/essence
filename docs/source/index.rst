.. essence documentation master file, created by
   sphinx-quickstart on Mon Oct  5 13:43:34 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to essence's documentation!
===================================

:mod:`essence` is an Entity-Component-System for Python.


What is an Entity-Component-System?
-----------------------------------
An Entity-Component-System (or ECS) is an architectural pattern
commonly used in games. Rather than model the world as a deep class hierarchy
it instead divides the world into:

Components
    Which hold the data for particular aspect of a thing in the game world,
    for example a position or an animation or the 'Health' counter.

Entities
    Which collect a group of Components together and represent a concrete thing
    in the game world, for example the player character or an asteroid from
    asteroids.

Systems
    Which operate on a group of entities to implement a behavior, for example
    a 'PhysicsSystem' which updates the position component based on the
    velocity component and whether the entity has collided with any other
    entities.

Where to find out more about ECSs
---------------------------------
- `Wikipedia Article <https://en.wikipedia.org/wiki/Entity_component_system/>`_

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

