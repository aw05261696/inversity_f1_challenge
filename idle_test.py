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

name = Label(screen,text="name:",)
    
def driver_select(driver):

    if driver=="Lewis":
        driver_number=44
    elif driver=="George":
        driver_number=63

    
    current_time=datetime.now() - timedelta(seconds=1)
    formatted_time = current_time.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00')
        
    if driver=="Lewis":
        response=urlopen(f'https://api.openf1.org/v1/car_data?driver_number=44&session_key=latest&date>{formatted_time}')
    elif driver=="George":
        response=urlopen(f'https://api.openf1.org/v1/car_data?driver_number=63&session_key=latest&date>{formatted_time}')

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

    btn = tk.Button(screen, text="Lewis", command=lambda: driver_select("Lewis"))
    btn.configure(
        bg="#00A19B",
        fg="black",
        width=11,
        activebackground="#C8CCCE",
        font=('Helvetica bold', 27))
    btn.place(x=75,y=200)
    
    btn = tk.Button(screen, text="George", command=lambda: driver_select("George"))
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
        font=('Helvetica bold', 27))
    name.place(x=450,y=100)

    nav.place(x=50,y=50)
    info.place(x=400,y=50)

    screen.after( 500, driver_select("Lewis"))

    screen.mainloop
    
main_screen()
