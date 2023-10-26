from tkinter import *
from tkinter import ttk
import requests
import json
import tkinter

root = Tk()
root.title("Прогноз погоды")

root.geometry("500x500")
root.resizable(width=500,height=500)
root["bg"] = "green2"

def city_(event):
    city = ent.get()
    import json
    url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

    weather_data = requests.get(url).json()
    weather_data_structure = json.dumps(weather_data, indent=2)

    temperature = weather_data['main']['temp']
    temperature_feels = weather_data['main']['feels_like']
    wind_speed = weather_data['wind']['speed']
    label = tkinter.Label(text='Сейчас в городе '+ city + ' ' + str(temperature)+ '°C', fg='Black', bg="green2")
    label.pack() 
    label = tkinter.Label(text='Ощущается как '+ str(temperature_feels)+ '°C', fg='Black', bg="green2")
    label.pack()
    label = tkinter.Label(text='Скорость ветра '+ str(wind_speed)+ 'м/с', fg='Black', bg="green2")
    label.pack()

    
city = 'Москва'

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = requests.get(url).json()

temperature = weather_data['main']['temp']
temperature_feels = weather_data['main']['feels_like']
label = tkinter.Label(text='Сейчас в Столице '+ str(temperature)+ '°C', fg='Black', bg="green2")
label.pack()
label = tkinter.Label(text='Ощущается как '+ str(temperature_feels)+ '°C', fg='Black', bg="green2")
label.pack()
print('Сейчас в Столице', str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')

ent = Entry(width=False)
ent.pack()
but = Button(text="Загрузить")
but.bind('<Button-1>',city_)
but.pack()
