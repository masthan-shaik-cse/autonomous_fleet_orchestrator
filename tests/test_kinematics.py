import pytest
from core.kinematic_translator import KinematicTranslator

def test_kinematic_translator_initialization():
    translator = KinematicTranslator()
    assert translator.max_speed == 15.0

def test_validate_kinematics_safe():
    translator = KinematicTranslator()
    assert translator.validate_kinematics((100.0, 200.0)) == True

def test_validate_kinematics_out_of_bounds():
    translator = KinematicTranslator()
    assert translator.validate_kinematics((600.0, 0.0)) == False
    assert translator.validate_kinematics((0.0, -600.0)) == False

def test_trajectory_generation():
    translator = KinematicTranslator()
    traj = translator.generate_trajectory((0, 0), (10, 10), num_points=10)
    assert len(traj) == 10
    assert traj[0][0] == 0
    assert traj[-1][0] == 10
