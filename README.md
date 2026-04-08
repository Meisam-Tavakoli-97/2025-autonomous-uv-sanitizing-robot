[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Meisam%20Tavakoli-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/meisam-tavakoli)
[![GitHub](https://img.shields.io/badge/GitHub-Meisam--Tavakoli--97-181717?style=flat&logo=github&logoColor=white)](https://github.com/Meisam-Tavakoli-97)
[![Google Scholar](https://img.shields.io/badge/Google%20Scholar-4285F4?style=flat&logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=aAzQLBoAAAAJ&hl=en)

# Autonomous UV Sanitizing Robot using ROS 2 and TurtleBot3

This repository presents a **ROS 2-based autonomous mobile robotics project** for mapping, navigation, and UV-based sanitization in indoor environments using a **TurtleBot3 Burger** in **Gazebo**.

The project was developed as part of a Master's project in Automation Engineering and integrates:

- autonomous exploration of an unknown environment,
- map generation and localization,
- goal-based navigation,
- room-wise sanitization planning,
- UV energy estimation on an occupancy grid with obstacle-aware visibility.

## Project Overview

The system addresses four main objectives:

1. Set up the TurtleBot3 Burger in Gazebo.
2. Explore an unknown indoor environment autonomously and build a map.
3. Navigate to target goals in the generated map.
4. Sanitize the environment autonomously using a UV-based energy model.

## Main Features

- **ROS 2 + Python implementation**
- **Gazebo simulation with TurtleBot3**
- **Frontier-based autonomous exploration**
- **Map generation and localization**
- **Navigation to frontier and room goals**
- **Room decomposition for sanitization**
- **UV energy distribution modeling**
- **Obstacle-aware UV propagation using Bresenham-based visibility checking**
- **Occupancy-grid visualization in RViz**
- **Demo video and result media included**

## Repository Structure

```text
2025-autonomous-uv-sanitizing-robot/
├── src/
│   ├── autonomous_exploration/
│   ├── my_robot_controller/
│   └── turtlebot3_simulations/
├── media/
├── maps/
├── docs/
└── README.md
```
Installation

This project was developed using ROS 2 and Python.

```bash
mkdir -p ~/sanitizing_ws/src
cd ~/sanitizing_ws/src
git clone <your-repository-url>
cd ..
colcon build
source install/setup.bash
```

Running the Project

A typical workflow is:

1. Launch the TurtleBot3 simulation
```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```
2. Run the autonomous exploration module
```bash
ros2 run autonomous_exploration <exploration_node>
 ```
3. Run the main robot controller / sanitization module
```bash
ros2 run my_robot_controller <controller_node>
```
5. Visualize results in RViz

Use RViz to inspect:

generated maps,
robot navigation,
UV light distribution,
sanitization coverage.

## Contact

🧑‍💻 Meisam Tavakoli

📧 meisam.tavakoli@studio.unibo.it
