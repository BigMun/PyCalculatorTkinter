import tkinter as tk

window = tk.Tk()

# Tkinter GUI window
window.title("Calculator")
window.geometry("390x324")
window.resizable(0, 0)

expression = ""

#Function for most buttons
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#Function for "C"
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

#Function for "="
def btn_equal():
    global expression

    result = str(eval(expression)) 
   
    input_text.set(result)
    expression = ""

#Function to X^2
def btn_poweroftwo():
    global expression
    expression = int(expression)
    result = expression * expression
    input_text.set(result)

#Function to X^3
def btn_powerofthree():
    global expression
    expression = int(expression)
    result = expression * expression * expression
    input_text.set(result)


input_text = tk.StringVar()

input_frame = tk.Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = tk.TOP)

input_field = tk.Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = tk.RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) 

#Button layout
btns_frame = tk.Frame(window, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

#Buttons

# First row "c" "/"
tk.Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#ff0000", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
tk.Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#00FFF3", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# Second row "7" "8" "9" "*"
tk.Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
tk.Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
tk.Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
tk.Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#E400FF", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

# Third row "4" "5" "6" "-"
tk.Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
tk.Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
tk.Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
tk.Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#FBFF00", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# Fourth row "1" "2" "3" "+"
tk.Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
tk.Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
tk.Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
tk.Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#FF8300", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# Fifth row "0" "." "="
tk.Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
tk.Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#7C00FF", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
tk.Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#36D11D", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

# Scientific modes "x^2" "x^3"
tk.Button(btns_frame, text = "X^2", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_poweroftwo()).grid(row = 0, column = 4, padx = 1, pady = 1)
tk.Button(btns_frame, text = "X^3", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_powerofthree()).grid(row = 1, column = 4, padx = 1, pady = 1)
tk.Button(btns_frame, text = "X^y", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click("**")).grid(row = 2, column = 4, padx =1, pady = 1)
tk.Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click("(")).grid(row = 3, column = 4, padx =1, pady = 1)
tk.Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#5C5C5C", cursor = "hand2", command = lambda: btn_click(")")).grid(row = 4, column = 4, padx =1, pady = 1)


window.mainloop()