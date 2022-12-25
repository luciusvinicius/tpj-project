from sprite_component import *


class Physics:
    def __init__(self, obj):
        self.obj = obj
        self.is_on_ground = False

    def update(self, pos, speed: list[float, float], direction: list[float, float], gravity: float):

        if self.is_on_ground and speed[1] >= 0:
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
        self.speed = [0, 0]

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
                target_left = target.sprite.rect.centerx - target.sprite.rect.width / 2
                actor_right = self.sprite.rect.centerx + self.sprite.rect.width / 2
                target_right = target.sprite.rect.centerx + target.sprite.rect.width / 2
                actor_left = self.sprite.rect.centerx - self.sprite.rect.width / 2
                actor_pos = self.sprite.rect.centerx
                is_left = actor_pos < target_left
                is_right = actor_pos > target_right


                # print(f"target_left: {target_left}, actor_right: {actor_right}, is_right: {is_right}")

                if target_left == 96.0:
                    print(f"actor_pos: {actor_pos}")
                    print(f"target_left: {target_left}, actor_right: {actor_right}, is_right: {is_right}")
                    print(f"target_right: {target_right}, actor_left: {actor_left}, is_left: {is_left}")
                    print(f"target img size: {target.sprite.img_size}")
                    print(f"actor img size: {self.sprite.img_size}")

                # if target_left == 144.0:
                #     print(f"actor_pos: {actor_pos}")
                #     print(f"target_left: {target_left}, actor_right: {actor_right}, is_right: {is_right}")
                #     print(f"target_right: {target_right}, actor_left: {actor_left}, is_left: {is_left}")
                #     print(f"target img size: {target.sprite.img_size}")
                #     print(f"actor img size: {self.sprite.img_size}")

                target_top = target.sprite.rect.centery + target.sprite.rect.h
                actor_bottom = self.pos[1] - self.sprite.img_size[1]

                if is_left or is_right:

                    if is_left:
                        self.speed[0] = 0
                else:
                    if target_top > actor_bottom:
                        self._physics.is_on_ground = True

