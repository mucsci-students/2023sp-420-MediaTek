'''
File is a temporary file that just runs the tempCLI.py
Created to load games from the root directory.
'''
import os
import subprocess
import sys
import argparse

clipath = os.path.abspath("MVC/view/tempCLI.py")

def run_appropriate_file():
    parser = argparse.ArgumentParser(description="Run the appropriate version of the application based on the operating system")
    parser.add_argument('--cli', action='store_true', help='run the command-line version')
    args = parser.parse_args()
    
    if args.cli:
        subprocess.run([sys.executable, clipath])

run_appropriate_file()

