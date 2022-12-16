import pygame as pg

class Command:
    def execute():
        raise NotImplementedError("You must implement the execute() method in the derived class!")

class PressUp(Command):
    def execute(actor):
        method = getattr(actor, "input_press_up", None)
        if callable(method):
            actor.input_press_up()
class PressDown(Command):
    def execute(actor):
        method = getattr(actor, "input_press_down", None)
        if callable(method):
            actor.input_press_down()
class PressLeft (Command):
    def execute(actor):
        method = getattr(actor, "input_press_left", None)
        if callable(method):
            actor.input_press_left()
class PressRight (Command):
    def execute(actor):
        method = getattr(actor, "input_press_right", None)
        if callable(method):
            actor.input_press_right()


class ReleaseUp(Command):
    def execute(actor):
        method = getattr(actor, "input_release_up", None)
        if callable(method):
            actor.input_release_up()
class ReleaseDown(Command):
    def execute(actor):
        method = getattr(actor, "input_release_down", None)
        if callable(method):
            actor.input_release_down()
class ReleaseLeft (Command):
    def execute(actor):
        method = getattr(actor, "input_release_left", None)
        if callable(method):
            actor.input_release_left()
class ReleaseRight (Command):
    def execute(actor):
        method = getattr(actor, "input_release_right", None)
        if callable(method):
            actor.input_release_right()

class InputManager:
    command_press = {
        pg.K_UP : PressUp,
        pg.K_LEFT : PressLeft,
        pg.K_DOWN : PressDown,
        pg.K_RIGHT : PressRight,
    }

    command_release = {
    pg.K_UP : ReleaseUp,
    pg.K_LEFT : ReleaseLeft,
    pg.K_DOWN : ReleaseDown,
    pg.K_RIGHT : ReleaseRight,
    }

    def __init__(self, engine):
        self.engine_ref = engine 
        self.command_to_use = None

    def handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
               self.engine_ref.stop_running()
            else:
                match event.type:
                    case pg.KEYDOWN:
                        self.command_to_use = self.command_press
                    case pg.KEYUP:
                        self.command_to_use = self.command_release
                    case _:
                        self.command_to_use = None


                if self.command_to_use != None:
                    match event.key:
                        case pg.K_UP:
                            return self.command_to_use[event.key]
                        case pg.K_DOWN:
                            return self.command_to_use[event.key]
                        case pg.K_LEFT:
                            return self.command_to_use[event.key]
                        case pg.K_RIGHT:
                            return self.command_to_use[event.key]
