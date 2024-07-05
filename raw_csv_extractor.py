import requests, csv, sys

url = input()

response = requests.get(url)


if response.status_code == 200:
    with open('extracted.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        rows = response.text.split('\n')

        for row in rows:
            writer.writerow([row])
    print("File extracted successfully")

else:
    print("Error: ", response.status_code)
    sys.exit(1)