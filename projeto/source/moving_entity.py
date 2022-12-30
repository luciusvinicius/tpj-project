from actor import Actor
import json
import os

json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
world_stats = json.load(open(json_path, "r"))["world"]

class MovingEntity(Actor):

    def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1], speed_x=1, speed_y=1, gravity=world_stats["gravity"]):
        super().__init__(engine, components, init_pos, init_scale)
        self.speed = [speed_x, speed_y]
        self.direction = [0, 0]
        self.gravity = gravity

    def update(self):
        self._physics.update(self.pos, self.speed, self.direction, self.gravity)
        super().update()
