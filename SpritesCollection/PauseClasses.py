import pygame


class PauseWindow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/pause_stuff/pause_window.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 267
        self.rect.y = 100


class ContinueBtn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/pause_stuff/continue_button.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 267 + 41
        self.rect.y = 100 + 84

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'continue'


class RestartBtn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/pause_stuff/restart_button.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 267 + 252
        self.rect.y = 100 + 84

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'restart'


class FromPauseToMenuBtn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/pause_stuff/menu_button.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 267 + 41
        self.rect.y = 100 + 270

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'menu'
