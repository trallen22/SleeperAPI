# use base image
FROM python:3.15-slim

# set up working directory 
WORKDIR /backend

# copy project files
COPY backend/app backend/requirements.txt ./app/

# install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# # expose the port; mostly for documentation purposes
# EXPOSE 5000

# # command to run
# CMD [ "python", "/app/src/backend_server.py" ]
# CMD [ "bin/sh", "-c", ]
CMD [ "uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--reload", "--port", "8000" ]
