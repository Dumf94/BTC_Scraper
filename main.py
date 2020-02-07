#Hello, if you see this and you are NOT one of the original coders, HOW THE FUCK DID YOU GET THIS SHIT?
#Anyway, hello, good luck understanding this shit, have fun :D
hours_wasted_debugging=2

import requests
from bs4 import BeautifulSoup
import json
import os

def scan(addr):    
    addr = str(addr)
    r = requests.get("https://chain.api.btc.com/v3/address/" + addr)
    if(r.status_code != 200):
        return
    content = r.content
    json_content = json.loads(content)
    try:
        print("Balance: " + str(json_content["data"]["balance"]) + " : " + addr)
        if(int(json_content["data"]["balance"]) != 0):
            os.system(addr)
    except:
        if(json_content["data"] == None):
            print("No data")
        else:
            print("Invalid: " + json_content["data"])

def main():
    r = requests.get("http://www.allprivatekeys.com/get-lucky.php")
    content = r.content
    bs = BeautifulSoup(content, 'html.parser')
    for aTag in bs.find_all('a'):
        if(str(aTag).find('data-address') != -1):
            grandPar = aTag.parent.parent
            greatGP = grandPar.parent.parent
            startPoint = str(greatGP).find("<div class=\"card-body small text-center monospace\"")
            if(startPoint != -1):
                secondSpl = str(greatGP).find("<div class=\"card-body small text-center monospace\"><img alt=\"\" class=\"pr-1\" height=\"20\" src=\"static/img/key.svg\"/>")
                secondSpl = str(greatGP).find("src=\"static/img/key.svg\"/>")
                endP = str(greatGP).find("<button class=")
                secondSpl = str(greatGP).find("svg\"/>")
                trimmed = str(greatGP)[secondSpl+7:endP]
                trimmed = trimmed.strip()
                print(trimmed)
                f = open('data_unfiltered.txt', 'a')
                f.write(trimmed + '\n')
                f.close()
            cutoff = str(aTag).find("data-type")
            addr = str(aTag)[17:cutoff-2]

while True:
	main()