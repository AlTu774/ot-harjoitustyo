import pygame
from stage import Stage

class Renderer():
    def __init__(self, stage, display):
        self.stage = stage
        self.stage_lenght = len(self.stage.map)
        self.stage_width = len(self.stage.map[0])
        self.block = pygame.Surface((50,50))
        self.display = display

    def render_stage(self):
        for y in range(0,self.stage_lenght):
            for x in range(0,self.stage_width):
                if self.stage.map[y][x] == 0:
                    pygame.draw.rect(self.display,(255,255,255),(190+x*30,50+y*30,30,30),1)
                elif self.stage.map[y][x] == 1:
                    pygame.draw.rect(self.display,(250,250,250),(190+x*30,50+y*30,30,30))
                elif self.stage.map[y][x] == 2:
                    pygame.draw.rect(self.display,(50,50,50),(190+x*30,50+y*30,30,30))
                    
        pygame.display.update()           

