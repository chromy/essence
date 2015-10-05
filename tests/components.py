from ecs import World, System, Component, DuplicateComponentError, NoSuchComponentError

import pytest
from fixtures import world

def test_can_add_components_to_entities(world):
    entity = world.new_entity()
    component = Component()
    assert not world.has_component(entity, Component)
    world.add_component(entity, component)
    assert world.has_component(entity, Component)
    assert world.get_component(entity, Component) is component

def test_can_remove_components(world):
    entity = world.new_entity()
    component = Component()
    world.add_component(entity, component)
    assert world.has_component(entity, Component)
    world.remove_component(entity, Component)
    assert not world.has_component(entity, Component)

def test_adding_a_duplicate_component_is_an_error(world):
    entity = world.new_entity()
    world.add_component(entity, Component())
    with pytest.raises(DuplicateComponentError):
        world.add_component(entity, Component())

def test_getting_a_non_existent_component_is_an_error(world):
    entity = world.new_entity()
    with pytest.raises(NoSuchComponentError):
        world.get_component(entity, Component)

def test_can_pass_a_default_when_getting_a_component(world):
    entity = world.new_entity()
    assert world.get_component(entity, Component, missing="foo") == "foo"
