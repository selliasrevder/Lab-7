import requests

#1

API_KEY = '11b4ba53fdf4dd1fe3e24d9449758f72'

city_name = 'Москва'

base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ru'

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    
    print(f'Погода в городе {city_name}:')
    print(f'Температура: {temperature}°C')
    print(f'Состояние: {weather}')
    print(f'Влажность: {humidity}%')
    print(f'Давление: {pressure} hPa')
else:
    print(f'Ошибка при запросе данных: {response.status_code}')

print('\n')

#2

import json

url_iss_location = "http://api.open-notify.org/iss-now.json"

url_astros = "http://api.open-notify.org/astros.json"

def get_iss_location():
    response = requests.get(url_iss_location)
    if response.status_code == 200:
        data = response.json()
        print("Текущее местоположение МКС:")
        print(f"Широта: {data['iss_position']['latitude']}")
        print(f"Долгота: {data['iss_position']['longitude']}")
        print(f"Время: {data['timestamp']}")
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")

def get_astros():
    response = requests.get(url_astros)
    if response.status_code == 200:
        data = response.json()
        print("\nЛюди в космосе:")
        print(f"Количество: {data['number']}")
        print("Имена:")
        for person in data['people']:
            print(f"- {person['name']} (на борту: {person['craft']})")
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")

if __name__ == "__main__":
    get_iss_location()
    get_astros()

#additional

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

def fetch_fox_image():
    response = requests.get("https://randomfox.ca/floof/")
    if response.status_code == 200:
        data = response.json()
        image_url = data['image']
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_data = image_response.content
            return image_data
    return None

def update_image():
    image_data = fetch_fox_image()
    if image_data:
        image = Image.open(BytesIO(image_data))
        image = image.resize((400, 400), Image.Resampling.LANCZOS)  
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo 

root = tk.Tk()
root.title("Генератор картинок с лисами")
root.geometry("450x500")

label = ttk.Label(root)
label.pack(pady=10)

button = ttk.Button(root, text="Новая лиса", command=update_image)
button.pack(pady=10)

update_image()

root.mainloop()
