import random, pyautogui

import tkinter as tk
from PIL import ImageTk, Image
from win32api import GetMonitorInfo, MonitorFromPoint 
from tktooltip import ToolTip

import pets

class Window(tk.Tk):

    monitor = GetMonitorInfo(MonitorFromPoint((0, 0)))
    area = monitor.get('Work')
    width = area[2]
    height = area[3]

    def __init__(self):
        super().__init__()

        self.pet = pets.Pets()
        self.pet.getAnimations()
        self.pet.setXPos(random.randrange(int(self.width*0.7), self.width))
        self.pet.setYPos(self.height-100)

        self.label = tk.Label(self, bd=0, bg='black')
        ToolTip(self.label, msg=f"{self.pet.name}")
        self.eventNumber = random.randint(1, 3)
        self.iFrame = 0

        self.config(highlightbackground='black')
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.wm_attributes('-transparentcolor', 'black')
        self.label.pack()

        self.after(1, self.update, self.iFrame, self.pet.state, self.eventNumber, self.pet.xPos)

        self.mainloop()    


    def event(self, iFrame, state, eventNumber, x):
        
        time = 100

        if self.eventNumber in self.pet.idle:
            time = 400
            self.pet.setState(0) 
        elif self.eventNumber == 12:
            self.pet.setState(1) 
        elif self.eventNumber in self.pet.sleep:
            time = 400
            self.pet.setState(2) 
        elif self.eventNumber == 26:
            self.pet.setState(3) 
        elif self.eventNumber in self.pet.walkLeft:
            self.pet.setState(4) 
        elif self.eventNumber in self.pet.walkRight:
            self.pet.setState(5) 

        self.after(time, self.update, self.iFrame, self.pet.state, self.eventNumber, self.pet.xPos)

    def update(self, iFrame, state, eventNumber, x):

        self.frame = self.pet.animations[self.pet.state][self.iFrame]
        a = 0
        b = 0

        s = self.pet.state
        if s == 0:
            a, b = 1, 18
        elif s == 1:
            a, b = 19, 19
        elif s == 2:
            a, b = 19, 26 
        elif s == 3: 
            a, b = 1, 1
        elif s == 4 and self.pet.xPos > 0: 
            a, b = 1, 18
            self.pet.xPos -= 3
        elif s == 5 and self.pet.xPos < (self.width-100): 
            a, b = 1, 18
            self.pet.xPos += 3

        self.iFrame, self.eventNumber = self.animate(self.iFrame, self.pet.animations[self.pet.state], self.eventNumber, a, b)

        self.geometry(f"100x100+{self.pet.xPos}+{self.pet.yPos}")
        self.label.configure(image=self.frame)
        self.after(1, self.event, self.iFrame, self.pet.state, self.eventNumber, self.pet.xPos)


    def animate(self, iFrame, frames, eventNumber, a, b):

        if self.iFrame == len(frames)-1:
            self.iFrame = 0
            self.eventNumber = random.randint(a, b)
        else:
            self.iFrame += 1

        return self.iFrame, self.eventNumber

