import logging
import folium
import config_resolver
import google_api_gateway

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config_resolver = config_resolver.ConfigResolver(logger)
config = config_resolver.load_config()

google_api_gateway = google_api_gateway.GoogleAPIGateway(logger, config)

address = input("Enter the map address:")

main_address = google_api_gateway.get_latitude_longitude(address)

if main_address is None:
    logger.error('Invalid address...')
    exit()

map = folium.Map(location=[main_address['latitude'], main_address['longitude']], zoom_start=13)

mark_address = ""
while True:
    mark_address = input("Enter the mark address or ':q' to stop: ")
    if mark_address == ":q":
        break

    mark_geocode = google_api_gateway.get_latitude_longitude(mark_address)

    if mark_geocode is not None:
        folium.Marker(location=[mark_geocode['latitude'],mark_geocode['longitude']], popup = "Pin", icon=folium.Icon(color = 'gray')).add_to(map)

map.save("map.html")