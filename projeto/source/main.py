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

    # Setting sound
    sounds_path = os.path.join(os.path.dirname(__file__), "..", "sounds")

    start_engine(TITLE, WIDTH, HEIGHT, SCALE, FPS, DEBUG, sounds_path)
    
def start_engine(title, width, height, scale, fps, debug, sounds_path):
    # Setup engine
    engine = Engine(title, width, height, scale, fps, debug)

    # ::::::::::::::::::::::::::Setup game:::::::::::::::::::::::::::
    # Level
    level = Level(os.path.join(os.path.dirname(__file__), "../maps/test1.map"), engine, scale, height)
    engine.add_level(level)
    if not SoundLoader.has_instance():
        SoundLoader(sounds_path)
    
    sound_loader = SoundLoader.get_instance()
    # ::::::::::::::::::::::::::Run:::::::::::::::::::::::::::
    sound_loader.play_bgm("bgm.wav", volume=0)
    return engine.run() 


if __name__ == '__main__':
    main()
