import pandas as pd

#---------------------------------------------------- CLEANING BILLBOARD DATA ----------------------------------------------------

# Clean billboard songs

def clean_billboard_songs(df):
    '''
    Cleans billboard_songs by

    1. Reordering and dropping unnecessary columns
    2. Dropping songs from 2020
    3. Dropping songs that could not be converted to datetime
    4. Dropping songs that re-enter the charts more than 3 times to limit the amount of
        Christmas/holiday songs that appear in the chart data

    PARAMS:
        df - pandas dataframe of billboard_songs.csv
    RETURNS:
        The cleaned pandas dataframe containing billboard_songs.csv 
    '''

    # Drop irrelevant column and reorder columns
    clean_col_order = ['SongID', 
                       'Song', 
                       'Performer', 
                       'WeekID', 
                       'Week Position', 
                       'Instance', 
                       'Previous Week Position', 
                       'Peak Position', 
                       'Weeks on Chart']
    df = df.drop(['url'], axis=1)[clean_col_order]
    
    # Drop Songs from 2020
    # Dropping instances of NA values is the same as dropping songs from 2020 since
    # 2020 songs have no chart info
    df = df[~df['Instance'].isnull()]
    
    # Convert WeekID to datetime
    df['WeekID'] = pd.to_datetime(df['WeekID'], format = '%m/%d/%Y').reset_index(drop=True)
    
    # Drop any values that could not be converted to datetime
    df = df[~df['WeekID'].isnull()]
    
    # CHRISTMAS CLEANING
    songs_to_drop = df[df['Instance'] > 3]['SongID'].unique()
    df = df[~df['SongID'].isin(songs_to_drop)]

    return df.reset_index(drop=True)

#---------------------------------------------------- CLEANING LAST.FM DATA ----------------------------------------------------

def clean_lastfm(user_profile_df, user_artist_df):
    
    # Remove observations with null values
    user_profile_df = user_profile_df[['user_id', 'age', 'country']].dropna().reset_index(drop=True)
    # Select rows with users from US-recommendation task targeted to US users
    user_profile_df = user_profile_df[user_profile_df['country'] == 'United States']
    cleaned_user_profile_df = user_profile_df[user_profile_df['age'] > 0]
    

    # Drop rows with missing values
    user_artist_df = user_artist_df[['user_id', 'artist_id', 'artist_name', 'plays']].dropna().reset_index(drop=True)
    # Extract listening histories from US users 
    cleaned_user_artist_df = extract_histories(user_artist_df, cleaned_user_profile_df)

    return cleaned_user_profile_df, cleaned_user_artist_df

# Given a set of users, pull their listening histories
def extract_histories(user_artist_df, user_profile_df):
    # Extract listening histories from users selected
    extracted_history = user_artist_df[user_artist_df['user_id'].isin(user_profile_df['user_id'])]
    return extracted_history