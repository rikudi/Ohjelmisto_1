import requests

def get_weather():
    query = input("Anna paikkakunta: ")
    api_key = "1ac3ee34109fe1df3a70367333bdb3f5"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}"

    res = requests.get(base_url)
    data = res.json()
    temp = data["weather"][0]["main"]
    kelvin = data["main"]["temp"]
    celsius = round(kelvin - 273.15, 1)
    return temp, celsius

print(get_weather())