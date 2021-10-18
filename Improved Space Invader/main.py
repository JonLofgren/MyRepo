import math
import random
import pygame
from pygame import mixer
from time import time

default_values = ["Multiplier: 1.0\n", "Starting invader count: 6\n", "How many points to add an invader: 5\n",
                  "Powerup additional bullets: 2\n", "Hold space: 1\n", "Sound: 1\n"]

settings = [1, 6, 5, 2, 1, 1]

rect = {0: 170, 1: 380, 2: 585, 3: 453, 4: 195, 5: 120}


class Player:
    def __init__(self):
        self.image = pygame.image.load("player.png")
        self.x = 370
        self.y = 480
        self.delta_X = 0

    def move(self):
        self.x += self.delta_X * multiplier
        screen.blit(self.image, (self.x, self.y))
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

    def reset(self):
        self.__init__()


class Bullet:
    def __init__(self):
        self.image = pygame.image.load("bullet.png")
        self.x = 0
        self.y = 480
        self.delta_y = -6
        self.state = False

    def move(self):
        if self.state:
            self.y += self.delta_y * multiplier
            screen.blit(self.image, (self.x + 16, self.y + 10))
            if self.y < 0:
                self.state = False
                self.__init__()

    def reset(self):
        self.__init__()


class Invaders:
    def __init__(self):
        self.image = pygame.image.load("enemy.png")
        self.x = random.randint(0, 735)
        self.y = random.randint(50, 150)
        self.delta_x = 3 * multiplier
        self.delta_y = 40

        self.special = 0

    def move(self):
        self.x += self.delta_x
        if self.x <= 0:
            self.delta_x *= -1
            self.y += self.delta_y
        elif self.x >= 736:
            self.delta_x *= -1
            self.y += self.delta_y
        if self.y > 440:
            game_over()
        screen.blit(self.image, (self.x, self.y))

    def reset(self, score=0):
        self.__init__()
        if score > 500:
            if random.randint(0, 125) % 125 == 0:
                self.image = pygame.image.load("bullets.png")
                self.special = 1  # random.randint(1, 3)
        elif score > 150:
            if random.randint(0, 75) % 75 == 0:
                self.image = pygame.image.load("bullets.png")
                self.special = 1  # random.randint(1, 3)
        elif score > 0:
            if random.randint(0, 50) % 50 == 0:
                self.image = pygame.image.load("bullets.png")
                self.special = 1  # random.randint(1, 3)


def update_locations():
    global bullets
    global epoch
    global score_value

    screen.blit(pygame.transform.scale(pygame.image.load("enemy.png"), (40, 40)), (15, 552))
    screen.blit(pygame.font.Font("freesansbold.ttf", 22).render(f"{len(invaders)}", True, (255, 255, 255)), (65, 565))
    x = 755 - 12 * (len(str(len(bullets))))
    screen.blit(pygame.font.Font("freesansbold.ttf", 22).render(f"{len(bullets)}", True, (255, 255, 255)), (x, 565))

    for i, bullet in enumerate(bullets):
        bullet.move()

        screen.blit(pygame.image.load("bullet.png"), (755, 555))
        if len(bullets) != 1 and time() > epoch + 5:
            if bullet.x < 460:
                bullets.pop(i)
                continue
    player.move()
    for enemy in invaders:
        enemy.move()
        for bullet in bullets:
            if collision(enemy, enemy.x, enemy.y, bullet.x, bullet.y):
                if sound:
                    mixer.Sound("explosion.wav").play()
                enemy.reset(score_value)
                score_value += 1
                bullet.state = False
                bullet.reset()
                if score_value % score_to_add == 0:
                    invaders.append(Invaders())
    time_x = 640 - 14 * (len(str(round(time() - 0.5 - time_since_start))) % 10)
    screen.blit(score_font.render(f"Score: {score_value}", True, (255, 255, 255)), (10, 10))
    screen.blit(score_font.render(f"Time: {round(time() - time_since_start, 2)}", True, (255, 255, 255)), (time_x, 10))


