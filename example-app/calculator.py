import tkinter as tk
from tkinter import messagebox
from colorama import init, Fore, Style

# Initialize colorama for cross-platform terminal colors
init(autoreset=True)

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.expression = ""

        # Display screen
        self.display_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Label for calculation history
        self.history_label = tk.Label(
            self.display_frame,
            text="",
            anchor="e",
            bg="#1e1e1e",
            fg="#888888",
            font=("Arial", 12),
            padx=10
        )
        self.history_label.pack(fill="both")

        # Main display text
        self.display_var = tk.StringVar(value="0")
        self.display_label = tk.Label(
            self.display_frame,
            textvariable=self.display_var,
            anchor="e",
            bg="#2d2d2d",
            fg="#ffffff",
            font=("Arial", 28, "bold"),
            padx=15,
            pady=15,
            bd=0,
            relief="flat"
        )
        self.display_label.pack(fill="both", expand=True)

        # Button layout
        self.buttons_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Define buttons configuration
        button_layout = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]

        # Style configurations
        self.style_config = {
            'font': ("Arial", 14, "bold"),
            'bd': 0,
            'relief': "flat",
            'activeforeground': "#ffffff"
        }

        # Configure grid row/column weights
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1, minsize=60)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1, minsize=60)

        # Create buttons
        for row_idx, row in enumerate(button_layout):
            for col_idx, val in enumerate(row):
                self.create_button(val, row_idx, col_idx)

        print(Fore.CYAN + Style.BRIGHT + "\n=== Python Calculator Started ===")
        print(Fore.CYAN + "Try clicking buttons in the GUI and watching the logs here!\n")

    def create_button(self, text, row, col):
        if text == '=':
            bg_color = "#007acc"
            fg_color = "#ffffff"
            active_bg = "#0098ff"
        elif text in ['/', '*', '-', '+']:
            bg_color = "#ff9500"
            fg_color = "#ffffff"
            active_bg = "#ffb040"
        elif text in ['C', '⌫', '%', '+/-']:
            bg_color = "#555555"
            fg_color = "#ffffff"
            active_bg = "#777777"
        else:
            bg_color = "#333333"
            fg_color = "#ffffff"
            active_bg = "#444444"

        btn = tk.Button(
            self.buttons_frame,
            text=text,
            bg=bg_color,
            fg=fg_color,
            activebackground=active_bg,
            command=lambda: self.on_button_click(text),
            **self.style_config
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    def on_button_click(self, char):
        print(Fore.YELLOW + f"[CLICK] Button: '{char}'")

        if char == 'C':
            self.expression = ""
            self.history_label.config(text="")
            self.display_var.set("0")
            print(Fore.WHITE + "[CLEAR] Reset display")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
            print(Fore.WHITE + f"[BACKSPACE] Expression is now: '{self.expression}'")
        elif char == '=':
            if self.expression:
                try:
                    expression_to_eval = self.expression.replace('%', '/100')
                    result = str(eval(expression_to_eval))
                    
                    if '.' in result and len(result.split('.')[1]) > 6:
                        result = f"{float(result):.6f}".rstrip('0').rstrip('.')
                        
                    self.history_label.config(text=self.expression + " =")
                    self.display_var.set(result)
                    
                    # Print success log in Green
                    print(Fore.GREEN + Style.BRIGHT + f"[SUCCESS] Evaluated: {self.expression} = {result}")
                    self.expression = result
                except ZeroDivisionError:
                    print(Fore.RED + Style.BRIGHT + "[ERROR] Attempted to divide by zero!")
                    messagebox.showerror("Error", "Cannot divide by zero")
                    self.clear_all()
                except Exception as e:
                    print(Fore.RED + Style.BRIGHT + f"[ERROR] Invalid expression: '{self.expression}'")
                    messagebox.showerror("Error", "Invalid Expression")
                    self.clear_all()
        elif char == '+/-':
            if self.expression:
                if self.expression.startswith('-'):
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
                self.display_var.set(self.expression)
        else:
            if char in ['/', '*', '-', '+', '.'] and self.expression and self.expression[-1] in ['/', '*', '-', '+', '.']:
                self.expression = self.expression[:-1] + char
            elif self.display_var.get() == "0" and char not in ['.', '/', '*', '-', '+']:
                self.expression = char
            else:
                self.expression += char
            self.display_var.set(self.expression)

    def clear_all(self):
        self.expression = ""
        self.display_var.set("0")
        self.history_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
