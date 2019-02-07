import pygame
import random


class Hammer(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pygame.image.load('data/Images/enemies/hammer.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1000
        self.rect.y = y
        self.x = 1000
        self.v = 350
        self.health = 100
        self.collision_damage = 25
        self.missing_damage = 20
        self.money = 10
        self.bombs = 1
        self.score = 200

    def update(self, time):
        self.x -= self.v * time
        self.rect.x = int(self.x)
        if self.health <= 0:
            self.kill()


class Bird(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.frames = [pygame.image.load('data/Images/enemies/bird' + str(i) + '.png') for i in range(1, 3)]
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1000
        self.rect.y = y
        self.x = 1000
        self.y = y
        self.vx = 200
        self.vy = 200
        self.health = 100
        self.collision_damage = 20
        self.missing_damage = 15
        self.money = 30
        self.bombs = random.randrange(1, 3)
        self.score = 400

        self.frame_counter = 0

    def update(self, time):
        if 0 <= self.frame_counter <= 4:
            self.image = self.frames[0]
        else:
            self.image = self.frames[1]
        self.frame_counter += 1
        self.frame_counter %= 10

        self.x -= self.vx * time
        self.y += self.vy * time
        if self.y >= 550 or self.y <= 0:
            self.vy *= -1
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        if self.health <= 0:
            self.kill()


class Enemy:
    enemies = (Hammer, Bird)

    @staticmethod
    def generate(pos):
        return random.choice(Enemy.enemies)(pos)
