import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

ball = pygame.Rect( 2 - 15, 2 - 15, 30, 30)
player = pygame.Rect( - 20, 2 - 60, 10, 120)
opponent = pygame.Rect(10, 2 - 60, 10, 120)

ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

player_speed = 0
opponent_speed = 5

player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = PADDLE_SPEED
            if event.key == pygame.K_UP:
                player_speed = -PADDLE_SPEED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_speed = 0

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    player.y += player_speed
