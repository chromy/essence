from essence import World, Entity

import pytest
from fixtures import world

def test_can_create_entity(world):
    entity = world.create_entity()
    entity.uid

def test_entities_ids_are_unique(world):
    a = world.create_entity()
    b = world.create_entity()
    assert a.uid != b.uid

def test_equilivent_entities_are_equal():
    earth = World()
    mars = World()
    alice = Entity(earth, 1)
    alice_clone = Entity(earth, 1)
    mars_alice = Entity(mars, 1)
    bob = Entity(earth, 2)
    mars_bob = Entity(mars, 2)

    # Entities are equal to themselves
    assert alice == alice
    assert bob == bob

    # Entities are equal if they have the same world and same uid
    assert alice == alice_clone

    # Entities from different worlds are never equal
    assert alice != mars_alice
    assert bob != mars_bob

    # Entities with diffrent uid's are not equal
    assert alice != bob
    assert mars_alice != mars_bob


