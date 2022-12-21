from actor import Actor
from sprite_component import SpriteComponent


class Tile(Actor):

    def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1]):
        super().__init__(engine, components, init_pos, init_scale)


    def is_on_ground(self) -> bool:
        return True
