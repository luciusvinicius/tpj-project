from input_interface import InputInterface
from state_machine import StateMachine
from player_states import *

class Player(MovingEntity, InputInterface):

    def __init__(self, engine, components, init_pos = [0, 0], init_scale = [1, 1]):
        super().__init__(engine, components, init_pos, init_scale)

        self.horizontal_states = {
            "idle": (IdleState(self), ["running"]),
            "running": (RunningState(self), ["idle"]),
        }
        self.vertical_states = {
            "idle": (IdleState(self), ["jumping", "falling"]),
            "jumping": (JumpingState(self), ["falling"]),
            "falling": (FallingState(self), ["idle"]),
        }

        self.horizontal_state_machine = StateMachine("idle", self.horizontal_states)
        self.vertical_state_machine = StateMachine("idle", self.vertical_states)

    def update(self):
        self.horizontal_state_machine.update()
        self.vertical_state_machine.update()
        super().update()

    # :::::::::::::::::::::::::::::: Inputs :::::::::::::::::::::::::::
    def input_press_up(self):
        self.vertical_state_machine.change_state("jumping")

    def input_press_left(self):
        self.direction[0] = -1
        self.horizontal_state_machine.change_state("running")

    def input_release_left(self):
        self.direction[0] = 0
        self.horizontal_state_machine.change_state("idle")

    def input_press_right(self):
        self.direction[0] = 1
        self.horizontal_state_machine.change_state("running")
    
    def input_release_right(self):
        self.direction[0] = 0
        self.horizontal_state_machine.change_state("idle")
