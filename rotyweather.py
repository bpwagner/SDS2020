from tkinter import *
import pyowm
import time

from PIL import ImageTk, Image
import requests
from io import BytesIO

import math


root = Tk()
root.title("Weather App")
root.configure(background='sky blue')
v = IntVar()
v.set(0)

LocationStr = StringVar()
LocationStr.set("Louisville")


owm = pyowm.OWM('978910f354606707ef717cdf3b483575')
observation = owm.weather_at_place(LocationStr.get())
w = observation.get_weather()
temp_dict = w.get_temperature('fahrenheit')
pres_dict = w.get_pressure()
stat_dict = w.get_status()
icon_dict = w.get_weather_icon_url()
wind = w.get_wind()
wdeg = wind['deg']

response = requests.get(icon_dict)
img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))


def UpdateTemp():
    if v.get() == 0:
        LabelTemp['text'] = w.get_temperature('fahrenheit')['temp']
    elif v.get() == 1:
        LabelTemp['text'] = w.get_temperature('celsius')['temp']
    elif v.get() == 2:
        LabelTemp['text'] = w.get_temperature('kelvin')['temp']


def UpdateTime():
    LabelTime['text'] = time.strftime("%-I:%M:%S %p")
    listenID = root.after(1000, UpdateTime)


def UpdateWeather():
    s = LocationStr.get()
    observation = owm.weather_at_place(LocationStr.get())
    w = observation.get_weather()
    v=1

    temp_dict = w.get_temperature('fahrenheit')
    icon_dict = w.get_weather_icon_url()
    response = requests.get(icon_dict)
    img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))

    LabelTemp['text'] = w.get_temperature('fahrenheit')['temp']
    LabelLoc['text'] = observation.get_location().get_name()

    img2 = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(icon_dict).content)))
    panel.configure(image=img2)
    panel.image = img2

    wind = w.get_wind()
    wdeg = wind['deg']
    print(wdeg)

    print("Weather Updated")


frame1 = Frame(root, bg="sky blue", bd=10)
frame1.pack(side=TOP)

frame2 = Frame(root, bg="sky blue")
frame2.pack()

frame2l = Frame(frame2, highlightbackground="black", highlightthickness=1)
frame2l.pack(side=LEFT)

frameI = Frame(root)
frameI.pack(side=RIGHT)

frame2r = Frame(frame2, highlightbackground="black", highlightthickness=1)
frame2r.pack(side=RIGHT)

frame3 = Frame(root, highlightbackground="black", highlightthickness=1)
frame3.pack(side=BOTTOM)

frame3l = Frame(frame3, highlightbackground="black", highlightthickness=1)
frame3l.pack(side=RIGHT)

LabelIcon = Label()

LabelTime = Label(frame1, text=time.strftime("%-I:%M:%S %p"), bg="white", fg="blue", borderwidth=1, relief="solid")
LabelTime.pack(side=LEFT)

LabelLoc = Label(frame1, text="Louisville", bg="white", fg="blue", borderwidth=1, relief="solid")
LabelLoc.pack(side=RIGHT)

b = Button(frame1, text="Search", fg="red", command=UpdateWeather)
b.pack(side=RIGHT)
e = Entry(frame1, textvariable=LocationStr)
e.pack()

LabelFeel = Label(frame2l, text="feels like 72°", fg="red")
LabelFeel.pack()
LabelTemp = Label(frame2l, font=("Courier", 44), text=str(temp_dict['temp']) + "°", fg="blue")
LabelTemp.pack()

panel = Label(frameI, image=img, borderwidth=1, relief="solid")
panel.pack(side="left", fill="both", expand="yes")

LabelWind = Label(frame2r, font=("Courier", 44), text=wdeg, bg="white", fg="red")
LabelWind.pack(side=BOTTOM)

windCanvas = Canvas(frame2r, width=100, height=100)
windCanvas.create_oval(10, 10, 90, 90, outline="blue", width=2)
x2 = -math.cos(math.radians(-wdeg + 90)) * 35 + 55
y2 = -math.sin(math.radians(-wdeg + 90)) * -35 + 55
print(str(x2) + " / " + str(y2))
windCanvas.create_line(50, 50, x2, y2,  arrow=LAST)
windCanvas.pack()

RF = Radiobutton(frame2l, text="F°", fg="red", padx=10, variable=v, value=0, command=UpdateTemp)
RF.pack(side=LEFT)
RC = Radiobutton(frame2l, text="C°", fg="red", padx=10, variable=v, value=1, command=UpdateTemp)
RC.pack(side=LEFT)
RK = Radiobutton(frame2l, text="K°", fg="red", padx=10, variable=v, value=2, command=UpdateTemp)
RK.pack(side=LEFT)

LabelPress = Label(frame3, text="Pressure Rising", bg="White", fg="Blue")
LabelPress.pack()

listenID = root.after(1000, UpdateTime)

mainloop()