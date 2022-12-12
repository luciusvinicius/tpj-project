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
    def __init__(self, obj, ):
        self.obj = obj
        self.custom_rect = pygame.Rect(obj.pos, obj.scale)
        self.rect_color = "green"


        self.sprite_sheet_image = pygame.image.load('sprites/amogus/walk1.png').convert_alpha()

        # sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image) """

    def update(self, display_ref):
        print("Update Draw")
        self.obj.my_game.blit(self.sprite_sheet_image, (0, 0))


class Entity:
    def __init__(self, display_ref):
        self.pos = [1, 1]
        self.scale = (10, 10)

        #Components
        self._input = Input() # <--- se calhar não precisa desse
        self._physics = Physics(self)
        self._graphics = GraphicsComponent(self)
        self.my_game = display_ref

    def update(self):
        self._physics.update([0, 0], [0, 0], 0)

    def render(self):
        # self._input.update(events)
        # self._physics.update(self.x, self.y, self.speed)

        self._graphics.update(self.my_game)

    def is_on_ground(self) -> bool:
        return False
