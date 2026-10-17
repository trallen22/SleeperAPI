import argparse
from pathlib import Path
import subprocess

def get_args():
    parser = argparse.ArgumentParser(description='Runs the containers for the fantasy API')
    # adding each argument to the parser
    parser.add_argument('-c', '--component', required=True, choices=['frontend', 'backend'], help='container to run (frontend/backend)')
    parser.add_argument('-i', '--interactive', action='store_true', help='container to run (frontend/backend)')

    args, unknown = parser.parse_known_args()
    return vars(args)

argDict = get_args()

component = argDict['component'] # which component to build (frontend/backend)
interactive = argDict['interactive']

imageName = f"fantasy-{component}"
HOST_IP = "127.0.0.1"
PORTS = {
    'frontend': '3000',
    'backend':  '5000'
}

if interactive:
    command = [ "docker",
        "run", 
        "--rm", 
        "-it", 
        "--init", 
        "--volume", f"{Path(__file__).resolve().parent}:/app", 
        "--publish", f"{HOST_IP}:{PORTS[component]}:{PORTS[component]}", 
        imageName, "/bin/bash" ]
else:
    command = [ "docker",
        "run", 
        "--rm", 
        "--init", 
        "--volume", f"{Path(__file__).resolve().parent}:/app", 
        "--publish", f"{HOST_IP}:{PORTS[component]}:{PORTS[component]}", 
        imageName ]

try:
    subprocess.run(command, check=True)
except Exception as e:
    print(f"ERROR: {e}")
