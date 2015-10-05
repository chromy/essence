from essence import World, System, Component
from fixtures import world


def test_can_create_world():
    world = World()

def test_can_create_entity(world):
    entity = world.new_entity()
    entity.uid

def test_can_create_system():
    system = System()

def xtest_can_add_systems(world):
    system = System()

def test_entities_ids_are_unique(world):
    a = world.new_entity()
    b = world.new_entity()
    assert a.uid != b.uid



