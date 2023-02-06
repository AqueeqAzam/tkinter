import tkinter as tk   # import tkinter module

x = tk.Tk()   # call the tk method
x.mainloop()     # to use main window open

# Add title
x.title('Welcome to GUI')

# Add geometry
x.geometry('500x400')


# Add label and pack function
# lable = tk.Label(x, text = 'python programming for engineer with Aqueeq')
# lable.pack()   # It uses the options fill , expand and side


# Add grid method but it can not use with label function
# label1 = tk.Label(x, text= 'welcome to python')
# label2 = tk.Label(x, text='python programming')
# label3 = tk.Label(x, text='with Aqueeq')

# label1.grid(row=0, column= 0)
# label2.grid(row=1, column=1)
# label3.grid(row=2, column=2)

x.mainloop()
