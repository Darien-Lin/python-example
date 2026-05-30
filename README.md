# 🐍 Welcome to Python! (Windows 64-bit Setup Guide)

Guide to setting up your local Python development environment on Windows (64-bit).

Getting your environment configured correctly is the single most important first step in your coding journey. Follow these step-by-step instructions carefully, and you'll be running Python code in no time!

---

## 📁 Repository Structure

```text
python-example/
├── example-app/           # The example Python application
│   ├── calculator.py      # Sleek Tkinter GUI Calculator source code
│   ├── requirements.txt   # Third-party dependency definition for the app
│   └── README.md          # Guide on how to run and understand the calculator
├── .gitignore             # Tells Git which files/folders to ignore (e.g. .venv)
├── LICENSE                # Repository License
└── README.md              # This Windows Python environment setup guide
```

---

## 📥 Step 1: Download and Install Python

First, we need to download Python onto your Windows computer.

1. **Go to the Official Python Downloads page:** 
   👉 [Python Downloads for Windows](https://www.python.org/downloads/windows/)
2. Under the **"Stable Releases"** section, look for the latest **Python 3.12.x** (or the current stable version).
3. Click on the link for **Windows installer (64-bit)** to download the installer executable.
4. **Run the Installer:** Double-click the downloaded `.exe` file.
5. ⚠️ **CRITICAL STEP (Do not skip!):** Before clicking "Install Now", make sure to check the box at the bottom that says **"Add python.exe to PATH"**. 
   > [!IMPORTANT]
   > If you do not check "Add python.exe to PATH", your command prompt won't recognize the `python` command, and you will have to reinstall Python!
6. Click **Install Now** and follow the prompt instructions.
7. (Optional but recommended) At the end of the installation, if it asks to **"Disable path length limit"**, click that option to prevent potential Windows path resolution issues.

---

## 🔍 Step 2: Verify Your Installation

Let's make sure Python was installed and configured correctly.

1. Open **Command Prompt** (press the `Win` key, type `cmd`, and press `Enter`).
2. Run the following command:
   ```cmd
   python --version
   ```
   *You should see output like: `Python 3.12.x`.*
3. Verify that `pip` (Python's package installer) is also available:
   ```cmd
   pip --version
   ```
   *You should see output showing the pip version and directory path.*

---

## 🛠️ Step 3: Setting Up a Virtual Environment (`venv`)

A **Virtual Environment** is like having a clean, isolated desk for each of your projects. It ensures that the external libraries we install for one project do not conflict with other projects on your computer.

### 1. Open your terminal in the project directory
Open **Command Prompt**, **PowerShell**, or **Git Bash**, and navigate to this project's folder:
```cmd
cd C:\path\to\your\python-example
```

### 2. Create the Virtual Environment
Run the following command to create a virtual environment named `.venv` in your project folder:
```cmd
python -m venv .venv
```
*(Wait a few seconds for Python to generate the folder structure).*

### 3. Activate the Virtual Environment
Depending on the shell you are using, run the corresponding command to activate the environment:

#### 💻 Option A: Command Prompt (CMD)
```cmd
.venv\Scripts\activate.bat
```

#### ⚡ Option B: Windows PowerShell
If you get a script execution error in PowerShell, run this bypass command first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Then, activate the environment:
```powershell
.venv\Scripts\Activate.ps1
```

#### 🐙 Option C: Git Bash (or VS Code Terminal configured with Bash/Git Bash)
```bash
source .venv/Scripts/activate
```

🎉 **How do you know it worked?**
Once activated, you will see `(.venv)` displayed at the very beginning of your command line prompt, like this:
```cmd
(.venv) C:\path\to\your\python-example>
```

---

## 📦 Step 4: Upgrade Pip and Install Dependencies

Once your virtual environment is active, update the package manager and install any required packages.

1. **Upgrade `pip`** to the latest version within your environment:
   ```cmd
   python -m pip install --upgrade pip
   ```
2. **Install the dependencies** from the `example-app/requirements.txt` file (this will install the `colorama` library needed for our example application):
   ```cmd
   pip install -r example-app/requirements.txt
   ```

---

## 🚪 Step 5: Deactivating the Environment

When you are done working on your project and want to return to your normal system command line, simply run:
```cmd
deactivate
```
This will turn off the virtual environment, and the `(.venv)` prefix will disappear from your prompt.

---

## 🎛️ Step 6: Setting Up VS Code as Your IDE

Visual Studio Code (VS Code) is a lightweight and powerful editor that is perfect for Python. Follow these steps to set it up:

1. **Download and Install VS Code:**
   👉 [Download Visual Studio Code](https://code.visualstudio.com/)
2. **Open Your Project Folder:**
   - Launch VS Code.
   - Click **File > Open Folder...** and select your `python-example` folder.
3. **Configure the Python Interpreter:**
   - Press `Ctrl + Shift + P` (or `F1`) to open the **Command Palette**.
   - Type `Python: Select Interpreter` and select it.
   - Choose the interpreter that points to your virtual environment (it will show `./.venv/Scripts/python.exe` or have a star next to it as recommended).
   - This tells VS Code to use the packages installed inside your virtual environment.

---

## 🔌 Essential VS Code Extensions for Python Beginners

To install these extensions, click on the **Extensions** icon on the left sidebar of VS Code (or press `Ctrl + Shift + X`), search for the extension names, and click **Install**.

1. **Python** (by Microsoft)
   - *Why you need it:* This is the official extension that adds rich support for Python, including code completion (IntelliSense), syntax highlighting, linting, debugging, and code navigation.
2. **Pylance** (by Microsoft)
   - *Why you need it:* Installed automatically with the Python extension, Pylance provides exceptionally fast, type-safe auto-completion and static analysis.
3. **Python Debugger** (by Microsoft)
   - *Why you need it:* Adds debugging capability to step through your code line by line, watch variables, and find bugs easily.
4. **Black Formatter** (by Microsoft)
   - *Why you need it:* Automatically formats your Python code to match the official PEP 8 style guide every time you save, ensuring clean and consistent code.
     > [!TIP]
     > Go to VS Code settings (`Ctrl + ,`), search for `Format On Save`, and check the box to automatically format your files when you save!
5. **Error Lens** (by Alexander)
   - *Why you need it:* Instead of just underlining errors in red, Error Lens displays the error message directly on the line of code itself. This is extremely helpful for beginners to catch syntax errors instantly.
6. **Path Intellisense** (by Christian Kohler)
   - *Why you need it:* Autocompletes filenames and file paths as you type them in your code, which prevents typos when reading files or importing modules.

---

## 📂 Step 7: Explore the Example Application

To help you get your feet wet, we have set up a complete example project in the [example-app](./example-app) directory! 

This contains a simple, sleek GUI Calculator application written in Python. It has its own dedicated documentation to walk you through running the app and understanding how the code works.

👉 **Go to [example-app/README.md](./example-app/README.md) to get started with the calculator!**

---

## 💡 General Tips & Troubleshooting

* **VS Code Integration:** Always make sure your VS Code interpreter points to your virtual environment (as detailed in Step 6) to avoid false-positive error highlights.
* **PATH issues:** If typing `python` opens the Microsoft Store, it means either Python is not installed, or you forgot to check the **"Add python.exe to PATH"** box during installation. Run the installer again, choose **Modify**, and ensure PATH is checked.
* **Keep it clean:** Always activate your virtual environment *before* running or installing packages using `pip install`. Never install packages globally!
* **Git Version Control:** Never commit your `.venv` directory to Git! We have included a `.gitignore` file in this repository to prevent Git from tracking the virtual environment files, as they are machine-specific and can be very large.


