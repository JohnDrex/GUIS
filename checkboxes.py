import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.cb1_var = tkinter.IntVar()
        self.cb2_var = tkinter.IntVar()
        self.cb3_var = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.topframe, text = "Option 1", variable = self.cb1_var)
        self.cb2 = tkinter.Checkbutton(self.topframe, text = "Option 2", variable = self.cb2_var)
        self.cb3 = tkinter.Checkbutton(self.topframe, text = "Option 3", variable = self.cb3_var)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.topframe.pack()
        self.bottomframe.pack()
        #create button
        self.mybutton = tkinter.Button(self.main_window, text= "Click Me!", command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.mybutton.pack(side ='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()

    def do_something(self):
        message = "You have selected: \n"

        if self.cb1_var.get() ==1:
            message += "Option 1\n"
        if self.cb2_var.get() ==1:
            message += "Option 2\n"
        if self.cb3_var.get() ==1:
            message += "Option 3\n"

        tkinter.messagebox.showinfo("Response", message)


my_gui = myGUI()

print("I am done")