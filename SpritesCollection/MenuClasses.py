import pygame
from pygame.sprite import Sprite


class StartButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/play_button.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 280
        self.rect.y = 375

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'game'
        else:
            return 'menu'


class InfoButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/info_button.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1000 - 95
        self.rect.y = 405

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'info'
        else:
            return 'menu'


class ShopButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/shop_button.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1000 - 114
        self.rect.y = 535


class MenuJar(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/fon_jar.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 40
        self.rect.y = 330
