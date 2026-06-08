import yaml
import logging
from typing import Dict, Any, Tuple

# Use loguru if available, fallback to logging
try:
    from loguru import logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)

class SafetyOverseer:
    """
    Constitutional AI Alignment Layer.
    Acts as a strict guardrail, evaluating the LLM Commander's outputs
    against predefined safety rules and physical bounds before allowing
    execution.
    """
    def __init__(self, rules_path: str = "alignment/constitutional_rules.yaml"):
        self.rules = self._load_rules(rules_path)
        
    def _load_rules(self, path: str) -> list:
        try:
            with open(path, 'r') as f:
                data = yaml.safe_load(f)
                return data.get('principles', [])
        except Exception as e:
            logger.warning(f"Could not load rules from {path}: {e}")
            return []

    def evaluate_dispatch(self, dispatch_command: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Evaluates the parsed JSON intent from the Commander agent.
        Returns (is_safe, reason).
        """
        drone_id = dispatch_command.get("drone_id")
        x = dispatch_command.get("target_x")
        y = dispatch_command.get("target_y")
        priority = dispatch_command.get("priority", "NORMAL")

        logger.info(f"Overseer evaluating dispatch for Drone {drone_id} to ({x}, {y})")

        # RULE 004: Type Validation
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            logger.error("[RULE_004 Violation] Malformed coordinates detected.")
            return False, "Coordinates must be numerical values."

        # RULE 001: Geofence and No-Fly Zones (Hardcoded for demo)
        # Assuming (0, 0) to (50, 50) is a hypothetical no-fly zone
        if 0 <= x <= 50 and 0 <= y <= 50:
            logger.error(f"[RULE_001 Violation] Attempted routing to restricted zone: ({x}, {y})")
            return False, "Target coordinates fall within a restricted No-Fly Zone."

        # RULE 003: Priority bounds
        if priority == "CRITICAL":
            logger.warning("[RULE_003 Violation] CRITICAL priority requires operator override.")
            return False, "CRITICAL priority dispatch rejected. Manual authorization required."

        logger.success("Alignment check passed. Dispatch is safe.")
        return True, "Dispatch aligned with safety protocols."
