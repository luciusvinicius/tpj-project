import random
import json
import os
import math

from actor import Actor
from enemy_default import Enemy, FastEnemy, SlowEnemy
from sprite_component import SpriteComponent
from collision_manager import CollisionLayers

json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
enemy_stats = json.load(open(json_path, "r"))["enemy"]
spawner = enemy_stats["spawner"]


class EnemySpawner(Actor):

    def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1], spawn_time_offset=0, spawn_rate=spawner["spawn_rate"],
                 spawn_once=False, disabled=False, direction=1):
        super().__init__(engine, components, init_pos, init_scale)
        self.spawn_rate = spawn_rate
        self.spawn_once = spawn_once
        self.has_spawned = False
        self.spawn_timer = spawn_time_offset
        self.timer = spawn_time_offset
        self.spawn_rate_variation = random.uniform(-spawner["spawn_rate_variation"], spawner["spawn_rate_variation"])
        self.disabled = disabled
        self.name = "EnemySpawner"
        self.direction = direction

    def update(self):
        super().update()
        if self.disabled: return
        self.spawn_timer += 1
        self.timer += 1
        spawn_time = self.spawn_rate + self.spawn_rate_variation
        spawn_time_intensifier = math.floor((self.timer / spawner["spawn_rate_intensification"]) + 1)
        if self.spawn_timer >= spawn_time / spawn_time_intensifier:
            if not self.spawn_once or not self.has_spawned:
                self.spawn_timer = 0
                self.spawn_enemy()
                self.has_spawned = True
                self.spawn_rate_variation = random.uniform(-spawner["spawn_rate_variation"], spawner["spawn_rate_variation"])
                

    def spawn_enemy(self):
        # Set up enemy
        enemy_graphics = SpriteComponent(self.engine_ref, "enemy.png", [3, 3], 40, 1, [0, 7], [0.5, 0.7],
                                         [CollisionLayers.Enemy],
                                         [CollisionLayers.Wall], True, True)

        enemy_graphics.set_up_animations(
            [ ["walk", [6, 9], True, 100], ["idle", [0, 5], True, 1], ["jump", [13, 13], False, 100]],
            [28, 21], [8, 4])

        enemy_pos = self.pos.copy()
        enemy_pos[0] -= enemy_graphics.rect.width / 2
        enemy_pos[1] += enemy_graphics.rect.height / 4
        
        # Check if enemy is slow or fast
        typ = None
        if spawner["fast_enemy_chance"] < random.random():
            typ = FastEnemy()
        else:
            typ = SlowEnemy()

        enemy = Enemy(self.engine_ref, [enemy_graphics], enemy_pos, initial_direction=[self.direction, 0], typ = typ)
        self.engine_ref.add_actor(enemy)
