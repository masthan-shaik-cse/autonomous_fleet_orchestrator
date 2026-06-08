import json
import datetime
from typing import Any, Dict

class XAITracer:
    """
    Explainable AI (XAI) Logging System.
    Captures the deterministic chain-of-thought and alignment evaluations 
    for auditability and compliance reporting.
    """
    def __init__(self, log_file: str = "xai_audit.log"):
        self.log_file = log_file

    def trace_decision(self, agent: str, input_state: Any, decision: Any, safety_passed: bool, reason: str):
        """
        Appends a structured, timestamped trace of an AI decision to the audit log.
        """
        trace = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "agent": agent,
            "input": input_state,
            "decision": decision,
            "alignment_check": {
                "passed": safety_passed,
                "reason": reason
            }
        }
        
        # In a real enterprise app, this would push to an ELK stack or Datadog
        with open(self.log_file, "a") as f:
            f.write(json.dumps(trace) + "\n")
            
        return trace
