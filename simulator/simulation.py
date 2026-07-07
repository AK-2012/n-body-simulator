from .body import Body
import math


class Simulation:
    def __init__(self, gravitational_constant=100.0):
        self.bodies = [] # contains all Body objects
        self.G = gravitational_constant

    def add_body(self, body: Body):
        self.bodies.append(body)

    def remove_body(self, body: Body):
        self.bodies.remove(body)

    def _update_bodies(self, elapsed_time):
        self._reset_acceleration() # reset all Body accelerations to 0
        self._update_accelerations() # updates all Body accelerations
        self._update_motion(elapsed_time) # update velocities and positions

    def step(self, elapsed_time):
        self._update_bodies(elapsed_time)

    def clear(self):
        self.bodies.clear()
    
    def _reset_acceleration(self):
        for body in self.bodies:
            body.acceleration = [0.0, 0.0]

    def _update_motion(self):
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                body1 = self.bodies[i]
                body2 = self.bodies[j]
                difference_x = body2.position[0] - body1.position[0] # x position diff
                difference_y = body2.position[1] - body1.position[1] # y position diff
                distance = math.sqrt((difference_x)**2 + (difference_y)**2) # distance between bodies
                if distance == 0: # to prevent zero division error. may change handling later
                    continue
                direction_x = difference_x / distance # direction in the x
                direction_y = difference_y / distance # direction in the y
                force = self.G * body1.mass * body2.mass / (distance)**2 # force
                acceleration1 = force / body1.mass # acceleration for 1st body
                acceleration2 = force / body2.mass # acceleration for 2nd body
                # update accelerations here
                body1.acceleration[0] += acceleration1 * direction_x
                body1.acceleration[1] += acceleration1 * direction_y
                body2.acceleration[0] -= acceleration2 * direction_x
                body2.acceleration[1] -= acceleration2 * direction_y

    def _update_other_vectors(self, elapsed_time):
        for body in self.bodies:
            body.velocity[0] += body.acceleration[0] * elapsed_time
            body.velocity[1] += body.acceleration[1] * elapsed_time
            body.position[0] += body.velocity[0] * elapsed_time
            body.position[1] += body.velocity[1] * elapsed_time