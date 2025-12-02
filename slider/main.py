from tkinter import *
from pl.slider import App

if __name__ == "__main__":
    screen = Tk()
    screen.geometry("400x500+500+100")
    screen.title("welcome")
    pageMe=App(screen)

    screen.mainloop()
