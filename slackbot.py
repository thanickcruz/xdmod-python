import requests
import pycurl
import sys
import getopt
import json
from datetime import date
import datetime

import xdmod.datawarehouse as xdw
                           
'''
def main(argv):
    
    message = ''
    
    try: 
        opts, args = getopt.getopt(argv, "hm:", ["message="])
   
    except getopt.Getopterror:
        print('slackbot.py -m <message>')
        sys.exit(2)
    if len(opts) == 0:
        message = "HI"
    for opt, arg in opts:
        if opt == '-h':
            print('slackbot.py -m <message>')
            sys.exit
        elif opt in ("-m", "--message"):
            message = arg
    
    send(message)

if __name__ == "__main__":
    main(sys.argv[1:])
    
'''

def main():
    today = date.today()
    sunday = today - datetime.timedelta(days=1)
    last_monday = today - datetime.timedelta(days=7)
    last_sunday = sunday - datetime.timedelta(days=1)
    lastlast_monday = last_monday - datetime.timedelta(days=7)
    
    host = "https://metrics-dev.ccr.buffalo.edu:9004"
    
    alerts = []
    
    with xdw.DataWareHouse(host) as warehouse:
        for type in ['gpu', 'hardware', 'cpu', 'realms']:
            today_data = warehouse.get_qualitydata({"start": last_monday.strftime("%Y-%m-%d"), "end": sunday.strftime("%Y-%m-%d"), "type": type})
            lastweek_data = warehouse.get_qualitydata({"start": lastlast_monday.strftime("%Y-%m-%d"), "end": last_sunday.strftime("%Y-%m-%d"), "type": type})
        
            print(today_data)
            print(lastweek_data)
            
    #response = requests.post('https://hooks.slack.com/services/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', 
                             #data = json.dumps(payload))
    #print(response.text)
    
if __name__ == "__main__":
    main()
        