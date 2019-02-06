import pygame
import json
import random
from pygame.sprite import Sprite, Group
from SpritesCollection.MainGameplayClasses import Jar, Background, Bomb, BombSymbol, MoneySymbol
from SpritesCollection.MainGameplayClasses import HealthGroup, PauseBtn
from SpritesCollection.MenuClasses import StartButton, InfoButton, ShopButton, MenuJar, Info_to_menu_btn
from SpritesCollection.PauseClasses import PauseWindow, ContinueBtn, RestartBtn, FromPauseToMenuBtn
from SpritesCollection.EnemyClasses import Enemy

f = open('saved.json', encoding='utf8')
data = json.loads(f.read())
f.close()

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

menumode_start_btn = None
menumode_info_btn = None
menumode_shop_btn = None
menumode_high_score_sprites = None
menumode_high_score = None
menumode_money_sprites = None

clock = None
gameplay_score_counter = None
gameplay_bombs_counter = None
gameplay_money_counter = None
gameplay_score = None
gameplay_bombs_number = None
gameplay_bomb_symbol = None
gameplay_money = None
gameplay_money_symbol = None
gameplay_health = None
gameplay_health_group = None
gameplay_pause = None
gameplay_enemies = None
gameplay_time = None
gameplay_enemies_period = None
gameplay_wall = None

info_menu_btn = None

pausemode_sprites = None
pausemode_window = None
pausemode_continue_btn = None
pausemode_restart_btn = None
pausemode_menu_btn = None

resultmode_fon = None
resultmode_score_group = None
resultmode_money_group = None
resultmode_total_group = None
resultmode_menu_button = None
resultmode_return_button = None
resultmode_bonus = None

# В игре 5 режимов: menu, game, pause, result, info
process_mode = 'menu'


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


def start_gameplay():
    global all_sprites, background, jar, process_mode, bombs, bomb_type, gameplay_time
    global gameplay_score_counter, gameplay_bombs_counter, gameplay_money_counter, gameplay_health_group
    global gameplay_score, gameplay_bombs_number, gameplay_bomb_symbol, gameplay_money
    global gameplay_money_symbol, gameplay_health, gameplay_pause, clock, gameplay_enemies
    global gameplay_enemies_period, gameplay_wall
    process_mode = 'game'

    all_sprites = Group()

    clock = pygame.time.Clock()

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
    transform_number(gameplay_money, gameplay_money_counter, (370, 3))
    gameplay_score_counter.draw(main_screen)

    gameplay_health = HealthGroup()
    gameplay_health.draw(main_screen)

    gameplay_wall = Sprite()
    gameplay_wall.image = pygame.Surface([1, 650])
    gameplay_wall.rect = pygame.Rect(-1, 0, 1, 650)

    gameplay_pause = PauseBtn()
    all_sprites.add(gameplay_pause)

    all_sprites.draw(main_screen)

    gameplay_enemies = Group()

    gameplay_time = 0
    gameplay_enemies_period = 3

    pygame.display.flip()


def start_menumode():
    global fon, menumode_start_btn, menumode_info_btn, menumode_shop_btn, jar, all_sprites, process_mode, menumode_money_sprites
    global menumode_high_score_sprites

    process_mode = 'menu'

    fon = pygame.transform.scale(pygame.image.load('data/images/menu/main_menu.png'), (width, height))
    main_screen.blit(fon, (0, 0))

    menumode_start_btn = StartButton()
    menumode_info_btn = InfoButton()
    menumode_shop_btn = ShopButton()
    jar = MenuJar()

    all_sprites = Group()
    all_sprites.add(menumode_start_btn)
    all_sprites.add(menumode_info_btn)
    all_sprites.add(menumode_shop_btn)
    all_sprites.add(jar)

    menumode_money_sprites = Group()
    transform_number(data['money'], menumode_money_sprites, (90, 20))
    menumode_money_sprites.draw(main_screen)

    menumode_high_score_sprites = Group()
    x = 1000 - 25 * (len(str(data['high score'])) + 1)
    transform_number(data['high score'], menumode_high_score_sprites, (x, 20))
    menumode_high_score_sprites.draw(main_screen)

    high_score = Sprite()
    high_score.image = pygame.image.load('data/Images/menu/high_score.png')
    high_score.mask = pygame.mask.from_surface(high_score.image)
    high_score.rect = high_score.image.get_rect()
    high_score.mask = pygame.mask.from_surface(high_score.image)
    high_score.rect.x = 760 - 25 * (len(str(data['high score'])) - 1)
    high_score.rect.y = 20
    all_sprites.add(high_score)
    all_sprites.draw(main_screen)

    pygame.display.flip()


