import tkinter as tk


root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("320x450")
root.config(bg="#2c3e50")  


expression = ""


def press(key):
    global expression
    expression += str(key)
    equation.set(expression)


def equal_press(event=None):  
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result  
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=('Arial', 24), bd=10, bg="#ecf0f1", justify='right')
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)
entry.focus_set()


def key_handler(event):
    key = event.char
    if key in "0123456789+-*/.()":
        press(key)
    elif event.keysym == 'Return':
        equal_press()
    elif event.keysym == 'BackSpace':
        backspace()

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

root.bind("<Key>", key_handler)6
root.bind("<Return>", equal_press)
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack()


buttons = [
    ('7', '#2980b9'), ('8', '#2980b9'), ('9', '#2980b9'), ('/', '#f39c12'),
    ('4', '#2980b9'), ('5', '#2980b9'), ('6', '#2980b9'), ('*', '#f39c12'),
    ('1', '#2980b9'), ('2', '#2980b9'), ('3', '#2980b9'), ('-', '#f39c12'),
    ('0', '#2980b9'), ('.', '#2980b9'), ('+', '#f39c12'), ('=', '#27ae60'),
    ('C', '#c0392b')
]


row = 0
col = 0
for (text, color) in buttons:
    if text == '=':
        btn = tk.Button(btn_frame, text=text, width=10, height=3, bg=color, fg="white", font=("Arial", 14),
                        command=equal_press)
        btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
        col += 2
    elif text == 'C':
        btn = tk.Button(btn_frame, text=text, width=44, height=2, bg=color, fg="white", font=("Arial", 14),
                        command=clear)
        btn.grid(row=row + 1, column=0, columnspan=4, padx=5, pady=10)
    else:
        btn = tk.Button(btn_frame, text=text, width=10, height=3, bg=color, fg="white", font=("Arial", 14),
                        command=lambda t=text: press(t))
        btn.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

root.mainloop()
