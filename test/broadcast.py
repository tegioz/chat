#!/usr/bin/env python

import sys
import json
import requests

SERVER="http://localhost:8888"

try:
    headers = {'Content-Type': 'application/json'}
    payload = {'msg': sys.argv[1]}
    r = requests.post('%s/api/broadcast/' % SERVER, headers=headers, data=json.dumps(payload))
    if (r.status_code == 201):
        print "Message sent successfully"
    else:
        print "ERROR: %d - %s" % (r.status_code, r.content)
except IndexError:
    print "Usage: python broadcast.py \"message\""
except requests.exceptions.ConnectionError:
    print "Error connecting to: %s" % SERVER
