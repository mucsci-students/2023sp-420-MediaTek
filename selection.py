import argparse
import subprocess


# Define the command-line arguments
parser = argparse.ArgumentParser(description='Launch application in GUI or CLI mode')
parser.add_argument('--cli', action='store_true', help='Launch application in CLI mode')

# Parse the arguments
args = parser.parse_args()

# Launch the application in the appropriate mode
if args.cli:
    print('Launching application in CLI mode...')
    # Run your CLI code here
    subprocess.run(["python", "gameapplication.py"])
else:
    print('Launching application in GUI mode...')
    # Run your GUI code here
    subprocess.run(["python", "GUI.py"])
