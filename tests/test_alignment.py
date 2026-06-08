import pytest
from alignment.safety_overseer import SafetyOverseer

@pytest.fixture
def overseer():
    # Use dummy rules for test isolation
    o = SafetyOverseer(rules_path="config/non_existent.yaml") # Will default to empty or rely on code logic
    return o

def test_overseer_rejects_malformed_coordinates(overseer):
    dispatch = {"drone_id": 1, "target_x": "fifty", "target_y": 10.0}
    is_safe, msg = overseer.evaluate_dispatch(dispatch)
    assert not is_safe
    assert "numerical" in msg.lower()

def test_overseer_rejects_nofly_zone(overseer):
    dispatch = {"drone_id": 2, "target_x": 25.0, "target_y": 25.0} # Within 0-50 no-fly zone
    is_safe, msg = overseer.evaluate_dispatch(dispatch)
    assert not is_safe
    assert "no-fly zone" in msg.lower()

def test_overseer_allows_safe_dispatch(overseer):
    dispatch = {"drone_id": 3, "target_x": 100.0, "target_y": -100.0}
    is_safe, msg = overseer.evaluate_dispatch(dispatch)
    assert is_safe
    assert "aligned" in msg.lower()

def test_overseer_blocks_critical_priority(overseer):
    dispatch = {"drone_id": 4, "target_x": 100.0, "target_y": -100.0, "priority": "CRITICAL"}
    is_safe, msg = overseer.evaluate_dispatch(dispatch)
    assert not is_safe
    assert "manual authorization" in msg.lower()
