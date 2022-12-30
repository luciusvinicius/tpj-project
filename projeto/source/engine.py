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
from signal_manager import SignalManager
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
        self.fps = fps

        self.setup()
        signal_manager = SignalManager.get_instance()
        signal_manager.listen_to_signal("enemy_dead", self)

    def setup(self, run=False):
        
        self.is_running = run
        self.should_restart = False
        self.clock = pg.time.Clock()

        # Managers
        self.input_manager = InputManager(self)
        self.render_manager = RenderManager(self)
        self.collision_manager = CollisionManager(self)

        self._game_actors = []
        self._input_game_actors = []

        # Score
        self.score = 0
        self.score_text = Text(self, f"Score: {self.score}", [10, 0], 32)
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

    def add_level(self, level):
        self.level = level
        level.load_map()

    def early_update(self):
        
        for obj in self._game_actors:
            obj.early_update()
            
        # Check for inputs
        commands = self.input_manager.handle_input()
        for command in commands:
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
        return self.should_restart

    def stop_running(self, should_restart=False):
        self.is_running = False
        self.should_restart = should_restart
    
    def restart_level(self):
        for actor in self._game_actors:
            if not isinstance(actor, Enemy): continue
            signal_manager = SignalManager.get_instance()
            signal_manager.unlisten_to_signal("pow_hit", actor)
        self.setup(True)
        self.level.load_map()

    def on_signal(self, signal, *args):
        if signal == "enemy_dead":
            enemy = args[0]
            if enemy.sprite.is_disabled: return
            self.score += enemy.score
            self.score_text.set_text(f"Score: {self.score}")
