import pygame
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
BALL_SPEED = 1
PADDLE_SPEED = 3

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)
opponent = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)

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

    player.y = max(0, min(player.y, HEIGHT - player.height))

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    if ball.left <= 0:
        player_score += 1
        if player_score == 20:
            print("Player wins!")
            pygame.quit()
            quit()
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    if ball.right >= WIDTH:
        opponent_score += 1
        if opponent_score == 20:
            print("Opponent wins!")
            pygame.quit()
            quit()
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)

    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 50))
    screen.blit(opponent_text, (3 * WIDTH // 4 - 30, 50))

    pygame.display.flip()