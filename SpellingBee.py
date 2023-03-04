import argparse
import subprocess
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('--cli', action='store_true', help='Run in CLI mode')
parser.add_argument('--mac', action='store_true', help=' Run the mac version of GUI')

args = parser.parse_args()

#get aboslute path for clirefactor and austinguitest.py
clipath = os.path.abspath("MVC/view/CLIrefactor.py")
guipath = os.path.abspath("MVC/view/austinguitest.py")
macpath = os.path.abspath("MVC/view/noahmac.py")

if args.cli:
    # Run CLI mode
    subprocess.run([sys.executable, clipath])
elif args.mac:
    subprocess.run([sys.executable, macpath])
else:
    # Run GUI mode
    subprocess.run([sys.executable, guipath])
