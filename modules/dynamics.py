import pygame

class Entities:
    def __init__(self, x, y, width, height, color):
        self.upper_boundary = (600, 800)
        self.position = [0, 0]
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
       

    def move(self):
        self.rect.x += self.position[0]
        self.rect.y += self.position[1]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def update(self):
        pass



class Platform(Entities):
    def __init__(self):
        super().__init__(x=240, y=750, width=120, height=16, color=(255, 255, 255))
    def update(self):
        self.move()
        # Boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.upper_boundary[0]:
            self.rect.right = self.upper_boundary[0]
        
class Ball(Entities):
    def __init__(self):
        super().__init__(x=292, y=732, width=16, height=16, color=(255, 0, 0))
        self.radius = 10        
        self.unactive = True
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def update(self):
        self.move()
        # Y-axis movement
        if self.rect.top < 0:
            self.position[1] = self.position[1] * -1
        if self.rect.bottom > self.upper_boundary[1]:
            self.position[1] = self.position[1] * -1
        
        # X-axis movement
        if self.rect.left < 0:
            self.position[0] = self.position[0] * -1
        if self.rect.right > self.upper_boundary[0]:
            self.position[0] = self.position[0] * -1

        