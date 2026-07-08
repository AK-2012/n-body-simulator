# N-Body Simulator
A Python implementation of an N-body gravitational simulation.

## Overview
This project is a Python implementation of an N-body gravitational simulator that models the interactions between multiple bodies using Newtonian gravity. Users can configure the number of bodies along with their initial mass, position, and velocity, then observe how the system evolves over time.

The project is being developed with an object-oriented, modular architecture to keep the physics engine, visualization, and simulation logic separate. It is currently a <mark>work in progress</mark>, with additional features and improvements being implemented as development continues.

## Features
- Simulate different numbers of bodies
- Configurable mass, position, and velocity
- Real-time visualization with Pygame
- Object-oriented, modular architecture
- Input validation

## Installation
Clone the repository:
```
git clone https://github.com/AK-2012/n-body-simulator.git
```
```
cd simulator
```

### Requirements
- Python 3
- Pygame CE

### Install dependencies
```
pip install pygame-ce
```

### Running the simulator
```
python main.py
```

## Roadmap

- [x] Project structure
- [x] `Body` class
- [x] Input validation
- [x] Unit tests
- [x] `Simulation` class as engine
- [x] Gravitational force calculations
- [ ] Real-time visualization with Pygame
- [ ] User configuration
- [ ] Performance optimizations
- [ ] Documentation improvements
