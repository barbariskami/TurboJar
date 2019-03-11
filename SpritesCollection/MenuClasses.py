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
        self.rect.y = 315

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
        self.rect.y = 545


class MenuJar(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/fon_jar.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 40
        self.rect.y = 330


class NameChangeButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/name_button.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1000 - 40
        self.rect.y = 2

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'changeName'
        else:
            return 'menu'


class Info_to_menu_btn(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/images/info_stuff/menu_button.png')
        self.rect = self.image.get_rect()
        self.rect.x = 680
        self.rect.y = 470

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'menu'
        else:
            return 'info'


class NameWindow(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/images/menu/change_name_window.png')
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 100


class NameCloseButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/change_name_close.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 740
        self.rect.y = 102

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'close'


class NameOkButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/change_name_ok.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 460
        self.rect.y = 356

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'ok'


class RatingButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/rating_button.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 1000 - 88
        self.rect.y = 435

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'rating'
        else:
            return 'menu'


class RatingWindow(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/info_stuff/rating_window.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 50


class RatingCloseButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/info_stuff/rating_close.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 740
        self.rect.y = 55

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'menu'


class SandButton(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/menu/save_button.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1000 - 69
        self.rect.y = 42

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'save'
