import pygame

import webbrowser

pygame.init()  # initialize all imported PyGame modules

WIDTH, HEIGHT = 700, 500
WHITE = (255, 255, 255)
base_font = pygame.font.Font(None, 32)
base_font2 = pygame.font.Font(None, 80)
user_text = ''
winnerSound = pygame.mixer.Sound('subtract a square assets/sound effects/Winner sound effect.mp3')
beepSound = pygame.mixer.Sound('subtract a square assets/sound effects/beep sound effect.mp3')
start_menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 220
player_number = 0


def button(scaleX, scaleY, x, y, image):
    image1 = pygame.transform.scale(pygame.image.load(image), (scaleX, scaleY)).convert_alpha()
    return start_menu_screen.blit(image1, (x, y))


def buttonAction(scaleX, scaleY, x, y, button1, image):
    image2 = pygame.transform.scale(pygame.image.load(image), (scaleX, scaleY)).convert_alpha()
    mouse_position = pygame.mouse.get_pos()
    if button1.collidepoint(mouse_position):
        start_menu_screen.blit(image2, (x, y))
        if pygame.mouse.get_pressed()[0]:
            return True


def buttons():
    if buttonAction(100, 75, 250, 245,
                    button(100, 75, 250, 245, 'subtract a square assets\s1.png'),
                    'subtract a square assets\s1-dark.png'):
        return 1

    elif buttonAction(100, 75, 360, 245,
                      button(100, 75, 360, 245, 'subtract a square assets\s4.png'),
                      'subtract a square assets\s4-dark.png'):
        return 4
    elif buttonAction(100, 75, 470, 245,
                      button(100, 75, 470, 245, 'subtract a square assets\s9.png'),
                      'subtract a square assets\s9-dark.png'):
        return 9
    elif buttonAction(100, 75, 580, 245,
                      button(100, 75, 580, 245,
                             'subtract a square assets\s16.png'), 'subtract a square assets\s16-dark.png'):
        return 16
    elif buttonAction(100, 75, 250, 335,
                      button(100, 75, 250, 335,
                             'subtract a square assets\s25.png'), 'subtract a square assets\s25-dark.png'):
        return 25
    elif buttonAction(100, 75, 360, 335,
                      button(100, 75, 360, 335,
                             'subtract a square assets\s36.png'), 'subtract a square assets\s36-dark.png'):
        return 36
    elif buttonAction(100, 75, 470, 335,
                      button(100, 75, 470, 335,
                             'subtract a square assets\s49.png'), 'subtract a square assets\s49-dark.png'):
        return 49
    elif buttonAction(100, 75, 580, 335,
                      button(100, 75, 580, 335,
                             'subtract a square assets\s64.png'), 'subtract a square assets\s64-dark.png'):
        return 64


def player1Wins():
    frameRate = pygame.time.Clock()
    while True:
        frameRate.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game_screen.fill(WHITE)

        QUIT_BUTTON = button(150, 100, 550, 400, 'subtract a square assets\quit.png')
        if buttonAction(150, 100, 550, 400, QUIT_BUTTON, 'subtract a square assets\quit-2.png'):
            pygame.quit()

        button(600, 400, 50, 0, 'subtract a square assets\sfirst-player-wins.png')

        PLAY_AGAIN_BUTTON = button(300, 200, 200, 240, 'subtract a square assets\play-again.png')
        if buttonAction(300, 200, 200, 240, PLAY_AGAIN_BUTTON, 'subtract a square assets\play-again-dark.png'):
            startMenu()

        pygame.display.update()


def player2Wins():
    frameRate = pygame.time.Clock()
    while True:
        frameRate.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game_screen.fill(WHITE)

        QUIT_BUTTON = button(150, 100, 550, 400, 'subtract a square assets\quit.png')
        if buttonAction(150, 100, 550, 400, QUIT_BUTTON, 'subtract a square assets\quit-2.png'):
            pygame.quit()

        button(600, 400, 50, 0, 'subtract a square assets\second-player-wins.png')

        PLAY_AGAIN_BUTTON = button(300, 200, 200, 240, 'subtract a square assets\play-again.png')
        if buttonAction(300, 200, 200, 240, PLAY_AGAIN_BUTTON, 'subtract a square assets\play-again-dark.png'):
            startMenu()

        pygame.display.update()


