import tkinter
import gui_help
import parsingengine


global result
result = ' '

def calculate(): # Function to run the calculations
    global entry1
    global result
    string = entry1.get()
    result = (parsingengine.parsingengine(string)) # Sends calculation to parsing engine
    Text.configure(state="normal") # Allows editing of the text variable
    Text.delete(1.0,tkinter.END) # Deletes current element in output text
    Text.insert(1.0,result) # Sets output text to the value of result
    Text.configure(state="disabled") #Disables editing of text variable

def helpmenu():
    gui_help.function() # Runs the help window

def savetoclipboard(): # Saves the output of the calculation to the clipboard 
    if result != ' ': #Checks that there is actually a calculation to copy [to prevent accidental clipboard loss]   
        r = tkinter.Tk()
        r.withdraw()
        r.clipboard_clear() #Clears active clearboard
        r.clipboard_append(result) #Updates clipboard
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()
    else:
        pass


#----------- Initial setup
root = tkinter.Tk() #Creates tkinter window
frame = tkinter.Frame(root)
frame.pack()


#----------- Element creation

#-- Entry element
entry1 = tkinter.Entry(root, bd = 5)
entry1.pack(side=tkinter.TOP)
entry1.focus_set()

#-- Calculate Button element
button = tkinter.Button(frame,text="CALCULATE",fg="blue",command= calculate)
button.pack(side=tkinter.LEFT)

#-- Help Button element
button = tkinter.Button(frame,text="HELP",fg="red",command=helpmenu)
button.pack(side=tkinter.BOTTOM)

#-- Clipboard Button element
button = tkinter.Button(frame,text="COPY",fg="green",command= lambda: savetoclipboard())
button.pack(side=tkinter.BOTTOM)

#-- Output text element
Text = tkinter.Text(root,height=1, width = 30)
Text.pack()
Text.configure(state="disabled")



root.mainloop() #-- Loops the window.