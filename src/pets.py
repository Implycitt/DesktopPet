import os, random
import tkinter as tk
from PIL import ImageTk, Image

class Pets():

    animation = []
    dir = '..\\assets\\'
    idle =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    sleep = [19, 20, 21, 22, 23, 24, 25] 
    walkLeft = [13, 14, 15]
    walkRight = [16, 17, 18]

    def __init__(self):
        self.dirName = 'jackie'
        self.name = "KITTY CAT"
        self.types = [file for file in os.listdir(self.dir)]

        self.animation = []
        self.getGifs()
        self.animations = {}
        self.state = 0 
        self.cycles = 0 
        self.xPos = 0
        self.yPos = 0

        self.getAnimations()

    def setXPos(self, x):
        self.xPos = x

    def setYPos(self, y):
        self.yPos = y

    def getAnimations(self):
        for num, i in enumerate(self.animation):
            self.animations[num] = self.getFrames(i)

    def getGifs(self):
        directory = self.dir + self.dirName
        for file in os.listdir(directory):
            self.animation.append(os.path.join(directory, file))

    def getGif(self, i):
        return self.animation[i]

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

    def setState(self, s):
        self.state = s

