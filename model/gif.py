from tkinter import *
import _thread
import time


class GifPlay:
    play = True

    def __init__(self, label, giffile, delay):
        self.frame=[]
        i=0
        while 1:
            try:
                image=PhotoImage(file = giffile, format="gif -index "+str(i))
                self.frame.append(image)
                i=i+1
            except:
                break
        print(i)
        self.totalFrames=i-1
        self.delay=delay
        self.labelspace=label
        self.labelspace.image=self.frame[0]

    def start(self):
        _thread.start_new_thread(self.infinite, ())
        self.play = True

    def stop(self):
        self.play = False

    def infinite(self):
        i=0
        while self.play:
            self.labelspace.configure(image=self.frame[i])
            i=(i+1)%self.totalFrames
            time.sleep(self.delay)
