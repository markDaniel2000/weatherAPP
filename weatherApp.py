from tkinter import *
from PIL import Image,ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz




main=Tk()
main.title("Weather App")
main.geometry("796x497")
main.resizable(0, 0)

#functions
def getWeather():


    city = txtField.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude, lat=location.latitude)

    #location and time
    home=pytz.timezone(result)
    localTime=datetime.now(home)
    currentTime=localTime.strftime("%I:%M %p")

    #weather information
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ac8ab8563d1905e5ec3a289d6319687c"
    json_data=requests.get(api).json()
    condit=json_data['weather'][0]['main']
    descipt=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    press=json_data['main']['pressure']
    humid=json_data['main']['humidity']
    w=json_data['wind']['speed']

    temperature.config(text=(temp,"°"))
    condition.config(text=(condit,"|",temp,"°"))
    wind.config(text=w)
    humidity.config(text=humid)
    description.config(text=descipt)
    pressure.config(text=press)

    time.config(text=currentTime)
    place.config(text=result)


#bg
bg_image=Image.open("weather_images/Untitled.png")
resized_image= bg_image.resize((794,497), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
bgLabel=Label(main, image=new_image)
bgLabel.pack()


#search
txtField=Entry(main, justify="center", width=17, font=("arial", 30, "bold"), bg="#D9D9D9",border=0,fg="black")
txtField.place(x=210, y=225)
txtField.focus()

searchIcon=PhotoImage(file="weather_images/searching.png")

search=Button(main,image=searchIcon,padx=25, pady=25,borderwidth=0,cursor="hand2",bg="#B0DDFC", command=getWeather)
search.place(x=610, y=210)

#labels
wind=Label(main, text="---", fg="black", font=("Arial",24,"bold"), bg="#8FB5FD")
wind.place(x=80,y=89)

humidity=Label(main, text="---", fg="black", font=("Arial",24,"bold"), bg="#8FB5FD")
humidity.place(x=260,y=89)

description=Label(main, text="---", fg="black", font=("Arial",15,"bold"), bg="#8FB5FD")
description.place(x=420,y=89)

pressure=Label(main, text="---", fg="black", font=("Arial",24,"bold"), bg="#8FB5FD")
pressure.place(x=630,y=89)

temperature=Label(main, text="", fg="black", font=("Arial",40,"bold"), bg="#8FB5FD")
temperature.place(x=340,y=330)

condition=Label(main, text=" ", fg="black", font=("Arial",17,"bold"), bg="#8FB5FD")
condition.place(x=327,y=425)

time=Label(main, text=" ", fg="black", font=("Arial",16,"bold"), bg="#D9D9D9")
time.place(x=77,y=230)

place=Label(main, text="   ", fg="black", font=("Arial",19,"bold"), bg="#8FB5FD")
place.place(x=330,y=148)







main.mainloop()