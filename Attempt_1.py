from No_Name_Game import No_name_game
from cijevi_game import cijevi_game
import pygame, time, random, math



No_name_game()
cijevi_game()


pygame.init()

WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

BACKGROUND = pygame.transform.scale(pygame.image.load("Assets_W/background_1.jpg"), (WIDTH, HEIGHT))
bec_rect = BACKGROUND.get_rect()
bec_rect.topleft = (0, 0)

METEOR_IMAGE = pygame.transform.scale(pygame.image.load("Assets_W/DALL_E_2023-03-02_13.20.05_-_circle_rock_pixel_art_dark_without_background-removebg-preview.png"), (50, 50))

GAMEOVER_IMAGE = pygame.transform.scale(pygame.image.load("Assets_W/gameover/gameover_image.png"), (400, 200))

PRESS_SPACE = pygame.transform.scale(pygame.image.load("Assets_W/Press_space1.png"), (400, 200))
space_rect = PRESS_SPACE.get_rect()
space_rect.center = WIDTH//2, HEIGHT//2

FONT = pygame.font.SysFont("arial", 20)
tekst = FONT.render("Press Esc to quit", True, (0, 0, 0))
tekst_rect = tekst.get_rect()
tekst_rect.topleft = (10, 10)

song1 = pygame.mixer.Sound("Assets_W/songs/NeverGonnaGUP.wav")
song1.play()
explosion_sound = pygame.mixer.Sound("Assets_W/songs/explosion.wav")
background_music = pygame.mixer.Sound("Assets_W/songs/background_music.wav")
gameover_song = pygame.mixer.Sound('Assets_W/songs/mixkit-sad-game-over-trombone-471.wav')

def sprite_load(SLIKA):
    return pygame.transform.scale(pygame.image.load(SLIKA), (120, 200))
def sprite_load_right(SLIKA):
    return pygame.transform.scale(pygame.image.load(SLIKA), (150, 200))
def sprite_load_left(SLIKA):
    return pygame.transform.flip(pygame.transform.scale(pygame.image.load(SLIKA), (150, 200)), True, False)
def proj_sprite(SLIKA):
    return pygame.transform.scale(pygame.image.load(SLIKA), (35, 35))
def plosionF(SLIKA):
    return pygame.transform.scale(pygame.image.load(SLIKA), (50, 50))

Idle = [sprite_load("Assets_W/idle/row-1-column-1.png"), sprite_load("Assets_W/idle/row-1-column-2.png"), sprite_load("Assets_W/idle/row-1-column-3.png")
        , sprite_load("Assets_W/idle/row-1-column-4.png"), sprite_load("Assets_W/idle/row-1-column-5.png"), sprite_load("Assets_W/idle/row-1-column-6.png")]
Right = [sprite_load_right("Assets_W/right/run (1).png"), sprite_load_right("Assets_W/right/run (2).png"), sprite_load_right("Assets_W/right/run (3).png"),
          sprite_load_right("Assets_W/right/run (4).png"), sprite_load_right("Assets_W/right/run (5).png"), sprite_load_right("Assets_W/right/run (6).png"),
         sprite_load_right("Assets_W/right/run (7).png"), sprite_load_right("Assets_W/right/run (8).png")]
Left = [sprite_load_left("Assets_W/right/run (1).png"), sprite_load_left("Assets_W/right/run (2).png"), sprite_load_left("Assets_W/right/run (3).png")
        , sprite_load_left("Assets_W/right/run (4).png"), sprite_load_left("Assets_W/right/run (5).png"), sprite_load_left("Assets_W/right/run (6).png"),
        sprite_load_left("Assets_W/right/run (7).png"), sprite_load_left("Assets_W/right/run (8).png")]
GameOver_list = [sprite_load("Assets_W/gameover/go (1).png"), sprite_load("Assets_W/gameover/go (2).png"), sprite_load("Assets_W/gameover/go (3).png"),
                 sprite_load("Assets_W/gameover/go (4).png"), sprite_load("Assets_W/gameover/go (5).png"), sprite_load("Assets_W/gameover/go (6).png"),
                 sprite_load("Assets_W/gameover/go (7).png"), ]
Proj_image_list = [proj_sprite("Assets_W/pr/proj (0).gif")]
BOOM_IMAGE_LIST = [plosionF("Assets_W/BOOM/egg (1).png"), plosionF("Assets_W/BOOM/egg (2).png"), plosionF("Assets_W/BOOM/egg (3).png"),
                   plosionF("Assets_W/BOOM/egg (4).png"), plosionF("Assets_W/BOOM/egg (5).png"), plosionF("Assets_W/BOOM/egg (6).png"),
                   plosionF("Assets_W/BOOM/egg (7).png"), ]

