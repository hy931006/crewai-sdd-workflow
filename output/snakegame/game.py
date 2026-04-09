"""贪吃蛇游戏 - 核心逻辑"""
import pygame
import random
import sys

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("贪吃蛇游戏 - 得分: 0")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset_game()
    
    def reset_game(self):
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.food = self._generate_food()
        self.score = 0
        self.game_over = False
    
    def _generate_food(self):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in self.snake:
                return pos
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self._handle_key(event.key)
            if not self.game_over:
                self._update()
            self._draw()
            self.clock.tick(FPS)
        self._show_game_over()
    
    def _handle_key(self, key):
        if key == pygame.K_UP and self.direction != (0, 1):
            self.direction = (0, -1)
        elif key == pygame.K_DOWN and self.direction != (0, -1):
            self.direction = (0, 1)
        elif key == pygame.K_LEFT and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key == pygame.K_RIGHT and self.direction != (-1, 0):
            self.direction = (1, 0)
        elif key == pygame.K_r and self.game_over:
            self.reset_game()
        elif key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    
    def _update(self):
        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
            new_head in self.snake):
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)
        
        if new_head == self.food:
            self.score += 10
            pygame.display.set_caption(f"贪吃蛇游戏 - 得分: {self.score}")
            self.food = self._generate_food()
        else:
            self.snake.pop()
    
    def _draw(self):
        self.screen.fill(BLACK)
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, (30, 30, 30), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, (30, 30, 30), (0, y), (SCREEN_WIDTH, y))
        
        for i, (x, y) in enumerate(self.snake):
            color = GREEN if i == 0 else DARK_GREEN
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(self.screen, color, rect)
        
        food_rect = pygame.Rect(self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE, 
                                  CELL_SIZE - 2, CELL_SIZE - 2)
        pygame.draw.rect(self.screen, RED, food_rect)
        
        score_text = self.font.render(f"得分: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        hint = self.font.render("方向键移动 | R键重来 | ESC退出", True, (150, 150, 150))
        self.screen.blit(hint, (SCREEN_WIDTH - 400, SCREEN_HEIGHT - 40))
        pygame.display.flip()
    
    def _show_game_over(self):
        self.screen.fill(BLACK)
        font_large = pygame.font.Font(None, 72)
        font_small = pygame.font.Font(None, 36)
        go_text = font_large.render("游戏结束!", True, RED)
        score_text = font_small.render(f"最终得分: {self.score}", True, WHITE)
        restart_text = font_small.render("按 R 键重新开始", True, GREEN)
        self.screen.blit(go_text, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 60))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 90, SCREEN_HEIGHT // 2))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.run()
                        return
                    elif event.key == pygame.K_ESCAPE:
                        waiting = False

if __name__ == "__main__":
    pygame.init()
    game = SnakeGame()
    game.run()
    pygame.quit()
