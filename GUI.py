# import Tkinter  
from tkinter import *

# define a drived class "Application" whose base class is "Frame"
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel=Label(self, text='Hello')
        self.helloLabel.pack()
        
        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.quitButton=Button(self, text='quit', command=self.quit)
        self.quitButton.pack()


# 
def main():
    app = Application()
    app.master.title('H')
    app.mainloop()

#
main()


    

