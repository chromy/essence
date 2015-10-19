from essence import World, System, Component, UnregisteredComponentError
from fixtures import world

import pytest

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

def test_shortcut_for_registered_components(world):
    world.register('component', Component)
    c = Component()
    e = world.create_entity()
    e.add(c)
    assert e.component == c

def test_fails_on_unregistered_components(world):
    e = world.create_entity()
    with pytest.raises(UnregisteredComponentError):
        e.component
