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
            print(actor.name)
            colliding_sprites = []

            for actor_group in actor.sprite.col_groups:
                colliding_sprite = pg.sprite.spritecollideany(actor.sprite, self.all_groups[actor_group])
                # print(f"colliding_sprite: {colliding_sprite}")
                if colliding_sprite is not None:
                    colliding_sprites.append(colliding_sprite)

                print(f"actor_group: {actor_group.value}")
                # if actor_group.value == CollisionLayers.Player.value:
                #     print("Gamer")
                #     for group in self.all_groups.values():
                #         colliding_test = pg.sprite.groupcollide(self.all_groups[actor_group], group, True, False)
                #         print(colliding_test)

            if len(colliding_sprites) > 0:
                actor.on_collision(colliding_sprites)
