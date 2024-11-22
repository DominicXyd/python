import pytest
from television import Television

@pytest.fixture
def tv():
    """Create and return a Television instance for testing."""
    return Television()

def test_initial_state(tv):
    """Test initial state of the television."""
    assert str(tv) == "Power = Off. Channel = 0. Volume = 0."

def test_power(tv):
    """Test the power method."""
    tv.power()
    assert str(tv) == "Power = On. Channel = 0. Volume = 0."
    tv.power()
    assert str(tv) == "Power = Off. Channel = 0. Volume = 0."

def test_mute(tv):
    """Test mute functionality."""
    tv.power()  # Turn the TV on
    tv.mute()
    assert str(tv) == "Power = On. Channel = 0. Volume = 0."
    tv.mute()  # Unmute
    assert str(tv) == "Power = On. Channel = 0. Volume = 0."
    tv.power()  # Turn the TV off
    tv.mute()  # Mute while off
    assert str(tv) == "Power = Off. Channel = 0. Volume = 0."

def test_channel_up(tv):
    """Test channel_up functionality."""
    tv.power()  # Turn the TV on
    tv.channel_up()
    assert str(tv) == "Power = On. Channel = 1. Volume = 0."
    for _ in range(3):  # Cycle through all channels
        tv.channel_up()
    assert str(tv) == "Power = On. Channel = 0. Volume = 0."

def test_channel_down(tv):
    """Test channel_down functionality."""
    tv.power()  # Turn the TV on
    tv.channel_down()
    assert str(tv) == "Power = On. Channel = 3. Volume = 0."
    for _ in range(3):  # Cycle through all channels
        tv.channel_down()
    assert str(tv) == "Power = On. Channel = 0. Volume = 0."

def test_volume_up(tv):
    """Test volume_up functionality."""
    tv.power()  # Turn the TV on
    tv.volume_up()
    assert str(tv) == "Power = On. Channel = 0. Volume = 1."
    tv.volume_up()  # Max volume
    assert str(tv) == "Power = On. Channel = 0. Volume = 2."
    tv.volume_up()  # No change at max volume
    assert str(tv) == "Power = On. Channel = 0. Volume = 2."

def test_volume_down(tv):
    """Test volume_down functionality."""
    tv.power()  # Turn the TV on
    tv.volume_up()  # Increase volume to max
    tv.volume_down()
    assert str(tv) == "Power = On. Channel = 0. Volume = 1."
    tv.volume_down()  # Min volume
    assert str(tv) == "Power = On. Channel = 0. Volume = 0."
    tv.volume_down()  # No change at min volume
    assert str(tv) == "Power = On. Channel = 0. Volume = 0."

