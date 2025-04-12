import os
import pygame
from game.world_generator import World
from game.consts import SPRITES_PATH
from game.algorithms import bfs

class Player:

    def __init__(self, image, location: tuple[int, int]):
        self._image = image
        self._location = location
        self._size = (World.TILE_SIZE * 0.8, World.TILE_SIZE * 0.8)
        self._sprite = self._pre_load_image()
        
    def get_pos(self):
        return self._location    
    
    def _pre_load_image(self):
        player = pygame.image.load(os.path.join(SPRITES_PATH, self._image))
        player = player.convert_alpha()
        player = pygame.transform.scale(player, self._size)
        return player
    
    def draw_player(self, world: World):
        offset = (World.TILE_SIZE - self._size[0]) // 2
        world.screen.blit(self._sprite, (self._location[0] + offset, self._location[1] + offset))

    def search_path(self, x, y, world: World):
        row, col = x // World.TILE_SIZE, y // World.TILE_SIZE
        path = bfs(row, col, World)
        if path:
            print(path)
            for location in path:
                world.draw_world()
                self._location = (location[1] * World.TILE_SIZE, location[0] * World.TILE_SIZE)
                print(f"Moving to {self._location}")
                self.draw_player(world)
                pygame.display.flip()
                pygame.time.delay(300)
            
            
            
        