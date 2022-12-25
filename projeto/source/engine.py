import os.path

import pygame as pg
from enum import Enum
from input_manager import*
from render_manager import*
from collision_manager import*
from input_interface import InputInterface
from enemy_default import Enemy
from sound_loader import SoundLoader
from Text import Text
from sprite_component import SpriteComponent


class ComponentTypes(Enum):
    Graphics = 1
    SomethingElse = 2


class Engine:

    def __init__(self, title, width, height, scale, fps, debug):

        pg.init()
        pg.font.init()
        self.debug = debug

        # Setup window
        self.title = title
        self.scale = scale
        self.monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
        self.aspect_ratio = self.monitor_size[0] / self.monitor_size[1]
        self.display = None

        # Set display to fullscreen if monitor matches set proportions, otherwise use init default scale
        if self.aspect_ratio == width / height and not self.debug:
            self.scale = self.monitor_size[0] / width
            self.display = pg.display.set_mode((self.monitor_size[0], self.monitor_size[1]), pg.FULLSCREEN)
        else:
            self.aspect_ratio = width / height
            self.display = pg.display.set_mode((width * scale, height * scale))

        pg.display.set_caption(title)

        self.is_running = False
        self.fps = fps
        self.clock = pg.time.Clock()

        # Managers
        self.input_manager = InputManager(self)
        self.render_manager = RenderManager(self)
        self.collision_manager = CollisionManager(self)

        self._game_actors = []
        self._input_game_actors = []

        # Score
        self.score = 0
        self.score_text = Text(self, "Score:", [10, 0], 32)
        self.render_manager.add_text(self.score_text)

    def add_actor(self, new_actor):
        self._game_actors.append(new_actor)
        if issubclass(type(new_actor), InputInterface):
            self._input_game_actors.append(new_actor)

        for component in new_actor.components:
            if issubclass(type(component), SpriteComponent):

                if new_actor.sprite.has_img:
                    self.render_manager.add_actor(new_actor)

                if new_actor.sprite.has_on_col:
                    self.collision_manager.add_actor(new_actor)

    def early_update(self):
        # Check for inputs
        command = self.input_manager.handle_input()
        if command is not None:
            for actor in self._input_game_actors:
                command.execute(actor)

    def update(self):
        # Update logic
        for obj in self._game_actors:
            obj.update()

        # Run collisions
        self.collision_manager.process()

    def late_update(self):
        # Render graphics
        self.render_manager.render()

    def play_bgm(self, bgm_path, volume=0.5):
        path = SoundLoader.sound_path
        pg.mixer.music.load(os.path.join(path, f"{bgm_path}"))
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(volume)

    # Game loop
    def run(self):
        self.is_running = True
      
        while self.is_running:

            if self.debug:
                self.display.fill("gray")

            self.early_update()
            self.update()
            self.late_update()

            self.clock.tick(self.fps)

        pg.quit()

    def stop_running(self):
        self.is_running = False
