import random, pyautogui

import tkinter as tk
from PIL import ImageTk, Image

import pets

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.createWidget()
        self.mainloop()

    def createWidget(self):
        frames = self.getImage()
        self.gifLabel = tk.Label(self)
        self.playGif(self.gifLabel, frames)

    def playGif(self, label, frames):

        totalDelay = 50
        delayFrames = 100

        for frame in frames:
            self.after(totalDelay, self.nextFrame, frame, label, frames)
            totalDelay += delayFrames

        self.after(totalDelay, self.nextFrame, frame, label, frames, True)


    def nextFrame(self, frame, label, frames, restart=False):

        if restart:
            self.after(1000, self.playGif, label, frames)
            return

        label.config(image=frame)
        label.pack()

    def getImage(self):
        pet = pets.Pets()
        frames = pet.getFrames(pet.getGif(pet.state))
        return frames
