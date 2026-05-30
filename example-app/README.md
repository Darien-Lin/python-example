# 🧮 Example Application: Python GUI Calculator

Welcome to the example application! This is a simple, modern dark-themed calculator built using Python's standard GUI library, **Tkinter**.

To demonstrate how to manage external Python libraries, this app requires an external package called **`colorama`** to output colorful status logs to your terminal. This library is defined in the `example-app/requirements.txt` file.

---

## 📦 Setting Up Dependencies & Running the Calculator

If you attempt to run the calculator before installing dependencies, Python will show an error:
`ModuleNotFoundError: No module named 'colorama'`. 

Follow these steps to set up your virtual environment and run the application:

### 1. Activate Your Virtual Environment
Make sure your terminal is inside the root directory (`python-example`) and activate your virtual environment (you should see `(.venv)` in your prompt):
- **Command Prompt (CMD):** `.venv\Scripts\activate.bat`
- **PowerShell:** `.venv\Scripts\Activate.ps1`
- **Git Bash:** `source .venv/Scripts/activate`

### 2. Install the Dependencies
With your virtual environment active, run the following command from the root folder to install the required libraries:
```cmd
pip install -r example-app/requirements.txt
```
*(Alternatively, if your terminal is already inside the `example-app` directory, run: `pip install -r requirements.txt`)*

*This downloads and installs `colorama` inside your isolated `.venv` environment.*

### 3. Run the Calculator
Now that your dependencies are successfully installed, run the application from the root directory:
```cmd
python example-app/calculator.py
```
*(Alternatively, you can `cd example-app` and run `python calculator.py`).*

A GUI window will pop up, and you'll see colorized status logs print in your terminal window whenever you click buttons or compute math problems!

---

## 🎓 How it Works (Under the Hood)

Here is a breakdown of the key concepts used:

### 1. Colorama (External Package)
We import and initialize `colorama` at the top of the file to enable cross-platform ANSI colors in the Windows terminal:
```python
from colorama import init, Fore, Style
init(autoreset=True)
```
Whenever an event occurs (like clicking a button), we use `colorama` styles to print colorized logs:
- `Fore.YELLOW` for click actions
- `Fore.GREEN` for successful calculations
- `Fore.RED` for mathematical errors

### 2. Tkinter Library
Tkinter is the standard Python interface to the Tk GUI toolkit. We use it to create the graphical interface:
```python
import tkinter as tk
from tkinter import messagebox
```

### 2. Grid Layout Manager
We arrange the display screen and the grid of buttons using Tkinter's `.grid()` geometry manager.
- Columns and rows are given a "weight" so they expand and resize dynamically:
  ```python
  self.buttons_frame.rowconfigure(i, weight=1, minsize=60)
  self.buttons_frame.columnconfigure(i, weight=1, minsize=60)
  ```
- Each button is placed at a specific grid coordinate `(row, col)` with `sticky="nsew"` to fill the entire cell grid.

### 3. Event Handling and Calculation
When a button is clicked, it calls `on_button_click(text)`.
- **String calculation:** We append number and operator characters to a string called `self.expression`.
- **Safe Evaluation:** When the `=` button is clicked, Python's built-in `eval()` function evaluates the mathematical expression.
- **Error Boundaries:** We wrap the evaluation in a `try/except` block to catch bad math operations (like dividing by zero or entering consecutive operators) without crashing the program:
  ```python
  try:
      result = str(eval(self.expression))
      self.display_var.set(result)
  except ZeroDivisionError:
      messagebox.showerror("Error", "Cannot divide by zero")
  except Exception:
      messagebox.showerror("Error", "Invalid Expression")
  ```

---

## 🛠️ Suggested Exercises & Next Steps

If you want to practice your Python and GUI skills, try adding these features:
1. **Keyboard Bindings:** Make it so pressing keys on your physical keyboard (like `+`, `-`, or the numbers) triggers the calculator.
2. **Additional Operations:** Add buttons for square root (`√`) or exponentiation (`^`).
3. **Color Themes:** Create a button that switches the calculator between Dark Mode and Light Mode.
