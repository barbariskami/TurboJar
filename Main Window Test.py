import pygame
import json
from pygame.sprite import Sprite, Group
from SpritesCollection.MainGameplayClasses import Jar, Background, Bomb
from SpritesCollection.MenuClasses import StartButton, InfoButton, ShopButton, MenuJar
from Functions import transform_number

data = json.loads(open('saved.json', encoding='utf8').read())

pygame.init()
size = width, height = 1000, 650
main_screen = pygame.display.set_mode(size)

running = True

all_sprites = None
background = None
jar = None
bombs = None
bomb_type = None
fon = None
start_btn = None
info_btn = None
shop_btn = None
money_sprites = None

process_mode = 'menu'


# В игре 5 режимов:
# menu
# game
# pause
# result
# info

def start_gameplay():
    global all_sprites, background, jar, process_mode, bombs, bomb_type

    process_mode = 'game'

    all_sprites = Group()

    background = Background()
    all_sprites.add(background)
    jar = Jar(1)
    all_sprites.add(jar)
    all_sprites.draw(main_screen)
    pygame.display.flip()

    bombs = Group()
    bomb_type = 'apple'


def start_menumode():
    global fon, start_btn, info_btn, shop_btn, jar, all_sprites, process_mode, money_sprites

    process_mode = 'menu'

    fon = pygame.transform.scale(pygame.image.load('data/images/menu/main_menu.png'), (width, height))
    main_screen.blit(fon, (0, 0))

    start_btn = StartButton()
    info_btn = InfoButton()
    shop_btn = ShopButton()
    jar = MenuJar()

    all_sprites = Group()
    all_sprites.add(start_btn)
    all_sprites.add(info_btn)
    all_sprites.add(shop_btn)
    all_sprites.add(jar)
    all_sprites.draw(main_screen)

    money_sprites = Group()
    transform_number(data['money'], money_sprites, (90, 20))
    money_sprites.draw(main_screen)

    high_score_sprites = Group()
    x = 1000 - 25 * (len(str(data['high score'])) + 1)
    transform_number(data['high score'], high_score_sprites, (x, 20))
    high_score_sprites.draw(main_screen)



def start_info():
    pass


clock = pygame.time.Clock()

start_menumode()

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

    elif process_mode == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_sprite = Sprite()
                click_sprite.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                click_group = Group()
                click_group.add(click_sprite)
                if start_btn.update(click_group) == 'game':
                    start_gameplay()
                elif info_btn.update(click_group) == 'info':
                    start_info()
                click_group.empty()

        pygame.display.flip()

pygame.quit()
