from image_loader import *

from engine import *
from player import *
from sound_loader import SoundLoader
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

    # Setting sound
    sounds_path = os.path.join(os.path.dirname(__file__), "..", "sounds")
    SoundLoader(sounds_path)

    # ::::::::::::::::::::::::::Setup game:::::::::::::::::::::::::::
    # Level
    Level(os.path.join(os.path.dirname(__file__), "../maps/test1.map"), engine, SCALE, HEIGHT)

    # ::::::::::::::::::::::::::Run:::::::::::::::::::::::::::
    engine.play_bgm("bgm.wav", volume=0)
    engine.run() 


if __name__ == '__main__':
    main()
