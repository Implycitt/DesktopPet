import os
import tkinter as tk
from PIL import ImageTk, Image

class Pets():

    animation = []
    dir = '..\\assets\\'

    def __init__(self):
        self.name = 'cat'
        self.state = 0 
        #self.index = 0
        self.getAnimations()
        self.image = self.animation[self.state]

    def getAnimations(self):
        directory = self.dir + self.name
        for file in os.listdir(directory):
            self.animation.append(os.path.join(directory, file))

    def getGif(self, index):
        return self.animation[index]

    def getFrames(self, image):
        with Image.open(image) as gif:
            index = 0
            frames = []
            while True:
                try:
                    gif.seek(index)
                    frame = ImageTk.PhotoImage(gif)
                    frames.append(frame)
                except EOFError:
                    break
                index += 1

            return frames

