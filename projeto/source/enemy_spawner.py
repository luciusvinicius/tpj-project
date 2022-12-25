import random
import json
import os

from actor import Actor
from enemy_default import Enemy
from sprite_component import SpriteComponent
from collision_manager import CollisionLayers

json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
enemy_stats = json.load(open(json_path, "r"))["enemy"]


class EnemySpawner(Actor):

    def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1], spawn_rate=50,
                 spawn_once=False, disbled=False):
        super().__init__(engine, components, init_pos, init_scale)
        self.spawn_rate = spawn_rate
        self.spawn_once = spawn_once
        self.do_once = False
        self.spawn_timer = 0
        self.disabled = disbled
        self.name = "EnemySpawner"

    def update(self):
        super().update()
        if self.disabled: return
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_rate:

            if self.do_once == False:
                self.spawn_timer = 0
                self.spawn_enemy()

            if self.spawn_once:
                self.spawn_once = False
                self.do_once = True

    def spawn_enemy(self):
        # print("Spawning enemy")
        enemy_graphics = SpriteComponent(self.engine_ref, "enemy.png", [3, 3], 40, 1, [0, 7], [0.5, 0.7],
                                         [CollisionLayers.Enemy],
                                         [], True, False)

        enemy_graphics.set_up_animations(
            [["idle", [0, 5], True, 1], ["walk", [6, 9], True, 100], ["jump", [13, 13], False, 100]],
            [28, 21], [8, 4])

        enemy_pos = [1, 0]
        enemy_speed = random.uniform(enemy_stats["min_speed"], enemy_stats["max_speed"])

        enemy = Enemy(self.engine_ref, [enemy_graphics], enemy_pos, speed_x=enemy_speed)
        self.engine_ref.add_actor(enemy)
