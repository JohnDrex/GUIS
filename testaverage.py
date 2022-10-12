import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('300x150')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.secframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.fourframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.prompt_label1 = tkinter.Label(self.topframe, text = "Enter the score for test 1:")
        self.prompt_label2 = tkinter.Label(self.secframe, text = "Enter the score for test 2:")
        self.prompt_label3 = tkinter.Label(self.midframe, text = "Enter the score for test 3:")

        self.entry1 = tkinter.Entry(self.topframe, width = 10)
        self.entry2 = tkinter.Entry(self.secframe, width = 10)
        self.entry3 = tkinter.Entry(self.midframe, width = 10)


        self.prompt_label1.pack(side = 'left')
        self.prompt_label2.pack(side = 'left')
        self.prompt_label3.pack(side = 'left')
        self.entry1.pack(side='left')
        self.entry2.pack(side='left')
        self.entry3.pack(side='left')

        self.avg_var = tkinter.StringVar()

        self.desc_label = tkinter.Label(self.fourframe, text="Average: ")
        self.avg = tkinter.Label(self.fourframe, textvariable=self.avg_var)

        self.desc_label.pack(side='left')
        self.avg.pack(side='left')

        self.topframe.pack(side = 'top')
        self.secframe.pack(side = 'top')
        self.midframe.pack(side = 'top')
        self.fourframe.pack()
        self.bottomframe.pack(side = 'top')
        #create button
        self.avg_button = tkinter.Button(self.main_window, text= "Average", command=self.convert)
        self.quitbutton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.avg_button.pack(side = 'left')
        self.quitbutton.pack(side = 'right')


        tkinter.mainloop()

    def convert(self):
        score1 = float(self.entry1.get())
        score2 = float(self.entry2.get())
        score3 = float(self.entry3.get())

        average = round(((score1+score2+score3)/3),2)

        self.avg_var.set(average)
        
        #tkinter.messagebox.showinfo("Result", str(kilo)+" Kilometers is equal to "+ str(miles) +"miles")


my_gui = myGUI()

print("I am done")