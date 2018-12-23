[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b9ed3c8e272546ceae2f8a98d13ee0f3)](https://www.codacy.com/app/maestro/analytics-maestro?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=maestro-server/analytics-maestro&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/maestro-server/analytics-maestro.svg?branch=master)](https://travis-ci.org/maestro-server/analytics-maestro)
[![Maintainability](https://api.codeclimate.com/v1/badges/c2272dfe465bdaea4900/maintainability)](https://codeclimate.com/github/maestro-server/analytics-maestro/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c2272dfe465bdaea4900/test_coverage)](https://codeclimate.com/github/maestro-server/analytics-maestro/test_coverage)

# Maestro Server #

Maestro Server is an open source software platform for management and discovery servers, apps and system for Hybrid IT. Can manage small and large environments, be able to visualize the latest multi-cloud environment state.

### Demo ###
To test out the demo, [Demo Online](http://demo.maestroserver.io "Demo Online")

## Documentation ##
* [UserGuide](http://docs.maestroserver.io/en/latest/userguide/cloud_inventory/inventory.html "User Guide")
* [API Contract](https://maestro-server.github.io/analytics-maestro/ "Analytics API Contract")

# Maestro Server - Analytics API #

Draw archtectures maps using NetworkX Graph and SVG write.

![arch](http://docs.maestroserver.io/en/latest/_images/analytics_internal.png)

**Core API, organized by modules:**

* Create grids
* Create bussiness graph
* Create network graph
* Create infra graph
* Drawing
* SVGs

## TechStack ##

* Python 3.6
* Flask 1.0.2
* SvgWrite
* NetworkX

## Service dependencies ##
* Maestro Data
* Maestro Analytics Front

## Setup ##

#### Installation by docker ####

```bash
docker run -p 5020
    -e "MAESTRO_DATA_URI=http://localhost:5010"
    -e "CELERY_BROKER_URL=amqp://rabbitmq:5672"
    -e 'MAESTRO_MONGO_URI=localhost'
    maestroserver/analytics-maestro

docker run
    -e "MAESTRO_DATA_URI=http://localhost:5010"
    -e "MAESTRO_ANALYTICS_FRONT_URI=http://localhost:9999"
    -e "CELERY_BROKER_URL=amqp://rabbitmq:5672"
    maestroserver/analytics-maestro-celery
```
Or by docker-compose

```bash
version: '2'

services:
    analytics:
        image: maestroserver/analytics-maestro
        ports:
        - "5020:5020"
        environment:
        - "CELERY_BROKER_URL=amqp://rabbitmq:5672"
        - "MAESTRO_DATA_URI=http://data:5010"

    analytics_worker:
        image: maestroserver/analytics-maestro-celery
        environment:
        - "MAESTRO_DATA_URI=http://data:5010"
        - "MAESTRO_ANALYTICS_FRONT_URI=http://analytics_front:9999"
        - "CELERY_BROKER_URL=amqp://rabbitmq:5672"
        - "CELERYD_MAX_TASKS_PER_CHILD=2"
```

#### Dev Env ####

Run python and celery.

```bash
cd devtools/

docker-compose up -d
```

Configure rabbitmq service in .env file

```bash
CELERY_BROKER_URL="amqp://localhost:5672"
CELERYD_TASK_TIME_LIMIT=30
```

Install pip dependences
```bash
pip install -r requeriments.txt
```

Run server
```bash
python -m flask run.py

or

FLASK_APP=run.py FLASK_DEBUG=1 flask run

or 

npm run server
```

Run workers
```bash
celery -A app.celery worker -E -Q discovery --hostname=discovery@%h --loglevel=info

or 

npm run celery
```

Run all tests 
```bash
python -m unittest discover
```

Create doc
```bash
npm install
apidoc -i app/controller/ -o docs/

or 

npm run docs
```

#### Important notes ####

* Controller used only graph to start all tasks:

* The drawer process is compound by:

    *  **entry:** First task, figure out all entry applications accordingly system endpoint parameters, our any direct application if avalaible.

    *  **graphlookup:** Request for Data App a aggregate query using MongoDB $graphLookup.

    *  **network bussiness:** Construct Grid Map, and send to enrichment and info bussines.

    *  **enrichment:** Request for Data App all servers used on grid.

    *  **info bussiness:** Calculate histogram, counts, density and connections.

    *  **network client:** Request for Data App all clients used in grid.

    *  **draw bussiness:** Create svgs based of grid.

    *  **notification:** Send updates for Data App.

    *  **send front app:** Send svgs to Analytics Front app.

* Each step have unique task.

    *  Config is managed by env variables, need to be, because in production env like k8s is easier to manager the pods.

    *  Repository it's pymongo objects.


### Env variables ###

| Env Variables                | Example                  | Description                                |
|------------------------------|--------------------------|--------------------------------------------|
| MAESTRO_PORT                 | 5020                     | API Port                                   |
| MAESTRO_DATA_URI             | http://localhost:5010    | Data Layer API URL                         |
| MAESTRO_ANALYTICS_FRONT_URI  | http://localhost:9999    | Analytics Front URL                        |
| MAESTRO_WEBSOCKET_URI        | http://localhost:8000    | Webosocket App - API URL                   |
|                              |                          |                                            |
| MAESTRO_WEBSOCKET_SECRET     | XXXX                     | Secret Key - JWT Websocket connections     |
| MAESTRO_SECRETJWT_PRIVATE    | XXX                      | Secret Key - JWT private connections       |
| MAESTRO_NOAUTH               | XXX                      | Secret Pass to validate private connections|
|                              |                          |                                            |     
| MAESTRO_GWORKERS             | 2                        | Prefetch used in translate worker          |
| CELERY_BROKER_URL            | amqp://rabbitmq:5672     | Rabbitmq URL                               |
| CELERYD_TASK_TIME_LIMIT      | 10                       | Timeout - worker                           |


### Contribute ###

Are you interested in developing Maestro Server, creating new features or extending them?

We created a set of documentation, explaining how to set up your development environment, coding styles, standards, learn about the architecture and more. Welcome to the team and contribute with us.

[See our developer guide](http://docs.maestroserver.io/en/latest/contrib.html)