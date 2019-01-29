import pygame


class Jar(pygame.sprite.Sprite):
    def __init__(self, jar_number):
        super().__init__()
        self.frames = [pygame.image.load('data/Images/jars/jar' + str(jar_number)
                                         + '/' + str(i) + '.png') for i in range(1, 3)]
        self.frame_counter = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 300
        self.yy = 300
        self.v = 400

    def update(self, buttons_state, seconds):
        if 0 <= self.frame_counter <= 2:
            self.image = self.frames[0]
        else:
            self.image = self.frames[1]
        self.frame_counter += 1
        self.frame_counter %= 6

        if buttons_state[0] == 1:
            self.yy -= self.v * seconds if self.rect.y >= 80 else 0
            self.rect.y = int(self.yy)
        if buttons_state[1] == 1:
            self.yy += self.v * seconds if self.rect.y <= 500 else 0
            self.rect.y = int(self.yy)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/background.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0
        self.v = 400
        self.xx = 0

    def update(self, seconds):
        self.xx -= seconds * self.v
        self.rect.x = int(self.xx) % (-1000)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, jar_y, type):
        super().__init__()
        self.image = pygame.image.load('data/Images/bombs/' + type + '.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 100
        self.rect.y = jar_y + 40
        self.v = 500
        self.xx = 100

    def update(self, seconds):
        self.xx += seconds * self.v
        self.rect.x = int(self.xx)


class BombSymbol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/gameplay_stuff/apple symbol.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 140
        self.rect.y = 3


class MoneySymbol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/gameplay_stuff/money symbol.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 300
        self.rect.y = 3

