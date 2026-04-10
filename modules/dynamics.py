import pygame

class Entities:
    def __init__(self, x, y, width, height, color):
        self.upper_boundary = (600, 700)
        self.velocity = [0, 0]
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
       

    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def test_collisions(self, obstacles):
        collisions = []
        for obstacle in obstacles:    
            if self.rect.colliderect(obstacle.rect):
                collisions.append(obstacle)
        return collisions
    
    def update(self, *args, **kwargs):
        pass



class Platform(Entities):
    def __init__(self):
        super().__init__(x=240, y=650, width=120, height=16, color=(255, 255, 255))
    def update(self):
        self.move()
        # Boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.upper_boundary[0]:
            self.rect.right = self.upper_boundary[0]
        
class Ball(Entities):
    def __init__(self):
        super().__init__(x=292, y=632, width=16, height=16, color=(235, 235, 235))
        self.radius = 10        
        self.unactive = True
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
        
    def update(self, obstacles):
        # --- Y-axis movement & collisions ---
        self.rect.y += self.velocity[1]
        collisions = self.test_collisions(obstacles)
        flip_direction = False
        # --- Obstacle collisions ---
        for collision in collisions:
            # Ball moving down: hitting the top
            if self.velocity[1] > 0:
                self.rect.bottom = collision.rect.top
                flip_direction = True
            # ball moving up: hitting the bottom
            elif self.velocity[1] < 0:
                self.rect.top = collision.rect.bottom
                flip_direction = True

        if flip_direction:
            self.velocity[1] *= -1

        # --- Y-axis boundary ---
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity[1] *= -1
        if self.rect.bottom >= self.upper_boundary[1]:
            self.rect.bottom = self.upper_boundary[1]
            self.velocity[1] *= -1

    # --- X-axis movement & collisions ---
        self.rect.x += self.velocity[0]
        collisions = self.test_collisions(obstacles)
        flip_direction = False
        # --- Obstacle collisions ---
        for collision in collisions:
            # ball moving right: hitting the left
            if self.velocity[0] > 0:
                self.rect.right = collision.rect.left
                flip_direction = True

            # Ball moving left: hitting the right
            elif self.velocity[0] < 0:
                self.rect.left = collision.rect.right
                flip_direction = True
                
        if flip_direction:
            self.velocity[0] *= -1

        # --- X-axis boundary ---
        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocity[0] = self.velocity[0] * -1
        if self.rect.right >= self.upper_boundary[0]:
            self.rect.right = self.upper_boundary[0]
            self.velocity[0] = self.velocity[0] * -1


       