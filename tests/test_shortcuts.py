from essence import World, System, Component
from fixtures import world

def xtest_there_is_a_global_world_instance():
    from essence.base import world

def test_entity_shorthand(world):
    entity = world.create_entity()
    assert not entity.has(Component)
    assert entity.get(Component, None) is None
    component = Component()
    entity.add(component)
    assert entity.has(Component)
    assert entity.get(Component) is component
    entity.remove(Component)
    assert not entity.has(Component)
    assert entity.get(Component, None) is None
    entity.destroy()
    assert entity not in world.entities


