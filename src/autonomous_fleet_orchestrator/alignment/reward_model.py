import math
from typing import Dict, Any

class SafetyRewardModel:
    """
    Reinforcement Learning from Human Feedback (RLHF) Proxy.
    Scores trajectories based on a Bradley-Terry model distribution, 
    penalizing unsafe behavior heavily while rewarding efficiency.
    """
    def __init__(self, penalty_weight: float = -100.0, efficiency_weight: float = 1.0):
        self.penalty_weight = penalty_weight
        self.efficiency_weight = efficiency_weight

    def compute_reward(self, is_safe: bool, trajectory_length: float, optimal_length: float) -> float:
        """
        Computes a scalar reward signal for the given dispatch attempt.
        """
        if not is_safe:
            return self.penalty_weight
            
        # Reward efficiency: closer to optimal length yields higher reward
        efficiency_ratio = optimal_length / max(trajectory_length, 0.001)
        # Logarithmic smoothing
        reward = self.efficiency_weight * math.log(1 + efficiency_ratio)
        return round(reward, 4)

    def evaluate_batch(self, batch_results: list) -> float:
        """ Evaluates average reward over an epoch of operations. """
        if not batch_results:
            return 0.0
        total_reward = sum(self.compute_reward(r['safe'], r['len'], r['opt_len']) for r in batch_results)
        return total_reward / len(batch_results)
