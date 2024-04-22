# Import necessary modules
import requests
import tkinter as tk
from tkinter import messagebox

# function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    api_key = '5071e6e27a20771f1ae38649a39d8701'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    # check if the response is successful
    if weather_data['cod'] == 200:

        # update labels with weather information
        city_label.config(text=weather_data['name'])
        temp_label.config(text=f"{weather_data['main']['temp']}°C")
        weather_label.config(text=weather_data['weather'][0]['description'])

        # get weather icon and display it
        icon_id = weather_data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
        icon_image = tk.PhotoImage(data=requests.get(icon_url).content)
        weather_icon.config(image=icon_image)
        weather_icon.image = icon_image
    else:

        # show error message if city is not found
        messagebox.showerror('Error', f"Cannot find weather data for {city}")

# function to handle search button click event
def search():
    city = city_entry.get()
    get_weather(city)

# function to handle placeholder text in city entry
def on_entry_click(event):
    if city_entry.get() == 'Enter city name...':
        city_entry.delete(0, "end") # delete placeholder text
        city_entry.insert(0, '') # insert blank for user input
        city_entry.config(fg='black')

# the main application window
root = tk.Tk()
root.title("Weather App")

# labels to display weather information
city_label = tk.Label(root, font=('Helvetica', 20))
city_label.pack()

temp_label = tk.Label(root, font=('Helvetica', 48, 'bold'))
temp_label.pack()

weather_label = tk.Label(root, font=('Helvetica', 16))
weather_label.pack()

weather_icon = tk.Label(root)
weather_icon.pack()

# entry field for city input
city_entry = tk.Entry(root, font=('Helvetica', 16))
city_entry.insert(0, 'Enter city name...') # placeholder text
city_entry.bind('<FocusIn>', on_entry_click) # click event to function
city_entry.pack(pady=10)

# search button
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

# to run the main loop or the application
root.mainloop()
