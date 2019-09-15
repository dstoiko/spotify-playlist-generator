import os
from dotenv import load_dotenv
from .radiox import RadioX
from .triplej import TripleJ


def scrape():
    '''
    Scrape all playlists and combine into one big playlist array
    '''
    load_dotenv(verbose=True)
    playlist = []
    playlist += RadioX.scrape(os.getenv('RADIOX_URL'))
    playlist += TripleJ.scrape(os.getenv('TRIPLEJ_URL'))
    print(playlist)
