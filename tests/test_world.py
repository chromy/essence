from essence import World, System, Component
from fixtures import world, SomeComponent, AnotherComponent

def test_remembers_entities(world):
    entities = set()
    assert set(world.entities) == entities
    entities.add(world.create_entity())
    assert set(world.entities) == entities
    entities.add(world.create_entity())
    assert set(world.entities) == entities
    entities.add(world.create_entity())
    assert set(world.entities) == entities

def test_destroyed_entities_are_forgotten(world):
    entity = world.create_entity()
    component = Component()
    entity.add(component)
    world.destroy_entitiy(entity)
    assert entity not in world.entities
    assert entity.get(Component, None) is None

def test_can_get_entities_with_component(world):
    a = world.create_entity()
    b = world.create_entity()
    c = world.create_entity()
    d = world.create_entity()
    a.add(SomeComponent())
    b.add(AnotherComponent())
    c.add(SomeComponent())
    c.add(AnotherComponent())
    assert list(world.entities_with(SomeComponent)) == [a, c]
    assert list(world.entities_with(AnotherComponent)) == [b, c]






