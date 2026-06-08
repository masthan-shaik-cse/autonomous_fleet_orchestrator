import pytest
from src.autonomous_fleet_orchestrator.red_team.adversarial_generator import AdversarialGenerator
from src.autonomous_fleet_orchestrator.alignment.safety_overseer import SafetyOverseer

def test_automated_red_teaming_suite():
    """
    Executes the entire red-teaming adversarial payload suite against the Safety Overseer
    to mathematically guarantee zero bypasses.
    """
    generator = AdversarialGenerator()
    overseer = SafetyOverseer(rules_path="src/autonomous_fleet_orchestrator/alignment/constitutional_rules.yaml")
    
    payloads = generator.generate_suite()
    assert len(payloads) > 0, "Adversarial generator failed to construct payloads."
    
    for payload in payloads:
        is_safe, reason = overseer.evaluate_dispatch(payload)
        # We assert that every single adversarial attack is caught and marked as NOT safe.
        assert is_safe is False, f"FATAL: Safety bypass achieved using payload: {payload}"
