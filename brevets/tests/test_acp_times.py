# """
# Nose tests for acp_times.py

# Write your tests HERE AND ONLY HERE.
# """

# from acp_times import open_time, close_time # Functions to test
# import arrow  # imported arrow
# import nose    # Testing framework
# import logging
# logging.basicConfig(format='%(levelname)s:%(message)s',
#                     level=logging.WARNING)
# log = logging.getLogger(__name__)


# # testing for 5 test cases for brevets
# def test_brevet1():
#     start_time = arrow.get("2023-02-20 00:00", "YYYY-MM-DD HH:mm")
#     dist = 200
#     checkpoints = {
#         # enter these into the website
#         # transfer data into these variables 
#         0: (start_time, start_time.shift(hours=1)), # 0km checkpoint
#         50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
#         150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
#         200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=30)),
#     }
#     # iterate through the checkpoint dictionary
#     for km, time_tuple in checkpoints.items(): 
#         checkpoint_open, checkpoint_close = time_tuple # unpacking tuple

#         # call open_time and close_time functions for testing
#         actual_open = open_time(km, dist, start_time) 
#         actual_close = close_time(km, dist, start_time)
#         print(f"Checkpoint {km}: expected ({checkpoint_open}, {checkpoint_close}), actual ({actual_open}, {actual_close})")
        
#         assert open_time(km, dist, start_time) == checkpoint_open
#         assert close_time(km, dist, start_time) == checkpoint_close

        
# def test_brevet2():
#     start_time = arrow.get("2023-02-20 00:00", "YYYY-MM-DD HH:mm")
#     dist = 300
#     checkpoints = {
#         0: (start_time, start_time.shift(hours=1)),
#         50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
#         100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
#         200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
#         300: (start_time.shift(hours=9), start_time.shift(hours=20)),
#     }

#     for km, time_tuple in checkpoints.items(): 
#         checkpoint_open, checkpoint_close = time_tuple 

#         actual_open = open_time(km, dist, start_time)
#         actual_close = close_time(km, dist, start_time)
#         print(f"Checkpoint {km}: expected ({checkpoint_open}, {checkpoint_close}), actual ({actual_open}, {actual_close})")

#         assert open_time(km, dist, start_time) == checkpoint_open
#         assert close_time(km, dist, start_time) == checkpoint_close

# def test_brevet3():
#     start_time = arrow.get("2023-02-20 00:00", "YYYY-MM-DD HH:mm")
#     dist = 400
#     checkpoints = {
#         0: (start_time, start_time.shift(hours=1)),
#         50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
#         150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
#         200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
#         300: (start_time.shift(hours=9), start_time.shift(hours=20)),
#         350: (start_time.shift(hours=10, minutes=34), start_time.shift(hours=23, minutes=20)),
#         400: (start_time.shift(hours=12, minutes=8), start_time.shift(hours=27))
#     }

#     for km, time_tuple in checkpoints.items(): 
#         checkpoint_open, checkpoint_close = time_tuple 

#         actual_open = open_time(km, dist, start_time)
#         actual_close = close_time(km, dist, start_time)
#         print(f"Checkpoint {km}: expected ({checkpoint_open}, {checkpoint_close}), actual ({actual_open}, {actual_close})")

#         assert open_time(km, dist, start_time) == checkpoint_open
#         assert close_time(km, dist, start_time) == checkpoint_close


# def test_brevet4():
#     start_time = arrow.get("2023-02-20 00:00", "YYYY-MM-DD HH:mm")
#     dist = 600
#     checkpoints = {
#         0: (start_time, start_time.shift(hours=1)),
#         50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
#         150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
#         200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
#         300: (start_time.shift(hours=9), start_time.shift(hours=20)),
#         350: (start_time.shift(hours=10, minutes=34), start_time.shift(hours=23, minutes=20)),
#         400: (start_time.shift(hours=12, minutes=8), start_time.shift(hours=26, minutes=40)),
#         450: (start_time.shift(hours=13, minutes=48), start_time.shift(hours=30)),
#         500: (start_time.shift(hours=15, minutes=28), start_time.shift(hours=33, minutes=20)),
#         600: (start_time.shift(hours=18, minutes=48), start_time.shift(hours=40))
#     }
#     for km, time_tuple in checkpoints.items(): 
#         checkpoint_open, checkpoint_close = time_tuple 

#         actual_open = open_time(km, dist, start_time)
#         actual_close = close_time(km, dist, start_time)
#         print(f"Checkpoint {km}: expected ({checkpoint_open}, {checkpoint_close}), actual ({actual_open}, {actual_close})")

#         assert open_time(km, dist, start_time) == checkpoint_open
#         assert close_time(km, dist, start_time) == checkpoint_close

# def test_brevet5():
#     start_time = arrow.get("2023-02-20 00:00", "YYYY-MM-DD HH:mm")
#     dist = 1000
#     checkpoints = {
#         0: (start_time, start_time.shift(hours=1)),
#         50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
#         150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
#         200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
#         300: (start_time.shift(hours=9), start_time.shift(hours=20)),
#         350: (start_time.shift(hours=10, minutes=34), start_time.shift(hours=23, minutes=20)),
#         400: (start_time.shift(hours=12, minutes=8), start_time.shift(hours=26, minutes=40)),
#         450: (start_time.shift(hours=13, minutes=48), start_time.shift(hours=30)),
#         500: (start_time.shift(hours=15, minutes=28), start_time.shift(hours=33, minutes=20)),
#         600: (start_time.shift(hours=18, minutes=48), start_time.shift(hours=40)),
#         650: (start_time.shift(hours=20, minutes=35), start_time.shift(hours=44, minutes=23)),
#         700: (start_time.shift(hours=22, minutes=22), start_time.shift(hours=48, minutes=45)),
#         750: (start_time.shift(hours=24, minutes=9), start_time.shift(hours=53, minutes=8)),
#         800: (start_time.shift(hours=25, minutes=57), start_time.shift(hours=57, minutes=30)),
#         900: (start_time.shift(hours=29, minutes=31), start_time.shift(hours=66, minutes=15)),
#         1000: (start_time.shift(hours=33, minutes=5), start_time.shift(hours=75))

#     }
#     for km, time_tuple in checkpoints.items(): 
#         checkpoint_open, checkpoint_close = time_tuple 

#         actual_open = open_time(km, dist, start_time)
#         actual_close = close_time(km, dist, start_time)
#         print(f"Checkpoint {km}: expected ({checkpoint_open}, {checkpoint_close}), actual ({actual_open}, {actual_close})")

#         assert open_time(km, dist, start_time) == checkpoint_open
#         assert close_time(km, dist, start_time) == checkpoint_close