def start_info():
    global fon, info_menu_btn, all_sprites, process_mode

    process_mode = 'info'
    all_sprites = Group()

    fon = pygame.transform.scale(pygame.image.load('data/images/info_stuff/info.png'), (width, height))
    main_screen.blit(fon, (0, 0))
    info_menu_btn = Info_to_menu_btn()
    all_sprites.add(info_menu_btn)
    all_sprites.draw(main_screen)

    pygame.display.flip()


def start_pausemode():
    global pausemode_sprites, process_mode, pausemode_continue_btn, pausemode_menu_btn, pausemode_window
    global pausemode_restart_btn

    process_mode = 'pause'

    pausemode_sprites = Group()

    pausemode_window = PauseWindow()
    pausemode_sprites.add(pausemode_window)

    pausemode_continue_btn = ContinueBtn()
    pausemode_sprites.add(pausemode_continue_btn)

    pausemode_restart_btn = RestartBtn()
    pausemode_sprites.add(pausemode_restart_btn)

    pausemode_menu_btn = FromPauseToMenuBtn()
    pausemode_sprites.add(pausemode_menu_btn)

    pausemode_sprites.draw(main_screen)

    pygame.display.flip()


def start_resultmode(result, money):
    global all_sprites, resultmode_fon, resultmode_money_group, resultmode_score_group, resultmode_total_group
    global resultmode_menu_button, resultmode_return_button, resultmode_bonus

    all_sprites = Group()

    resultmode_fon = Sprite()
    resultmode_fon.image = pygame.image.load('data/Images/game_over_stuff/gameover.png')
    resultmode_fon.rect = resultmode_fon.image.get_rect()
    resultmode_fon.rect.x = 182
    resultmode_fon.rect.y = 50
    all_sprites.add(resultmode_fon)

    resultmode_menu_button = Sprite()
    resultmode_menu_button.image = pygame.image.load('data/Images/game_over_stuff/menu button.png')
    resultmode_menu_button.rect = resultmode_menu_button.image.get_rect()
    resultmode_menu_button.rect.x = 182 + 45
    resultmode_menu_button.rect.y = 470
    all_sprites.add(resultmode_menu_button)

    resultmode_return_button = Sprite()
    resultmode_return_button.image = pygame.image.load('data/Images/game_over_stuff/return button.png')
    resultmode_return_button.rect = resultmode_return_button.image.get_rect()
    resultmode_return_button.rect.x = 400
    resultmode_return_button.rect.y = 470
    all_sprites.add(resultmode_return_button)

    all_sprites.draw(main_screen)

    resultmode_score_group = Group()
    transform_number(result, resultmode_score_group, (175 + 182, 205))
    resultmode_score_group.draw(main_screen)

    resultmode_money_group = Group()
    x = transform_number(str(money) + '+', resultmode_money_group, (150 + 182, 290))
    resultmode_money_group.draw(main_screen)

    bonus = int(result * 0.02)
    resultmode_bonus = Group()
    transform_number(bonus, resultmode_bonus, (x, 290))
    resultmode_bonus.draw(main_screen)

    resultmode_total_group = Group()
    transform_number(money + bonus, resultmode_total_group, (150 + 182, 395))
    resultmode_total_group.draw(main_screen)

    pygame.display.flip()

    if data['high score'] < result:
        data['high score'] = result
    data['money'] += money + bonus


def generate_enemy():
    position = random.randrange(80, 500)
    enemy = Enemy.generate(position)
    gameplay_enemies.add(enemy)


start_menumode()
pygame.display.flip()

