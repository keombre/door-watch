from gpiozero import Button
from urllib2 import request

btn = Button(26, pull_up=True, bounce_time=0.2)

while True:
    btn.wait_for_press()
    request.urlopen(request.Request("http://127.0.0.1/add", data=urllib.urlencode({}))
