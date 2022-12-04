import pygame as pg

JUMP_SPEED = 5

class Command:
    def execute(self):
        raise NotImplementedError("You must implement the execute() method in the derived class!")


class Jump(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.direction[1] = -1
        self.player.speed[1] = -JUMP_SPEED
        self.player.vertical_state_machine.change_state("jumping")


class MoveRight(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.direction[0] = 1
        self.player.horizontal_state_machine.change_state("running")


class MoveLeft(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.direction[0] = -1
        self.player.horizontal_state_machine.change_state("running")


class Nothing(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.direction[0] = 0
        self.player.horizontal_state_machine.change_state("idle")
