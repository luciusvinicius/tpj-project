import random
import json
import os

from actor import Actor
from enemy_default import Enemy
from graphics_component import GraphicsComponent

json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
enemy_stats = json.load(open(json_path, "r"))["enemy"]


class EnemySpawner(Actor):

    def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1], spawn_rate=50):
        super().__init__(engine, components, init_pos, init_scale)
        self.spawn_rate = spawn_rate
        self.spawn_timer = 0

    def update(self):
        super().update()
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_rate:
            self.spawn_timer = 0
            self.spawn_enemy()

    def spawn_enemy(self):
        print("Spawning enemy")
        enemy_graphics = GraphicsComponent(self.engine_ref, "player.png", [1, 1])

        enemy_pos = [1, 0]
        enemy_speed = random.uniform(enemy_stats["min_speed"], enemy_stats["max_speed"])

        enemy = Enemy(self.engine_ref, [enemy_graphics], enemy_pos, speed_x=enemy_speed)
        self.engine_ref.add_actor(enemy)
