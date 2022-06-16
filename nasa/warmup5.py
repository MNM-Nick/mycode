#!/usr/bin/env python3

import requests
import datetime

ISSURL= "http://api.open-notify.org/iss-now.json"

def main():

    iss = requests.get(f"{ISSURL}?limit=1000")
    iss = iss.json()
    date_time=datetime.datetime.fromtimestamp(iss['timestamp'])

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Lon: {iss['iss_position']['longitude']}")
    print(f"Lat: {iss['iss_position']['latitude']}")
    
    print(f"Time & Date: {date_time}")

if __name__=="__main__":
    main()
