from MovingEntity import MovingEntity
from state import State


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

    # def update(self):
    #     pass
        # print(f"Updating Running State to direction {self.obj.direction}")

    def exit(self):
        print("Exiting Running State")


class JumpingState(State):
    def __init__(self, player: MovingEntity):
        super().__init__("jumping", player)

    def enter(self):
        print("Entering Jumping State")

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
