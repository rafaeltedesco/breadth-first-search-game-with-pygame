import sys
import pygame
from game.world_generator import World
from game.player import Player
from game.consts import COLORS

def main():
    pygame.init()
    pygame.display.set_caption("Path Finding")

    font = pygame.font.SysFont("Arial", 24)

    text = font.render("Press ↓ to start", True, COLORS.WHITE.value)


    world = World()
    player = Player("seiya2.png", (0, 0))
    
    running = True
    while running:
        world.draw_world()
        world.screen.blit(text, (World.WIDTH // 2 - text.get_width() //2, 0))
        player.draw_player(world)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    x, y = player.get_pos()
                    player.search_path(x, y, world)                    
                    text = font.render("Completed!", True, COLORS.WHITE.value)

        pygame.time.delay(30)
    
if __name__ == "__main__":
    main()
