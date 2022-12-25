import pygame as pg
import os

class Text:

    def __init__(self, engine, content, position, size, color="white", bg_color=None):
        # self.font = pg.font.Font('freesansbold.ttf', size)
        self.font = pg.font.Font("arial.ttf", size)
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
        self.text_rect.center = self.position

    def render(self):
        self.engine.display.blit(self.text, self.text_rect)
