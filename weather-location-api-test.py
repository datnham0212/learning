import requests, json

my_API_key = "" 

# url = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'

def get_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_API_key}')
    return response.json()

def main():
    city = input("Enter city: ")
    details = get_weather(city)['main']

    # Print table header
    print("Weather Details:")
    print("-----------------")
    print("City:", details['name'])
    print("Country:", details['sys']['country'])
    temperature = details['main']['temp'] - 273.15
    feels_like = details['main']['feels_like'] - 273.15
    print(f"Temperature: {temperature:.2f}", "°C")
    print(f"Feels Like: {feels_like:.2f}", "°C")
    print("Humidity:", details['main']['humidity'], "%")
    print("Description:", details['weather'][0]['description'])
    print("Wind Speed:", details['wind']['speed'], "m/s")
    print("Cloudiness:", details['clouds']['all'], "%")
    print("Sunrise:", details['sys']['sunrise'])
    print("Sunset:", details['sys']['sunset'])
    print("-----------------")
    

if __name__ == "__main__":
    main()
