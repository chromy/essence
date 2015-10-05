from essence import World

import pytest

@pytest.fixture
def world():
    return World()