def game_over():
    global invaders
    global score_value
    global space
    space = False

    if sound:
        mixer.Sound("game_over.wav").play()
    screen.blit(pygame.image.load("background.png"), (0, 0))

    screen.blit(score_font.render(f"{round(time() - time_since_start, 2)}s", True, (255, 255, 255)), (360, 205))
    screen.blit(end_font.render(f"GAME OVER", True, (255, 255, 255)), (200, 245))

    try:
        with open("high_score.txt", "r") as f_r:
            high_score = int(f_r.read()[:-1])
    except FileNotFoundError:
        with open("high_score.txt", "w") as f_e:
            f_e.write(f"{score_value}\n")
        high_score = score_value
    if high_score < score_value:
        with open("high_score.txt", "w") as f_w:
            f_w.write(f"{score_value}\n")
            high_score = score_value
    screen.blit(score_font.render(f"Score: {score_value}", True, (255, 255, 255)), (335, 315))
    screen.blit(score_font.render(f"High Score: {high_score}", True, (255, 255, 255)), (290, 360))
    screen.blit(score_font.render(f"Press \"ESC\" To Continue", True, (255, 255, 255)), (200, 410))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player.reset()
                    for bullet in bullets:
                        bullet.reset()
                        bullet.state = False
                    for enemy in invaders:
                        enemy.reset()
                    score_value = 0
                    invaders = []
                    for _ in range(num_of_invaders):
                        invaders.append(Invaders())
                    if sound:
                        mixer.Sound("key_press.wav").play()
                    loading_screen()


def key_handler():
    global space
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.delta_X = -4.5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.delta_X = 4.5
            if event.key == pygame.K_SPACE:
                if hold_space:
                    space = True
                else:
                    for bullet in bullets:
                        if not bullet.state:
                            if sound:
                                mixer.Sound("laser.wav").play()
                            bullet.x = player.x
                            bullet.state = True
                            break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT\
                    or event.key == pygame.K_a or event.key == pygame.K_d:
                player.delta_X = 0
            if event.key == pygame.K_SPACE:
                space = False
    if hold_space and space:
        for bullet in bullets:
            if not bullet.state:
                if sound:
                    mixer.Sound("laser.wav").play()
                bullet.x = player.x
                bullet.state = True
                break


def give_ability(ability):
    global epoch
    if sound:
        mixer.Sound("mystery_box.wav").play()

    epoch = time()

    if ability == 1:
        for _ in range(powerup_bullets):
            bullets.append(Bullet())

    elif ability == 2:
        pass
    elif ability == 3:
        pass
    else:
        print("ERROR")


