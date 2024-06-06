import os, random
import tkinter as tk
from PIL import ImageTk, Image

class Pets():

    animation = []
    dir = '..\\assets\\'

    def __init__(self):
        self.name = 'cat'
        self.getAnimations()
        self.state = 0 
        self.cycles = 0 
        self.getCycles()
        self.image = self.animation[self.state]

    def getAnimations(self):
        directory = self.dir + self.name
        for file in os.listdir(directory):
            self.animation.append(os.path.join(directory, file))

    def getGif(self):
        return self.animation[self.state]

    def getCycles(self):
        name = self.getGif() 
        if 'to' in name:
            self.cycles = 1
        else:
            self.cycles = random.randint(1, 5)

    def newState(self):
        self.state = random.randint(0, len(self.animation)-1)

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

