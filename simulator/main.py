from .body import Body
from .simulation import Simulation
from .visualizer import Visualizer

def main():
    body1, body2 = Body(10, 10, [0, 5], (255, 0, 0)), Body(20, 5, [0, 0], (0, 0, 255))
    sim = Simulation()
    sim.add_body(body1, body2)
    vis = Visualizer(sim)
    vis.run()

if __name__ == "__main__":
    main()