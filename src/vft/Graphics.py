__author__ = 'Will'

import pygame
from Color import color
from Rectangle import rectangle


class graphics:
    screen = None
    font = None

    def initialize(self):
        self.screen = pygame.display.set_mode((1024, 768), pygame.HWSURFACE | pygame.DOUBLEBUF, 32)
        self.font = pygame.font.SysFont("couriernew", 16)

    def clear(self):
        self.screen.fill((0, 0, 0))
        return


    def draw_texture(self, texture, source: rectangle, destination: rectangle):
        self.screen.blit(texture.surface.subsurface(source.X, source.Y, source.Width, source.Height),
                         pygame.Rect(destination.X, destination.Y, destination.Width, destination.Height))

        return


    def draw_string(self, text, position):
        string = self.font.render(text, True, (0, 128, 0))
        self.screen.blit(string, position)