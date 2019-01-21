import pygame
import json
from SpritesCollection.MainGameplayClasses import Jar, Background, Bomb

data = json.loads(open('saved.json', encoding='utf8').read())

pygame.init()
size = width, height = 1000, 650
main_screen = pygame.display.set_mode(size)

running = True

process_mode = 'game'
# В игре 4 режима:
# menu
# game
# pause
# result

all_sprites = pygame.sprite.Group()

background = Background()
all_sprites.add(background)
jar = Jar(1)
all_sprites.add(jar)
all_sprites.draw(main_screen)
pygame.display.flip()

bombs = pygame.sprite.Group()

clock = pygame.time.Clock()

bomb_type = 'apple'

while running:
    if process_mode == 'game':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bombs.add(Bomb(jar.rect.y, bomb_type))
        buttons = pygame.key.get_pressed()
        buttons = [buttons[i] for i in (273, 274, 32, 304)]
        time = clock.tick() / 100
        background.update(time)
        jar.update(buttons, time)
        bombs.update(time)
        all_sprites.draw(main_screen)
        bombs.draw(main_screen)

        pygame.display.flip()
        
pygame.quit()