def player1(minuend):
    frameRate = pygame.time.Clock()
    while True:
        frameRate.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        game_screen.fill(WHITE)
        button(800, 600, -50, -130, 'subtract a square assets\subtract-a-square-logo.png')

        QUIT_BUTTON = button(150, 100, 550, 400, 'subtract a square assets\quit.png')
        if buttonAction(150, 100, 550, 400, QUIT_BUTTON, 'subtract a square assets\quit-2.png'):
            pygame.quit()

        button(520, 350, 185, 120, 'subtract a square assets\player-choices-board.png')

        button(260, 175, 15, 145, 'subtract a square assets\player-one-turn.png')

        button(260, 175, 15, 280, 'subtract a square assets\snumber-of-nodes.png')

        text_surface = base_font2.render(str(minuend), True, (214, 131, 64))
        game_screen.blit(text_surface, (120, 360))

        if buttons() is not None:
            if minuend - buttons() < 0:
                beepSound.play()
                player1(minuend)

            elif minuend - buttons() == 0:
                winnerSound.play()
                player1Wins()

            elif minuend - buttons() > 0:
                break
        pygame.display.update()
    player2(minuend - buttons())


def player2(minuend):
    frameRate = pygame.time.Clock()
    while True:
        frameRate.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        game_screen.fill(WHITE)
        button(800, 600, -50, -130, 'subtract a square assets\subtract-a-square-logo.png')

        QUIT_BUTTON = button(150, 100, 550, 400, 'subtract a square assets\quit.png')
        if buttonAction(150, 100, 550, 400, QUIT_BUTTON, 'subtract a square assets\quit-2.png'):
            pygame.quit()

        button(520, 350, 185, 120, 'subtract a square assets\player-choices-board.png')

        button(260, 175, 15, 145, 'subtract a square assets\player-two-turn.png')

        button(260, 175, 15, 280, 'subtract a square assets\snumber-of-nodes.png')

        text_surface = base_font2.render(str(minuend), True, (214, 131, 64))
        game_screen.blit(text_surface, (120, 360))

        if buttons() is not None:

            if minuend - buttons() < 0:
                beepSound.play()
                player2(minuend)

            elif minuend - buttons() == 0:
                winnerSound.play()
                player2Wins()

            elif minuend - buttons() > 0:
                break
        pygame.display.update()
    player1(minuend - buttons())


def mainGameScreen():
    user_input = ''
    frameRate = pygame.time.Clock()
    while True:
        frameRate.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key != pygame.K_BACKSPACE and len(user_input) < 2:
                    user_input += event.unicode
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    player1(int(user_input))

        text_surface = base_font.render(user_input, True, (214, 131, 64))
        game_screen.blit(text_surface, (370, 140))

        pygame.display.update()

        mainGameDesign()


def mainGameDesign():
    game_screen.fill(WHITE)
    button(800, 600, -50, -130, 'subtract a square assets\subtract-a-square-logo.png')

    button(400, 300, 40, 0, 'subtract a square assets\start-number-2.png')

    QUIT_BUTTON = button(150, 100, 550, 400, 'subtract a square assets\quit.png')
    if buttonAction(150, 100, 550, 400, QUIT_BUTTON, 'subtract a square assets\quit-2.png'):
        pygame.quit()

    pygame.display.update()


def startMenuDesign():
    start_menu_screen.fill(WHITE)
    button(800, 600, -50, -90, 'subtract a square assets\welcome-logo.png')

    startButton = button(300, 200, 200, 150, 'subtract a square assets\start.png')
    if buttonAction(300, 200, 200, 150, startButton, 'subtract a square assets/start-2.png'):
        return True

    HOW_TO_PLAY_BUTTON = button(150, 100, 550, 400, 'subtract a square assets\how-to-play.png')
    if buttonAction(150, 100, 550, 400, HOW_TO_PLAY_BUTTON, 'subtract a square assets\how-to-play-2.png'):
        webbrowser.open('http://en.wikipedia.org/wiki/Subtract_a_square')

    QUIT_BUTTON = button(300, 200, 200, 280, 'subtract a square assets\quit.png')
    if buttonAction(300, 200, 200, 280, QUIT_BUTTON, 'subtract a square assets\quit-2.png'):
        pygame.quit()

    pygame.display.update()


def startMenu():
    frameRate = pygame.time.Clock()
    while True:
        frameRate.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        startMenuDesign()
        if startMenuDesign() is True:
            mainGameScreen()


if __name__ == '__main__':
    startMenu()
