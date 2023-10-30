import os
import tkinter as tk
from tkinter import filedialog
import subprocess

# تابع برای انتخاب فایل با پسوند .py
#Function for selecting a file with the .py extension
def select_python_file():
    root = tk.Tk()
    root.withdraw()  # مخفی کردن پنجره اصلی
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    return file_path

# انتخاب فایل با پسوند .py
#Selecting a .py file
selected_file = select_python_file()

if selected_file:
    # نام فایل انتخاب شده
    #The name of the selected file
    file_name = os.path.basename(selected_file)

    # پرسش کاربر برای تبدیل به فایل نصبی
    #User prompt for conversion to an installer file
    convert_choice = input(f"Do you want to convert '{file_name}' to an executable file? (yes/no): ").strip().lower()

    if convert_choice == "yes":
        # دستور تبدیل با PyInstaller
        #Conversion command with PyInstaller
        cmd = f"pyinstaller --onefile {selected_file}"
        subprocess.run(cmd, shell=True)

        print(f"'{file_name}' has been converted to an executable.")
    else:
        print("Conversion aborted.")
else:
    print("No .py file selected.")
