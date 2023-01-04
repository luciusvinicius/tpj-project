import pygame as pg
from enum import Enum


class CollisionLayers(Enum):
    Player = 1
    Wall = 2
    Enemy = 3
    POW = 4


class CollisionManager:
    def __init__(self, engine):
        self._engine_ref = engine
        self.all_groups = {}
        self._actors_with_col = []

        for Layer in CollisionLayers:
            self.all_groups[Layer] = pg.sprite.Group()

    def add_actor(self, new_actor):
        self._actors_with_col.append(new_actor)
    
    def remove_actor(self, actor):
        if actor in self._actors_with_col:
            self._actors_with_col.remove(actor)

    def process(self):

        for actor in self._actors_with_col:
            colliding_sprites = []
            colliding_test = []

            for target_group in actor.sprite.col_groups:

                for actor_group in actor.sprite.own_groups:
                    colliding_test = pg.sprite.groupcollide(self.all_groups[actor_group], self.all_groups[target_group], False, False)
                    for sprite in colliding_test:
                        if sprite.actor_ref == actor:
                            for target_sprites in colliding_test.values():
                                # Extending list
                                colliding_sprites += target_sprites     

                               
            if len(colliding_sprites) > 0:
                actor.on_collision(colliding_sprites)
