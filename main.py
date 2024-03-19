import pygame
from pygame import mixer
from fighter import Fighter
from Database import GameData
from Database import Selection
from SelectCh import *

import sys
from button import Button
from button import Button1
from database_interaction import retrieve_data_from_database
import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

mixer.init()
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Finger Flex Fury")

BG = pygame.image.load("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/Images/Main.png").convert_alpha()
warr = 2
warr2 = 3

def get_font(size):  # Returns Press-Start-2P in the desired size
  return pygame.font.Font("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/fonts/turok.ttf", size)


def play():
  while True:
    mixer.init()
    pygame.init()

    # create game window
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Finger Flex Fury")

    # set framerate
    clock = pygame.time.Clock()
    FPS = 60

    # define colours
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLUE = (48, 94, 110)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    LGREEN = (255, 191, 0)

    # define game variables
    intro_count = 3
    last_count_update = pygame.time.get_ticks()
    score = [0, 0]  # player scores. [P1, P2]
    round_over = False
    ROUND_OVER_COOLDOWN = 1900

    # define fighter variables
    WARRIOR_ANIMATION_STEPS, WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET, IMAGE_LINK = retrieve_data_from_database(warr)
    # WARRIOR_SIZE = W_SI
    # WARRIOR_SCALE = W_SC
    # WARRIOR_OFFSET = W_OFF
    WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

    WIZARD_ANIMATION_STEPS, WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET, IMAGE_LINK2 = retrieve_data_from_database(warr2)
    # WIZARD_SIZE = 250
    # WIZARD_SCALE = 3
    # WIZARD_OFFSET = [112, 107]
    WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

    # load music and sounds
    pygame.mixer.music.load("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/audio/music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)
    sword_fx = pygame.mixer.Sound("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/audio/sword.wav")
    sword_fx.set_volume(0.5)
    magic_fx = pygame.mixer.Sound("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/audio/magic.wav")
    magic_fx.set_volume(0.75)

    # check=0 + options()
    # print(check)
    # checked3 = Selection(check).FSelect()

    # load background image
    bg_image = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/background/t1.jpg").convert_alpha()
    bg_image1 = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/background/t4.png").convert_alpha()
    bg_image2 = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/background/Death.jpg").convert_alpha()
    bg_image3 = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/background/fire1.jpg").convert_alpha()
    bg_image4 = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/background/desert.jpg").convert_alpha()
    # bg_image5 = pygame.image.load(
    #   "C:/Users/Admin/PycharmProjects/FingerFlexFury/assets/images/background/desert.jpg").convert_alpha()
    logo_image = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/logo/logo.png").convert_alpha()
    # load spritesheets
    warrior_sheet = pygame.image.load(IMAGE_LINK).convert_alpha()
    wizard_sheet = pygame.image.load(IMAGE_LINK2).convert_alpha()

    victory_img = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/images/Vict1.png").convert_alpha()
    playerone_img = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/images/P11.png").convert_alpha()
    playertwo_img = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/images/P22.png").convert_alpha()
    pause_image = pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/background/pause.png").convert_alpha()
    # Score
    score = [score[0], score[1]]
    checked = GameData()
    checked2 = Selection(warr)
    checked3 = checked2.FSelect()
    checkedb = Selection(warr2)
    checkedc = checked2.FSelect()

    # define number of steps in each animation
    if warr==6:
      WARRIOR_ANIMATION_STEPS = [10, 8, 6, 7, 6, 3, 11, 9]
    elif warr==4:
      WARRIOR_ANIMATION_STEPS = [8, 8, 2, 4, 4, 4, 6, 4]
    else:
      WARRIOR_ANIMATION_STEPS = [8, 8, 2, 5, 5, 3, 8, 7]

    if warr2==3:
      WIZARD_ANIMATION_STEPS = [8, 8, 2, 6, 6, 4, 6]
    elif warr2==1:
      WIZARD_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7, 8]
    else:
      WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

    # define font
    count_font = pygame.font.Font("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/fonts/turok.ttf", 80)
    score_font = pygame.font.Font("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/fonts/turok.ttf", 30)

    # function for drawing text
    def draw_text(text, font, text_col, x, y):
      img = font.render(text, True, text_col)
      screen.blit(img, (x, y))

    # Function to draw BackGround while pause
    def pause():
      paused = True
      while paused:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
              paused = False
        p_bg = pygame.transform.scale(pause_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(p_bg, (0, 0))
        # screen.fill(RED)
        pygame.display.update()
        clock.tick(5)

    # function for drawing background
    def draw_bg():
      if score[1] == 0 and score[0] == 0:
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        scaled_logo = pygame.transform.scale(logo_image, (280, 180))
        screen.blit(scaled_bg, (0, 0))
        screen.blit(scaled_logo, (350, -30))
      elif score[1] + score[0] == 1 and fighter_1.alive == True and fighter_2.alive == True or score[1] + score[0] == 2 and fighter_1.alive == False or fighter_2.alive == False:
        scaled_bg = pygame.transform.scale(bg_image1, (SCREEN_WIDTH, SCREEN_HEIGHT))
        scaled_logo = pygame.transform.scale(logo_image, (280, 180))
        screen.blit(scaled_bg, (0, 0))
        screen.blit(scaled_logo, (350, -30))
      elif score[1] + score[0] == 2 and fighter_1.alive == True and fighter_2.alive == True or score[1] + score[0] == 3 and fighter_1.alive == False or fighter_2.alive == False:
        scaled_bg = pygame.transform.scale(bg_image2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        scaled_logo = pygame.transform.scale(logo_image, (280, 180))
        screen.blit(scaled_bg, (0, 0))
        screen.blit(scaled_logo, (350, -30))
      elif score[1] + score[0] == 3 and fighter_1.alive == True and fighter_2.alive == True or score[1] + score[0] == 4 and fighter_1.alive == False or fighter_2.alive == False:
        scaled_bg = pygame.transform.scale(bg_image3, (SCREEN_WIDTH, SCREEN_HEIGHT))
        scaled_logo = pygame.transform.scale(logo_image, (280, 180))
        screen.blit(scaled_bg, (0, 0))
        screen.blit(scaled_logo, (350, -30))
      elif score[1] + score[0] == 4 and fighter_1.alive == True and fighter_2.alive == True or score[1] + score[0] == 5 and fighter_1.alive == False or fighter_2.alive == False:
        scaled_bg = pygame.transform.scale(bg_image4, (SCREEN_WIDTH, SCREEN_HEIGHT))
        scaled_logo = pygame.transform.scale(logo_image, (280, 180))
        screen.blit(scaled_bg, (0, 0))
        screen.blit(scaled_logo, (350, -30))
      else:
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        scaled_logo = pygame.transform.scale(logo_image, (280, 180))
        screen.blit(scaled_bg, (0, 0))
        screen.blit(scaled_logo, (350, -30))

    # function for drawing fighter health bars
    def draw_health_bar(health, x, y):
      ratio = health / 100
      pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
      pygame.draw.rect(screen, RED, (x, y, 400, 30))
      pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

    def draw_guard(guard, x, y):
      ratio1 = guard / 50
      pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
      pygame.draw.rect(screen, RED, (x, y, 400, 30))
      pygame.draw.rect(screen, BLUE, (x, y, 400 * ratio1, 30))

    def draw_circle(circle, x, y):
      pygame.draw.circle(screen, WHITE, (x, y), 15)
      pygame.draw.circle(screen, BLACK, (x, y), 13)
      pygame.draw.circle(screen, WHITE, (x + 35, y), 15)
      pygame.draw.circle(screen, BLACK, (x + 35, y), 13)
      pygame.draw.circle(screen, WHITE, (x + 70, y), 15)
      pygame.draw.circle(screen, BLACK, (x + 70, y), 13)
      pygame.draw.circle(screen, WHITE, (x + 105, y), 15)
      pygame.draw.circle(screen, BLACK, (x + 105, y), 13)
      pygame.draw.circle(screen, WHITE, (x + 140, y), 15)
      pygame.draw.circle(screen, BLACK, (x + 140, y), 13)

    def draw_vic_circle(circle, round_over, x, y):
      warrior = checked.checking2()
      wizard = checked.checking()

      if score[0] == 1:
        pygame.draw.circle(screen, GREEN, (x, y), 11)
        # pygame.draw.circle(screen, RED, (x + 570, y - 5), 11)
      if score[1] == 1:
        # pygame.draw.circle(screen, RED, (x, y), 11)
        pygame.draw.circle(screen, GREEN, (x + 570, y - 5), 11)
      if score[0] == 2:
        pygame.draw.circle(screen, GREEN, (x + 35, y), 11)
        # pygame.draw.circle(screen, RED, (x + 605, y - 5), 11)
      if score[1] == 2:
        # pygame.draw.circle(screen, RED, (x + 35, y), 11)
        pygame.draw.circle(screen, GREEN, (x + 605, y - 5), 11)
      if score[0] == 3:
        pygame.draw.circle(screen, GREEN, (x + 70, y), 11)
        # pygame.draw.circle(screen, RED, (x + 640, y - 5), 11)
      if score[1] == 3:
        # pygame.draw.circle(screen, RED, (x + 70, y), 11)
        pygame.draw.circle(screen, GREEN, (x + 640, y - 5), 11)
      if score[0] == 4:
        pygame.draw.circle(screen, GREEN, (x + 105, y), 11)
        # pygame.draw.circle(screen, RED, (x + 675, y - 5), 11)
      if score[1] == 4:
        # pygame.draw.circle(screen, RED, (x + 105, y), 11)
        pygame.draw.circle(screen, GREEN, (x + 675, y - 5), 11)

    def round_img(x, y):
      if score[1] + score[0] >= 5:
        score[1] = 0
        score[0] = 0
        # database clearing and new game data insertion
        gClear = checked.NewG_data()

      if score[1] == 0 and score[0] == 0:
        round1_img = pygame.image.load(
          "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/rounds/round1.png").convert_alpha()
      elif score[1] == 1 and score[0] == 0 or score[1] == 0 and score[0] == 1:
        round1_img = pygame.image.load(
          "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/rounds/round2.png").convert_alpha()
      elif score[1] == 2 and score[0] == 1 or score[1] == 1 and score[0] == 2 or score[1] == 2 and score[0] == 2 or \
              score[1] == 1 and score[0] == 1 or score[1] == 0 and score[0] == 2 or score[0] == 0 and score[1] == 2:
        round1_img = pygame.image.load(
          "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/rounds/round3.png").convert_alpha()
      else:
        round1_img = pygame.image.load(
          "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/rounds/round3.png").convert_alpha()
      screen.blit(round1_img, (x, y))

    # create two instances of fighters
    fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
    fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

    # game loop
    run = True
    while run:

      clock.tick(FPS)

      # draw background
      draw_bg()

      # show player stats
      draw_health_bar(fighter_1.health, 20, 20)
      draw_health_bar(fighter_2.health, 580, 20)
      draw_circle(fighter_1.circle, 90, 80)
      draw_circle(fighter_2.circle, 660, 75)
      draw_guard(fighter_2.guard, 580, 95)
      draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
      draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)
      draw_vic_circle(fighter_1.circle, round_over, 90, 80)
      draw_vic_circle(fighter_2.circle, round_over, 90, 80)

      # update countdown
      if intro_count <= 0:
        # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
      else:
        # display count timer
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        # update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
          intro_count -= 1
          last_count_update = pygame.time.get_ticks()

      # update fighters
      fighter_1.update()
      fighter_2.update()

      # draw fighters
      fighter_1.draw(screen)
      fighter_2.draw(screen)

      checking = 0
      checking2 = 0

      if score[1] + score[0] >= 5:
        checking2 = checked.checking2()
        checking = checked.checking()

      if intro_count == 3 or intro_count == 2 or intro_count == 1:
        round_img(260, 80)

      # check for player defeat
      if round_over == False:
        if fighter_1.alive == False:
          score[1] += 1
          InsScore2 = checked.update_score2()
          draw_vic_circle(fighter_1.circle, round_over, 90, 80)
          round_over = True
          round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
          score[0] += 1
          InsScore = checked.update_score()
          round_over = True
          round_over_time = pygame.time.get_ticks()
      else:
        if checking > checking2:
          draw_text("P1 Won: " + str(score[0]), score_font, BLACK, 320, 150)
          screen.blit(playerone_img, (380, 130))
          screen.blit(victory_img, (380, 250))
        elif checking < checking2:
          draw_text("P2 Won: " + str(score[1]), score_font, BLACK, 320, 150)
          screen.blit(playertwo_img, (380, 130))
          screen.blit(victory_img, (380, 250))
        else:
          draw_text("Get Ready Fight is About To Begin !!!! ", score_font, BLACK, 260, 150)
        # display victory image
        # screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
          round_over = False
          intro_count = 3
          fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
          fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

      # event handler
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_p:
            pause()

      # update display
      pygame.display.update()

    # exit pygame
    pygame.quit()

def options():
  warrior = "Samurai"
  warrior1 = "Neith"
  global warr
  global warr2
  while True:
    OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    selectbg=pygame.image.load("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/warrior/Sprites/selectbg.png").convert_alpha()
    SCREEN.fill("White")
    F1 = Button1(image=pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/warrior/Sprites/char.png").convert_alpha(), pos=(845, 145),
                          text_input="Samurrai", font=get_font(20), base_color="Light Blue", hovering_color="Green")
    F2 = Button1(image=pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/warrior/Sprites/cha.png").convert_alpha(),
                 pos=(585, 145),
                 text_input="Logger", font=get_font(20), base_color="Light Blue", hovering_color="Green")
    F3 = Button1(image=pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/warrior/Sprites/king3.png").convert_alpha(),
                 pos=(522, 325),
                 text_input="King", font=get_font(20), base_color="Light Blue", hovering_color="Green")
    F4 = Button1(image=pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/warrior/Sprites/char4.png").convert_alpha(),
                 pos=(784, 325),
                 text_input="Warrior", font=get_font(20), base_color="Light Blue", hovering_color="Green")
    F5 = Button1(image=pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/warrior/Sprites/char2.png").convert_alpha(),
                 pos=(465, 495),
                 text_input="Neith", font=get_font(20), base_color="Light Blue", hovering_color="Green")
    F6 = Button1(image=pygame.image.load(
      "C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/assets/images/warrior/Sprites/char3.png").convert_alpha(),
                 pos=(725, 495),
                 text_input="Witch", font=get_font(20), base_color="Light Blue", hovering_color="Green")
    F1.changeColor(OPTIONS_MOUSE_POS)
    F1.update(SCREEN)
    F2.changeColor(OPTIONS_MOUSE_POS)
    F2.update(SCREEN)
    F3.changeColor(OPTIONS_MOUSE_POS)
    F3.update(SCREEN)
    F4.changeColor(OPTIONS_MOUSE_POS)
    F4.update(SCREEN)
    F5.changeColor(OPTIONS_MOUSE_POS)
    F5.update(SCREEN)
    F6.changeColor(OPTIONS_MOUSE_POS)
    F6.update(SCREEN)
    SCREEN.blit(selectbg,(0,-120))

    SCREEN.blit(get_font(35).render("Character", True, "Black"), (990, 220))
    SCREEN.blit(get_font(35).render("Selected :" + warrior, True, "Black"), (990, 250))
    SCREEN.blit(get_font(35).render("Character", True, "Black"), (10, 520))
    SCREEN.blit(get_font(35).render("Selected :" + warrior1, True, "Black"), (10, 550))
    OPTIONS_BACK = Button(image=None, pos=(200, 50),
                          text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

    OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
    OPTIONS_BACK.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
          main_menu()
        if F1.checkForInput(OPTIONS_MOUSE_POS):
          warrior="Samurai"
          warr2 = 3
        if F2.checkForInput(OPTIONS_MOUSE_POS):
          warr = 6
          warrior1="Logger"
        if F3.checkForInput(OPTIONS_MOUSE_POS):
          warrior1="King"
          warr = 4
        if F4.checkForInput(OPTIONS_MOUSE_POS):
          warrior="Warrior"
          warr2 = 1
        if F5.checkForInput(OPTIONS_MOUSE_POS):
          warrior1="Neith"
          warr = 2
        if F6.checkForInput(OPTIONS_MOUSE_POS):
          warrior="Witch"
          warr2 = 5

    pygame.display.update()



def main_menu():
  while True:
    SCREEN.blit(BG, (-50, 0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 250))

    PLAY_BUTTON = Button(image=pygame.image.load("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/Images/Play Rect.png"), pos=(640, 370),
                         text_input="PLAY", font=get_font(75), base_color="WHITE", hovering_color="#d7fcd4")
    OPTIONS_BUTTON = Button(image=pygame.image.load("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/Images/Options Rect.png"), pos=(640, 500),
                            text_input="Characters", font=get_font(75), base_color="WHITE", hovering_color="#d7fcd4")
    QUIT_BUTTON = Button(image=pygame.image.load("C:/Users/Dnyaneshwar Parmekar/PycharmProjects/FingerFlexFury/Images/Quit Rect.png"), pos=(640, 630),
                         text_input="QUIT", font=get_font(75), base_color="WHITE", hovering_color="#d7fcd4")

    SCREEN.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
      button.changeColor(MENU_MOUSE_POS)
      button.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
          play()
        if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
          options()

        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
          pygame.quit()
          sys.exit()

    pygame.display.update()


main_menu()
