import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
	"x-rapidapi-key": "",
	"x-rapidapi-host": "google-translate1.p.rapidapi.com",
	"Accept-Encoding": "application/gzip"
}

response = requests.get(url, headers=headers)

print(response.text)
