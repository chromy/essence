from essence import World, Component

import pytest

@pytest.fixture
def world():
    return World()

class SomeComponent(Component):
    pass

class AnotherComponent(Component):
    pass

