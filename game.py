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