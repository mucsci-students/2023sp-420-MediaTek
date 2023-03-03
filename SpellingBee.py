import argparse
import subprocess
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('--cli', action='store_true', help='Run in CLI mode')

args = parser.parse_args()

#get aboslute path for clirefactor and austinguitest.py
clipath = os.path.abspath("MVC/view/CLIrefactor.py")
guipath = os.path.abspath("MVC/view/austinguitest.py")

if args.cli:
    # Run CLI mode
    subprocess.run([sys.executable, clipath])
else:
    # Run GUI mode
    subprocess.run([sys.executable, guipath])
