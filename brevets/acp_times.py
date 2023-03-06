"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):

    speed_limit = [
    (0, 200, 15, 34), 
    (201, 400, 15, 32), 
    (401, 600, 15, 30), 
    (601, 1000, 11.428, 28), 
    (1001, 1300, 13.333, 26)]


    if control_dist_km > brevet_dist_km:
      control_dist_km = brevet_dist_km

    
    if control_dist_km == 0:
       return brevet_start_time

    total_time = 0                                                              
    
    for min_km, max_km, min_speed, max_speed in speed_limit: # for each tuple in speed_limit 
        if control_dist_km <= max_km: 
            if control_dist_km <= min_km:
                total_time += control_dist_km / min_speed
            elif control_dist_km <= 200:
                total_time += control_dist_km / max_speed
            elif control_dist_km <= 400:
                total_time += (200 / 34) + ((control_dist_km - 200) / 32)
            elif control_dist_km <= 600:
                total_time += (200 / 34) + (200 / 32) + ((control_dist_km - 400) / 30)
            elif control_dist_km <= 1000:
                total_time += (200/ 34) + (200 / 32) + (200 / 30) + ((control_dist_km - 600) / 28)
            break 
    
    
    hours = int(total_time)
    minutes = round((total_time - hours) * 60)

    return brevet_start_time.shift(hours=hours, minutes=minutes)
 
def close_time(control_dist_km, brevet_dist_km, brevet_start_time):

    last_checkpoint_times = {
    200: {"hours": 13, "minutes": 30},
    300: {"hours": 20, "minutes": 0},
    400: {"hours": 27, "minutes": 0},
    600: {"hours": 40, "minutes": 0},
    1000: {"hours": 75, "minutes": 0},
}
    # if control_dist_km is >= brevet_dist_km, meaning if you have a 200km brevet, 210, up tp 240 (which is the max distance for a 200km brevet) (up to 20% higher), then its the last checkpoint
    if control_dist_km >= brevet_dist_km:
        final_hours = last_checkpoint_times[brevet_dist_km]["hours"]
        final_minutes = last_checkpoint_times[brevet_dist_km]["minutes"]
        return brevet_start_time.shift(hours=final_hours, minutes=final_minutes)


    total_time = 0

    # first checkpoint at 0km always opens at brevet start time(not shifted) and always closes after 1 hour(dont have to calculate, just shift by 1 hour)
    if control_dist_km == 0:
        return brevet_start_time.shift(hours=1)
    # if control_dist_km is less than 60km, then add 1 hour to total_time                               
    elif control_dist_km <= 60: 
        total_time += (control_dist_km / (20) + 1) # adjust for distances under 60km
    elif control_dist_km <= 600: 
        total_time += (control_dist_km / 15) # adjust for distances under 600km
    else:
        total_time += (600 / 15) + ((control_dist_km - 600) / 11.428) # adjust for distances over 600km

    hours = int(total_time)
    minutes = round((total_time - hours) * 60)
    return brevet_start_time.shift(hours=hours, minutes=minutes)
