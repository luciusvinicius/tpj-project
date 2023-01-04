import os
import json

from sound_loader import SoundLoader
from state import State
from moving_entity import MovingEntity

print(os.path.join(os.path.dirname(__file__)))
json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
player_stats = json.load(open(json_path, "r"))["player"]

class IdleState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("idle", player)

    def enter(self):
        if self.obj.vertical_state_machine.current_state.state_name == "idle":
            self.obj.direction[1] = 0

    def update(self):
        if self.obj.vertical_state_machine.current_state.state_name == "idle" and not self.obj._physics.is_on_ground:
            #self.obj.vertical_state_machine.change_state("falling")
            pass
        if self.obj.horizontal_state_machine.current_state.state_name == "idle" and self.obj._physics.is_on_ground:
            self.obj.sprite.change_animation("idle")
                
class RunningState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("running", player)

    def enter(self):
        self.obj.speed[0] = player_stats["speed"]

    def update(self):
        # if self.obj.vertical_state_machine.current_state.state_name == "idle":
        if self.obj._physics.is_on_ground:
                self.obj.sprite.change_animation("walk")

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

    def exit(self):
        pass

class FallingState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("falling", player)

    def enter(self):
        self.obj.direction[1] = -1
        self.obj.sprite.change_animation("jump")

    def update(self):
        if self.obj._physics.is_on_ground:
            self.obj.vertical_state_machine.change_state("idle")

    def exit(self):
        pass