import os
import tkinter as tk
from PIL import ImageTk, Image

class Pets():

    animation = []
    dir = '..\\assets\\'

    def __init__(self):
        self.name = 'cat'
        self.state = 0 
        self.index = 0
        self.animation = self.get_animations()
        self.image = self.animation[self.state]

    def get_animations(self):
        directory = self.dir + self.name
        for file in os.listdir(directory):
            self.animation.append(os.path.join(directory, file))

        return self.animation

    def get_frame(self):
        frame = self.animation[self.index]

        self.index += 1
        if self.index == len(self.animation):
            self.index = 0

        return ImageTk.PhotoImage(Image.open(frame))
