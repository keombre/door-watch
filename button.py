from gpiozero import Button
from datetime import datetime
import select
import sqlite3

def released():
    print("opened " + str(datetime.now()))
    con = sqlite3.connect("./db.sqlite")
    con.cursor().execute("INSERT INTO entries VALUES (?, 0);", (datetime.now(),))
    con.commit()
    con.close()

btn = Button(26, pull_up=True, bounce_time=0.2, hold_time=0.5)
btn.when_released = released

select.select([], [], [])

