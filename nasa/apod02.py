#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds)

    ## strip off json
    apod = apodresp.json()

    usr_date=input("Put type a start date for more details on APODs. format...<yyy-mm-dd>")
    
    if 'date' >= usr_date:

        print(f"{apod['title']}\n {apod['date']}\n {apod['explanation']}\n {apod['url']}")


            #print(apod)

            #print(apod["title"] + "\n")

            #print(apod["date"] + "\n")

            #print(apod["explanation"])

            #print(apod["url"])
    # print(apod)

    #  print()

if __name__ == "__main__":
    main()

