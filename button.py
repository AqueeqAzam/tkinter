from tkinter import *
root = Tk()
root.title('first gui code')
root.geometry('500x300')

# Label method
l = Label(root, text='Hay student')
l.pack()

# Button method
b = Button(root, text='Click me')
b.pack()

# Button features
b1 = Button(root, text= 'Fenish me', width= 25, command=root.destroy)
b1.pack()
root.mainloop()


