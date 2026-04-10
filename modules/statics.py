import pygame

class TileMap:
    def __init__(self):
        self.border_display_active = False
        self.game_size = (600, 700)
        self.tiles = []
        self.build_tile()
    
    def build_tile(self):
        bk_ht = self.game_size[1] // 20
        bk_wt = self.game_size[0] // 6
        color_list = [(0, 225,0), (225, 0 , 0), (0, 0, 225), (245, 125, 0), (255, 215, 0)]
        
        # Generate block rows and columns
        for row in range(5):
            for col in range(6):
                x = col * bk_wt
                y = row * bk_ht
                color = color_list[row % 5]
                if not row == 0 and not row == 5:
                    block = Standard(x , y, bk_wt, bk_ht, color)
                    self.tiles.append(block)
    
    def render_blocks(self, screen):
        for tile in self.tiles:
            tile.render(screen)
            

        

class Tile:
    def __init__(self, x, y, width, height, color, healthpoints):
        self.rect = pygame.Rect(x, y, width, height)
        self.healthpoints = healthpoints
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 50), self.rect, 3)

class Standard(Tile):
    def __init__(self, x, y, width, height, color, health_points=1):
        super().__init__(x, y, width, height, color, health_points)

   
class Hard(Tile):
    def __init__(self, x, y, width, height, color, healthpoints=2):
        super().__init__(x, y, width, height, color, healthpoints)

class TNT(Tile):
    def __init__(self, x, y, width, height, color, healthpoints):
        super().__init__(x, y, width, height, color, healthpoints)
  