import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.topframe, text = "John")
        self.label2 = tkinter.Label(self.topframe, text = "Jim")
        self.label3 = tkinter.Label(self.topframe, text = "Jerry")

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottomframe, text = "Jill")
        self.label5 = tkinter.Label(self.bottomframe, text = "Jen")
        self.label6 = tkinter.Label(self.bottomframe, text = "Jessica")

        self.label4.pack()
        self.label5.pack()
        self.label6.pack()

        self.topframe.pack()
        self.bottomframe.pack()
        #create button
        self.mybutton = tkinter.Button(self.main_window, text= "Click Me!", command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.mybutton.pack(side ='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Response", "Thanks for clicking me!")


my_gui = myGUI()

print("I am done")