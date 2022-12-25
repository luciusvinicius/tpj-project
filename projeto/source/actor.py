from sprite_component import *


class Physics:
    def __init__(self, obj):
        self.obj = obj
        self.is_on_ground = False

    def update(self, pos, speed: list[float, float], direction: list[float, float], gravity: float):

        if self.is_on_ground:
            speed[1] = 0
        else:
            speed[1] += gravity

        pos[0] += speed[0] * direction[0]
        pos[1] += speed[1] * direction[1]


class Actor:
    def __init__(self, engine, components_ref: list, init_pos=[0, 0], init_scale=[1, 1]):
        self.pos = init_pos
        self.scale = init_scale
        self.engine_ref = engine
        self.sprite = None
        self._physics = Physics(self)
        self.name = "Actor"

        # Set up components
        self.components = components_ref

        for component in self.components:
            if issubclass(type(component), SpriteComponent):
                self.sprite = component
                self.sprite.set_up(self)

    def update(self):
        self.update_col()
        self._physics.is_on_ground = False
        for component in self.components:
            # component.update()
            pass

    def update_col(self):
        if self.sprite is not None:
            self.sprite.update_col()

    def render(self):
        if self.sprite is not None:
            self.sprite.render()

    def on_collision(self, colliding_sprites):
        for sprite in colliding_sprites:
            target = sprite.actor_ref
            if "Tile" in target.name:
                self._physics.is_on_ground = True

                # print("Ficou on ground")

