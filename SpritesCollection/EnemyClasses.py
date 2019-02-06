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
        self.v = 340
        self.health = 100
        self.collision_damage = 25
        self.missing_damage = 20
        self.money = 10
        self.bombs = 1
        self.score = 300

    def update(self, time):
        self.x -= self.v * time
        self.rect.x = int(self.x)
        if self.health <= 0:
            self.kill()


class Bird(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pygame.image.load('data/Images/enemies/hammer.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1000
        self.rect.y = y
        self.x = 1000
        self.y = y
        self.vx = 200
        self.vy = 250
        self.health = 300
        self.collision_damage = 20
        self.missing_damage = 15
        self.money = 30
        self.bombs = 2
        self.score = 300

    def update(self, time):
        self.x -= self.vx * time
        self.y += self.vy * time
        if self.y >= 550 or self.y <= 0:
            self.vy *= -1
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        if self.health <= 0:
            self.kill()


class Enemy:
    enemies = (Hammer,)

    @staticmethod
    def generate(pos):
        return random.choice(Enemy.enemies)(pos)
