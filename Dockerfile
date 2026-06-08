FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . /app

# Set Python path to ensure module resolution
ENV PYTHONPATH=/app/src

# Command to run the orchestrator
CMD ["python", "-m", "autonomous_fleet_orchestrator.agent.fleet_commander"]
