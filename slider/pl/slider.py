from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.master=screen
        self.master.overrideredirect(True)
        self.createWidget()

    def createWidget(self):

        image = Image.open("file/layer1.jpg")
        self.player_1 = ImageTk.PhotoImage(image)

        image2 = Image.open("file/layer2.jpg")
        self.player_2 = ImageTk.PhotoImage(image2)

        image3 = Image.open("file/layer3.jpg")
        self.player_3 = ImageTk.PhotoImage(image3)


        self.layer_1=Frame(self.master,bg="red",width=400,height=500)

        self.lblimage1=Label(self.layer_1,image=self.player_1)
        self.lblimage1.pack(fill=BOTH)
        self.lblimage1.bind("<Button-3>", self.ShowLayer_2)

        self.lbltitle=Label(self.layer_1,text="Burj Alarab",font="nazanin 15 bold",bg="light yellow").place(x=20,y=300)

        self.lblcaption=Label(self.layer_1,text="It is a beautiful tower that made in 1999\nlord of Dubai was wanting that it would be a sign of the city but\n it has a non muslim sign on the top\n so he changed his mind ",width=50)
        self.lblcaption.place(x=20,y=350)

        self.lblmap=Label(self.layer_1,text="show in map")
        self.lblmap.place(x=10,y=430)
        self.lblmap.bind("<Button-1>",self.ShowLink)
        self.layer_1.place(x=0,y=0)

        self.layer_2=Frame(self.master,bg="blue",width=400,height=500)
        self.lblimage2=Label(self.layer_2,image=self.player_2)
        self.lblimage2.pack(fill=BOTH)
        self.lblimage2.bind("<Button-3>", self.ShowLayer_3)
        self.layer_2.place(x=0,y=0)

        self.layer_3=Frame(self.master,bg="black",width=400,height=500)
        self.lblimage3=Label(self.layer_3,image=self.player_3)
        self.lblimage3.pack(fill=BOTH)
        self.lblimage3.bind("<Button-3>", self.ShowLayer_1)
        self.layer_3.place(x=0,y=0)

        self.btnclose=Button(self.master,text="x",command=self.master.destroy).place(x=5,y=5)

        self.HideLayer_All()
        self.ShowLayer_1()

    def HideLayer_1(self):
        self.layer_1.place_forget()
    def ShowLayer_1(self,e=""):
        self.HideLayer_All()
        self.layer_1.place(x=0,y=0)

    def HideLayer_2(self):
        self.layer_2.place_forget()
    def ShowLayer_2(self,e=""):
        self.HideLayer_All()
        self.layer_2.place(x=0, y=0)

    def HideLayer_3(self):
        self.layer_3.place_forget()
    def ShowLayer_3(self,e=""):
        self.HideLayer_All()
        self.layer_3.place(x=0, y=0)

    def HideLayer_All(self):
        self.layer_1.place_forget()
        self.layer_2.place_forget()
        self.layer_3.place_forget()

    def ShowLink(self,e):
        webbrowser.open("https://www.google.com")