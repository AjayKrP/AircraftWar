#!bin/python3
from player import *
from enemy import *
from cloud import *
from config import *

pygame.init()
player = Player()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# all_sprites.add(player)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

clock = pygame.time.Clock()

pygame.mixer.music.load('music/Apoxode_-_Electric_1.mp3')
pygame.mixer.music.play(loops=-1)


def show_home_screen():
    # defining a font
    font_property = pygame.font.SysFont('Corbel', 35)
    # rendering a text written in
    # this font
    text = font_property.render('quit', True, COLOR_WHITE)
    running = True
    while running:
        for event in pygame.event.get():
            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                # if the mouse is clicked on the
                # button the game is terminated
                if SCREEN_WIDTH / 2 <= mouse[0] <= SCREEN_WIDTH / 2 + 140 and SCREEN_HEIGHT / 2 <= mouse[
                    1] <= SCREEN_HEIGHT / 2 + 40:
                    start_main_game()

                    # fills the screen with a color
            screen.fill((60, 25, 60))
            # if mouse is hovered on a button it
            # changes to lighter shade
            if SCREEN_WIDTH / 2 <= mouse[0] <= SCREEN_WIDTH / 2 + 140 and SCREEN_HEIGHT / 2 <= mouse[
                1] <= SCREEN_HEIGHT / 2 + 40:
                pygame.draw.rect(screen, COLOR_LIGHT, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 140, 40])

            else:
                pygame.draw.rect(screen, COLOR_DARK, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 140, 40])

                # superimposing the text onto our button
            screen.blit(text, (SCREEN_WIDTH / 2 + 50, SCREEN_HEIGHT / 2))

            # updates the frames of the game
            pygame.display.update()


def start_main_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            # Add a new cloud?
            elif event.type == ADDCLOUD:
                # Create the new cloud and add it to sprite groups
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        enemies.update()
        clouds.update()

        # Fill the screen with sky blue
        screen.fill(BACKGROUND_COLOR)

        # screen.fill((0,0,0))
        for entity in all_sprites:
            screen.blit(entity.surf,
                        entity.rect)  # ((SCREEN_WIDTH - player.surf.get_width())//2, (SCREEN_HEIGHT - player.surf.get_height())//2))
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            move_up_sound.stop()
            move_down_sound.stop()
            collision_sound.play()
            running = False
        pygame.display.flip()
        clock.tick(30)

    # All done! Stop and quit the mixer.
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

show_home_screen()

