import pygame
import os
import get_png_dimensions
from characters.base import Character
from characters.enemy import Enemy
from characters.hero import Hero

def main():

    pygame.init()
    bg = pygame.image.load(os.path.join("images", "background.png"))
    bg_width, bg_height = get_png_dimensions.png_info(os.path.join("images", "background.png"))
    screen = pygame.display.set_mode((bg_width, bg_height))

    hero = Hero("hero.png",  increment = 1, bg = (bg_width, bg_height), screen = screen)
    goblin1 = Enemy("goblin.png", increment = 20, bg = (bg_width, bg_height), time = 0.3, screen = screen)
    goblin2 = Enemy("goblin.png", increment = 20, bg = (bg_width, bg_height), time = 0.3, screen = screen)
    goblin3 = Enemy("goblin.png", increment = 20, bg = (bg_width, bg_height), time = 0.3, screen = screen)
    monster = Enemy("monster.png",  increment = 30, bg = (bg_width, bg_height), time = 0.3, screen = screen)

    black_color = (0, 0, 0)

    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    end_game = False
    fontsize = 40
    font = pygame.font.Font(None, fontsize)
    who_caught = ""

    # while handles quitting the game
    while not stop_game:
        # waits for the quit button being pressed
        for event in pygame.event.get():
            # if it is pressed, exit the while loop and closes the window
            if event.type == pygame.QUIT:
                stop_game = True
            # Event handling


        if pygame.key.get_pressed()[pygame.K_DOWN]:
            hero.move_down()
        elif pygame.key.get_pressed()[pygame.K_UP]:
            hero.move_up()
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            hero.move_left()
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            hero.move_right()


        screen.blit(bg,(0,0))
        # hero.move_leftdown()
        monster.move_random()
        goblin1.move_random()
        goblin2.move_random()
        goblin3.move_random()
        hero.display()
        monster.display()
        goblin1.display()
        goblin2.display()
        goblin3.display()
        if hero.catch(monster) == True:
            who_caught = "hero"
            end_game = True

        elif goblin1.catch(hero) == True or goblin2.catch(hero) == True or goblin3.catch(hero) == True:
            who_caught = "goblin"
            end_game = True
        # Game display

        pygame.display.update()
        clock.tick(60)

        while end_game == True:
            screen.blit(bg,(0,0))
            if who_caught == "hero":
                hero.display()
                text1 = font.render("You won!", True, black_color)
                screen.blit(text1, (bg_width/2-60, bg_width/2 - fontsize * 1.5))
            elif who_caught == "goblin":
                goblin1.display()
                goblin2.display()
                goblin3.display()
                text3 = font.render("You lost!", True, black_color)
                screen.blit(text3, (bg_width/2-55, bg_width/2 - fontsize * 1.5))
            text2 = font.render("Hit enter to play again.", True, black_color)
            screen.blit(text2, (bg_width/2-150, bg_width/2 - fontsize * 0.5))
            pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                end_game = False
                hero.caught = False
                hero.random_position()
                monster.random_position()
                goblin1.random_position()
                goblin2.random_position()
                goblin3.random_position()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
                    end_game = False
                    break

    pygame.display.update()
    #pygame.quit()

if __name__ == '__main__':
    main()
