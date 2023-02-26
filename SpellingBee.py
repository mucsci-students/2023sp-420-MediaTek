import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--cli', action='store_true', help='Run in CLI mode')

args = parser.parse_args()

if args.cli:
    # Run CLI mode
    subprocess.run([sys.executable, 'CLIrefactor.py'])
else:
    # Run GUI mode
    subprocess.run([sys.executable, 'austinguitest.py'])
