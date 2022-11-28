import pygame as pg

class Input: 
    def update(self, events):
        pass #process events pass 

class Physics: 
    def update(self, x, y, speed): #process physics pass 
        pass

class Graphics: 
    def __init__(self) -> None:
        self.custom_rect = pg.Rect(1, 1, self.size, self.size)
        self.rect_color = "green"


    def update(self, x, y): 
        pass

class GameObject:
    def __init__ (self) -> None: 
        self.x = 0 
        self.y = 0 
        self.speed = 0 

class Entity:
    def __init__(self) -> None:

        self.pos = (1, 1)
        
        
       


        self._input = Input() 
        self._physics = Physics() 
        self._graphics = Graphics() 

    def update(self, events): 
        self._input.update(events) 
        self._physics.update(self.x, self.y, self.speed) 
        self._graphics.update(self.x, self.y) 




myDisplay = pg.display.set_mode((10, 10))