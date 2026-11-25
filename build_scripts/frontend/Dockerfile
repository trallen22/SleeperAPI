# use base image
FROM node:24.22-bookworm-slim

# set up working directory 
WORKDIR /app

# copy project files
# COPY requirements.txt .
COPY ./my-react-app .

# install dependencies

# # expose the port; mostly for documentation purposes
# EXPOSE 3000

# command to run
CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0" ]