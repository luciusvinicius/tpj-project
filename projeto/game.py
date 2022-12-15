import pygame
from entity import Entity
from player import Player
from command import Command


class Game:

    def __init__(self, title, width, height, scale, fps):
        
        pygame.init()

        # Setup window
        self.title = title
        self.scale = scale
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.aspect_ratio = self.monitor_size[0] / self.monitor_size[1]
        
        # Set display to fullscreen if monitor matches set proportions, otherwise use init default scale
        if self.aspect_ratio == width/height:
            self.scale = self.monitor_size[0] / width
            self.display = pygame.display.set_mode((self.monitor_size[0], self.monitor_size[1]), pygame.FULLSCREEN)
        else:
            self.aspect_ratio = width/height
            self.display = pygame.display.set_mode((width * scale, height * scale))

        pygame.display.set_caption(title)
        

        self.is_running = False
        self.fps = fps
        self.clock = pygame.time.Clock()
        
        self.player = Player(self.display)
        self.objs = [self.player]

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                return

            elif event.type == pygame.KEYUP:
                event_str = f"release_{event.key}"
                if event_str in self.player.commands:
                    self.player.commands[event_str].execute()

            elif event.type == pygame.KEYDOWN:
                if event.key in self.player.commands:
                    self.player.commands[event.key].execute()

    def logic_loop(self):
        for obj in self.objs:
            obj.update()

    def render_loop(self):
        self.display.fill("gray")
        for obj in self.objs:
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
