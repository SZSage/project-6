import os
from pymongo import MongoClient


client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

# uses database "brevets"
db = client.brevets

# Uses collection "table" in the database
collection = db.table

# MongoDB Functions 

# separate database components from flask
 
def brevet_insert(brevet_dist, begin_time, checkpoints):
    """
    Inserts a new to-do list into the database "todo", under the collection "lists".
    
    Inputs a start_time (string), brevet_dist (string), and checkpoints (list of dictionaries)
    
    Returns the unique ID assigned to the document by mongo (primary key.)

    Taken from TodoListApp example.
    """
      
    output = collection.insert_one({
        "brevet_dist": brevet_dist,
        "begin_time": begin_time, 
        "checkpoints": checkpoints
    })
    
    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)


def brevet_find():
    """
    Obtains the newest document in the "lists" collection in database "brevets".
    
    Returns title (string) and items (list of dictionaries) as a tuple.
    
    Taken from TodoListApp example.
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    lists = collection.find().sort("_id", -1).limit(1) # -1 means descending order (newest first) and 1 means limit to 1 document (row) 

    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:
    for brevets in lists:
        # We store all of our lists as documents with three fields:
        ## brevet_dist: string # km value of brevet
        ## start_name: string # start time
        ## checkpoints: list # list of dictionaries
        ## brevet_dist = brevets["brevet_dist"]
        ## start_name = brevets["start_name"]
        ## checkpoints = brevets["checkpoints"]

        ### every brevet has 5 fields:
        #### miles: int   # checkpoint in miles
        #### km: int  # checkpoint in km
        #### location: string # location name of checkpoint
        #### open: string # open time of checkpoint
        #### close: string # close time of checkpoint
        return brevets["brevet_dist"], brevets["begin_time"], brevets["checkpoints"]
