import pygame
import json
from pygame.sprite import Sprite, Group
from SpritesCollection.MainGameplayClasses import Jar, Background, Bomb, BombSymbol, MoneySymbol
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
gameplay_score_counter = None
gameplay_bombs_counter = None
gameplay_money_counter = None
gameplay_score = None
gameplay_bombs_number = None
gameplay_bomb_symbol = None
gameplay_money = None
gameplay_money_symbol = None
gameplay_health = None

process_mode = 'menu'


# В игре 5 режимов:
# menu
# game
# pause
# result
# info

def start_gameplay():
    global all_sprites, background, jar, process_mode, bombs, bomb_type
    global gameplay_score_counter, gameplay_bombs_counter, gameplay_money_counter, gameplay_health_group
    global gameplay_score, gameplay_bombs_number, gameplay_bomb_symbol, gameplay_money
    global gameplay_money_symbol, gameplay_health

    process_mode = 'game'

    all_sprites = Group()

    background = Background()
    all_sprites.add(background)
    jar = Jar(1)
    all_sprites.add(jar)

    bombs = Group()
    bomb_type = 'apple'

    gameplay_score = 0
    gameplay_score_counter = Group()
    transform_number(gameplay_score, gameplay_score_counter, (3, 3))
    gameplay_score_counter.draw(main_screen)

    gameplay_bombs_number = 25
    gameplay_bomb_symbol = BombSymbol()
    all_sprites.add(gameplay_bomb_symbol)
    gameplay_bombs_counter = Group()
    transform_number(gameplay_bombs_number, gameplay_bombs_counter, (200, 3))
    gameplay_bombs_counter.draw(main_screen)

    gameplay_money = 0
    gameplay_money_symbol = MoneySymbol()
    all_sprites.add(gameplay_money_symbol)
    gameplay_money_counter = Group()
    transform_number(gameplay_money, gameplay_money_counter, (360, 3))
    gameplay_score_counter.draw(main_screen)

    gameplay_health = Group()

    all_sprites.draw(main_screen)
    pygame.display.flip()


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

    money_sprites = Group()
    transform_number(data['money'], money_sprites, (90, 20))
    money_sprites.draw(main_screen)

    high_score_sprites = Group()
    x = 1000 - 25 * (len(str(data['high score'])) + 1)
    transform_number(data['high score'], high_score_sprites, (x, 20))
    high_score_sprites.draw(main_screen)

    high_score = Sprite()
    high_score.image = pygame.image.load('data/Images/menu/high_score.png')
    high_score.mask = pygame.mask.from_surface(high_score.image)
    high_score.rect = high_score.image.get_rect()
    high_score.mask = pygame.mask.from_surface(high_score.image)
    high_score.rect.x = 760 - 25 * (len(str(data['high score'])) - 1)
    high_score.rect.y = 20
    all_sprites.add(high_score)
    all_sprites.draw(main_screen)


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
                if event.key == pygame.K_SPACE and gameplay_bombs_number > 0:
                    bombs.add(Bomb(jar.rect.y, bomb_type))
                    gameplay_bombs_number -= 1
                    gameplay_bombs_counter.empty()
                    transform_number(gameplay_bombs_number, gameplay_bombs_counter, (200, 3))
        buttons = pygame.key.get_pressed()
        buttons = [buttons[i] for i in (273, 274, 32, 304)]
        time = clock.tick() / 1000
        background.update(time)
        jar.update(buttons, time)
        bombs.update(time)
        all_sprites.draw(main_screen)
        bombs.draw(main_screen)

        gameplay_score += time * 300
        gameplay_score_counter.empty()
        transform_number(int(gameplay_score), gameplay_score_counter, (3, 3))
        gameplay_score_counter.draw(main_screen)

        gameplay_bombs_counter.draw(main_screen)

        gameplay_money_counter.draw(main_screen)

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
