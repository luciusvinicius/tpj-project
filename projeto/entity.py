import pygame
from state_machine import StateMachine


class Input:
    def update(self, events):
        # process events pass
        pass


class Physics:

    def update(self, x, y, speed):
        # process physics pass
        pass


class GraphicsComponent:
    def __init__(self, pos=(0, 0), scale=(1, 1)):
        self.custom_rect = pygame.Rect(pos, scale)
        self.rect_color = "green"

    def update(self, display_ref):
        print("Update Draw")
        pygame.draw.rect(display_ref, self.rect_color, (1, 1, 10, 10))


class Entity:
    def __init__(self, display_ref):
        self.pos = (1, 1)
        self.scale = (1, 1)
        self.direction = [0, 0]
        self._input = Input()
        self._physics = Physics()
        self._graphics = GraphicsComponent()
        self.my_game = display_ref

    def update(self):
        # self._input.update(events)
        # self._physics.update(self.x, self.y, self.speed)

        self._graphics.update(self.my_game)
