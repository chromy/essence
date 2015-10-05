from essence import World, System, Component
from fixtures import world

def xtest_there_is_a_global_world_instance():
    from essence.base import world

def test_entity_shorthand(world):
    entity = world.new_entity()
    component = Component()
    assert not entity.has(Component)
    assert entity.get(Component, None) is None
    entity.add(component)
    assert entity.has(Component)
    assert entity.get(Component) is component
    entity.remove(Component)
    assert not entity.has(Component)
    assert entity.get(Component, None) is None

