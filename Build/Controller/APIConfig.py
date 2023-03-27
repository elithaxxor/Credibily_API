import requests
import json
import os
import sys
import base64


# BE SURE TO RUN THE CONFIG FILE BEFORE RUNNING THE FILE.
# TO BUILD COMMUNCIATION BETWEEN END USER AND API
# build notes:
## BE SURE TO RUN THE BUID CONFIG API.SH
# pip install requests
# get fresh token from shareholder to run live test 



class APConfig():

    def __init__(self, apiURL):

        self.TOKEN = "90565ed6e9c84dbea4144de09bd35a93" # SAMPLE GIVEN FROM API DOC
        self.USER = "TEMP_USERNAME"
        ## ENTER API INFO HERE
        self.parameters = {
            "Anthorization": self.TOKEN,
            'Content-Type':'application/ison'
        }
        self.fetchAPI(apiURL)


    def printRes(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)

        print(f"[TEXT] Printing Res  \n {text}")


    def RunRequest(self):

        s = requests.Session()
        personalLogin = (self.USER, self.TOKEN)
        s.headers.update({'x-test': 'true'})


        # both 'x-test' and 'x-test2' are sent
        s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

        print(f"[!] {s.auth}")

    def fetchAPI(self, url):
        print(f"[!] running fetch api for {url}")
        print(self.parameters)

       # r = requests.get(url, auth=(self.parameters)) # MAY NEED TO BE PASSED AS A TUPLE
        r = requests.get(url=url, headers=self.parameters)

       # response = r.get(url)
        #header = r.headers["Content-Type"]

        ## BUILD- to set get request

        print(f"fetching with this header {r.headers}")
        print(url)

        if r.status_code == 200:
            print(f"[STATUS-CODE] {r.status_code}, proceeding")
            self.RunRequest()
            self.printRes(r.json())

        else:
            print(f"[STATUS-CODE] {r.status_code} Terminating ")
            return

        print ("[+] fetch api complete ")



    def sendAPIB63(self): ## NOT NEEDED, AS OF NOW (api docs)
        content = base64.b64encode(open("/path/to/file.pdf", "rb").read()
                                   ).decode()
        # content is now a string


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/1"
    run = APConfig(url)
    run.fetchAPI(url)

