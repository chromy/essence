from essence import World, System, Component
from fixtures import world

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


