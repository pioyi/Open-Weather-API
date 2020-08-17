import requests, json

api_key = "ae0d881be2506b06acd3cb0c3f0f6439"

def get_input():
    city = input("Insert city: ")

    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(request_url)
    return json.loads(response.text) if response.ok else get_input()

def main():
    data = get_input()
    values_to_extract = {
        "weather main": {"Title": "State"},
        "weather description": {"Title": "Description"},
        "main temp": {"Title": "Temperature","Unit": " °C"},
        "wind speed": {"Title": "Wind Speed", "Unit": " meters/sec"},
        "main humidity": {"Title": "Humidity", "Unit": "%"},
        "sys country": {"Title": "Country"}
    }

    print("------------------\n")
    for i,v in values_to_extract.items():
        a,b = i.split()
        value = str(data[a][0][b] if a == 'weather' else data[a][b]).title()
        print("%-15s %s" % (v['Title'], value + v.get('Unit','')))

if __name__ == "__main__":
    print("\n⫸  Open Weather API\n")
    main()