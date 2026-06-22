# Object-Oriented Programming (OOP) in Python
class Particle(object):
    def __init__(self):
        self.mass = 1.0
        

class FreeFallParticle(Particle):
    def __init__(self, height, dt=0.1):
        super().__init__()
        self.height = height
        self.velocity = 0.0
        self.time = 0.0
        self.dt = dt
        self.g = -9.8

    def get_num_steps(self):
        num_steps = int(self.time/self.dt)
        return num_steps
    
    def simulate_timestep(self):
        self.time += self.dt
        self.velocity += self.g * self.dt
        self.height += self.velocity * self.dt
        
        return self.height, self.velocity, self.time
    
ball = FreeFallParticle(height=10)
print(ball.time, ball.height)
while ball.height >= 0:
    ball.simulate_timestep()
print(ball.time, ball.height)