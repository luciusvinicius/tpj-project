from moving_entity import MovingEntity
from signal_manager import SignalManager
from sound_loader import SoundLoader
import os 
import json
import random

json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
enemy_stats = json.load(open(json_path, "r"))["enemy"]

class Enemy(MovingEntity):
    
    def __init__(self, engine, components, init_pos = [0, 0], init_scale = [1, 1], 
                 initial_direction=[-1, 0], typ=None):
        super().__init__(engine, components, init_pos, init_scale)
        
        self.name = "Enemy"
        self.typ = typ
        self.score = typ.score
        self.direction = initial_direction
        self.speed = self.typ.speed
        signal_manager = SignalManager.get_instance()
        signal_manager.listen_to_signal("pow_hit", self)

        self.direction[1] = -1

    def check_player_death(self, player):

        player_center_y = player.sprite.rect.centery
        enemy_center_y = self.sprite.rect.centery
        
        is_above = player_center_y < enemy_center_y
        if is_above and player.speed[1] > 0:
            
            signal_manager = SignalManager.get_instance()
            signal_manager.send_signal("enemy_dead", self)
            self.kill()
            return True
        
        return False
    
    def update(self):
        if self.direction[0] > 0:
            self.sprite.flip_X = False
        elif self.direction[0] < 0:
            self.sprite.flip_X = True


        level_height = self.engine_ref.level.get_height()
        act_height = self.sprite.rect.centery
        if act_height < 0 or act_height > level_height:
            if not self.is_dead:
                self.kill(False)
            
        super().update()

    def on_collision(self, colliding_sprites):
        if not self.is_dead:
            super().on_collision(colliding_sprites)
            for sprite in colliding_sprites:
                if self.is_dead:
                    break
                target = sprite.actor_ref

                if "Tile" in target.name:
        
                    actor_center_y = self.sprite.rect.centery
                    target_center_y = target.sprite.rect.centery
                    is_above = actor_center_y < target_center_y

                    if is_above:
                        self._physics.is_on_ground = True

    
        
    def on_signal(self, signal, *args):
        if signal == "pow_hit":
            SignalManager.get_instance().send_signal("enemy_dead", self)
            self.kill()
        # return super().on_signal(signal, *args)
            
    def kill(self, play_sound=True):
        if play_sound:
            SoundLoader.get_instance().play_sound("damage.mp3", 0.2)
        super().kill()
    
    
class EnemyType():
    def __init__(self, speed, score):
        self.speed = [speed, 0]
        self.score = score
        
class SlowEnemy(EnemyType):
    def __init__(self):
        stats = enemy_stats["slow_enemy"]
        speed = random.uniform(stats["min_speed"], stats["max_speed"])
        score = stats["score"]
        super().__init__(speed, score)

class FastEnemy(EnemyType):
    def __init__(self):
        stats = enemy_stats["fast_enemy"]
        speed = random.uniform(stats["min_speed"], stats["max_speed"])
        score = stats["score"]
        super().__init__(speed, score)