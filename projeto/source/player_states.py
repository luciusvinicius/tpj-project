import os
import json

from state import State
from moving_entity import MovingEntity

print(os.path.join(os.path.dirname(__file__)))
json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
player_stats = json.load(open(json_path, "r"))["player"]

class IdleState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("idle", player)

    def enter(self):
        print("Entering Idle State")
        if self.obj.vertical_state_machine.current_state.state_name == "idle":
            self.obj.direction[1] = 0


    def update(self):
        if self.obj.vertical_state_machine.current_state.state_name == "idle":
            if not self.obj._physics.is_on_ground:
                self.obj.vertical_state_machine.change_state("falling")

    def exit(self):
        # print("Exiting Idle State")
        pass

class RunningState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("running", player)

    def enter(self):
        # print("Entering Running State")
        self.obj.speed[0] = player_stats["speed"]

    def exit(self):
        # print("Exiting Running State")
        pass


class JumpingState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("jumping", player)

    def enter(self):
        # print("Entering Jumping State")
        self.obj.direction[1] = -1
        self.obj.speed[1] = -player_stats["jump_speed"]
        print(f"Jump Speed Enter: {self.obj.speed[1]}")

    def update(self):
        print(f"Jumping Speed Update: {self.obj.speed[1]}")
        if self.obj.speed[1] >= 0:
            self.obj.vertical_state_machine.change_state("falling")

    def exit(self):
        # print("Exiting Jumping State")
        pass

class FallingState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("falling", player)
        # self.obj.direction[1] = -1


    def enter(self):
        print("Entering Falling State")
        self.obj.direction[1] = -1
        pass

    def update(self):
        if self.obj._physics.is_on_ground:
            print("Falling: On ground")
            self.obj.vertical_state_machine.change_state("idle")

    def exit(self):
        # print("Exiting Falling State")
        pass