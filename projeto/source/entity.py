from image_loader import*
from engine import*


class GraphicsComponent:
    def __init__(self, obj):
        self.obj = obj
        self.sprite_sheet_image = ImageLoader.get_instance().image_dict["walk1.png"]

    def update(self):

        self.obj.engine_ref.display.blit(self.sprite_sheet_image, (self.obj.pos[0], -self.obj.pos[1]))

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


class Entity:
    def __init__(self, engine, components_ref: list[ComponentTypes], init_pos = [0, 0], init_scale = [1, 1]):
        self.pos = init_pos
        self.scale = init_scale
        self.engine_ref = engine

        self.components = []
        for component in components_ref:
            match component:
                case ComponentTypes.Graphics:
                    self._graphics = GraphicsComponent(self)
                    self.components.append(self._graphics)
                case ComponentTypes.Physics:
                    self._physics = Physics(self)
                    self.components.append(self._physics)

    def update(self):
        for component in self.components:
            pass
            #component.update()
        
    def render(self):
        # self._input.update(events)
        # self._physics.update(self.x, self.y, self.speed)

        self._graphics.update()

    def is_on_ground(self) -> bool:
        return False