def collision(enemy, enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 27:
        if enemy.special != 0:
            give_ability(enemy.special)
        return True
    else:
        return False


def load_conf():
    try:
        with open("config.conf", "r") as config:
            for index, values in enumerate(config):
                settings[index] = float(values[values.index(":") + 1:-1])
    except FileNotFoundError:
        with open("config.conf", "w") as config:
            for index, values in enumerate(default_values):
                config.write(values)
                settings[index] = float(values[values.index(":") + 1:-1])


def main():
    global time_since_start
    time_since_start = time()
    running = True
    while running:
        screen.blit(background, (0, 0))
        key_handler()
        update_locations()

        pygame.display.update()


def loading_screen():
    try:
        with open("high_score.txt", "r") as file:
            previous_score = file.read()[:-1]
        score_flag = True
    except FileNotFoundError:
        score_flag = False
    while True:
        screen.blit(pygame.image.load("background.png"), (0, 0))
        if score_flag:
            screen.blit(score_font.render("High Score:", True, (255, 255, 255)), (510, 235))
            screen.blit(score_font.render(previous_score, True, (255, 255, 255)), (510, 280))
        screen.blit(score_font.render("Settings (ESC)", True, (255, 255, 255)), (50, 257))
        screen.blit(pygame.font.Font("freesansbold.ttf", 48).render(f"Welcome to Space Invaders!",
                                                                    True, (255, 255, 255)), (60, 100))
        screen.blit(pygame.image.load("player.png"), (360, 300))
        screen.blit(pygame.image.load("bullet.png"), (376, 260))
        screen.blit(pygame.image.load("enemy.png"), (360, 190))
        screen.blit(score_font.render("Press Space to Start!", True, (255, 255, 255)), (230, 420))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if sound:
                    mixer.Sound("key_press.wav").play()
                if event.key == pygame.K_SPACE:
                    main()
                if event.key == pygame.K_ESCAPE:
                    settings_screen()
        pygame.display.update()


def setting_selection(option, val_list):
    k_up = False
    k_down = False
    selection = default_values[option][:default_values[option].index(":") + 1]
    value = val_list[option]
    if option == 0:
        value = float(value)
    else:
        value = int(value)

    while True:
        screen.blit(pygame.image.load("background.png"), (0, 0))
        screen.blit(score_font.render(f"{selection} {value}", True, (255, 255, 255)), (30, 280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if sound:
                    mixer.Sound("key_press.wav").play()

                if event.key == pygame.K_UP:
                    k_up = True
                if event.key == pygame.K_DOWN:
                    k_down = True
                if event.key == pygame.K_RETURN:
                    return value
            if event.type == pygame.KEYUP:
                k_up = False
                k_down = False

            if option == 0:
                if k_up:
                    value += 0.1
                if k_down:
                    value += -0.1
                value = round(value, 1)
                if value <= 1.0:
                    value = 1.0
            elif option == 1 or option == 2 or option == 3:
                if k_up:
                    value += 1
                if k_down:
                    value += -1
                    if value <= 1:
                        value = 1
            elif option == 4 or option == 5:
                if k_up and value < 1:
                    value += 1
                if k_down and value > 0:
                    value += -1

        pygame.display.update()


def conf():
    global multiplier
    global num_of_invaders
    global score_to_add
    global powerup_bullets
    global hold_space
    global sound
    load_conf()

    multiplier = settings[0]
    num_of_invaders = int(settings[1])
    score_to_add = int(settings[2])
    powerup_bullets = int(settings[3])
    hold_space = int(settings[4])
    sound = int(settings[5])


def settings_screen():
    global invaders

    value = []
    setting = []
    position = 0
    offset = 75
    left = 0
    top = 0
    height = 40
    with open("config.conf", "r") as config:
        for values in config:
            value.append(float(values[values.index(":") + 1:-1]))
            setting.append(values[:values.index(":")])
    while True:
        screen.blit(pygame.image.load("background.png"), (0, 0))
        for i, option in enumerate(setting):
            screen.blit(score_font.render(option, True, (255, 255, 255)), (50, 100 + (offset * i)))
        screen.blit(pygame.font.Font("freesansbold.ttf", 48).render(f"Settings", True, (255, 255, 255)), (280, 15))
        screen.blit(pygame.font.Font("freesansbold.ttf", 22).render("Restore (r)", True, (255, 255, 255)), (600, 535))
        screen.blit(pygame.font.Font("freesansbold.ttf", 22).render("Save and Exit (e)",
                                                                    True, (255, 255, 255)), (600, 565))
        pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(left + 40, top + 95, rect[position], height), 3)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if sound:
                    mixer.Sound("key_press.wav").play()
                if event.key == pygame.K_UP:
                    position -= 1
                    if position < 0:
                        position = 0
                    else:
                        top -= offset
                if event.key == pygame.K_DOWN:
                    position += 1
                    if position >= len(setting):
                        position = len(setting) - 1
                    else:
                        top += offset
                if event.key == pygame.K_RETURN:
                    value[position] = setting_selection(position, value)
                if event.key == pygame.K_r:
                    with open("config.conf", "w") as file:
                        for values in default_values:
                            file.write(values)
                    conf()

                    if sound:
                        mixer.music.load("background.wav")
                        mixer.music.play(-1)
                    else:
                        mixer.music.pause()

                    invaders = []
                    for _ in range(num_of_invaders):
                        invaders.append(Invaders())

                    loading_screen()
                if event.key == pygame.K_e:
                    with open("config.conf", "w") as file:
                        for i, line in enumerate(default_values):
                            if i != 0:
                                num = int(value[i])
                            else:
                                num = float(value[i])
                            file.write(f"{line[:line.index(':')]}: {num}\n")
                    conf()

                    if sound:
                        mixer.music.load("background.wav")
                        mixer.music.play(-1)
                    else:
                        mixer.music.pause()

                    invaders = []
                    for _ in range(num_of_invaders):
                        invaders.append(Invaders())

                    loading_screen()


if __name__ == '__main__':
    multiplier = 0
    num_of_invaders = 0
    score_to_add = 0
    powerup_bullets = 0
    hold_space = 0
    sound = 0

    conf()

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load("background.png")
    if sound:
        mixer.music.load("background.wav")
        mixer.music.play(-1)

    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load("ufo.png")
    pygame.display.set_icon(icon)

    while True:
        time_since_start = 0
        player = Player()
        bullets = [Bullet()]

        invaders = []
        for _ in range(num_of_invaders):
            invaders.append(Invaders())

        score_value = 0
        score_font = pygame.font.Font("freesansbold.ttf", 32)
        end_font = pygame.font.Font("freesansbold.ttf", 64)

        epoch = time()

        space = False

        loading_screen()
        main()
