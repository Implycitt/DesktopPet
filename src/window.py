import random, pyautogui

import tkinter as tk
from PIL import ImageTk

import pets

class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.pet = pets.Pets() 
        self.createWindow()

    def update(self):
        frame = self.pet.get_frame()
        self.label = tk.Label(image=frame)
        self.label.pack()

    def createWindow(self):
        self.window = tk.Tk()
        frame = self.pet.get_frame()
        self.label = tk.Label(image=frame)
        self.label.pack()
        self.window.mainloop()

