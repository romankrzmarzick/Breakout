import pygame
import sys
from modules.dynamics import Platform, Ball
from modules.statics import TileMap

WINDOW_SIZE = (600, 700)


class Breakout:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
    
    def run(self):
        platform = Platform()
        ball = Ball()
        tilemap = TileMap()
        ball_obstacles = [platform]
        ball_obstacles.extend(tilemap.tiles)
        

        while True:
            
            # --- Event Phase ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()     
                if event.type == pygame.KEYDOWN:
                    if ball.unactive:
                        if event.key == pygame.K_UP:
                            ball.velocity[0] = 5
                            ball.velocity[1] = -5
                            ball.unactive = False
                    
                    # Dev border display.
                    if event.key == pygame.K_k:
                        pass

            # --- Input ---
            keys = pygame.key.get_pressed()
            platform.velocity[0] = 0
            
            if keys[pygame.K_LEFT]:
                platform.velocity[0] = -4
            if keys[pygame.K_RIGHT]:
                platform.velocity[0] = 4
            
            # Ball follows platform at the start before [up] is pressed.
            if ball.unactive:
                ball.rect.centerx = platform.rect.centerx
           
            # --- Update ---
            platform.update()
            ball.update(ball_obstacles)
           
            # --- Render ---
            # Background
            self.screen.fill((0, 0, 50))
            # Statics
            tilemap.render_blocks(self.screen)
            # Dynamics
            platform.render(self.screen)
            ball.render(self.screen)     
               
            pygame.display.flip()
            self.clock.tick(60)
    
    


Breakout().run()