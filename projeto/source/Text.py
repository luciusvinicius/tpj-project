import pygame as pg
import os

class Text:

    def __init__(self, engine, content, position, size, color="white", bg_color=None):
        self.font = pg.font.Font(os.path.join(os.path.dirname(__file__), "../fonts/comic-sans-ms/ComicSansMS3.ttf")
                                 , size)
        self.engine = engine
        self.content = content
        self.position = position
        self.size = size
        self.color = color
        self.bg_color = bg_color

        if bg_color is None:
            self.text = self.font.render(self.content, True, self.color)
        else:
            self.text = self.font.render(self.content, True, self.color, self.bg_color)

        self.text_rect = self.text.get_rect()
        self.text_rect.center = [self.position[0] + self.text_rect.width / 2, self.position[1] + self.text_rect.height / 2]

    def render(self):
        self.engine.display.blit(self.text, self.text_rect)
