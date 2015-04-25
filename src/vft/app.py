__author__ = 'Will'
import pygame
from Engine import engine


class app:
    def run(self):
        eng = engine()
        pygame.init()
        done = False
        eng.initialize()
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            eng.update()
            eng.render()

            pygame.display.flip()
            clock.tick(60)
            eng.fps = clock.get_fps()

if __name__ == '__main__':
    app = app()
    app.run()