import platform
import os
import subprocess
import sys
import argparse

clipath = os.path.abspath("MVC/view/CLI.py")
winpath = os.path.abspath("MVC/view/winGUI.py")
macpath = os.path.abspath("MVC/view/macGUI.py")
linuxpath = os.path.abspath("MVC/view/winGUI.py")

def run_appropriate_file():
    parser = argparse.ArgumentParser(description="Run the appropriate version of the application based on the operating system")
    parser.add_argument('--cli', action='store_true', help='run the command-line version')
    args = parser.parse_args()
    
    os_name = platform.system()
    print(f"Detected OS: {os_name}")
    
    if os_name == "Windows":
        if args.cli:
            subprocess.run([sys.executable, clipath])
        else:
            subprocess.run([sys.executable, winpath])
    elif os_name == "Darwin":
        if args.cli:
            subprocess.run([sys.executable, clipath])
        else:
            subprocess.run([sys.executable, macpath])
    elif os_name == "Linux":
        if args.cli:
            subprocess.run([sys.executable, clipath])
        else:
            subprocess.run([sys.executable, linuxpath])
    else:
        print("Unsupported OS")

run_appropriate_file()

