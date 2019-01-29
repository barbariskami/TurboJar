import pygame


def transform_number(number, group, start_cords):
    number = str(number)
    x, y = start_cords
    for i in number:
        number_sprite = pygame.sprite.Sprite()
        number_sprite.image = pygame.image.load('data/Images/pink_numbers/' + i + '.png')
        number_sprite.mask = pygame.mask.from_surface(number_sprite.image)
        number_sprite.rect = number_sprite.image.get_rect()
        number_sprite.rect.x = x
        number_sprite.rect.y = y
        x += number_sprite.rect.width
        group.add(number_sprite)
    return x
