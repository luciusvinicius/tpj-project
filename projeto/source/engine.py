import pygame
from enum import Enum
from input_manager import*
from input_interface import InputInterface


class ComponentTypes(Enum):
    Graphics = 1
    Physics = 2
    

class Engine:

    def __init__(self, title, width, height, scale, fps, debug):
        
        pygame.init()
        self.debug = debug

        # Setup window
        self.title = title
        self.scale = scale
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.aspect_ratio = self.monitor_size[0] / self.monitor_size[1]
        
        # Set display to fullscreen if monitor matches set proportions, otherwise use init default scale
        if self.aspect_ratio == width/height and not self.debug:
            self.scale = self.monitor_size[0] / width
            self.display = pygame.display.set_mode((self.monitor_size[0], self.monitor_size[1]), pygame.FULLSCREEN)
        else:
            self.aspect_ratio = width/height
            self.display = pygame.display.set_mode((width * scale, height * scale))

        pygame.display.set_caption(title)
        

        self.is_running = False
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.input_manager = InputManager(self)
        
        self._game_actors = []
        self._input_game_actors = []

    def add_actor(self, new_actor):
        self._game_actors.append(new_actor)

        if issubclass(type(new_actor), InputInterface):
            self._input_game_actors.append(new_actor)
        

    def early_update(self):

        # Check for inputs
        command = self.input_manager.handle_input()
        if command != None:
            for actor in self._input_game_actors:
                command.execute(actor)

    def update(self):
        for obj in self._game_actors:
            obj.update()

    def late_update(self):
        self.display.fill("gray")
        for obj in self._game_actors:
            obj.render()

        pygame.display.flip()

    # Game loop
    def run(self):
        self.is_running = True
        while self.is_running:
            
            self.early_update()
            self.update()
            self.late_update()
    
            self.clock.tick(self.fps)
        
        pygame.quit()

    def stop_running(self):
        self.is_running = False