while running:
    if process_mode == 'game':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gameplay_bombs_number > 0:
                    bombs.add(Bomb(jar.rect.y, bomb_type))
                    gameplay_bombs_number -= 1
                    gameplay_bombs_counter.empty()
                    transform_number(gameplay_bombs_number, gameplay_bombs_counter, (200, 3))
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_sprite = Sprite()
                click_sprite.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                click_group = Group()
                click_group.add(click_sprite)
                if gameplay_pause.update(click_group) == 'pause':
                    start_pausemode()

                click_group.empty()

        if process_mode == 'game':
            buttons = pygame.key.get_pressed()
            buttons = [buttons[i] for i in (273, 274, 32, 304)]
            time = clock.tick() / 1000
            background.update(time)
            jar.update(buttons, time)
            bombs.update(time)
            all_sprites.draw(main_screen)
            bombs.draw(main_screen)

            gameplay_score += time * 100
            gameplay_score_counter.empty()
            transform_number(int(gameplay_score), gameplay_score_counter, (3, 3))
            gameplay_score_counter.draw(main_screen)

            gameplay_bombs_counter.draw(main_screen)

            if pygame.sprite.spritecollide(jar, gameplay_enemies, False):
                collision_enemies = pygame.sprite.spritecollide(jar, gameplay_enemies, True)
                res = gameplay_health.update(sum([i.collision_damage for i in collision_enemies]))
                if res == 'result':
                    process_mode = res
                    start_resultmode(int(gameplay_score), gameplay_money)
                    continue
            if pygame.sprite.spritecollide(gameplay_wall, gameplay_enemies, False):
                collision_enemies = pygame.sprite.spritecollide(gameplay_wall, gameplay_enemies, True)
                res = gameplay_health.update(sum([i.missing_damage for i in collision_enemies]))
                if res == 'result':
                    process_mode = res
                    start_resultmode(int(gameplay_score), gameplay_money)
                    continue

            if pygame.sprite.groupcollide(gameplay_enemies, bombs, False, False):
                res = pygame.sprite.groupcollide(gameplay_enemies, bombs, False, True)
                for i in res.keys():
                    if res[i]:
                        i.health -= 100
                    if i.health <= 0:
                        gameplay_money += i.money
                        gameplay_money_counter.empty()
                        transform_number(gameplay_money, gameplay_money_counter, (370, 3))

                        gameplay_score += i.score

                        gameplay_bombs_number += i.bombs
                        gameplay_bombs_counter.empty()
                        transform_number(gameplay_bombs_number, gameplay_bombs_counter, (200, 3))

            gameplay_time += time
            if gameplay_time >= gameplay_enemies_period:
                gameplay_time = 0
                generate_enemy()

            gameplay_enemies.update(time)
            gameplay_enemies.draw(main_screen)

            gameplay_money_counter.draw(main_screen)

            gameplay_health.draw(main_screen)

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
                if menumode_start_btn.update(click_group) == 'game':
                    start_gameplay()
                elif menumode_info_btn.update(click_group) == 'info':
                    start_info()
                click_group.empty()

    elif process_mode == 'info':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_sprite = Sprite()
                click_sprite.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                click_group = Group()
                click_group.add(click_sprite)
                if info_menu_btn.update(click_group) == 'menu':
                    start_menumode()
                click_group.empty()

    elif process_mode == 'pause':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_sprite = Sprite()
                click_sprite.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                click_group = Group()
                click_group.add(click_sprite)
                if pausemode_continue_btn.update(click_group) == 'continue':
                    process_mode = 'game'
                    clock = pygame.time.Clock()
                    pausemode_sprites.empty()
                elif pausemode_restart_btn.update(click_group) == 'restart':
                    start_gameplay()
                    pausemode_sprites.empty()
                elif pausemode_menu_btn.update(click_group) == 'menu':
                    start_menumode()
                    pausemode_sprites.empty()
                click_group.empty()

    elif process_mode == 'result':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_sprite = Sprite()
                click_sprite.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                click_group = Group()
                click_group.add(click_sprite)
                if pygame.sprite.spritecollideany(resultmode_menu_button, click_group):
                    start_menumode()
                elif pygame.sprite.spritecollideany(resultmode_return_button, click_group):
                    start_gameplay()

pygame.quit()

f = open('saved.json', encoding='utf8', mode='w')
f.write(json.dumps(data))
f.close()
