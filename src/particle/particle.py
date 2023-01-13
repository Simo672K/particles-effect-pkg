import pygame
import sys
import random
import debugger


WIDTH = 1200
HEIGHT = 960
FPS= 30
class Particle:
    def __init__(self, surf, pos, color):
        self.surf= surf
        self.r = random.randint(5, 20)
        self.x= pos[0]
        self.y= pos[1]
        self.dx= random.randint(-10, 10)
        self.dy= random.randint(-10, 10)
        self.color= color

    def draw(self):
        pygame.draw.circle(self.surf, self.color, (self.x, self.y), self.r)

    def update(self):
        if self.x -self.r <= 0:
            self.dx = -self.dx
        if self.x+self.r >= WIDTH:
            self.dx = -self.dx
        if self.y-self.r <= 0:
            self.dy = -self.dy
        if self.y+self.r >= HEIGHT:
            self.dy = -self.dy

        self.x+= self.dx
        self.y+= self.dy

        self.draw()


def populate(surf, pos):
    color= (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    particles= []
    for i in range(10):
        particles.append(Particle(surf, pos, color))

    return particles

def main():
    pygame.init()

    display= pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Animation')
    fps_clock= pygame.time.Clock()
    display.fill((255, 255, 255))
    mouse_pos= (0, 0)
    particles= []
    
    while True:
        # display.fill((255, 255, 255))
        debugger.debugger("Number of particles: {}".format(str(len(particles))))
        if len(particles):
            for particle in particles:
                
                # if abs(particle.x - mouse_pos[0]) < 100 and abs(particle.y - mouse_pos[1]) < 100:
                # pygame.draw.line(display, particle.color, (particle.x, particle.y), (mouse_pos[0], mouse_pos[1]))

                # for particle2 in particles:
                #    if abs(particle.x - particle2.x) < 100 and abs(particle.y - particle2.y) < 100 and particle != particle2 :
                #        pygame.draw.line(display, particle.color, (particle.x, particle.y), (particle2.x, particle2.y))
                particle.update()
                
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN :
                particles += populate(display, mouse_pos)
            if event.type == pygame.MOUSEMOTION :
                mouse_pos= pygame.mouse.get_pos()
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock= fps_clock.tick(FPS)
        debugger.debugger("Number of particles: {}".format(str(len(particles))))
        debugger.debugger("Number of frames: {}".format(str(clock)), 10, 35)
        pygame.display.update()

if __name__ == '__main__':
    main()

    
