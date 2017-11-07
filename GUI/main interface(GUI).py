"""main interface"""

from tkinter import *

root = Tk()

root.title('กินอะไรดี')

topFrame = Frame(root,height = 100)
topFrame.pack()

menuFrame = Label(topFrame)
menuFrame.pack(side=LEFT)




def main():