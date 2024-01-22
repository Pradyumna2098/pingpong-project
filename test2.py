import pygame
import random

class PingPongGame:
    def __init__(self, width, height):
        pygame.init()

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Ping Pong Game")

        self.ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)
        self.player = pygame.Rect(width - 20, height // 2 - 60, 10, 120)
        self.opponent = pygame.Rect(10, height // 2 - 60, 10, 120)

        self.ball_speed_x = random.choice([1, -1])
        self.ball_speed_y = random.choice([1, -1])

        self.player_speed = 0
        self.opponent_speed = 5

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player_speed = -5
            elif event.key == pygame.K_DOWN:
                self.player_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player_speed = 0

    def update_game_state(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y
        self.player.y += self.player_speed


    def check_collision_with_walls(self):
        if self.ball.top <= 0 or self.ball.bottom >= self.height:
            self.ball_speed_y *= -1

    def check_collision_with_paddles(self):
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
            self.ball_speed_x *= -1

    def reset_ball(self):
        self.ball = pygame.Rect(self.width // 2 - 15, self.height // 2 - 15, 30, 30)
        self.ball_speed_x = random.choice([1, -1])
        self.ball_speed_y = random.choice([1, -1])
