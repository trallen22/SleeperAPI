# SleeperAPI
This is for connecting with the sleeper API

# sqlite database
`brew install sqlite`

# Running Docker compose

NOTE: run from root of project

## full stack commands
start:
`docker compose -f compose.yaml up`

stop:
`docker compose -f compose.yaml down`

## individual component commands
start container:
`docker compose up -d <service>`

run container interactively:
`docker run -it --rm --init --volume <src>:<dest> <container name>`
