# use base image
FROM node:24.22-bookworm-slim

# set up working directory 
WORKDIR /app

# install dependencies
# COPY ./frontend .
COPY ./frontend/package*.json ./
RUN npm ci

# copy project files
COPY ./frontend ./

# # expose the port; mostly for documentation purposes
# EXPOSE 3000

# command to run
CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0" ]