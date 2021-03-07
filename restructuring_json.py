import json

with open("./db_structured.json") as f:
    data = json.load(f)

data["activity_periods"] = []

# restructuring json to become suitable for JSON Specifications based json-server

for i in range(len(data["members"])):
    member = data["members"][i]
    for j in range(len(member["activity_periods"])):
        activity_period = member["activity_periods"][j]
        activity_period["id"] = f'{member["id"]}_{activity_period["id"]}'
        activity_period["memberId"] = member["id"]
        data["activity_periods"].append(activity_period)

    del member["activity_periods"]
    data["members"][i] = member


with open('./db.json', 'w') as outfile:
    json.dump(data, outfile)
