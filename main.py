import math
import random
import pygame
from pygame import mixer
from time import time

multiplier = 1
num_of_invaders = 6
score_to_add = 5


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
        if score > 150:
            if random.randint(0, 60) % 60 == 0:
                self.image = pygame.image.load("bullets.png")
                self.special = 1  # random.randint(1, 3)
        elif score > 500:
            if random.randint(0, 100) % 100 == 0:
                self.image = pygame.image.load("bullets.png")
                self.special = 1  # random.randint(1, 3)
        elif score > 35:
            if random.randint(0, 40) % 40 == 0:
                self.image = pygame.image.load("bullets.png")
                self.special = 1  # random.randint(1, 3)


def update_locations():
    global bullets
    global epoch
    global score_value
    for i, bullet in enumerate(bullets):
        bullet.move()
        if len(bullets) != 1:
            screen.blit(pygame.image.load("bullets.png"), (730, 540))
        else:
            screen.blit(pygame.image.load("bullet.png"), (755, 555))
        if len(bullets) != 1 and time() > epoch + 5:
            if bullet.x < 475:
                bullets.pop(i)
                continue
    player.move()
    for enemy in invaders:
        enemy.move()
        for bullet in bullets:
            if collision(enemy, enemy.x, enemy.y, bullet.x, bullet.y):
                mixer.Sound("explosion.wav").play()
                enemy.reset(score_value)
                score_value += 1
                bullet.state = False
                bullet.reset()
                if score_value % score_to_add == 0:
                    invaders.append(Invaders())
    time_x = 640 - 13 * (len(str(round(time() - 0.5 - time_since_start))) % 10)
    screen.blit(score_font.render(f"Score: {score_value}", True, (255, 255, 255)), (10, 10))
    screen.blit(score_font.render(f"Time: {round(time() - time_since_start, 2)}", True, (255, 255, 255)), (time_x, 10))


def game_over():
    global invaders
    global score_value

    mixer.Sound("game_over.wav").play()
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
                    loading_screen()


def key_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.delta_X = -4.5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.delta_X = 4.5
            if event.key == pygame.K_SPACE:
                for bullet in bullets:
                    if not bullet.state:
                        mixer.Sound("laser.wav").play()
                        bullet.x = player.x
                        bullet.state = True
                        break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                player.delta_X = 0


def give_ability(ability):
    global epoch
    mixer.Sound("mystery_box.wav").play()

    epoch = time()

    if ability == 1:
        for _ in range(2):
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
    while True:
        screen.blit(pygame.image.load("background.png"), (0, 0))
        screen.blit(pygame.font.Font("freesansbold.ttf", 48).render(f"Welcome to Space Invaders!", True, (255, 255, 255)), (60, 100))
        screen.blit(pygame.image.load("player.png"), (360, 300))
        screen.blit(pygame.image.load("bullet.png"), (376, 260))
        screen.blit(pygame.image.load("enemy.png"), (360, 190))
        screen.blit(score_font.render("Press Any Key to Start!", True, (255, 255, 255)), (220, 420))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                mixer.Sound("starting.wav").play()
                main()
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load("background.png")

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

        loading_screen()
        main()
