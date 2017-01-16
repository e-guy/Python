from tkinter import *


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



def main():
    app = Application()
    app.master.title('H')
    app.mainloop()


main()


    

