import os
import json

from sound_loader import SoundLoader
from state import State
from moving_entity import MovingEntity

print(os.path.join(os.path.dirname(__file__)))
json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
player_stats = json.load(open(json_path, "r"))["player"]

class HorizontalIdleState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("idle", player)

    def update(self):
        if self.obj._physics.is_on_ground:
            self.obj.sprite.change_animation("idle")
        if self.obj.direction[0] != 0:
            self.obj.horizontal_state_machine.change_state("running")
                
class RunningState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("running", player)

    def enter(self):
        self.obj.speed[0] = player_stats["speed"]

    def update(self):
        if self.obj._physics.is_on_ground:
            self.obj.sprite.change_animation("walk")
        if self.obj.direction[0] == 0:
            self.obj.horizontal_state_machine.change_state("idle")
        else:
            if self.obj.direction[0] > 0:
                self.obj.sprite.flip_X = False
            else:
                self.obj.sprite.flip_X = True
                
class VerticalIdleState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("idle", player)

    def enter(self):
        self.obj.direction[1] = 0

    def update(self):
        if not self.obj._physics.is_on_ground:
            self.obj.vertical_state_machine.change_state("falling")       

class JumpingState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("jumping", player)

    def enter(self):
        if self.obj.is_dead: return
        SoundLoader.get_instance().play_sound("jump.wav", 0.1)
        self.obj.direction[1] = -1
        self.obj.speed[1] = -player_stats["jump_speed"]

    def update(self):
        if self.obj.speed[1] >= 0:
            self.obj.vertical_state_machine.change_state("falling")

class FallingState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("falling", player)

    def enter(self):
        self.obj.direction[1] = -1
        self.obj.sprite.change_animation("jump")

    def update(self):
        if self.obj._physics.is_on_ground:
            self.obj.vertical_state_machine.change_state("idle")