import requests
import os
import time
from prometheus_client import start_http_server, Gauge, Info

TOKEN = os.environ["AQICN_TOKEN"]
CITIES = os.environ["CITIES"].lower().split(",")

aqi = Gauge('aqi_external', 'AQI from waqi', ['name'])
pm25 = Gauge('pm25_external', 'PM25 from waqi', ['name'])
temp = Gauge('temp_external', 'Temperature from waqi', ['name'])
humidity = Gauge('humidity_external', 'humidity from waqi', ['name'])

def exit_with_error(error):
    sys.exit(error)


if __name__ == '__main__':
    port_number = 8000


def metrics_by_city(city, token):
    response = requests.get('https://api.waqi.info/feed/%s/?token=%s' % (city, token))

    js_data = response.json()["data"]
    if isinstance(js_data, str):
        print("Error with %s: %s" % (city, js_data["data"]))
        return
    aqi.labels(city).set(js_data["aqi"])
    pm25.labels(city).set(js_data["iaqi"]["pm25"]["v"])
    temp.labels(city).set(js_data["iaqi"]["t"]["v"])
    humidity.labels(city).set(js_data["iaqi"]["h"]["v"])


if __name__ == '__main__':
    port_number = 8000
    time_scrap = 60 * 60
    start_http_server(port_number)

    while True:
        try:
            for city in CITIES:
                metrics_by_city(city, TOKEN)
        except OSError as error:
            pass
        time.sleep(time_scrap)

