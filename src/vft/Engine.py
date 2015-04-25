__author__ = 'Will'

import pygame, os, pytmx
from Graphics import graphics
from Color import color
from Texture import texture
from Rectangle import rectangle


class engine:
    gfx = graphics()
    tex = texture()
    level = None
    fps = 0

    def initialize(self):
        self.gfx.initialize()
        self.tex.load(os.path.join('data', 'newtileset.png'))
        self.tex.surface = pygame.transform.scale\
            (self.tex.surface, (self.tex.surface.get_width(), self.tex.surface.get_height()))
        self.level = pytmx.TiledMap(os.path.join('data', 'level.tmx'))
        return

    def update(self):
        return

    def render(self):
        self.gfx.clear()

        for y in range(self.level.height):
            for x in range(self.level.width):
                self.render_tile_layer(0, x, y)
                self.render_tile_layer(1, x, y)

        self.gfx.draw_string("FPS: {0}".format(int(self.fps)), (5, 5))
        return

    def render_tile_layer(self, index, x, y):
        images = self.level.get_tile_image(x, y, index)
        if images is not None:
            destination = rectangle()
            source = rectangle()
            points = images[1]
            source.set(points[0], points[1], points[2], points[3])
            destination.set(x * 16, y * 16, 16, 16)
            self.gfx.draw_texture(self.tex, source, destination)
