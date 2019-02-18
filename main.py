import re
import os
import requests
import wget
import  tarfile
from logging import Logger


LOG = Logger(__name__)

def download_file(url):
    LOG.warning(f'Downloading file from {url}...')
    file_name = wget.download(url)
    LOG.warning(f'{file_name} downloaded successfuly!')
    return file_name


def unpack_file(file_name, destiny):
    """
        Function to unpack and delete a tar.gz file.
    """

    geo_file_path = file_name.split('.')[0]
    geo_file_name = file_name.split('_')[0]
    
    LOG.warning(f'Unpacking {file_name}...')
    tar = tarfile.open(file_name, 'r:gz')
    file = tar.getmember(f'{geo_file_path}/{geo_file_name}.mmdb')
    file.name =  os.path.basename(file.name)
    tar.extract(file, destiny)
    LOG.warning(f'{file_name} Unpacked successfuly!')
    
    LOG.warning(f'Removing {file_name}...')
    os.remove(file_name)
    LOG.warning(f'{file_name} removed successfuly!')

if __name__ == '__main__':
    # Citys file
    file_name = download_file('https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz')
    unpack_file(file_name, 'GEO_IP')

    # Country file
    file_name = download_file('https://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz')
    unpack_file(file_name, 'GEO_IP')
    
    