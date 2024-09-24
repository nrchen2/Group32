import requests
import config

def get_walk_time(origin, destination, api_key):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&mode=walking&key={api_key}"
    response = requests.get(url).json()
    if response["status"] == "OK":
        #print(response)
        return response["rows"][0]["elements"][0]["duration"]["text"]
    else:
        return "Error"

if __name__ == "__main__":
    print(get_walk_time("Illini Union", "Grainger Library", config.api_key))

#Should work now