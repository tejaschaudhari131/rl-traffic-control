# Reinforcement Learning-Based Traffic Control System

## Overview

This project aims to optimize city traffic flow using reinforcement learning (RL) and computer vision techniques. The RL model is trained to reduce congestion by adjusting traffic signals dynamically, achieving up to 50% faster traffic flow in simulated environments.

## Features

- **Reinforcement Learning**:
  - AI-based model trained using traffic simulation data.
  - Real-time decision-making to optimize traffic lights.

- **Computer Vision**:
  - Integration with cameras to monitor real-time traffic conditions.
  - Object detection for vehicle and pedestrian tracking.

- **Hardware Integration**:
  - Deployed on Raspberry Pi and Arduino for edge computing.
  - Simulated with SUMO (Simulation of Urban MObility).

## Technology Stack

- **Programming**: Python, C++
- **AI/ML**: TensorFlow, OpenCV
- **Hardware**: Raspberry Pi, Arduino
- **Simulation**: SUMO

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tejaschaudhari131/rl-traffic-control.git
Set up the environment:

bash
Copy code
pip install -r requirements.txt
Prepare the hardware:

Flash the Arduino with the provided firmware (arduino/traffic_control.ino).
Set up the Raspberry Pi with the necessary Python scripts.
Run the simulation:

Start the SUMO simulation using the provided configuration files.
Execute the RL model to control traffic lights.
Usage
Simulation: Use SUMO to simulate traffic and test the RL model's effectiveness.
Deployment: Deploy the system on real-world hardware for testing.
Contributing
Contributions are welcome, especially in areas like model improvement, hardware integration, and expanding the simulation scenarios.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries, please contact:

Tejaram Chaudhari: tejaschaudhari131@gmail.com
