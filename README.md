# UOCIS322 - Project 6 #
Brevet time calculator with MongoDB, and a RESTful API!

Read about MongoEngine and Flask-RESTful before you start: [http://docs.mongoengine.org/](http://docs.mongoengine.org/), [https://flask-restful.readthedocs.io/en/latest/](https://flask-restful.readthedocs.io/en/latest/).

## Overview

This project is a web application that provides a Brevet time calculator, utilizing the RUSA ACP controle time algorithm as described on https://rusa.org/pages/acp-brevet-control-times-calculator. It's an extension of Project-5 (https://github.com/SZSage/project-5), which already includes two essential services, Brevets (implemented with Flask) and MongoDB (used for efficient data storage and retrieval).

The objective of this project is to incorporate the `brevets/` directory from Project-5 and develop a RESTful API service that enables the storage and retrieval of structured data in MongoDB and to replace every database related code in `brevets/` with calls to the new API.


## Tasks
The steps used to complete this project are as follows,

- Copy over Project 5 
- Add new Flask service: `api` 
	- Connect it to the database service: `db` 
	- Create your API
	- Test it locally
- Connect `brevets` to `api`, remove dependency between `brevets` and `db` 
- Remove PyMongo interface and replace it with requests to the API 


### Back-end (API)
To implement a RESTful API, a Python script was created (`api/database/models.py`) to define two classes (`Checkpoint` and `Brevet`) using the MongoEngine library for working with MongoDB databases. 

- `Checkpoint`: an embedded document that contains `miles`, `km`, `location`, and `open`/`close` times.
- `Brevet`: a MongoDB document that contains `brevet_dist`, `begin_time`, and `checkpoints`.


Using this schema, a Flask-RESTful API was implemented in `api/resources/`.

- `brevet.py`: allows manipulation of a single Brevet object in the MongoDB database with `GET`, `PUT`, and `DELETE` methods. 

	- `GET`: retrieves a Brevet object with specified `ID` and responds with a JSON object and status code `200` (OK).
	- `PUT`: updates an existing Brevet object with specified `ID` using the JSON payload and returns an empty response with status code `200` (OK).
	- `DETETE`: deletes an existing Brevet object with specified `ID` and returns an empty response with status code `200` (OK).

- `brevets.py` manages a collection of Brevets that contains a set of methods `GET` and `POST` to retrieve all Brevets. 
	- `GET`: returns a JSON object containing all Brevets in database. 
	- `POST`: get JSON paylod, creates new Brevet, and returns `ID` of new Brevet.


The `api.py` file was created to set up a RESTful API that interacts with a MongoDB database using the MongoEngine library. The API contains two endpoints, `/api/brevet/<id>` and `/api/brevets`, which allow for the retrieval of a single brevet document by `ID` and all brevet documents. The Flask app listens on a specified `PORT` and accepts incoming requests. 


Finally, the `brevets/flask_brevets.py` file was adjusted to use environment variables to determine the `PORT` and `DEBUG` values. It now uses an API to interact with the MongoDB database that inserts and retrieves data. Two new functions `brevet_insert` and `brevet_find` uses the API to insert a new document into the database and retrieves the newest document. 


### Front-end

No new additions/changes were made for the front-end. It remains the same as it was in Project-5.


## Testing
To test these newly implemented APIs, the following `curl` commands are used,

_Note that `API` should be replaced with the API address and `PORT` should be replaced with specified port_.

- `curl -X GET http://API:PORT/api/brevets`: Retrieve and display all brevets stored in the database.
- `curl -X GET http://API:PORT/api/brevet/ID`: Replace `ID` with the ID of brevet you want to retrieve.
- `curl -X POST http://API:PORT/api/brevets`: Inserts brevet object into the database.
- `curl -X DELETE http://API:PORT/api/brevet/ID`: Replace `ID` with the ID of brevet you want to delete.
- `curl -X POST http://API:PORT/api/brevet/ID`: Replace `ID` with the ID of brevet you want to update.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.

Completed by Simon Zhao: simonz@uoregon.edu
