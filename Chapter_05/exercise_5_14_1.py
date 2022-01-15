""""Chapter 5 examples and exercises"""

# Exercise 5.1

import time
import math

gross_time=time.time()

current_time = gross_time%(24*60*60)

current_hours = math.floor(current_time/(60*60))

print("Current hours (GMT):", current_hours)

current_minutes = math.floor((current_time%(60*60))/60)

print("Current minutes:", current_minutes)

current_seconds = round(current_time%60)

print("Current seconds:", current_seconds)

print("Current time (GMT):", current_hours, "h", current_minutes, "m", current_seconds, "s")

n_days_since_epoch = gross_time/(24*60*60)

print("Numbers of days since the epoch:", round(n_days_since_epoch,2), "days")







