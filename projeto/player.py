from entity import Entity
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


class Player(Entity):

    def __init__(self, display_ref):
        super().__init__(display_ref)
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
