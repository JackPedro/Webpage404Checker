from tkinter import *
import requests as r
from time import sleep as s
from datetime import datetime as dt

#url to check
url = "https://google.com"

#using requests goes to the website and checks time
def getwebpage():
    x = r.get(url)
    tm = dt.now()
#prints status code
    print(tm, "~",x.status_code)
#if status code of webpage is 404 retries in 10s
    if x.status_code == 404:
        s(10)
        getwebpage()
    else:
    #prints 10 times that the page is not 404
        print("ATTENTION WEBSITE HAS CHANGED\n"*10)

if __name__ == "__main__":
    getwebpage()