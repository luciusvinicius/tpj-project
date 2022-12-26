import pygame as pg


class Command:
    def execute():
        raise NotImplementedError("You must implement the execute() method in the derived class!")


class PressUp(Command):
    def execute(actor):
        actor.input_press_up()


class PressDown(Command):
    def execute(actor):
        actor.input_press_down()


class PressLeft(Command):
    def execute(actor):
        actor.input_press_left()


class PressRight(Command):
    def execute(actor):
        actor.input_press_right()


class ReleaseUp(Command):
    def execute(actor):
        actor.input_release_up()


class ReleaseDown(Command):
    def execute(actor):
        actor.input_release_down()


class ReleaseLeft(Command):
    def execute(actor):
        actor.input_release_left()


class ReleaseRight(Command):
    def execute(actor):
        actor.input_release_right()


class InputManager:
    command_press = {
        pg.K_UP: PressUp,
        pg.K_LEFT: PressLeft,
        pg.K_DOWN: PressDown,
        pg.K_RIGHT: PressRight,
    }

    command_release = {
        pg.K_UP: ReleaseUp,
        pg.K_LEFT: ReleaseLeft,
        pg.K_DOWN: ReleaseDown,
        pg.K_RIGHT: ReleaseRight,
    }

    def __init__(self, engine):
        self.engine_ref = engine
        self.command_to_use = None

    def handle_input(self):
        keys = pg.key.get_pressed()
        commands = []
        
        for command_key in self.command_press:
            if keys[command_key]:
                commands.append(self.command_press[command_key])
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.engine_ref.stop_running()

        return commands
