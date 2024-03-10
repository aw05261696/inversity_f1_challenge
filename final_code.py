from logging import root
from urllib.request import urlopen
import json
import pandas as pd
from tkinter import *
import tkinter as tk
import sys
from datetime import datetime, timedelta

screen = tk.Tk()
screen.title("f1_stats")
screen.geometry('1900x900')
screen.configure(bg="#565F64")
nav = Canvas(screen,bg = "black",height = 800,width = 300)
info = Canvas(screen,bg= "black", height = 800, width = 1250)

throttle_bar=Canvas(screen,bg= "#565F64", height = 50,  width= 200)
throttle_percent=Canvas(screen,bg= "#00A19B", height = 50,  width= 0)
throttle_bar.place(x=825,y=275)
throttle_percent.place(x=825,y=275)

brake_bar=Canvas(screen,bg= "#565F64", height = 50,  width= 200)
brake_percent=Canvas(screen,bg= "#00A19B", height = 50,  width= 0)
brake_bar.place(x=825,y=575)
brake_percent.place(x=825,y=575)

speed_monitor=Canvas(screen,bg= "black", height = 115,  width= 200)
arc=speed_monitor.create_arc(10, 10, 200, 200, start=15, extent=150, fill="grey")
arc2=speed_monitor.create_arc(10, 10, 200, 200, start=-195, extent=-130, fill="#00A19B")
speed_monitor.place(x=450,y=275)

rpm_monitor=Canvas(screen,bg= "black", height = 115,  width= 200)
arc=rpm_monitor.create_arc(10, 10, 200, 200, start=15, extent=150, fill="grey")
arc2=rpm_monitor.create_arc(10, 10, 200, 200, start=-195, extent=-120, fill="#00A19B")
rpm_monitor.place(x=450,y=575)

name = Label(screen,text="name",)

# VVVV car data VVVV
rpm = tk.Label(
    screen,
    text="rpm",
    fg="black",
    bg="#00A19B",
    font=('Helvetica bold', 27),
    width=11)
rpm.place(x=450,y=500)

speed = tk.Label(
    screen,
    text="speed",
    fg="black",
    bg="#00A19B",
    font=('Helvetica bold', 27),
    width=11)
speed.place(x=450,y=200)

gear = tk.Label(
    screen,
    text="gear",
    fg="black",
    bg="#00A19B",
    font=('Helvetica bold', 27),
    width=11)
gear.place(x=1200,y=500)
    
throttle = tk.Label(
    screen,
    text="throttle",
    fg="#00A19B",
    bg="black",
    font=('Helvetica bold', 27),
    width=11)
throttle.place(x=800,y=200)

drs = tk.Label(
    screen,
    text="drs",
    fg="black",
    bg="#00A19B",
    font=('Helvetica bold', 27),
    width=11)
drs.place(x=1200,y=250)

brake = tk.Label(
    screen,
    text="brake",
    fg="#00A19B",
    bg="black",
    font=('Helvetica bold', 27),
    width=11)
brake.place(x=800,y=500)



# end of car data
    
def car_data(driver):

    if driver=="Lewis":
        driver_number=44
    elif driver=="George":
        driver_number=63

    
    current_time=datetime.now() - timedelta(seconds=1)
    formatted_time = current_time.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00')
        
    if driver=="Lewis":
        response=urlopen('https://api.openf1.org/v1/car_data?driver_number=44&session_key=latest&date=2024-03-09T17:08:20.739000')
    elif driver=="George":
        response=urlopen('https://api.openf1.org/v1/car_data?driver_number=63&session_key=latest&date=2024-03-09T17:08:20.739000')

    try:
        data = json.loads(response.read().decode('utf-8'))
        df = pd.DataFrame(data)

        driver_info={
            "meeting" : (df.iloc[0,0]),     #0
            "session" : (df.iloc[0,1]),     #1
            "number" : (df.iloc[0,2]),      #2
            "date" : (df.iloc[0,3]),        #3
            "rpm" : (df.iloc[0,4]),         #4
            "speed" : (df.iloc[0,5]),       #5
            "gear" : (df.iloc[0,6]),        #6
            "throttle" : (df.iloc[0,7]),    #7
            "drs" : (df.iloc[0,8]),         #8
            "brake" : (df.iloc[0,9]),       #9
        }

        print(driver_info)
    
        temp = (driver_number, driver)
        name.config(text=temp)

        temp = ("rpm:", driver_info["rpm"])
        rpm.config(text=temp)

        temp = ("speed:", driver_info["speed"], "km/h")
        speed.config(text=temp, width=13)

        temp = ("gear:", driver_info["gear"])
        gear.config(text=temp)

        temp = ("throttle:", driver_info["throttle"])
        throttle.config(text=temp)

        temp = ("drs:", driver_info["drs"])
        drs.config(text=temp)

        temp = ("brake:", driver_info["brake"])
        brake.config(text=temp)

        # bars
        temp = driver_info["throttle"]*2
        throttle_percent.config(width=temp)

        temp = driver_info["brake"]*2
        brake_percent.config(width=temp)
        
            
    except Exception as e:
        print(f"error: {e}")

    

def quit_monitor():
    screen.destroy()
    sys.exit(0)
        
        
def main_screen():
    
    lbl = tk.Label(
        screen,
        text="select driver",
        fg="#00A19B",
        bg="black",
        font=('Helvetica bold', 27),
        width=11)
    lbl.place(x=75,y=100)

    btn = tk.Button(screen, text="Lewis", command=lambda: car_data("Lewis"))
    btn.configure(
        bg="#00A19B",
        fg="black",
        width=11,
        activebackground="#C8CCCE",
        font=('Helvetica bold', 27))
    btn.place(x=75,y=200)
    
    btn = tk.Button(screen, text="George", command=lambda: car_data("George"))
    btn.configure(
        bg="#00A19B",
        fg="black",
        width=11,
        activebackground="#C8CCCE",
        font=('Helvetica bold', 27))
    btn.place(x=75,y=300)
    

    btn = tk.Button(screen, text="Quit", command=quit_monitor)
    btn.configure(
        bg="#00A19B",
        fg="black",
        width=11,
        activebackground="#C8CCCE",
        font=('Helvetica bold', 27))
    btn.place(x=75,y=750)

    name.configure(
        bg="black",
        fg="#00A19B",
        font=('Helvetica bold', 30))
    name.place(x=450,y=100)

    nav.place(x=50,y=50)
    info.place(x=400,y=50)

    screen.mainloop
    
main_screen()
