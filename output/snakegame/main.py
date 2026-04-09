"""贪吃蛇游戏 - 主入口"""
import pygame
import sys
from game import SnakeGame

def main():
    pygame.init()
    game = SnakeGame()
    game.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
