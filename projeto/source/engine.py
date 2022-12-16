import pygame
from command import Command
from enum import Enum
from input_manager import*


class ComponentTypes(Enum):
    Graphics = 1
    Physics = 2
    

class Engine:

    def __init__(self, title, width, height, scale, fps):
        
        pygame.init()

        # Setup window
        self.title = title
        self.scale = scale
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.aspect_ratio = self.monitor_size[0] / self.monitor_size[1]
        
        # Set display to fullscreen if monitor matches set proportions, otherwise use init default scale
        if self.aspect_ratio != width/height:
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
        
        self.game_actors = []

    def event_loop(self):
        command = self.input_manager.handle_input()
        if command != None:
            for actor in self.game_actors:
                command.execute(actor)

            """   
            elif event.type == pygame.KEYUP:
                event_str = f"release_{event.key}"
                if event_str in self.player.commands:
                    self.player.commands[event_str].execute()

            elif event.type == pygame.KEYDOWN:
                if event.key in self.player.commands:
                    self.player.commands[event.key].execute() """

    def logic_loop(self):
        for obj in self.game_actors:
            obj.update()

    def render_loop(self):
        self.display.fill("gray")
        for obj in self.game_actors:
            obj.render()

    # Game loop
    def run(self):
        self.is_running = True
        while self.is_running:
            # Temporary
            # print(f"Game inputs: {Game.INPUTS_EVENT}")
            # pygame.event.post(self.inputs_ev)
            # pygame.event.post(self.graphics_ev)

            # Loops
            self.event_loop()
            self.logic_loop()
            self.render_loop()

            # Update window
            pygame.display.flip()
            self.clock.tick(self.fps)
        
        pygame.quit()

    def stop_running(self):
        self.is_running = False
