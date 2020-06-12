import pygame

# Class for the paddle
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((255,255,255))

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0
    
    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 1400:
            self.rect.x = 1400