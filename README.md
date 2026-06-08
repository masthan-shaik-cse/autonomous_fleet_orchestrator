# Multi-Agent LLM Orchestration for Autonomous Fleet Management

A centralized language-driven agent system designed to manage a fleet of simulated autonomous delivery drones.

## Core Innovations
- **LLM Fleet Commander (`agent/fleet_commander.py`)**: Parses natural language dispatch requests (e.g., "Send drone 2 to sector 7") using few-shot prompting.
- **ROS2 Tool-former Interface (`ros2_interface/action_server_bridge.py`)**: Allows the language model to execute function calls that translate directly into ROS2 Action Server goals.
- **Kinematic Constraints (`core/kinematic_translator.py`)**: Ensures that LLM hallucinatory outputs do not violate physical drone kinematic boundaries or geo-fences.

## Execution Flow
1. Operator types natural language command.
2. `FleetCommanderLLM` extracts intent and target coordinates.
3. `KinematicTranslator` validates safety.
4. `ROS2ActionServerBridge` dispatches the goal to the simulated drone in Gazebo/MuJoCo.
