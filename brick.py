import pygame

# Class for the bricks
class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((255,255,255))

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()