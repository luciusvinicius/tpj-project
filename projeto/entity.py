import pygame

class Input: 
    def update(self, events):
        pass #process events pass 

class Physics: 
    def update(self, x, y, speed): #process physics pass 
        pass

class Graphics: 
    def __init__(self):
        self.custom_rect = pygame.Rect(1, 1, 10, 10)
        self.rect_color = "green"

    def update(self, display_ref): 
        print("Update Draw")
        pygame.draw.rect(display_ref, self.rect_color, (1, 1, 10, 10))

class GameObject:
    def __init__ (self): 
        self.x = 0 
        self.y = 0 
        self.speed = 0 

class Entity:
    def __init__(self, display_ref) -> None:

        self.pos = (1, 1)
        
        self._input = Input() 
        self._physics = Physics() 
        self._graphics = Graphics() 
        self.my_game = display_ref

    def update(self): 
        #self._input.update(events) 
        #self._physics.update(self.x, self.y, self.speed) 

        self._graphics.update(self.my_game) 
