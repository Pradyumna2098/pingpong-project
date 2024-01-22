import unittest
import pygame
import sys

from game import PingPongGame

class TestPingPongGame(unittest.TestCase):

    def setUp(self):
        pygame.init()

        self.game = PingPongGame(800, 600)

    def tearDown(self):
        pygame.quit()

    def test_initialization(self):
    
        self.assertEqual(self.game.width, 800)
        self.assertEqual(self.game.height, 600)
        self.assertIsInstance(self.game.player, pygame.Rect)
        self.assertIsInstance(self.game.opponent, pygame.Rect)
        self.assertIsInstance(self.game.ball, pygame.Rect)

    def test_ball_movement(self):
    
        initial_ball_position = self.game.ball.x, self.game.ball.y
        self.game.update_game_state()
        updated_ball_position = self.game.ball.x, self.game.ball.y
        self.assertNotEqual(initial_ball_position, updated_ball_position)

    def test_player_movement(self):
    
        initial_player_position = self.game.player.y
        self.game.handle_events(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP}))
        self.game.update_game_state()
        updated_player_position = self.game.player.y
        self.assertNotEqual(initial_player_position, updated_player_position)

    def test_collision_with_walls(self):
    
        self.game.ball.y = 0
        initial_ball_speed_y = self.game.ball_speed_y
        self.game.update_game_state()
        updated_ball_speed_y = self.game.ball_speed_y
        self.assertNotEqual(initial_ball_speed_y, updated_ball_speed_y)

    def test_collision_with_paddles(self):
    
        initial_ball_speed_x = self.game.ball_speed_x
        self.game.ball.x = self.game.player.x
        self.game.update_game_state()
        updated_ball_speed_x = self.game.ball_speed_x
        self.assertNotEqual(initial_ball_speed_x, updated_ball_speed_x)

if __name__ == '__main__':
    unittest.main()
