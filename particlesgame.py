import pygame
import random
import sys
import time

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Particles")

particles = []
colors = [(255, 255,250), (235, 65, 54), (255, 69, 0)]


class Particle():
    def __init__(self, x, y, xvel, yvel, radius, color, gravity=None):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.radius = radius
        self.color = color
        self.gravity = gravity

    def render(self, win):
        self.x += self.xvel
        self.y += self.yvel
        if self.gravity != None:
            self.yvel += self.gravity
        self.radius -= 0.1

        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



def DrawParticles():
    for particle in particles:
        particle.render(win)
        if particle.radius <= 0:
            particles.remove(particle)



while True:
    clock.tick(60)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    for x in range(random.randint(5, 20)):
        particle = Particle(pos[0], pos[1], random.randint(-100, 0) / 10, random.randint(1, 3), random.randint(2, 5),
                            random.choice(colors))
        particles.append(particle)

    win.fill((0, 0, 0))
    DrawParticles()
    pygame.display.update()


