from player import Player
from sprite_component import SpriteComponent
from tile import Tile
from collision_manager import CollisionLayers


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

        self.load_map(map_path)


    def load_map(self, map_path):
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

        for idx_line, tile_line in enumerate(reversed(tile_map)):
            tiles_idx = idx_line + self.tile_scale
            line_height = self.game_scale * (self.height - tiles_idx)
            for idx, tile in enumerate(tile_line):
                match tile:
                    case "-":
                        tile_gc = SpriteComponent(self.engine, "tile.jpg", [self.tile_scale, self.tile_scale], 40, 0, [0,0], [1, 1], 
                         [CollisionLayers.Wall], [], True, False)
                        new_tile = Tile(self.engine, [tile_gc], [idx * self.game_scale * self.tile_scale, -line_height])
                        self.tiles.append(new_tile)
                        self.engine.add_actor(new_tile)
                        # print("Added tile at", idx * self.game_scale, line_height)
