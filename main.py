import re
import os
import requests
import  tarfile
from logging import Logger


LOG = Logger(__name__)

def download_file(url):
    """
        Function to download a file and return a tuple with file name and file content bytes.
    """
    resp = requests.get(url)
    content_disposition = resp.headers['content-disposition']
    file_name = re.findall("filename=(.+)", content_disposition)
    return file_name[0], resp.content


def unpack_file(file_name):
    """
        Function to unpack and delete a tar.gz file.
    """
    LOG.warning(f'Unpacking {file}...')
    tar = tarfile.open(file_name, 'r:gz')
    LOG.warning(f'{file} Unpacked successfuly!')
    LOG.warning(f'Removing {file}...')
    tar.extractall('GEO_IP')
    os.remove(file_name)
    LOG.warning(f'{file} removed successfuly!')

def write_file(file_name, file_content):
    open(file_name, 'wb').write(file_content)
    unpack_file(file_name)
    

if __name__ == '__main__':
    file = download_file('https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz')
    write_file(*file)
    LOG.warning(file[0])

        