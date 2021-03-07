import json
import datetime
import random
import pytz

# db.json generated from Mockaroo Fake Data Generator
# didn't have an option to add end_time relative to start_time so made this program
# to fill end_time with [2, 3, 4 , 1] random integer for hour timedelta

# read & parse json file without end_time
with open("./db_unstructured.json") as f:
    data = json.load(f)

# function to add time delta to start time to get end time


def add_delta_convert_tz(input_datetime, tz):
    fmt = '%Y-%m-%dT%H:%M:%SZ'
    d = datetime.datetime.strptime(input_datetime, fmt)
    h = random.choice([2, 4, 3, 1])
    t = datetime.timedelta(hours=h)
    r = d + t
    return (d.astimezone(tz).strftime(fmt), r.astimezone(tz).strftime(fmt))


for i in range(len(data["members"])):
    member = data["members"][i]
    tz = pytz.timezone(member['tz'])
    for j in range(len(member["activity_periods"])):
        activity_period = member["activity_periods"][j]
        activity_period["start_time"], activity_period["end_time"] = add_delta_convert_tz(
            activity_period["start_time"], tz)
        member["activity_periods"][j] = activity_period

    data["members"][i] = member

# parse & write json file with end_time
with open('db_structured.json', 'w') as outfile:
    json.dump(data, outfile)
