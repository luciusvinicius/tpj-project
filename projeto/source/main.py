from image_loader import *

from engine import *
from player import *
from sprite_component import *
from actor import *
from enemy_spawner import EnemySpawner
from level import Level


def main():
    TITLE = "Super Sussy Bros"
    WIDTH, HEIGHT = 16, 9
    SCALE = 64  # Corresponds to a low 16/9 resolution aka 1024/576
    FPS = 60
    DEBUG = True  # Affects fullscreen behaviour and collision debug

    # Setting image loader
    images_path = os.path.join(os.path.dirname(__file__), "..", "sprites/amogus")
    images_path = os.path.join(os.path.dirname(__file__), "..", "sprites/strangePlanet")
    ImageLoader(images_path)

    # Setup engine
    engine = Engine(TITLE, WIDTH, HEIGHT, SCALE, FPS, DEBUG)

    # ::::::::::::::::::::::::::Setup game:::::::::::::::::::::::::::
    # Level
    level = Level(os.path.join(os.path.dirname(__file__), "../maps/test1.map"), engine, SCALE, HEIGHT)


    # Player
    p_sprite = SpriteComponent(engine, "player.png", [3, 3], 40, 1, [0, 7], [0.5, 0.7], [CollisionLayers.Player], [CollisionLayers.Wall, 
     CollisionLayers.Enemy], True, True)
    p_sprite.set_up_animations([["idle", [0, 5], True, 1], ["walk", [6, 9], True, 100], ["jump", [13, 13], False, 100]], [28, 21], [8, 4])


    player1 = Player(engine, [p_sprite], [100, -200])
    engine.add_actor(player1)


    #def __init__(self, engine, components, init_pos=[0, 0], init_scale=[1, 1], spawn_rate=50, spawn_once=False):
    enemy_spawner = EnemySpawner(engine, [], [1, 1], [1, 1], 50, True)
    engine.add_actor(enemy_spawner)

    # ::::::::::::::::::::::::::Run:::::::::::::::::::::::::::
    engine.run()


if __name__ == '__main__':
    main()
