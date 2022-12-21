import pygame as pg
from enum import Enum

class CollisionLayers(Enum):
    Player = 1
    Wall = 2
    Enemy = 3

class CollisionManager:
    def __init__(self, engine) -> None:
        self._engine_ref = engine
        self.all_groups = {}
        self._actors_with_col = []

        for Layer in CollisionLayers:
            self.all_groups[Layer] = pg.sprite.Group()

    def add_actor(self, new_actor):
        self._actors_with_col.append(new_actor)

    def process(self):
        for actor in self._actors_with_col:
            colliding_sprites = []

            for group in actor.sprite.col_groups:
                colliding_sprite = pg.sprite.spritecollideany(actor.sprite, self.all_groups[group])

                if colliding_sprite is not None:
                    colliding_sprites.append(colliding_sprite)

            if len(colliding_sprites) > 0:
                actor.on_collision(colliding_sprites)
                
