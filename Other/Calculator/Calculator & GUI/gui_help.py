import tkinter

def function(): # Main helpbox function
    root = tkinter.Tk() # Defines window
    frame = tkinter.Frame(root) # Defines frame
    frame.pack()

    Text = tkinter.Text(root,height=8, width = 100) # Defines length of text label.
    Text.pack()
    Text.insert(tkinter.END,"Welcome to Luke Parkin's First calculator. \nPlease use the format: (a & b) & (c & d) \nWhere ABCD are any positive numbers, and & is an operator (+/*-)\nNote that operators do not have to be the same\nfor any abcd you may use n^e where n is abc or d, and e is any positive number.\n\nCurrently only two brackets are supported with BIDMAS, \nHowever more brackets may be used without this.")
    Text.configure(state="disabled") # Disables user editing of the text label.

    root.mainloop() # Loops main.