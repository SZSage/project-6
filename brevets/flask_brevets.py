"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""
import os # for os.environ
import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
#from mypymongo import brevet_insert, brevet_find # import from mypymongo.py 

# so it doesn't crash when I run it
def brevet_insert(*args, **kwargs):
    pass

def brevet_find(*args, **kwargs):
    pass

import logging
import traceback

###
# Globals
###

logging.basicConfig(level=logging.DEBUG)
app = flask.Flask(__name__, static_folder="static")
app.debug = True

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
    
    app.logger.debug(f'Request JSON: {request.get_json()}') # 
    try: # read entire request body as JSON
        input_json = request.json
        brevet_dist = input_json["brevet_dist"]
        begin_time = input_json["begin_date"]
        checkpoints = input_json["checkpoints"]

        brevets = brevet_insert(brevet_dist, begin_time, checkpoints)
        return flask.jsonify(result={},
                             message = "Inserted!",
                             status = 1,
                             mongo_id = brevets)
                        
    except Exception as e:
        traceback.print_exc()
        return flask.jsonify(result={}, message=e, status=0, mongo_id="None")


@app.route("/_find_brevet")
def _find_brevet():
    """
    /fetch : fetches the latest brevets from the database
    
    Accepts GET requests ONLY!

    JSON interface: gets JSON, responds with JSON

    Taken from TodoListApp example
    """
    try:
        brevet_dist, begin_time, checkpoints = brevet_find()   
        return flask.jsonify(
                result={"brevet": brevet_dist, "start": begin_time, "checkpoints": checkpoints}, 
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
    brevit_dist = request.args.get("brevit_dist", 999, type=float)
    start_time = request.args.get("start_time", "2023-02-2000:00", type=str)
    start_time = arrow.get(start_time, "YYYY-MM-DDTHH:mm")
    
    app.logger.debug("start_time={}".format(start_time))
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    
    open_time = acp_times.open_time(km, brevit_dist, start_time).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brevit_dist, start_time).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

app.debug = os.environ["DEBUG"]
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    # write fail case incase PORT and DEBUG are not in the environment variables
    app.run(port=os.environ["PORT"], host="0.0.0.0")
