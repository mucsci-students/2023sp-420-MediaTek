import platform
import os
import subprocess
import sys
import argparse

clipath = os.path.abspath("MVC/view/CLI.py")
guipath = os.path.abspath("MVC/view/GUI.py")

def run_appropriate_file():
    parser = argparse.ArgumentParser(description="Run the appropriate version of the application based on the operating system")
    parser.add_argument('--cli', action='store_true', help='run the command-line version')
    args = parser.parse_args()
    
    os_name = platform.system()
    
    if os_name == "Windows":
        if args.cli:
            subprocess.run([sys.executable, clipath])
        else:
            subprocess.run([sys.executable, guipath])
    elif os_name == "Darwin":
        if args.cli:
            subprocess.run([sys.executable, clipath])
        else:
            subprocess.run([sys.executable, guipath])
    else:
        if args.cli:
            subprocess.run([sys.executable, clipath])
        else:
            subprocess.run([sys.executable, guipath])

run_appropriate_file()

