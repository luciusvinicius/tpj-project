from moving_entity import MovingEntity
from signal_manager import SignalManager


class Enemy(MovingEntity):

    def __init__(self, engine, components, init_pos = [0, 0], init_scale = [1, 1], speed_x=1, speed_y=1):
        super().__init__(engine, components, init_pos, init_scale)
        self.name = "Enemy"
        signal_manager = SignalManager.get_instance()
        signal_manager.listen_to_signal("enemy_hit", self)

