from command import *
from player_states import *
import pygame

from state_machine import StateMachine

COMMANDS = {
    pygame.K_UP: Jump,
    pygame.K_LEFT: MoveLeft,
    pygame.K_RIGHT: MoveRight,
    f"release_{pygame.K_LEFT}": Nothing,
    f"release_{pygame.K_RIGHT}": Nothing,
}


class Player(MovingEntity):

    def __init__(self, engine, components):
        super().__init__(engine, components)
        self.commands = COMMANDS

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

        for command in self.commands:
            self.commands[command] = self.commands[command](self)

    def update(self):
        self.horizontal_state_machine.update()
        self.vertical_state_machine.update()
        super().update()


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
