from image_loader import*

from engine import*
from player import*


def main():
    TITLE = "Super Sussy Bros"
    WIDTH, HEIGHT = 16, 9
    SCALE = 64 # Corresponds to a low 16/9 resolution aka 1024/576
    FPS = 60
    DEBUG = True # As of right now, this just messes with the default fullscreen support in engine's "init"
 
    # Setting image loader
    images_path = os.path.join(os.path.dirname(__file__), "..", "sprites/amogus")
    ImageLoader(images_path)

    # Setup engine
    engine = Engine(TITLE, WIDTH, HEIGHT, SCALE, FPS, DEBUG)

    # Setup game
    player1 = Player(engine, [ComponentTypes.Graphics, ComponentTypes.Physics], [1, 1])
    engine.game_actors.append(player1)

    # Run
    engine.run()


if __name__ == '__main__':
    main()
