print("seronimo engine beta 0.1.0")
import pygame as pygame
import sys

print("Hello from DCS https://danger-cow-studios.glitch.me/")


def key_down(key):
    keys = pygame.key.get_pressed()
    statement = "keys[pygame." + key + "]"

    if eval(statement):
        return True
    else:
        return False


class Window(object):
    def __init__(self, name, resolution, color):
        self.window = pygame.display.set_mode(resolution)
        self.color = color

        self.window.fill(color)
        pygame.display.flip()
        pygame.display.set_caption(name)

    def circle(self, color, pos, radius):
        pygame.draw.circle(self.window, color, pos, radius)

    def rect(self, color, rect):
        pygame.draw.rect(self.window, color, rect)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

    def fill(self):
        self.window.fill(self.color)
