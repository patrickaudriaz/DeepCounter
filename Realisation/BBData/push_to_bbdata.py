'''
    Author: Matthieu Jourdan
    Date created: 25.06.2019
'''

import requests
import json
import datetime

# constants used to push new measure in BBData
url = 'https://bbdata.daplab.ch/input/measures'
headers = {'content-type': 'application/json', 'accept': 'application/json'}

def push_to_bbdata(object_id, object_token, value):
    # get current timestamp and format to ISO
    now = datetime.datetime.utcnow().replace(microsecond=0).isoformat()

    # form the payload with parameters
    payload = {"objectId": object_id, "token": object_token, "timestamp": now, "value": value}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # 0 if success and -1 if there is an error
    if response.status_code == 200:
        print("Success")
        print(response.json())
        return 0
    else:
        print("Error")
        return -1
