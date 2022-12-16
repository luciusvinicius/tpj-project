from engine import*
from graphics_component import*

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


class Actor:
    def __init__(self, engine, components_ref : list, init_pos = [0, 0], init_scale = [1, 1]):
        self.pos = init_pos
        self.scale = init_scale
        self.engine_ref = engine
        self._graphics = None
        self._physics = Physics(self)
        
        # Set up components
        self.components = components_ref
        for component in self.components:

            if issubclass(type(component), GraphicsComponent):
                self._graphics = component
                self._graphics.set_up(self)

    def update(self):
        for component in self.components:
            #component.update()
            pass
        
    def render(self):
        if self._graphics != None:
            self._graphics.render()

    def is_on_ground(self) -> bool:
        return False
