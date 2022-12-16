from MovingEntity import MovingEntity
from state import State
import json
import os

print(os.path.join(os.path.dirname(__file__)))
json_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
player_stats = json.load(open(json_path, "r"))["player"]

class IdleState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("idle", player)

    def enter(self):
        print("Entering Idle State")

    # def update(self):
    #     pass
        # print("Updating Idle State")

    def exit(self):
        print("Exiting Idle State")


class RunningState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("running", player)

    def enter(self):
        print("Entering Running State")
        self.obj.speed[1] = player_stats["speed"]

    def exit(self):
        print("Exiting Running State")


class JumpingState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("jumping", player)

    def enter(self):
        print("Entering Jumping State")
        self.obj.direction[1] = -1
        self.obj.speed[1] = -player_stats["jump_speed"]

    # def update(self):
    #     pass
        # print("Updating Jumping State")

    def exit(self):
        print("Exiting Jumping State")


class FallingState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("falling", player)

    def enter(self):
        print("Entering Falling State")

    # def update(self):
    #     pass
        # print("Updating Falling State")

    def exit(self):
        print("Exiting Falling State")
