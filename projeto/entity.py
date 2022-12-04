import pygame
from state_machine import StateMachine


class Input:
    def update(self, events):
        # process events pass
        pass


class Physics:
    def __init__(self, obj):
        self.obj = obj
    def update(self, speed: list[float, float],
               direction: list[float, float], gravity: float):
        print(f"Obj Pos: {self.obj.pos}")
        if self.obj.is_on_ground():
            speed[1] = 0
        else:
            speed[1] += gravity

        self.obj.pos[0] += speed[0] * direction[0]
        self.obj.pos[1] += speed[1] * direction[1]


class GraphicsComponent:
    def __init__(self, pos=(0, 0), scale=(1, 1)):
        self.custom_rect = pygame.Rect(pos, scale)
        self.rect_color = "green"

    def update(self, display_ref):
        # print("Update Draw")
        pygame.draw.rect(display_ref, self.rect_color, (1, 1, 10, 10))


class Entity:
    def __init__(self, display_ref):
        self.pos = [1, 1]
        self.scale = (1, 1)
        self._input = Input() # <--- se calhar não precisa desse
        self._physics = Physics(self)
        self._graphics = GraphicsComponent()
        self.my_game = display_ref

    def update(self):
        self._physics.update([0, 0], [0, 0], 0)

    def render(self):
        # self._input.update(events)
        # self._physics.update(self.x, self.y, self.speed)

        self._graphics.update(self.my_game)

    def is_on_ground(self) -> bool:
        return False
