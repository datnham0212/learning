import requests

api_key = ''

user_input = input('What to look up? ');

response = requests.get(f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={user_input}')

print(response.status_code)
print(response.json()['foods'][0])
