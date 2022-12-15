import pygame
from state_machine import StateMachine
import os
from image_loader import*


class Input:
    def update(self, events):
        # process events pass
        pass


class Physics:
    def __init__(self, obj):
        self.obj = obj

    def update(self, pos, speed: list[float, float], direction: list[float, float], gravity: float):

        #print(f"Obj Pos: {obj.pos}")
        if self.obj.is_on_ground():
            speed[1] = 0
        else:
            speed[1] += gravity

        pos[0] += speed[0] * direction[0]
        pos[1] += speed[1] * direction[1]


class GraphicsComponent:
    def __init__(self, obj):
        self.obj = obj
        self.sprite_sheet_image = ImageLoader.get_instance().image_dict["walk1.png"]

    def update(self, display_ref):

        self.obj.display.blit(self.sprite_sheet_image, (self.obj.pos[0], -self.obj.pos[1]))


class Entity:
    def __init__(self, display_ref):
        self.pos = [1, 1]
        self.scale = (10, 10)

        self.display = display_ref

        #Components
        self._input = Input() # <--- se calhar não precisa desse
        self._physics = Physics(self)
        self._graphics = GraphicsComponent(self)

    def update(self):
        print(f"Update Obj Pos: {self.pos}")
        
    def render(self):
        # self._input.update(events)
        # self._physics.update(self.x, self.y, self.speed)

        self._graphics.update(self.display)

    def is_on_ground(self) -> bool:
        return False
