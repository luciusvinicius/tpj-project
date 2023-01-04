from input_interface import InputInterface
from signal_manager import SignalManager
from state_machine import StateMachine
from player_states import *
from tile import Tile
import pygame as pg

class Player(MovingEntity, InputInterface):
    
    RESTART_TIME = 3

    def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1]):
        super().__init__(engine, components, init_pos, init_scale)
        self.name = "Player"
        self.horizontal_states = {
            "idle": (HorizontalIdleState(self), ["running"]),
            "running": (RunningState(self), ["idle"]),
        }
        self.vertical_states = {
            "idle": (VerticalIdleState(self), ["jumping", "falling"]),
            "jumping": (JumpingState(self), ["falling"]),
            "falling": (FallingState(self), ["idle"]),
        }

        self.horizontal_state_machine = StateMachine("idle", self.horizontal_states)
        self.vertical_state_machine = StateMachine("idle", self.vertical_states)
        self.death_time = 0

        self.has_changed_dir = False
        self.cur_dir = 0
        self.cached_dir = 0

    def early_update(self):
        self.direction[0] = 0
        self.has_changed_dir = False
        return super().early_update()

    def before_col_update(self):

        if self.cur_dir != self.cached_dir:
            self.has_changed_dir = True

        self.cached_dir = self.cur_dir

        return super().before_col_update()

    def update(self):
        if self.is_dead:
            if pg.time.get_ticks() - self.death_time > Player.RESTART_TIME * 1000:
                self.engine_ref.restart_level()
        else:         

            self.horizontal_state_machine.update()
            self.vertical_state_machine.update()

            super().update()
            if self.direction[0] == 0 and self.direction[1] == 0:
                self.horizontal_state_machine.change_state("idle")
    
    def on_collision(self, colliding_sprites):
        if not self.is_dead:
            super().on_collision(colliding_sprites)
            for sprite in colliding_sprites:
                if self.is_dead:
                    break
                target = sprite.actor_ref
                if target.is_dead: continue
                if target.name == "Enemy":
                    enemy_is_killed = target.check_player_death(self)
                    if not enemy_is_killed:
                        self.kill()
                
                if target.name == "Pow":
                    # TODO: later, check if the player is on bottom of the pow. If not, act like a tile
                    target.hit()

                if "Tile" in target.name:
                    actor_center_x = self.sprite.rect.centerx
                    actor_center_y = self.sprite.rect.centery

                    target_center_y = target.sprite.rect.centery

                    target_left = target.sprite.rect.centerx - target.sprite.rect.width / 2
                    target_right = target.sprite.rect.centerx + target.sprite.rect.width / 2
                    is_left = actor_center_x < target_left
                    is_right = actor_center_x > target_right

                    is_above = actor_center_y < target_center_y
                    is_below = actor_center_y > target_center_y

                    if is_above:
                        self._physics.is_on_ground = True
                    elif is_left or is_right:
                        print("leftright")
                        if not self.has_changed_dir:
                            print("leftright0")
                            self.direction[0] = 0

                    if not is_above:
                        if is_below:
                            self.speed[1] = 0
    
    
    def kill(self):
        if not self.is_dead:
            SoundLoader.get_instance().play_sound("player_death.mp3", 1)
            self.is_dead = True
            self.death_time = pg.time.get_ticks()
            super().remove_from_engine()

# :::::::::::::::::::::::::::::: Inputs :::::::::::::::::::::::::::
    def input_press_up(self):
        self.vertical_state_machine.change_state("jumping")
        self.sprite.change_animation("jump")

    def input_press_left(self):
        self.direction[0] -= 1
        self.cur_dir = -1

    def input_press_right(self):
        self.direction[0] += 1
        self.cur_dir = 1