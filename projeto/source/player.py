from input_interface import InputInterface
from signal_manager import SignalManager
from state_machine import StateMachine
from player_states import *
from tile import Tile


class Player(MovingEntity, InputInterface):

    def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1]):
        super().__init__(engine, components, init_pos, init_scale)
        self.name = "Player"
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

    def early_update(self):
        self.direction[0] = 0
        return super().early_update()

    def update(self):
        self.horizontal_state_machine.update()
        self.vertical_state_machine.update()

        super().update()
        if self.direction[0] == 0 and self.direction[1] == 0:
            self.horizontal_state_machine.change_state("idle")

    # :::::::::::::::::::::::::::::: Inputs :::::::::::::::::::::::::::
    def input_press_up(self):
        self.vertical_state_machine.change_state("jumping")
        self.sprite.change_animation("jump")

    def input_press_left(self):
        self.direction[0] -= 1
        self.filter_horizontal_input()

    def input_press_right(self):
        self.direction[0] += 1
        self.filter_horizontal_input()

    def filter_horizontal_input(self):
        if self.direction[0] == 0:
            self.horizontal_state_machine.change_state("idle")
        if self.direction[0] != 0:
            self.horizontal_state_machine.change_state("running")
            if self.direction[0] > 0:
                self.sprite.flip_X = False
            else:
                self.sprite.flip_X = True
    
    def on_collision(self, colliding_sprites):
        super().on_collision(colliding_sprites)
        for sprite in colliding_sprites:
            target = sprite.actor_ref
            if target.name == "Enemy":
                target.check_player_death(self)
            
            if target.name == "Pow":
                # TODO: later, check if the player is on bottom of the pow. If not, act like a tile
                target.hit()