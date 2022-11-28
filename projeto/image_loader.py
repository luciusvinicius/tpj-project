import os
import pygame as pg

class ImageLoader:
    __instance = None
    @staticmethod
    def get_instance():
        if ImageLoader.__instance == None:
            ImageLoader()
        return ImageLoader.__instance
    
    def __init__(self, image_path):
        if ImageLoader.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ImageLoader.__instance = self
            self.image_path = image_path
            self.image_dict = {}
            self.load_images()
    
    def load_images(self):
        for image in os.listdir(self.image_path):
            self.image_dict[image] = pg.image.load(os.path.join(self.image_path, image))