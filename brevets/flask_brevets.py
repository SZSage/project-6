"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""
import os # for os.environ
import flask
from flask import request
import arrow
import requests  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
#from mypymongo import brevet_insert, brevet_find # import from mypymongo.py 
import logging


###
# Globals
###

logging.basicConfig(level=logging.DEBUG)
app = flask.Flask(__name__, static_folder="static")
app.debug = True if "DEBUG" not in os.environ else os.environ["DEBUG"]
port_num = True if "PORT" not in os.environ else os.environ["PORT"]
app.logger.setLevel(logging.DEBUG)

API_ADDR = os.environ["API_ADDR"]
API_PORT = os.environ["API_PORT"]
API_URL = f"http://{API_ADDR}:{API_PORT}/api/"


def brevet_insert(brevet_dist, begin_date, checkpoints):
    """
    Inserts a new to-do list into the database by calling the API.
    
    Inputs a brevet distance (int), begin time (string), and checkpoints (list of dictionaries)
    """
    
    _id = requests.post(f"{API_URL}/brevets", json={"brevet_dist": brevet_dist, "begin_date": begin_date, "checkpoints": checkpoints}).json()
    return _id # return the id of the inserted document


def brevet_find():
    """
    Obtains the newest document in the "lists" collection in database
    by calling the RESTful API.

    Returns brevet distance (int), begin time (string), and checkpoints (list of dictionaries) as a tuple.
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.
    lists = requests.get(f"{API_URL}/brevets").json()

    # lists of dictionaries
    # get last element 
    brevet = lists[-1]
    return brevet["brevet_dist"], brevet["begin_date"], brevet["checkpoints"]


###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############


@app.route("/_insert_brevet", methods=["POST"])
def _insert_brevet():
    """
    /insert : inserts a brevet into the database

    Accepts POST requests ONLY!

    JSON interface: gets JSON, responds with JSON

    Taken from TodoListApp example
    """

    app.logger.debug('Received a request to insert a brevet')
    app.logger.debug(f'Request JSON: {request.get_json()}') 
    try: # read entire request body as JSON
        input_json = request.json
        brevet_dist = input_json["brevet_dist"]
        begin_date = input_json["begin_date"]
        checkpoints = input_json["checkpoints"]

        brevets = brevet_insert(brevet_dist, begin_date, checkpoints)

        app.logger.debug(f'Response JSON: {{"result": {{}}, "message": "Inserted!", "status": 1, "mongo_id": {brevets}}}')
        return flask.jsonify(result={},
                             message = "Inserted!",
                             status = 1,
                             mongo_id = brevets)
                        
    except Exception as e:
        # traceback.print_exc()
        # app.logger.error(f'Error occurred while inserting brevet: {e}')
        return flask.jsonify(result={}, message=str(e), status=0, mongo_id="None")


@app.route("/_find_brevet")
def _find_brevet():
    """
    /fetch : fetches the latest brevets from the database
    
    Accepts GET requests ONLY!

    JSON interface: gets JSON, responds with JSON

    Taken from TodoListApp example
    """
    try:
        brevet_dist, begin_date, checkpoints = brevet_find()   
        return flask.jsonify(
                result={"brevet": brevet_dist, "begin_date": begin_date, "checkpoints": checkpoints}, 
                status=1,
                message="Successfully fetched a brevet!")
    except:
        return flask.jsonify(
                result={}, 
                status=0,
                message="Something went wrong, couldn't fetch any brevets!")


@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    brevet_dist = request.args.get("brevet_dist", 999, type=float)
    begin_date = request.args.get("begin_date", type=str)
    begin_date = arrow.get(begin_date, "YYYY-MM-DDTHH:mm")
    logging.debug("begin_date={}".format(begin_date)) # debug
    app.logger.debug("begin_date={}".format(begin_date))
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))

    open_time = acp_times.open_time(km, brevet_dist, begin_date).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brevet_dist, begin_date).format('YYYY-MM-DDTHH:mm')

    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

if __name__ == "__main__":
    app.run(port=os.environ["PORT"], host="0.0.0.0")
