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
        self.v = 450
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
        self.rect.x = 150
        self.rect.y = 3


class MoneySymbol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/gameplay_stuff/money symbol.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 310
        self.rect.y = 3


class HealthGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.health = 316

        white_scale = pygame.sprite.Sprite()
        image1 = pygame.Surface([318, 45])
        image1.fill(pygame.Color("white"))
        white_scale.image = image1
        white_scale.rect = white_scale.image.get_rect()
        white_scale.rect.x = 575
        white_scale.rect.y = 5
        self.add(white_scale)

        self.pink_scale = pygame.sprite.Sprite()
        image1 = pygame.Surface([318, 45])
        image1.fill(pygame.Color(172, 90, 130))
        self.pink_scale.image = image1
        self.pink_scale.rect = self.pink_scale.image.get_rect()
        self.pink_scale.rect.x = 575
        self.pink_scale.rect.y = 5
        self.add(self.pink_scale)

        main_scale = pygame.sprite.Sprite()
        main_scale.image = pygame.image.load('data/Images/gameplay_stuff/scale_.png')
        main_scale.rect = main_scale.image.get_rect()
        main_scale.mask = pygame.mask.from_surface(main_scale.image)
        main_scale.rect.x = 510
        main_scale.rect.y = 3
        self.add(main_scale)

    def update(self, difference):
        if difference >= self.pink_scale.rect.width:
            return 'result'

        image = pygame.Surface([self.pink_scale.rect.width - difference, 45])
        image.fill(pygame.Color(172, 90, 130))
        self.pink_scale.image = image
        self.pink_scale.rect = self.pink_scale.image.get_rect()
        self.pink_scale.rect = self.pink_scale.image.get_rect()
        self.pink_scale.rect.x = 575
        self.pink_scale.rect.y = 5


class PauseBtn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Images/gameplay_stuff/pause.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 935
        self.rect.y = 585

    def update(self, sprite):
        if pygame.sprite.spritecollideany(self, sprite):
            return 'pause'


class Boom(pygame.sprite.Sprite):
    def __init__(self, cords):
        super().__init__()
        self.frames = [pygame.image.load('data/Images/gameplay_stuff/cloud/cloud' + str(i) + '.png') for i in
                       range(1, 6)]
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = cords[0]
        self.rect.y = cords[1]
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        self.image = self.frames[self.frame_counter // 3]
        if self.frame_counter >= 14:
            self.kill()
