import requests

class GoogleAPIGateway:

    def __init__(self, logger, config):
        self.logger = logger
        self.config = config

    def get_latitude_longitude(self, address):
        url = self.config['url'].format(address, self.config['key'])
        self.logger.info('get_latitude_longitude URL: {}'.format(url))
        r = requests.get(url).json()

        if r['status'] == "ZERO_RESULTS":
            self.logger.info('Address not found...')
            return None

        latitude = r['results'][0]['geometry']['location']['lat']
        longitude = r['results'][0]['geometry']['location']['lng']

        latlng = {'latitude': latitude, 'longitude': longitude}

        return latlng