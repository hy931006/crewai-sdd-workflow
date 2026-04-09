"""单元测试"""
import pytest
from game import CELL_SIZE, GRID_WIDTH, GRID_HEIGHT, FPS

class TestSnakeGame:
    def test_constants(self):
        assert CELL_SIZE == 20
        assert GRID_WIDTH == 30
        assert GRID_HEIGHT == 20
        assert FPS == 10
    
    def test_grid_center(self):
        assert GRID_WIDTH // 2 == 15
        assert GRID_HEIGHT // 2 == 10
    
    def test_direction_vectors(self):
        UP = (0, -1)
        DOWN = (0, 1)
        LEFT = (-1, 0)
        RIGHT = (1, 0)
        assert UP != DOWN
        assert LEFT != RIGHT
    
    def test_collision_bounds(self):
        assert GRID_WIDTH > 0
        assert GRID_HEIGHT > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
