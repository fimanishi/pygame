import pygame
import os
import get_png_dimensions
from characters.base import Character
from characters.enemy import Enemy
from characters.hero import Hero
import mechanics.engines

def main():

    # initializes pygame
    pygame.init()

    # creates the window caption
    pygame.display.set_caption('My Game')

    # initializes the clock for the pygame
    clock = pygame.time.Clock()

    # Game initialization

    # constants

    stop_game = False
    end_game = False
    fontsize = 40
    font = pygame.font.Font(None, fontsize)
    who_caught = ""
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)

    # initializes background and retrieve its width and height
    bg = pygame.image.load(os.path.join("images", "background.png"))
    bg_width, bg_height = get_png_dimensions.png_info(os.path.join("images", "background.png"))

    # sets the screen size based on the size of the background
    screen = pygame.display.set_mode((bg_width, bg_height))

    # # creates a dictionary of the characters with the hero and the monster
    # chars_dict = {"monster": Enemy("monster.png",  increment = 30, bg = (bg_width, bg_height), time = 0.3, screen = screen),
    #               "hero": Hero("hero.png",  increment = 1, bg = (bg_width, bg_height), screen = screen)
    # }
    #
    # # creates the number of goblins desired and append to the characters' dictionary
    # for goblin_count in range(1,goblins+1):
    #     key = "goblin" + str(goblin_count)
    #     chars_dict[key] = Enemy("goblin.png", increment = 20, bg = (bg_width, bg_height), time = 0.3, screen = screen)
    chars_dict, goblin_count = mechanics.engines.create_chars_dict(bg_width, bg_height, screen)


    # while handles quitting the game
    while not stop_game:
        # waits for the quit button being pressed
        for event in pygame.event.get():
            # if it is pressed, exit the while loop and closes the window
            if event.type == pygame.QUIT:
                stop_game = True

        # displays the background
        screen.blit(bg,(0,0))

        # displays the level
        text1 = font.render("Level: {}".format(goblin_count-2), True, white_color)
        screen.blit(text1, (10, 10))

        # enables the user to move the hero up, down, left and right by pressing the arrows in the keyboard
        mechanics.engines.hero_movement(chars_dict["hero"])

        # moves the monster and goblins randomly around the screen
        mechanics.engines.enemy_movement(chars_dict)

        # displays all goblins
        mechanics.engines.goblins_display(chars_dict)

        # displays the hero and the monster
        chars_dict["hero"].display()
        chars_dict["monster"].display()

        # checks if the hero caught the monster
        if chars_dict["hero"].catch(chars_dict["monster"]) == True:
            who_caught = "hero"
            end_game = True
        # checks if any of the goblins caught the hero
        elif mechanics.engines.enemy_catch(chars_dict) == True:
            who_caught = "goblin"
            end_game = True

        # Game display
        pygame.display.update()
        clock.tick(60)

        while end_game == True:
            # updates the screen with an empty background
            screen.blit(bg,(0,0))

            # if the hero caught the monster, displays only the hero and prints the winning message
            if who_caught == "hero":
                chars_dict["hero"].display()
                text1 = font.render("You won!", True, black_color)
                screen.blit(text1, (bg_width/2-60, bg_width/2 - fontsize * 1.5))

            # if the goblins caught the hero, displays only the goblins and prints the losing message
            elif who_caught == "goblin":
                mechanics.engines.goblins_display(chars_dict)
                text1 = font.render("You lost!", True, black_color)
                screen.blit(text1, (bg_width/2-55, bg_width/2 - fontsize * 1.5))

            # prints the message to see whether the user wants to play again
            text2 = font.render("Hit enter to play again.", True, black_color)
            screen.blit(text2, (bg_width/2-150, bg_width/2 - fontsize * 0.5))

            # updates the screen
            pygame.display.update()

            # if the user wants to play again, by pushing the return key, generates random positions for the characters
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                # adds one more goblin to the Game
                if who_caught == "hero":
                    goblin_count += 1
                    key = "goblin" + str(goblin_count)
                    chars_dict[key] = Enemy("goblin.png", increment = 10, bg = (bg_width, bg_height), time = 0.3, screen = screen)
                # if user loses reset the number of goblins to the default value
                elif who_caught == "goblin":
                    chars_dict, goblin_count = mechanics.engines.create_chars_dict(bg_width, bg_height, screen)

                # resets all the checkers to False
                who_caught = False
                end_game = False
                chars_dict["hero"].caught = False

                clear = False
                while clear == False:
                    # reposition all the characaters randomly
                    mechanics.engines.chars_random_position(chars_dict)
                    # checks if the hero was generated touching the monster, if yes redo
                    if chars_dict["hero"].catch(chars_dict["monster"]) == True:
                        mechanics.engines.chars_random_position(chars_dict)
                    # checks if the goblins were generated touching the hero, if yes redo
                    elif mechanics.engines.enemy_catch(chars_dict) == True:
                        mechanics.engines.chars_random_position(chars_dict)
                    else:
                        clear = True


            # waits for the quit button being pressed
            for event in pygame.event.get():
                # if it is pressed, exit the while loop and closes the window
                if event.type == pygame.QUIT:
                    stop_game = True
                    end_game = False
                    break

    # updates the screen
    pygame.display.update()

    # pygame.quit()

if __name__ == '__main__':
    main()
