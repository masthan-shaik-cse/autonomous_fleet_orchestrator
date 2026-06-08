# Autonomous Fleet Orchestrator 🚁 🧠

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Alignment: Constitutional AI](https://img.shields.io/badge/Alignment-Constitutional_AI-green.svg)](#)

An enterprise-grade, Multi-Agent LLM Orchestration system designed for the secure and aligned management of simulated autonomous delivery drones. 

Built with **AI Alignment** at its core, this system guarantees that large language models operating in physical-world abstractions adhere strictly to predefined kinematic and ethical safety bounds.

## 🌟 Core Architecture

### 1. 🛡️ Constitutional AI & Safety Overseer (`alignment/`)
A dedicated Guardrail Agent validates every natural language dispatch request before execution. 
- Prevents prompt-injection attacks aiming to override physical constraints.
- Dynamically enforces geofenced No-Fly Zones.
- Enforces strict human-in-the-loop overrides for "CRITICAL" priority requests.

### 2. 🧠 LLM Fleet Commander (`agent/fleet_commander.py`)
Parses complex natural language dispatch requests using Few-Shot Chain-of-Thought prompting methodologies. Outputs are strictly validated using **Pydantic** to ensure perfect structural alignment with robotic systems.

### 3. ⚙️ Advanced Kinematics (`core/kinematic_translator.py`)
Utilizes NumPy and SciPy to translate discrete coordinate waypoints into continuous, physically realizable **Cubic Spline Trajectories**, ensuring simulated drones do not violate acceleration or velocity thresholds.

### 4. 🚀 ROS2 Action Server Bridge (`ros2_interface/action_server_bridge.py`)
Asynchronous `rclpy` node abstraction that allows the LLM to directly interface with the ROS2 navigation stack via Tool-former methodologies.

## 🚀 Quickstart

### Docker (Recommended)
Deploy the entire orchestration suite and mock ROS2 nodes using Docker Compose:
```bash
docker-compose up --build
```

### Local Development
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
pytest tests/
```

## 🧪 Testing & Validation
The system features comprehensive Pytest coverage specifically validating the `SafetyOverseer` boundary logic and `KinematicTranslator` spline math.

```bash
pytest -v
```

## 🔒 Alignment Philosophy
As LLMs move from text generation to physical actuation, **Alignment** is the critical bottleneck. This project serves as a proving ground for embedding verifiable safety bounds into opaque LLM decision-making loops.
