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
        self.death_time = 0
        self.colliding_tiles = []

    def early_update(self):
        self.direction[0] = 0
        self.colliding_tiles = []

        self.speed[1] = 0
        return super().early_update()

    def update(self):
        if self.is_dead:
            if pg.time.get_ticks() - self.death_time > Player.RESTART_TIME * 1000:
                self.engine_ref.restart_level()
        else:
            
            

            self._physics.update(self.pos, self.speed, self.direction, self.gravity, True)
            self.treat_tile_cols(True)
            self._physics.update(self.pos, self.speed, self.direction, self.gravity, False)
            self.treat_tile_cols(False)

            self.horizontal_state_machine.update()
            self.vertical_state_machine.update()

            self._physics.is_on_ground = False
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

                # Tile logic
                if "Tile" in target.name:
                    self.colliding_tiles.append(sprite)
                
                # Logic if Enemy
                if target.name == "Enemy":
                    enemy_is_killed = target.check_player_death(self)
                    if not enemy_is_killed:
                        self.kill()
                
                # Logic if Pow
                if target.name == "Pow":
                    # TODO: later, check if the player is on bottom of the pow. If not, act like a tile
                    target.hit()


    def treat_tile_cols(self, is_horizontal):

        if len(self.colliding_tiles) < 10:
            for sprite in self.colliding_tiles:
                if sprite.rect.colliderect(self.sprite.rect):

                    actor_center_x = self.sprite.rect.centerx
                    actor_center_y = self.sprite.rect.centery
    
                    actor_left = actor_center_x - self.sprite.rect.width / 2
                    actor_right = actor_center_x + self.sprite.rect.width / 2
    
                    actor_bottom = actor_center_y - self.sprite.rect.height / 2
                    actor_top = actor_center_y + self.sprite.rect.height / 2
    
            
                    target_center_x = sprite.rect.centerx
                    target_center_y = sprite.rect.centery
    
                    target_left = target_center_x - sprite.rect.width / 2
                    target_right = target_center_x + sprite.rect.width / 2
    
                    target_bottom = target_center_y - sprite.rect.height / 2
                    target_top = target_center_y + sprite.rect.height / 2
    
    
                    if is_horizontal:
                        
                        if self.direction[0] < 0: 
                            print("left")
                            
                            self.pos[0] += target_right - actor_left
                            self.pos[0] += 5
                            
                        if self.direction[0] > 0: 
                            print("actorright")
                            print(self.sprite.rect.right)
                            print("targetleft")
                            print(sprite.rect.left)
                            print("pos")
                            print(self.pos[0])
                            self.pos[0] += target_left - actor_right
                            self.pos[0] -= 5
                            
                    else:
                        print(self.speed[1])
                        
                        if self.speed[1] > 0:
                            
                            #print(actor_bottom - target_top)
                
                            self.pos[1] += target_top - actor_bottom
                            self._physics.is_on_ground = True

                        if self.speed[1] < 0:
                            
                            self.pos[1] += target_bottom - actor_top

                        


                """ 
                actor_center_x = self.sprite.rect.centerx
                actor_center_y = self.sprite.rect.centery

                target_center_x = sprite.rect.centerx
                target_center_y = sprite.rect.centery

                target_left = target_center_x - sprite.rect.width / 2
                target_right = target_center_x + sprite.rect.width / 2

                is_left = actor_center_x < target_left
                is_right = actor_center_x > target_right
                is_above = actor_center_y < target_center_y

                if is_above:
                    self._physics.is_on_ground = True
                elif is_left or is_right:
                    self.direction[0] = 0 """
    
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
    