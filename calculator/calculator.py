import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("380x580")
        self.root.resizable(False, False)
        self.root.config(bg="#1a1a2e")
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.create_display()
        self.create_buttons()
    
    def create_display(self):
       
        display_frame = tk.Frame(self.root, bg="#1a1a2e", height=150)
        display_frame.pack(fill="both", padx=20, pady=20)
        
        
        display = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=("Segoe UI", 28, "bold"),
            bg="#0f3460",
            fg="#ffffff",
            bd=0,
            justify="right",
            state="readonly",
            readonlybackground="#0f3460"
        )
        display.pack(fill="both", expand=True, ipady=20, ipadx=10)
    
    def create_buttons(self):
        
        button_frame = tk.Frame(self.root, bg="#1a1a2e")
        button_frame.pack(padx=20, pady=(0, 20))
        
        
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                
                if button_text == '=':
                    bg = "#667eea"
                    fg = "#ffffff"
                    colspan = 2
                elif button_text == 'C':
                    bg = "#f44336"
                    fg = "#ffffff"
                    colspan = 1
                elif button_text in ['/', '*', '-', '+', '(', ')']:
                    bg = "#e65100"
                    fg = "#ffffff"
                    colspan = 1
                else:
                    bg = "#2d2d44"
                    fg = "#ffffff"
                    colspan = 1
                
                btn = tk.Button(
                    button_frame,
                    text=button_text,
                    font=("Segoe UI", 18, "bold"),
                    bg=bg,
                    fg=fg,
                    activebackground=bg,
                    activeforeground="#ffffff",
                    bd=0,
                    cursor="hand2",
                    command=lambda x=button_text: self.on_button_click(x)
                )
                
                if button_text == '=':
                    btn.grid(row=i, column=j, columnspan=colspan, sticky="nsew", padx=3, pady=3, ipadx=10, ipady=20)
                elif button_text == '0':
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=3, pady=3, ipadx=10, ipady=20)
                else:
                    btn.grid(row=i, column=j, columnspan=colspan, sticky="nsew", padx=3, pady=3, ipadx=10, ipady=20)
                
                
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#5a6fd8" if b['text'] == '=' else "#d32f2f" if b['text'] == 'C' else "#ff6f00" if b['text'] in ['/', '*', '-', '+', '(', ')'] else "#3d3d5c"))
                btn.bind("<Leave>", lambda e, b=btn, c=bg: b.config(bg=c))
        
       
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, button_text):
        if button_text == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button_text == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                messagebox.showerror("Error", "Invalid expression!")
                self.expression = ""
                self.input_text.set("")
        else:
            self.expression += str(button_text)
            self.input_text.set(self.expression)


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()