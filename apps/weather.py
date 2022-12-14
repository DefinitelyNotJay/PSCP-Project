import tkinter as tk
from tkinter import PhotoImage
import requests
import json
import datetime
from PIL import ImageTk, Image

def weather_widget():
    """ weather widgets """
    #Weather
    root = tk.Toplevel()
    root.title("Weather App") # Header
    root.geometry("650x410+320+100")
    root.resizable(False, False)
    icon = PhotoImage(file="images/icon/temperature-high.png")
    root.iconphoto(False, icon)
    image = PhotoImage(file='images/weather_img/Weather App.png')
    # photo1 = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=image, bg="#4a536b")
    label.grid(row=1)
    

    # Dates and time
    datetimenow = datetime.datetime.now()
    date = tk.Label(root, text=datetimenow.strftime('%A'), bg="#191845", fg = 'white', font="Friendly 10").place(x=150, y=350)
    month = tk.Label(root, text=datetimenow.strftime('%d %B %Y'), bg="#191845", fg="White", font="Friendly 10 bold").place(x=230, y=350)
    hour = tk.Label(root, text=datetimenow.strftime("%H:%M:%S"), bg='#191845', fg="White", font="Friendly 10 bold").place(x=150, y=370)
    
    # Entercity
    name_of_city = tk.StringVar()
    enter_city = tk.Entry(root, textvariable=name_of_city, width=20, font="Friendly 10")
    enter_city.place(x=270, y=20)

    def name_of_city():
        """ api_request """
        # Get current weather information
        api_request = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" +
            enter_city.get() + "&units=metric&appid=" + "f3256695f79844af82d1b56355815b9f")
        print(api_request)
        if(api_request == "<Response [401]>"): # if city not found
            city.configure(text="City Not Found")
            return
        print(api_request.content)
        api = json.loads(api_request.content)
        
        # Following details from current weather
        y = api['main']
        current_temprature = y['temp']
        humidity = y['humidity']
        tempmin = y['temp_min']
        tempmax = y['temp_max']
        pressure = y['pressure']
        p = api['weather']
        status = p[0]['description']
        z = api['sys']
        country = z['country']
        citi = api['name']
        q = api['wind']
        windspeed = q['speed']
        print(status)
        print(windspeed)

        # Add information into the screen
        temp.configure(text=current_temprature)
        humi.configure(text=humidity)
        min_temp.configure(text=tempmin)
        max_temp.configure(text=tempmax)
        pressure_val.configure(text=pressure)
        status_val.configure(text=status)
        country_val.configure(text=country)
        city.configure(text=citi)
        windspeed_val.configure(text=windspeed)
    
    # Enter Button
    img_button = PhotoImage(file='images/weather_img/Button.png')
    # img_button2 = PhotoImage(file='images/weather_img/Button2.png')
    city_nameButton = tk.Button(root, image=img_button, command=name_of_city, bg="#A00B88", relief=tk.SUNKEN, cursor='hand2', border=0, borderwidth = 0, activebackground='#A00B88')
    city_nameButton.place(x=465, y=14)

# -------------------------------------------------------------------------------------------
# Add text and info

    # Country and status
    city = tk.Label(root, text="", width=0, bg = 'white', font="Friendly 20 bold")
    city.place(x=245, y=74)

    country_val = tk.Label(root, text="", width=0, bg='white', font="Friendly 20 bold")
    country_val.place(x=365, y=74)

    status_val = tk.Label(root, text="", width=0, bg='white', font="Friendly 10")
    status_val.place(x=280, y=113)

    # Temperature
    temp = tk.Label(root, text="...", width=0, bg='white', font="Friendly 60", fg='black')
    temp.place(x=20, y=180)

    celsiustxt = tk.Label(root, text = "celsius", bg = 'white', font="Friendly 15").place(x=170, y=290)

    # Humidity
    humi = tk.Label(root, text="Humidity", width=0, bg='white', font="Friendly 15")
    humi.place(x=400, y=160)

    humi = tk.Label(root, text="", width=0, bg='white', font="Friendly 15 bold")
    humi.place(x=570, y=160)
    
    # Max Temperature
    maxi = tk.Label(root, text="Max Temperature", width=0, bg='white', font="Friendly 15 ")
    maxi.place(x=400, y=190)

    max_temp = tk.Label(root, text="", width=0, bg='white', font="Friendly 15 bold")
    max_temp.place(x=570, y=190)

    # Min Temperature
    mini = tk.Label(root, text="Min Temperature", width=0, bg='white', font="Friendly 15 ")
    mini.place(x=400, y=220)

    min_temp = tk.Label(root, text="", width=0, bg='white', font="Friendly 15 bold")
    min_temp.place(x=570, y=220)

    # Pressure
    pres = tk.Label(root, text="Pressure", width=0, bg='white', font="Friendly 15 ")
    pres.place(x=400, y=250)

    pressure_val = tk.Label(root, text="", width=0, bg='white', font="Friendly 15 bold")
    pressure_val.place(x=570, y=250)

    # Wind Speed
    wind = tk.Label(root, text="Wind Speed", width=0, bg='white', font="Friendly 15")
    wind.place(x=400, y=280)

    windspeed_val = tk.Label(root, width=0, bg='white', font="Friendly 15 bold")
    windspeed_val.place(x=570, y=280)

    root.mainloop()
