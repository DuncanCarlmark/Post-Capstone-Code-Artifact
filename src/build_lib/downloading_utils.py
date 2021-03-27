import os
import pandas as pd
import requests

# Paths for storing data
DATA_DIR = './data'
# Data subdirectories
DATA_DIR_RAW = os.path.join(DATA_DIR, 'raw')
DATA_DIR_CLEAN = os.path.join(DATA_DIR, 'clean')
DATA_DIR_RECOMMENDATIONS = os.path.join(DATA_DIR, 'recommendations')

# last.fm files 
USER_PROFILE_PATH_RAW = os.path.join(DATA_DIR_RAW, 'user_profile.csv')
USER_ARTIST_PATH_RAW = os.path.join(DATA_DIR_RAW, 'user_artist.csv')

# billboard files
BILLBOARD_SONGS_PATH_RAW = os.path.join(DATA_DIR_RAW, 'billboard_songs.csv')
BILLBOARD_FEATURES_PATH_RAW = os.path.join(DATA_DIR_RAW, 'billboard_features.csv')

# last.fm files
USER_PROFILE_PATH_CLEAN = os.path.join(DATA_DIR_CLEAN, 'user_profile.csv')
USER_ARTIST_PATH_CLEAN = os.path.join(DATA_DIR_CLEAN, 'user_artist.csv')

# billboard files
BILLBOARD_SONGS_PATH_CLEAN = os.path.join(DATA_DIR_CLEAN, 'billboard_songs.csv')
BILLBOARD_FEATURES_PATH_CLEAN = os.path.join(DATA_DIR_CLEAN, 'billboard_features.csv')




def download_all_data(user_profile_url, user_artist_url, billboard_songs_url, billboard_features_url):
    """
    Downloads all required data from a public Amazon S3 bucket and saves it to a raw data
    directory.

    PARAMS:
        user_profile_url (str) - S3 url for user_profile.csv
        user_artist_url (str) - S3 url for user_artist.csv
        billboard_songs (str) - S3 url for billboard_songs.csv
        billboard_features (str) - S3 url for billboard_features.csv

    RETURNS:
        None
    """

    # LAST.FM files
    print('Downloading user_profile')
    r = requests.get(user_profile_url)
    open(USER_PROFILE_PATH_RAW, 'wb').write(r.content)

    print('Downloading user_artist')
    r = requests.get(user_artist_url)
    open(USER_ARTIST_PATH_RAW, 'wb').write(r.content)
    
    
    # Billboard files
    print('Downloading billboard_songs')
    r = requests.get(billboard_songs_url)
    open(BILLBOARD_SONGS_PATH_RAW, 'wb').write(r.content)

    print('Downloading billboard_features')
    r = requests.get(billboard_features_url)
    open(BILLBOARD_FEATURES_PATH_RAW, 'wb').write(r.content)
    print('Billboard data downloaded')
