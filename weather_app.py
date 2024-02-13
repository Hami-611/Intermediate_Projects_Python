from tkinter import *
from tkinter import messagebox
import requests

API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def tell_weather():
    city_name = city_field.get()
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}"
    
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            temp_field.insert(15, f"{current_temperature} Kelvin")
            atm_field.insert(10, f"{current_pressure} hPa")
            humid_field.insert(15, f"{current_humidity} %")
            desc_field.insert(10, weather_description)

        else:
            messagebox.showerror("Error", "City Not Found \nPlease enter a valid city name")
            city_field.delete(0, END)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def clear_all():
    for entry in [city_field, temp_field, atm_field, humid_field, desc_field]:
        entry.delete(0, END)
    city_field.focus_set()

if __name__ == "__main__":
    root = Tk()
    root.title("Weather Application")
    root.configure(background="light blue")
    root.geometry("425x200")

    headlabel = Label(root, text="Weather Gui Application", fg='white', bg='Black', pady=10)
    headlabel.grid(row=0, column=0, columnspan=2)

    labels = ["City name:", "Temperature:", "Atm Pressure:", "Humidity:", "Description:"]
    for i, label_text in enumerate(labels, start=1):
        label = Label(root, text=label_text, fg='white', bg='dark gray')
        label.grid(row=i, column=0, sticky="E", pady=5)

    entries = [Entry(root) for _ in range(5)]
    for i, entry in enumerate(entries, start=1):
        entry.grid(row=i, column=1, ipadx="100", pady=5)

    button1 = Button(root, text="Submit", bg="pink", fg="black", command=tell_weather)
    button2 = Button(root, text="Clear", bg="pink", fg="black", command=clear_all)
    button1.grid(row=6, column=0, columnspan=2, pady=10)
    button2.grid(row=7, column=0, columnspan=2)

    root.mainloop()
