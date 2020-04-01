# iot-roomme

A simple server to store arbitrary JSON documents

## Requirements

- Linux or macOS
- Docker Compose

## Build

    sudo docker build -t iot-roomme . 

## Run

Note that some distributions may not need the commands run under `sudo`.

Before running the first time:

    mkdir db
    
To start:

    sudo docker-compose up
   
## Use

There are three endpoints: `/`, `/locations`, `/locations/id/<id>`

### Adding a Document

    echo '{"name": "fred", "status": "chill"}' | curl -X POST -H "Content-Type: application/json" --data-binary @- http://127.0.0.1/locations
    
Each document will have a unique ID, which will be returned in responses.

### Retrieving all Documents

    curl -s http://127.0.0.1/locations | jq 

As shown, you can use the `jq` utility to pretty-print or filter the response.

### Retrieving a Document By ID

    curl http://127.0.0.1/locations/id/5e84df860db6ec32402fbb6c
    
## Other Info

### Architecture:

This is a two-container application managed with Docker Compose. The application,
running in one container is a Python application written using the Flask framework.
The application uses Nginx as the web frontend. The data store, running in the other
container, is MongoDB.

### Data

The MongoDB container is configured (in `docker-compose.yml`) to mount a directory
named `db` in the current working directory of the host as its data storage area.
This means the data will persist across runs of the container set and is easily
accessible. You can tar up this directory and move it to different machines if you
need to change servers or want to use the data offline.

### Security

Right now it is not secure: the transport is unencrypted and there is no authentication.
It may be possible to use Let's Encrypt to use HTTPS however, and a simple API key based
auth could be added to the app.

### Helpful Docker Compose Commands

#### To start the containers in the background:

    sudo docker-compose up -d
    
To keep it in the foreground, for debugging, etc., leave the `-d` off.

#### To see what's running:

    sudo docker-compose ps
    
#### To get a shell inside the MongoDB container:

    sudo docker-compose exec db bash

You can run the `mongo` client to access the database via the MongoDB shell.
 
#### To get a shell inside the application container:
 
    sudo docker-compose exec app bash
 
You can tinker with the application script, or write new Python programs. 

