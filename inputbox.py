import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.topframe, text = "Please enter the distance in kilometers")

        self.kilo_entry = tkinter.Entry(self.topframe, width = 10)

        self.topframe.pack()
        self.bottomframe.pack()
        #create button
        self.mybutton = tkinter.Button(self.main_window, text= "Convert", command=self.convert)
        self.quitbutton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.mybutton.pack(side ='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_enrty.get())

        miles = round(kilo*0.6214,2)
        
        tkinter.messagebox.showinfo("Result", str(kilo)+" Kilometers is equal to "+ str(miles) +"miles")


my_gui = myGUI()

print("I am done")