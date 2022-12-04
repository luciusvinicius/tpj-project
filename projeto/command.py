import pygame as pg


class Command:
    def execute(self):
        raise NotImplementedError("You must implement the execute() method in the derived class!")


class Jump(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        print("Jumping")
        self.player.vertical_state_machine.change_state("jumping")
        # self.player.jump()


class MoveRight(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.direction[0] = 1
        self.player.horizontal_state_machine.change_state("running")
        # self.player.move((1, 0))


class MoveLeft(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.direction[0] = -1
        self.player.horizontal_state_machine.change_state("running")
        # self.player.move((-1, 0))


class Nothing(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.direction[0] = 0
        self.player.horizontal_state_machine.change_state("idle")
