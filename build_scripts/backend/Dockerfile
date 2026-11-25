# use base image
FROM python:3.15-slim

# set up working directory 
WORKDIR /backend

# copy project files
COPY src build_scripts/backend/requirements.txt ./src/

# install dependencies
RUN pip install --no-cache-dir -r src/requirements.txt

# # expose the port; mostly for documentation purposes
# EXPOSE 5000

# # command to run
# CMD [ "python", "/app/src/backend_server.py" ]
# CMD [ "bin/sh", "-c", ]
CMD [ "uvicorn", "src.backend_server:app", "--host", "0.0.0.0", "--reload", "--port", "8000" ]
