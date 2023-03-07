def cijevi_game():
    import pygame
    pygame.mixer.init()

    pygame.init()

    WIDTH = 750
    HEIGHT = 600
    BACKGROUND = pygame.transform.scale(pygame.image.load('Cijevi_assets/cijevibackground.png'), (WIDTH, HEIGHT))
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    CIJEV1 = pygame.transform.scale(pygame.image.load('Cijevi_assets/cijev1-removebg-preview.png'), (150, 150))
    CIJEV2 = pygame.transform.scale(pygame.image.load('Cijevi_assets/cijev2-removebg-preview.png'), (150, 133))
    CIJEV3 = pygame.transform.scale(pygame.image.load('Cijevi_assets/cijev3-removebg-preview.png'), (150, 150))
    WINNER_FONT = pygame.font.SysFont('comicsans', 100)
    WIN_SOUND = pygame.mixer.Sound('Cijevi_assets/tadaa-47995.wav')
    ROTATE_SOUND = pygame.mixer.Sound('Cijevi_assets/mixkit-falling-on-metal-roof-752.wav')


    class Cijev(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y, cijev, _id):
            super().__init__()
            self.image = cijev
            self.rect = pygame.Rect(pos_x, pos_y, 150, 150)
            self.id = _id
            self.angle = 0


    cijev_1 = Cijev(150, 0, CIJEV2, 1)
    cijev_2 = Cijev(300, 0, CIJEV3, 2)
    cijev_3 = Cijev(450, 0, CIJEV2, 3)
    cijev_4 = Cijev(0, 150, CIJEV2, 4)
    cijev_5 = Cijev(150, 150, CIJEV2, 5)
    cijev_6 = Cijev(300, 150, CIJEV1, 6)
    cijev_7 = Cijev(450, 150, CIJEV1, 7)
    cijev_8 = Cijev(600, 150, CIJEV2, 8)
    cijev_9 = Cijev(150, 300, CIJEV1, 9)
    cijev_10 = Cijev(300, 300, CIJEV3, 10)
    cijev_11 = Cijev(450, 300, CIJEV2, 11)
    cijev_12 = Cijev(150, 450, CIJEV2, 12)
    cijev_13 = Cijev(300, 450, CIJEV1, 13)
    cijev_14 = Cijev(450, 450, CIJEV1, 14)

    grupa_cijevi = pygame.sprite.Group()
    grupa_cijevi.add(cijev_1, cijev_2, cijev_3, cijev_5, cijev_6, cijev_7,
                     cijev_14, cijev_13, cijev_12, cijev_9, cijev_10, cijev_11, cijev_4, cijev_8)



    running = True
    pygame.mouse.set_visible(True)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                mouse_pos_rect = pygame.Rect(mouse_pos_x, mouse_pos_y, 1, 1)
                for s in grupa_cijevi:
                    if s.id != 4 and s.id != 8:
                        if s.rect.colliderect(mouse_pos_rect):
                            s.image = pygame.transform.rotate(s.image, 90)
                            s.angle += 90
                            if s.angle == 360:
                                s.angle = 0
                            ROTATE_SOUND.play()


        WIN.blit(BACKGROUND, (0, 0))
        grupa_cijevi.draw(WIN)
        if (cijev_5.angle == 0 or cijev_5.angle == 180) and\
            (cijev_6.angle == 270) and (cijev_10.angle == 90 or cijev_10.angle == 270) and\
            (cijev_13.angle == 90) and (cijev_14.angle == 180) and\
            (cijev_11.angle == 90 or cijev_11.angle == 270) and (cijev_7.angle == 0):
                draw_text = WINNER_FONT.render("POBJEDA !", 1, (255, 0, 0))
                WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
                pygame.display.update()
                WIN_SOUND.play()
                pygame.time.delay(4000)
                break
        pygame.display.flip()



    pygame.quit()
if __name__ == '__main__':
    cijevi_game()