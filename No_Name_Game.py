def No_name_game():
    import pygame
    import os
    import math
    pygame.font.init()
    pygame.mixer.init()

    pygame.init()


    class Character(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y, width, height, image_path, flip_image_path, speed, max_jumps, max_projectiles):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
            self.flip_image = pygame.transform.scale(pygame.image.load(flip_image_path), (width, height))
            self.rect = pygame.Rect(pos_x, pos_y, width, height)
            self.rect.x = pos_x
            self.rect.y = pos_y
            self.speed = speed
            self.max_jumps = max_jumps
            self.max_proj = max_projectiles


    class Enemy(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y, width, height, image_path, speed):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
            self.rect = pygame.Rect(pos_x + 10, pos_y, width - 50, height)  # hardcode
            self.rect.x = pos_x
            self.rect.y = pos_y
            self.speed = speed


    zombieL = Enemy(0, 413, 100, 200, 'Assets/zombie-removebg-preview.png', 1)
    zombieR = Enemy(1200, 413, 100, 200, 'Assets/zombiefliped.png', 1)

    ruka = Character(500, 100, 100, 100, 'Assets/R-modified.png', 'Assets/R.png', 3, 2, 1)

    GAMEOVER_SONG = pygame.mixer.Sound(os.path.join('Assets/mixkit-sad-game-over-trombone-471.wav'))
    FIRE_SOUND = pygame.mixer.Sound('Assets/726ZS62-wizard-fire-spell-cast-2-[AudioTrimmer.com].wav')

    FONT = pygame.font.SysFont('comicsans', 50)


    WIDTH, HEIGHT = 1200, 700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    TLO_SIRINA = 100
    TLO_VISINA = 100
    PROJEKTIL_SIRINA = 100
    PROJEKTIL_VISINA = 50
    BRZINA_PROJEKTILA = 5

    PROJEKTIL_IMAGE = pygame.image.load(os.path.join('Assets/34c645_d40947803670443dbcfd33d1ee205d0f.png'))
    PROJEKTIL_IMAGE2 = pygame.image.load(os.path.join('Assets/34c645_d40947803670443dbcfd33d1ee205d0f-modified.png'))
    PROJEKTIL = pygame.transform.scale(PROJEKTIL_IMAGE, (PROJEKTIL_SIRINA, PROJEKTIL_VISINA))
    PROJEKTIL2 = pygame.transform.scale(PROJEKTIL_IMAGE2, (PROJEKTIL_SIRINA, PROJEKTIL_VISINA))
    BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets/ecec9f0dbde599a13bb61512654552ba.png'))
    BACKGROUD = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
    TLO_IMAGE = pygame.image.load(os.path.join('Assets/zemlja.png'))
    TLO = pygame.transform.scale(TLO_IMAGE, (TLO_SIRINA, TLO_VISINA))
    GUBITAK = pygame.transform.scale(pygame.image.load(
        'Assets/png-clipart-es-game-over-text-thumbnail-removebg-preview.png'), (1000, 500))


    pygame.display.set_caption("Game by Andrija")


    def draw_window(ruka, lista_projektila, orijentacija, score_count):
        WIN.blit(BACKGROUD, (0, 0))
        WIN.blit(TLO, (0, 600))
        WIN.blit(TLO, (100, 600))
        WIN.blit(TLO, (200, 600))
        WIN.blit(TLO, (300, 600))
        WIN.blit(TLO, (400, 600))
        WIN.blit(TLO, (500, 600))
        WIN.blit(TLO, (600, 600))
        WIN.blit(TLO, (700, 600))
        WIN.blit(TLO, (800, 600))
        WIN.blit(TLO, (900, 600))
        WIN.blit(TLO, (1000, 600))
        WIN.blit(TLO, (1100, 600))
        if orijentacija == 1:
            WIN.blit(ruka.image, (ruka.rect.x, ruka.rect.y))
        if orijentacija == 0:
            WIN.blit(ruka.flip_image, (ruka.rect.x, ruka.rect.y))
        for projektil in lista_projektila:
            WIN.blit(PROJEKTIL, (projektil.x, projektil.y))
        WIN.blit(zombieL.image, (zombieL.rect.x, zombieL.rect.y))
        text = FONT.render(f"Score: {score_count}", True, (255, 255, 255))
        WIN.blit(text, (800, 100))
        pygame.display.update()


    def moj_lik_movement(ruka):
        if pygame.key.get_pressed()[pygame.K_d]:
            ruka.rect.x += ruka.speed
        if pygame.key.get_pressed()[pygame.K_a]:
            ruka.rect.x -= ruka.speed


    def main():
        lik_ubrzanje = 0
        gravitacija = 1
        snaga_skoka = -15
        brojac_skokova = 0
        orijentacija = 1  # desno
        run = True
        lista_projektila = []
        postoji_proj = False
        score_count = 0
        while run:
            clock = pygame.time.Clock()
            clock.tick(90)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(lista_projektila) < ruka.max_proj:
                        pygame.time.delay(30)
                        moj_projektil = pygame.Rect(ruka.rect.x, ruka.rect.y, PROJEKTIL_SIRINA,
                                                    PROJEKTIL_VISINA)
                        lista_projektila.append(moj_projektil)
                        postoji_proj = True
                        FIRE_SOUND.play()
                    if event.key == pygame.K_w and brojac_skokova < ruka.max_jumps:  # JUMP
                        lik_ubrzanje = snaga_skoka
                        brojac_skokova += 1
            lik_ubrzanje += gravitacija
            ruka.rect.y += lik_ubrzanje

            if ruka.rect.y > 536:
                lik_ubrzanje = 0
                ruka.rect.y = 536
                brojac_skokova = 0
            if pygame.key.get_pressed()[pygame.K_d]:
                orijentacija = 1
            if pygame.key.get_pressed()[pygame.K_a]:
                orijentacija = 0

            moj_lik_movement(ruka)
            if not postoji_proj:
                C_rukex = ruka.rect.x
                C_rukey = ruka.rect.y

            if not postoji_proj:
                mouse_x_C = mouse_x
                mouse_y_C = mouse_y

            x_orientation = (mouse_x_C - C_rukex)
            y_orientation = (mouse_y_C - C_rukey)
            hypotenuse = (math.sqrt(x_orientation ** 2 + y_orientation ** 2)) / 10
            for projektil in lista_projektila:
                projektil.x += x_orientation / hypotenuse
                projektil.y += y_orientation / hypotenuse
                if projektil.x > WIDTH or projektil.x < 0 or projektil.y > HEIGHT or projektil.y < 0:  # uvjeti
                    lista_projektila.remove(projektil)
                    postoji_proj = False
                if projektil.colliderect(zombieL.rect):
                    lista_projektila.remove(projektil)
                    postoji_proj = False
                    zombieL.rect.x = 0
                    zombieL.rect.y = 413
                    zombieL.speed *= 1.2
                    score_count += 1

            zombieL.rect.x += zombieL.speed

            draw_window(ruka, lista_projektila, orijentacija, score_count)
            if ruka.rect.colliderect(zombieL.rect):
                WIN.blit(GUBITAK, (WIDTH/2 - GUBITAK.get_width()/2, HEIGHT/2 - GUBITAK.get_height()/2))
                pygame.display.update()
                GAMEOVER_SONG.play()
                pygame.time.delay(4000)
                break

        pygame.quit()

    main()
if __name__ == '__main__':
    No_name_game()