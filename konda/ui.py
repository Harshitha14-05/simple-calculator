import tkinter as tk
from tkinter import ttk, messagebox
from calculator import Calculator

class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.calculator = Calculator()
        self.setup_ui()
        self.current_input = ""  # Track input separately
        
    def setup_ui(self):
        self.root.title("Modern Calculator")
        self.root.geometry("350x400")
        self.root.resizable(False, False)
        
        # Styling
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=10)
        style.configure('TLabel', font=('Helvetica', 14))
        
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Entry Widgets
        self.entry_var = tk.StringVar()  # Single entry for all input
        
        ttk.Label(main_frame, text="Calculator").pack()
        self.entry = ttk.Entry(main_frame, textvariable=self.entry_var, 
                             font=('Helvetica', 14), justify='right')
        self.entry.pack(fill=tk.X, pady=10)
        
        # Operation Buttons
        operations_frame = ttk.Frame(main_frame)
        operations_frame.pack(pady=10)
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]
        
        for (text, row, col) in buttons:
            btn = ttk.Button(operations_frame, text=text, 
                           command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            operations_frame.grid_columnconfigure(col, weight=1)
    
    def on_button_click(self, button_text):
        if button_text == 'C':
            self.entry_var.set('')
            self.current_input = ""
        elif button_text == '=':
            self.perform_calculation()
        else:
            self.current_input += button_text
            self.entry_var.set(self.current_input)
    
    def perform_calculation(self):
        try:
            # Evaluate the entire expression
            result = eval(self.current_input)
            self.entry_var.set(result)
            self.current_input = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.entry_var.set('')
            self.current_input = ""
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression")
            self.entry_var.set('')
            self.current_input = ""

def run_calculator():
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_calculator()