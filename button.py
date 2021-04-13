from gpiozero import Button
from urllib import request
from datetime import datetime

def released():
    print("opened " + str(datetime.now()))
    request.urlopen(request.Request("http://127.0.0.1/add", data=b''))

btn = Button(26, pull_up=True, bounce_time=0.2, hold_time=0.5)
btn.when_released = released

while True:
    input()

