import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.current = "0"
        self.display_var = tk.StringVar(value=self.current)
        

        display = tk.Entry(root, textvariable=self.display_var, 
                          font=('Arial', 16), justify='right', state='readonly')
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
        
        # Buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]
        
        for i, row in enumerate(buttons, 1):
            for j, btn_text in enumerate(row):
                if btn_text == 'C':
                    btn = tk.Button(root, text=btn_text, 
                                   command=self.clear, font=('Arial', 12))
                    btn.grid(row=i, column=j, columnspan=4, 
                            padx=5, pady=5, sticky='ew')
                else:
                    btn = tk.Button(root, text=btn_text, 
                                   command=lambda t=btn_text: self.button_click(t),
                                   font=('Arial', 12))
                    btn.grid(row=i, column=j, padx=5, pady=5, sticky='ew')
    
    def button_click(self, char):
        if char == '=':
            try:
                self.current = str(eval(self.current))
            except:
                self.current = "Error"
        else:
            if self.current == "0":
                self.current = char
            else:
                self.current += char
        
        self.display_var.set(self.current)
    
    def clear(self):
        self.current = "0"
        self.display_var.set(self.current)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()