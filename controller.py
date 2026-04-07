import pygame
import sys
from modules.dynamics import Platform, Ball

WINDOW_SIZE = (600, 700)


class Breakout:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
    
    def run(self):
        platform = Platform()
        ball = Ball()
        obstacles = platform.rect
        
        while True:
            
            # --- Event Phase ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()     
                if event.type == pygame.KEYDOWN:
                    if ball.unactive:
                        if event.key == pygame.K_UP:
                            ball.velocity[0] = 4
                            ball.velocity[1] = -4
                            ball.unactive = False

            # --- Input ---
            keys = pygame.key.get_pressed()
            platform.velocity[0] = 0

            if keys[pygame.K_LEFT]:
                platform.velocity[0] = -5
            if keys[pygame.K_RIGHT]:
                platform.velocity[0] = 5

            if ball.unactive:
                ball.velocity[0] = platform.velocity[0]

            # Background Color
            self.screen.fill((0, 0, 50))

            # --- Render ---
            platform.render(self.screen)
            ball.render(self.screen)

            # --- Update --- 
            platform.update()
            ball.update(obstacles)

            # --- Interactions ---
            
                
               
            pygame.display.flip()
            self.clock.tick(60)
    
    


Breakout().run()