import numpy as np
from scipy.interpolate import CubicSpline
try:
    from loguru import logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)

class KinematicTranslator:
    """
    Translates discrete coordinate waypoints into physically realizable, 
    time-parameterized continuous trajectories using Cubic Splines.
    """
    def __init__(self, max_speed: float = 15.0, bounds: tuple = (-500.0, 500.0, -500.0, 500.0)):
        self.max_speed = max_speed
        self.bounds = bounds # (x_min, x_max, y_min, y_max)
        
    def validate_kinematics(self, target_pose: tuple) -> bool:
        """ Ensures target does not exceed the absolute operational geofence. """
        x, y = target_pose
        x_min, x_max, y_min, y_max = self.bounds
        
        if not (x_min <= x <= x_max):
            logger.error(f"Kinematic Violation: X-coordinate {x} out of bounds.")
            return False
        if not (y_min <= y <= y_max):
            logger.error(f"Kinematic Violation: Y-coordinate {y} out of bounds.")
            return False
            
        return True
        
    def generate_trajectory(self, current_pose: tuple, target_pose: tuple, num_points: int = 50) -> np.ndarray:
        """
        Generates a smooth polynomial B-Spline trajectory to avoid sudden accelerations
        which could physically destabilize the simulated drone.
        """
        logger.info(f"Generating cubic spline trajectory from {current_pose} to {target_pose}")
        
        t = [0, 1] # Normalized time
        x = [current_pose[0], target_pose[0]]
        y = [current_pose[1], target_pose[1]]
        
        # Simple straight-line parameterization for base implementation
        cs_x = CubicSpline(t, x)
        cs_y = CubicSpline(t, y)
        
        t_new = np.linspace(0, 1, num_points)
        traj_x = cs_x(t_new)
        traj_y = cs_y(t_new)
        
        trajectory = np.vstack((traj_x, traj_y)).T
        logger.debug(f"Generated {len(trajectory)} interpolation points.")
        return trajectory
