from requests import *
from tkinter import *
from tkinter.ttk import *
from time import strftime
room=Tk()
room.title("MUDRIK MOHD IDDI")
door="https://api.thingspeak.com/channels/2634942/feeds.json?api_key=XZD8794U78ZGFSY6&results=1"
door2="https://api.thingspeak.com/channels/2655243/feeds.json?api_key=E2A0NI4FNCHZ0JTA&results=1"
door3="https://api.thingspeak.com/channels/2655254/feeds.json?api_key=P0SVJBWY7WP2P9QP&results=1"
read_spika="https://api.thingspeak.com/channels/2653317/feeds.json?api_key=YHEJKMD4TPE7L5DL&results=1"
def my_saa():
    door_response = get(door)
    door_data = door_response.json()
    mwizi = door_data['feeds'][0]['field2']
    mwizi,_,_ = str(mwizi).partition('.')
    if(int(mwizi) not in range(170,174)):
        mw='Emergency 1: Their is a new person in room, is you?'
    else:
        mw='Happy 1: Your room is safe'

    door2_response = get(door2)
    door2_data = door2_response.json()
    mwizi2 = door2_data['feeds'][0]['field1']
    mwizi2,_,_ = str(mwizi2).partition('.')
    if(int(mwizi2) not in range(170,174)):
        mw2='Emergency 2: Their is a new person in room, is you?'
    else:
        mw2='Happy 2: Your room is safe'

    door3_response = get(door3)
    door3_data = door3_response.json()
    mwizi3 = door3_data['feeds'][0]['field1']
    mwizi3,_,_ = str(mwizi3).partition('.')
    if(int(mwizi3) not in range(170,174)):
        mw3='Emergency 3: Their is a new person in room, is you?'
    else:
        mw3='Happy 3: Your room is safe'

    r_s = get(read_spika)
    rs_data = r_s.json()
    r_spika = rs_data['feeds'][0]['field1']
    if(int(r_spika)==10):
        rsk='You confirm DANGER\n\tSpika: ON alarm'
    else:
        rsk='Spika: OFF alarm'

    saa.config(text=strftime(f"""
\t%A %d-%B-20%y %I:%M %p\n
\t{mw}
\t{mw2}
\t{mw3}
\n\t{rsk}
"""))
    saa.after(4000,my_saa)
saa=Label(room,font=("Digital",30),background=("blue"),foreground=("black"))
saa.pack(anchor=("n"))
def spk_on():
    get("https://api.thingspeak.com/update?api_key=C43DPG0T68I3T287&field1=10")
def spk_off():
    get("https://api.thingspeak.com/update?api_key=C43DPG0T68I3T287&field1=20")
        

on_button = Button(text='''

\n\t\tIs me\t\t\n

''', command=spk_off)
on_button.pack(anchor='center')

off_button = Button(text='''

\n\t\tNot me\t\t\n

''', command=spk_on)
off_button.pack(anchor='center')

my_saa()
mainloop()
