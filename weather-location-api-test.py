import requests, json

my_API_key = "" 

# url = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'

def get_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_API_key}')
    return response.json()

def main():
    city = input("Enter city: ")
    details = get_weather(city)['main']
    print(details)   
    

if __name__ == "__main__":
    main()
