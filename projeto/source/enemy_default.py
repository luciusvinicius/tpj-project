from moving_entity import MovingEntity
from signal_manager import SignalManager


class Enemy(MovingEntity):

    def __init__(self, engine, components, init_pos = [0, 0], init_scale = [1, 1], 
                 speed_x=1, speed_y=1, score=100):
        super().__init__(engine, components, init_pos, init_scale)
        self.name = "Enemy"
        self.score = score
        signal_manager = SignalManager.get_instance()
        signal_manager.listen_to_signal("enemy_hit", self)

    def on_signal(self, signal_name, *args):
        if signal_name == "enemy_hit":
            player = args[0]
            # Check if player hit above enemy
            player_center_y = player.sprite.rect.centery
            enemy_center_y = self.sprite.rect.centery
            
            is_above = player_center_y < enemy_center_y
            if is_above and player.speed[1] > 0:
                signal_manager = SignalManager.get_instance()
                signal_manager.send_signal("enemy_dead", self)
                self.kill_enemy()
            
            else:
                # Player took damage
                # print("Player took damage")
                pass
            
    def kill_enemy(self):
        self.engine_ref.render_manager.remove_actor(self)
        self.engine_ref.collision_manager.remove_actor(self)
        self.sprite.is_disabled = True
        self.sprite.kill()
