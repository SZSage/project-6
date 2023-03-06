"""
Nose tests for pymongo.py

"""

from mypymongo import brevet_insert, brevet_find  
import arrow  
import nose 
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_insert():
    """
    Test that we can insert data into the database
    """
    start_time = arrow.get("2023-02-20 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = [
        {"miles": 0, "km": 0, "open": str(start_time), "close": str(start_time.shift(hours=1)), "location": 'Checkpoint1'},
        {"miles": 31.0686, "km": 50, "open": str(start_time.shift(hours=1, minutes=28)), "close": str(start_time.shift(hours=3, minutes=30)), "location": 'Checkpoint2'},
        {"miles": 93.2057, "km": 150, "open": str(start_time.shift(hours=4, minutes=25)), "close": str(start_time.shift(hours=10)), "location": 'Checkpoint3'},
        {"miles": 124.274, "km": 200, "open": str(start_time.shift(hours=5, minutes=53)), "close": str(start_time.shift(hours=13, minutes=30)), "location": 'Checkpoint4'}
    ]
    
    # call brevet_insert() to insert data into the database
    brevet_insert_id = brevet_insert(str(start_time), dist, checkpoints)
    assert isinstance(brevet_insert_id, str) and len(brevet_insert_id) > 0 
    
def test_find():
    """
    Test that we can find the data we just inserted
    """
    start_time = arrow.get("2023-02-20 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = [
        {"miles": 0, "km": 0, "open": str(start_time), "close": str(start_time.shift(hours=1)), "location": 'Checkpoint1'},
        {"miles": 31.0686, "km": 50, "open": str(start_time.shift(hours=1, minutes=28)), "close": str(start_time.shift(hours=3, minutes=30)), "location": 'Checkpoint2'},
        {"miles": 93.2057, "km": 150, "open": str(start_time.shift(hours=4, minutes=25)), "close": str(start_time.shift(hours=10)), "location": 'Checkpoint3'},
        {"miles": 124.274, "km": 200, "open": str(start_time.shift(hours=5, minutes=53)), "close": str(start_time.shift(hours=13, minutes=30)), "location": 'Checkpoint4'}
    ]
    
    # call brevet_insert() to insert data into the database
    brevet_insert(str(start_time), dist, checkpoints)

    # check that the data we inserted is the same as the data we got back
    # assert brevet_find() == (str(start_time), dist, checkpoints) 
    assert brevet_find()[0] == str(start_time)
    assert brevet_find()[1] == dist
    assert brevet_find()[2] == checkpoints
        