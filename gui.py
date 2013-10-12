from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style
from urlOpener import * 

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("URL OPENER")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand = 1)
        def getInput():
            print "received input"
        googleButton = Button(self, text = "Google", command= lambda : browserOpener.openIESite('www.google.com'))
        googleButton.pack()
        ignButton = Button(self, text = "IGN", command = lambda : browserOpener.openIESite('www.ign.com'))
        ignButton.pack()
    
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()
if __name__ == '__main__':
    browserOpener = myBrowserOpener()
    main()
