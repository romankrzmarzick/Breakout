import pygame
import sys

WINDOW_SIZE = (600, 800)


class Breakout:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        
    def run(self):
       
        platform_rect = pygame.Rect(50, 750, 125, 15)
        movement = [False, False]


        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        movement[1] = False
            
            if movement[0]:
                platform_rect[0] -= 10

            if movement[1]:
                platform_rect[0] += 10
                

            # Background
            self.screen.fill((0, 0, 50))

            
            pygame.draw.rect(self.screen, (255, 255, 255), platform_rect)
            
            

            pygame.display.flip()
            self.clock.tick(60)

   



Breakout().run()