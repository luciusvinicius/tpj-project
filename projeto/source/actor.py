from sprite_component import *
import json
import os

json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
world_stats = json.load(open(json_path, "r"))["world"]

class Physics:
    def __init__(self, obj):
        self.obj = obj
        self.is_on_ground = False

    def update(self, pos, speed: list[float, float], direction: list[float, float], gravity: float, is_horizontal):

        if is_horizontal:
            pos[0] += speed[0] * direction[0]
            pass
        else:

            if self.is_on_ground:
                print("groudn")
                #speed[1] = 0
            else:
                #speed[1] += gravity
                pass


            #pos[1] += speed[1] * direction[1]


class Actor:
    
    id = 1
    
    def __init__(self, engine, components_ref: list, init_pos=[0, 0], init_scale=[1, 1]):
        self.id = Actor.id
        Actor.id += 1
        self.pos = init_pos
        self.scale = init_scale
        self.engine_ref = engine
        self.sprite = None
        self._physics = Physics(self)
        self.name = "Actor"
        self.speed = [0, 0]
        self.direction = [0, 0]
        self.is_dead = False
        self.gravity = 0

        # Set up components
        self.components = components_ref

        for component in self.components:
            if issubclass(type(component), SpriteComponent):
                self.sprite = component
                self.sprite.set_up(self)

    def early_update(self):
        pass

    def update(self):
        self.update_col()

        for component in self.components:
            # component.update()
            pass

        # Remove player if it is dead and out of bounds
        if self.is_dead:
            level_height = self.engine_ref.level.get_height()
            act_height = self.sprite.rect.centery
            if act_height < 0 or act_height > level_height:
                self.remove_from_engine()

    def update_col(self):
        if self.sprite is not None:
            self.sprite.update_col()

    def render(self):
        if self.sprite is not None:
            self.sprite.render()

    def on_collision(self, colliding_sprites):
        if self.is_dead: return

    def on_signal(self, signal, *args):
        print("Signal received: " + signal)
        print("Args: " + str(args))
    
    def kill(self):
        self.is_dead = True
        self.sprite.flip_Y = True
        self.direction[1] = -1
        self.speed[1] = 0
        self.gravity = world_stats["death_gravity"]
    
    def remove_from_engine(self):
        self.engine_ref.render_manager.remove_actor(self)
        self.engine_ref.collision_manager.remove_actor(self)
        self.sprite.is_disabled = True
        self.sprite.kill()