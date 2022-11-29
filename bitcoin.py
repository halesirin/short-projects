#gets the current bitcoin equivalent of the entered dolar amount based on the bitcoin price index

import sys
import requests
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    sys.argv[1] = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" )
    #print(json.dumps(response.json(), indent = 2))
except:
   requests.RequestException
   pass

o = response.json()
rate = (o["bpi"]["USD"]["rate_float"])
print("$", "{:,.4f}".format(rate * sys.argv[1]), sep ="")