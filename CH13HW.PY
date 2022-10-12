import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x500')
        self.main_window.title('Pizza')

        self.topframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


        ###
        self.radio_var = tkinter.IntVar()
        self.add = tkinter.Label(self.topframe, text = "Name")
        self.entry = tkinter.Entry(self.topframe, width = 10)
        self.crust = tkinter.Label(self.midframe, text = "CRUST")
        self.rb1 = tkinter.Radiobutton(self.midframe, text = "Regular Crust($0)", variable = self.radio_var, value = 0)
        self.rb2 = tkinter.Radiobutton(self.midframe, text = "Thin Crust(+$1)", variable = self.radio_var, value = 1)
        self.rb3 = tkinter.Radiobutton(self.midframe, text = "Thick Crust(+$2)", variable = self.radio_var, value = 2)

        self.rb1.select()
        self.add.pack(side="left")
        self.entry.pack(side="left")


        self.crust.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.cb1_var = tkinter.IntVar()
        self.cb2_var = tkinter.IntVar()
        self.cb3_var = tkinter.IntVar()
        self.cb4_var = tkinter.IntVar()
        self.cb5_var = tkinter.IntVar()
        self.cb6_var = tkinter.IntVar()

        self.toppings = tkinter.Label(self.midframe, text = "TOPPINGS")
        self.cb1 = tkinter.Checkbutton(self.midframe, text = "Pepperoni(+$0.50)", variable = self.cb1_var)
        self.cb2 = tkinter.Checkbutton(self.midframe, text = "Sausage(+$0.60)", variable = self.cb2_var)
        self.cb3 = tkinter.Checkbutton(self.midframe, text = "Ham(+$0.65)", variable = self.cb3_var)
        self.cb4 = tkinter.Checkbutton(self.midframe, text = "Pineapple(+$0.30)", variable = self.cb4_var)
        self.cb5 = tkinter.Checkbutton(self.midframe, text = "Jalepanos(+$0.25)", variable = self.cb5_var)
        self.cb6 = tkinter.Checkbutton(self.midframe, text = "Peppers(+$0.15)", variable = self.cb6_var)

        self.toppings.pack()
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        

        self.topframe.pack()
        self.midframe.pack()
        self.bottomframe.pack()

        self.mybutton = tkinter.Button(self.main_window, text= "Review Order",foreground = "blue", command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text="Quit Order",foreground = "red", command=self.main_window.destroy)

        self.mybutton.pack(side ='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()

    def do_something(self):
        #tkinter.messagebox.showinfo("Selected Crust: ", "The Crust Choice costs you an additional $" + str(self.radio_var.get()))
        name = self.entry.get()
        message = ("The toppings you have selected are: \n" + "--------------------------------------------- \n")
        topcost = 0

        if self.cb1_var.get() ==1:
            message += "Pepperoni\n"
            topcost += 0.50
        if self.cb2_var.get() ==1:
            message += "Sausage\n"
            topcost += 0.60
        if self.cb3_var.get() ==1:
            message += "Ham\n"
            topcost += 0.65
        if self.cb4_var.get() ==1:
            message += "Pineapple\n"
            topcost += 0.30
        if self.cb5_var.get() ==1:
            message += "Jalepanos\n"
            topcost += 0.25
        if self.cb6_var.get() ==1:
            message += "Peppers\n"
            topcost += 0.15
        
        totcost = 5 + topcost + self.radio_var.get()

        tkinter.messagebox.showinfo("Cost of pizza: ","Order Name: " + name + "\n" + "Pizza Cost: " + "${:,.2f}".format(totcost)+ "\n")

my_gui = MyGUI()

print("I am done")