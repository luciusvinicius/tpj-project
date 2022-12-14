import pygame as pg

class RenderManager:
    def __init__(self, engine) -> None:
        self._engine_ref = engine
        self._actors_to_render = []
        self._text_to_render = []

    def add_actor(self, actor):
        self._actors_to_render.append(actor)
        self._actors_to_render.sort(key=self.sort_actors)

    def add_text(self, text):
        self._text_to_render.append(text)

    def render(self):
        if not self._engine_ref.debug:
            self._engine_ref.display.fill("gray")

        for actor in self._actors_to_render:
            actor.sprite.render()

        for text in self._text_to_render:
            text.render()

        pg.display.flip()
    
    def remove_actor(self, actor):
        for i,a in enumerate(self._actors_to_render):
            if a.id == actor.id:
                self._actors_to_render.pop(i)
                
    def sort_actors(self, val):
        return val.sprite.layer