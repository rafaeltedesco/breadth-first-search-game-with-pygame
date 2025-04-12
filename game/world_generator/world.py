import pygame
from game.consts import COLORS, MAP

class World:

    MAP = MAP
    COLORS_MAPPER = {
        "S": COLORS.GREEN,
        "E": COLORS.GREEN,
        "0": COLORS.GRAY,
        "1": COLORS.BLUE
    }
    TILE_SIZE = 40
    ROWS, COLS = len(MAP), len(MAP[0])
    WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE

    def __init__(self):
        self._screen = pygame.display.set_mode((World.WIDTH, World.HEIGHT))

    @property
    def screen(self) -> pygame.Surface:
        return self._screen

    def draw_world(self):
        for row in range(World.ROWS):
            for col in range(World.COLS):
                cel = World.MAP[row][col]
                color = World.COLORS_MAPPER[cel]
                pygame.draw.rect(self._screen, color.value, (col * World.TILE_SIZE, row * World.TILE_SIZE, World.TILE_SIZE, World.TILE_SIZE))
    

