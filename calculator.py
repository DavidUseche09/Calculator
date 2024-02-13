from tkinter import *
import sys

#Window Config
window = Tk()
window.title("Calculator")

i = 0

#Entry
eText = Entry(window, font=("Calibri 20"))
eText.grid(row= 0, column= 0, columnspan= 4, padx= 50, pady= 5)

#Functions
def clickButton(value):
    global i 
    eText.insert(i, value)
    i += 1

def delete():
    eText.delete(0, END)
    i = 0

def doMath():
    operation = eText.get()
    result = eval(operation)
    eText.delete(0, END)
    eText.insert(0, result)
    i = 0

def exitProgram():
    window.quit()
    window.destroy()
    sys.exit()
    
def menuTest():
    mainManu = Menu(window)
    submenu = Menu(mainManu, tearoff=0)
    submenu.add_command(label='New File')
    submenu.add_separator()
    submenu.add_command(label='Exit', command=exitProgram)
    mainManu.add_cascade(menu=submenu, label='Menu')
    subMenuHelp = Menu(mainManu, tearoff=0)
    subMenuHelp.add_command(label='Fuck you')
    mainManu.add_cascade(menu=subMenuHelp, label='Help')
    window.config(menu=mainManu)

#Number Buttons
button1 = Button(window, text= "1", width= 5, height= 2, command= lambda: clickButton(1))
button2 = Button(window, text= "2", width= 5, height= 2, command= lambda: clickButton(2))
button3 = Button(window, text= "3", width= 5, height= 2, command= lambda: clickButton(3))
button4 = Button(window, text= "4", width= 5, height= 2, command= lambda: clickButton(4))
button5 = Button(window, text= "5", width= 5, height= 2, command= lambda: clickButton(5))
button6 = Button(window, text= "6", width= 5, height= 2, command= lambda: clickButton(6))
button7 = Button(window, text= "7", width= 5, height= 2, command= lambda: clickButton(7))
button8 = Button(window, text= "8", width= 5, height= 2, command= lambda: clickButton(8))
button9 = Button(window, text= "9", width= 5, height= 2, command= lambda: clickButton(9))
button0 = Button(window, text= "0", width= 10, height= 2, command= lambda: clickButton(0))

#Other Buttons
deleteButton = Button(window, text= "Undo", width= 5, height= 2, command= lambda: delete())
bracketButton1 = Button(window, text= "(", width= 5, height= 2, command= lambda: clickButton("("))
bracketButton2 = Button(window, text= ")", width= 5, height= 2, command= lambda: clickButton(")"))
dotButton = Button(window, text= ".", width= 5, height= 2, command= lambda: clickButton("."))

#Operation Buttons
sumButton = Button(window, text= "+", width= 5, height= 2, command= lambda: clickButton("+"))
minusButton = Button(window, text= "-", width= 5, height= 2, command= lambda: clickButton("-"))
timesButton = Button(window, text= "*", width= 5, height= 2, command= lambda: clickButton("*"))
divButton = Button(window, text= "/", width= 5, height= 2, command= lambda: clickButton("/"))
equalsButton = Button(window, text= "=", width= 5, height= 2, command= lambda: doMath())

#Adding buttons with positions
deleteButton.grid(row=1, column=0, padx=5, pady=5)
bracketButton1.grid(row=1, column=1, padx=5, pady=5) 
bracketButton2.grid(row=1, column=2, padx=5, pady=5)
divButton.grid(row=1, column=3, padx=5, pady=5)

button7.grid(row= 2, column= 0, padx=5, pady=5)
button8.grid(row= 2, column= 1, padx=5, pady=5)
button9.grid(row= 2, column= 2, padx=5, pady=5)
timesButton.grid(row= 2, column= 3, padx=5, pady=5)

button4.grid(row= 3, column= 0, padx=5, pady=5)
button5.grid(row= 3, column= 1, padx=5, pady=5)
button6.grid(row= 3, column= 2, padx=5, pady=5)
sumButton.grid(row= 3, column= 3, padx=5, pady=5)

button1.grid(row= 4, column= 0, padx=5, pady=5)
button2.grid(row= 4, column= 1, padx=5, pady=5)
button3.grid(row= 4, column= 2, padx=5, pady=5)
minusButton.grid(row= 4, column= 3, padx=5, pady=5)

button0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
dotButton.grid(row=5, column=2, padx=5, pady=5)
equalsButton.grid(row=5, column=3, padx=5, pady=5)


menuTest()

window.mainloop()