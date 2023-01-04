import random

from player import Player
from enemy_spawner import EnemySpawner
from sprite_component import SpriteComponent
from tile import Tile
from collision_manager import CollisionLayers
from pow_obj import Pow
from actor import Actor


ENTITIES = {
    "-": Tile,
}


class Level:

    def __init__(self, map_path, engine, game_scale=64, height=9, tile_scale=0.75):
        self.tiles = []
        self.entities = []
        self.engine = engine
        self.game_scale = game_scale
        self.height = height
        self.tile_scale = tile_scale
        self.map_path = map_path

        # TODO: properly implement width 
        self.width = 15
    
    def get_height(self):
        return self.game_scale * self.height

    def get_width(self):
        return self.game_scale * self.width

    def load_map(self):
        map_path = self.map_path
        max_width = 0
        tile_map = []
        with open(map_path, "r") as f:
            has_started = False
            for line in f:
                line = line[:-1] # Remove newline character
                if line == "START":
                    has_started = True
                    continue

                if not has_started: continue
                line_width = len(line)
                if line_width > max_width: max_width = line_width
                tile_map.append(line)


        # Adding background
        bg_sprite = SpriteComponent(self.engine, "background.png", [4, 4])
        bg = Actor(self.engine, [bg_sprite], [0, 100])
        self.engine.add_actor(bg)
                        
        for idx_line, tile_line in enumerate(reversed(tile_map)):
            line_height = self.game_scale * (self.height - (idx_line + 1) * self.tile_scale)

            for idx, tile in enumerate(tile_line):
                horizontal_offset = idx * self.game_scale * self.tile_scale
                match tile:
                    case "-":
                        tile_gc = SpriteComponent(self.engine, "tile.jpg", [self.tile_scale, self.tile_scale], 40, 0, [0,0], [1, 1], 
                         [CollisionLayers.Wall], [], True, False)
                        new_tile = Tile(self.engine, [tile_gc], [horizontal_offset, -line_height])
                        self.tiles.append(new_tile)
                        self.engine.add_actor(new_tile)
                        # print("Added tile at", idx * self.game_scale, line_height)

                    case "P":
                        p_sprite = SpriteComponent(self.engine, "player.png", [3, 3], 40, 1, [0, 7], [0.5, 0.7],
                                                   [CollisionLayers.Player], [CollisionLayers.Wall,
                                                                              CollisionLayers.Enemy, CollisionLayers.POW], True, True)
                        p_sprite.set_up_animations(
                            [["idle", [0, 5], True, 1], ["walk", [6, 9], True, 100], ["jump", [13, 13], False, 100]], [28, 21],
                            [8, 4])

                        player1 = Player(self.engine, [p_sprite], [horizontal_offset - p_sprite.rect.width / 2, -line_height + p_sprite.rect.height / 2])
                        self.engine.add_actor(player1)

                    case "R":
                        es_sprite = SpriteComponent(self.engine, "portal2.png", [0.07, 0.07], 40, 1, [0, 7], [0.5, 0.7],
                                                [], [], True, False)

                        es_sprite.set_up_animations(
                            [["idle", [0, 5], True, 100]], [3200/5, 1280/2], [5, 2]
                        )
                        random_val = random.random() * 100
                        enemy_spawner = EnemySpawner(self.engine, [es_sprite], [horizontal_offset, -line_height], [1, 1], random_val, direction=1)
                        self.engine.add_actor(enemy_spawner)
                    
                    case "L":
                        es_sprite = SpriteComponent(self.engine, "portal2.png", [0.07, 0.07], 40, 1, [0, 7], [0.5, 0.7],
                                                [], [], True, False)

                        es_sprite.set_up_animations(
                            [["idle", [0, 5], True, 100]], [3200/5, 1280/2], [5, 2]
                        )
                        random_val = random.random() * 100
                        enemy_spawner = EnemySpawner(self.engine, [es_sprite], [horizontal_offset, -line_height], [1, 1], random_val, direction=-1)
                        self.engine.add_actor(enemy_spawner)
                    
                    case "O":
                        po_sprite = SpriteComponent(self.engine, "pow_tile.png", [2/7, 2/7], 40, 0, [0, 0], [1, 1], [CollisionLayers.POW], [], True, False)
                        po_obj = Pow(self.engine, [po_sprite], [horizontal_offset, -line_height])
                        self.engine.add_actor(po_obj)