rec_sprite = Idle[0].get_rect()
rec_sprite.bottomleft = (0, HEIGHT - 10)

run = True
space = False
idle = True
right = False
left = False
boom = False
GameOver = False
go_var = True
GO_brojac = 0
boom_start_time = time.time()
boom_brojac = 0
boom_coordinates = 0, 0
brojac = 0
start_time = time.time()
another_time = time.time()
meteorList =[]
projectiles = []
projectile_speed = 10

def animation(Lista):
    global start_time
    global brojac
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= 0.1:
        brojac += 1
        start_time = time.time()
        if brojac > len(Lista) - 1:
            brojac = 0
    rndslika = Lista[brojac]
    return rndslika



while run:

    clock = pygame.time.Clock()
    clock.tick(90)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                space = True

            if event.key == pygame.K_w:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - rec_sprite.centerx
                dy = mouse_y - rec_sprite.centery
                distance = math.sqrt(dx ** 2 + dy ** 2)
                direction = (dx / distance, dy / distance)
                velocity = (direction[0] * projectile_speed, direction[1] * projectile_speed)
                projectile_rect = Proj_image_list[0].get_rect()
                projectile_rect.center = rec_sprite.midtop
                if len(projectiles) < 3:
                    projectiles.append((projectile_rect, velocity))

    if pygame.key.get_pressed()[pygame.K_d]:
        right = True
        idle = False
    else:
        right = False
        if left == False and idle == False:
            brojac = 0
            idle = True
    if pygame.key.get_pressed()[pygame.K_a]:
        left = True
        idle = False
    else:
        left = False
        if right == False and idle == False:
            brojac = 0
            idle = True


    trenutno = time.time()
    if trenutno - another_time >= 1:
        meteorList.append(pygame.Rect(random.randint(100, WIDTH - 100), 50, 50, 50))
        another_time = time.time()


    for i in range(len(projectiles)):
        projectiles[i][0].move_ip(projectiles[i][1])

    #Remove projectile
    projectiles = [p for p in projectiles if screen.get_rect().colliderect(p[0])]

    for meteor in meteorList:
        for proj in projectiles:
            if meteor.colliderect(proj[0]):
                meteorList.remove(meteor)
                projectiles.remove(proj)
                boom_coordinates = meteor.center
                boom = True
                explosion_sound.play()


    for meteor in meteorList:
        if meteor.colliderect(rec_sprite):
            GameOver = True
            idle = False
            right = False
            left = False
            boom = False
            if go_var:
                GO_start_time = time.time()
                go_var = False
                gameover_song.play()

    screen.blit(BACKGROUND, bec_rect)
    if space:
        song1.fadeout(1500)
        if idle or (right and left):
            if brojac > 5:
                brojac = 0
            screen.blit(animation(Idle), rec_sprite)
        if right and left == False:
            screen.blit(animation(Right), rec_sprite)
            if rec_sprite.x < WIDTH - 120:
                rec_sprite.x += 5
        if left and right == False:
            screen.blit(animation(Left), rec_sprite)
            if rec_sprite.x > 0:
                rec_sprite.x -= 5
        if boom:
            current_time = time.time()
            elapsed_time = current_time - boom_start_time
            if elapsed_time >= 0.1:
                boom_brojac += 1
                boom_start_time = time.time()
                if boom_brojac > len(BOOM_IMAGE_LIST) - 1:
                    boom_brojac = 0
                    boom = False
            boom_rndslika = BOOM_IMAGE_LIST[boom_brojac]
            screen.blit(boom_rndslika, boom_coordinates)
        if GameOver == False:
            for meteor in meteorList:
                screen.blit(METEOR_IMAGE, meteor)
                meteor.y += 2
            for proj in projectiles:
                screen.blit(Proj_image_list[0], proj[0])
        if GameOver:

            GO_current_time = time.time()
            GO_elapsed_time = GO_current_time - GO_start_time
            if GO_elapsed_time >= 0.3:
                GO_brojac += 1
                GO_start_time = time.time()
                if GO_brojac > len(GameOver_list) - 1:
                    print(GAMEOVER_IMAGE)
                    screen.blit(GAMEOVER_IMAGE, (WIDTH/2, HEIGHT/2))
                    print(screen)
                    time.sleep(3)
                    break
            screen.blit(GameOver_list[GO_brojac], rec_sprite)
            #print(GO_current_time, GO_start_time, go_var)
    else:
        if time.time() % 1 > 0.3:
            screen.blit(PRESS_SPACE, space_rect)
        screen.blit(tekst, tekst_rect)
    pygame.display.flip()

"""
run2 = True
while run2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run2 = False

    screen.fill((255, 0, 255))
    pygame.display.flip()
"""
pygame.quit()