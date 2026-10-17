# use base image
FROM node:24.1-bookworm-slim

# set up working directory 
WORKDIR /app

# copy project files
# COPY requirements.txt .

# install dependencies

# expose the port; mostly for documentation purposes
EXPOSE 3000

# command to run
CMD [ "npm", "start", "--prefix", "/app/frontend" ]