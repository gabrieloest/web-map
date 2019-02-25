import logging
import folium
import requests
import config_resolver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config_resolver = config_resolver.ConfigResolver(logger)
config = config_resolver.load_config()

address = input("Enter the address:")

url = config['url'].format(address, config['key'])

r = requests.get(url).json()

latitude = r['results'][0]['geometry']['location']['lat']
longitude = r['results'][0]['geometry']['location']['lng']

map = folium.Map(location=[latitude,longitude], zoom_start=20)

folium.Marker(location=[latitude,longitude], popup = "Pin", icon=folium.Icon(color = 'gray')).add_to(map)

map.save("map.html")