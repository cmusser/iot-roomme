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

### Retrieving a Document It's Unique ID

    curl http://127.0.0.1/locations/id/5e84df860db6ec32402fbb6c
