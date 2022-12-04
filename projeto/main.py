from game import Game


def main():
    TITLE = "Super Sussy Bros"
    WIDTH, HEIGHT = 80, 60
    SCALE = 10
    FPS = 10
    game = Game(TITLE, WIDTH, HEIGHT, SCALE, FPS)

    game.run()


if __name__ == '__main__':
    main()
