import argparse
import docker

def get_args():
    parser = argparse.ArgumentParser(description='Builds the images used for the fantasy API')
    # adding each argument to the parser
    parser.add_argument('-c', '--component', required=True, choices=['frontend', 'backend'], help='component to build (frontend/backend)')

    args, unknown = parser.parse_known_args()
    return vars(args)

argDict = get_args()

component = argDict['component'] # which component to build (frontend/backend)

client = None
try:
    client = docker.from_env()
except Exception as e:
    print(f"ERROR: {e}")

IMAGE_TAG = f"fantasy-{component}"
if client:
    _, build_logs = client.images.build(path=component, tag=IMAGE_TAG)
    for chunk in build_logs:
        if 'stream' in chunk:
            print(chunk['stream'].strip())
        elif 'error' in chunk:
            print(f"Error: {chunk['error']}")
else:
    print("ERROR: no client found")
