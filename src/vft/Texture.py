__author__ = 'Will'

import pygame.image


class texture:

    surface = None

    def get(self):
        return self.surface

    def load(self, filename):
        self.surface = pygame.image.load(filename)
        return

