#import all the related packages
import requests
import os
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from requests.exceptions import HTTPError

import io
import PIL
from PIL import Image

# Function 1: get the basic info of a movie by searching its title
def name_get(movie=''):
  """
  A function to get the basic information and ratings of a movie by search its title. The search is keyword fuzzy search supported by the API url.

  Parameters
  ----------
  movie: a string. Enter the movie name you want to search. e.g. The Shawshank Redemption

  Returns
  -------
  A dataframe including all the related movies and their basic info.
  """
  api_url = 'https://api.wmdb.tv/api/v1/movie/search'
  params = {'q': movie, 'limit':50, 'skip': 0, 'lang':'En'}
  import requests
  r_title = requests.get(api_url, params=params)

  if r_title.status_code ==200:
    Title_json = r_title.json()
    df_t1 = pd.json_normalize(Title_json)
    df_t2 = pd.json_normalize(Title_json, "data")
    df_t = pd.concat([df_t2, df_t1.iloc[:,4:18]], axis=1)

    return df_t[['originalName','genre','year','description','imdbRating','rottenRating','doubanRating']]

  else:
    print(f'Request error code:400')

#Function 2: get the poster image of a movie

def poster_get(movie=''):
  """
  A function to get the poster image of a movie by search its title. The search is keyword fuzzy search supported by the API url.

  Parameters
  ----------
  movie: a string. Enter the movie name you want to search. e.g. The Shawshank Redemption

  Returns
  -------
  Open an image of the movie's poster.
  """
  api_url = 'https://api.wmdb.tv/api/v1/movie/search'
  params = {'q': movie, 'limit':50, 'skip': 0, 'lang':'En'}

  r_title = requests.get(api_url, params=params)

  if r_title.status_code ==200:
    Title_json = r_title.json()
    df_t1 = pd.json_normalize(Title_json)
    df_t2 = pd.json_normalize(Title_json, "data")
    df_t = pd.concat([df_t2, df_t1.iloc[:,4:18]], axis=1)

    poster = df_t[['name','poster']]
    p_url = poster[poster['name'] == movie]
    if p_url['poster'].values.size != 0:
        url = p_url['poster'].values[0]
        response = requests.get(url)
        image_bytes = io.BytesIO(response.content)
        img = PIL.Image.open(image_bytes)
        return img
    else:
        raise AssertionError(f'No such movies found. You may type the wrong title.')

  else:
    print(f'Request error code:400')

#Function 3: get the top N movies in the imdb TOP250 dataset and show their basic information.
def movie_data(top=1):
  """
  A function to get the top N movies among the imdb TOP250 movies.

  Parameters
  ----------
  top : an integer, number of the top movies you want to get. Default=1

  Returns
  -------
  A data frame showing the basic information of the movies.
  """
  try:
    r = requests.get('https://api.wmdb.tv/api/v1/top?type=Imdb&skip=0&limit=250&lang=En')
    r.raise_for_status()

  except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
  except Exception as err:
    print(f'Other error occurred: {err}')
  else:
    print('Data-aquisation success!')
    Movie_json = r.json()
    df1 = pd.json_normalize(Movie_json)
    df2 = pd.json_normalize(Movie_json, "data")
    df = pd.concat([df2, df1.iloc[:,5:18]], axis=1)

    df_top = df[["name","genre","language","year","imdbRating"]].sort_values(["imdbRating"], ascending=False)
    df_top = df_top.iloc[0:top,:].reset_index(drop=True)
    return df_top

#Function 4: get the year range of the TOP250 imdb movies
def y_range():
  """
  A function wich could show you the year range of the top 250 imdb movies and the latest and the earliest release years.

  Parameters
  ----------
  No parameters required.

  Returns
  -------
  The latest release year, the earliest release year and the year range of TOP250 movies.
  """
  r = requests.get('https://api.wmdb.tv/api/v1/top?type=Imdb&skip=0&limit=250&lang=En')
  if r.status_code == 200:
    Movie_json = r.json()
    df1 = pd.json_normalize(Movie_json)
    df2 = pd.json_normalize(Movie_json, "data")
    df = pd.concat([df2, df1.iloc[:,5:18]], axis=1)

    y_latest = df["year"].max()
    y_earliest = df["year"].min()
    y_range = int(y_latest)-int(y_earliest)

    print(f'The latest release year of TOP250 movies: {y_latest}')
    print(f'The earliest release year of TOP250 movies: {y_earliest}')

    return print(f'The range of release year of TOP250 movies: {y_range}')
  else:
    print('Request error code: 400')

#Function 5: search the movies by a specific year in TOP250 list
def get_movies(year):
  """
  A function to get the movies produced in a specific year in TOP250 list

  Parameters
  ----------
  year: an integer e.g. 1921

  Returns
  -------
  A data frame showing the basic information and ratings of the movies. If no such movies are produced in the specific year, return the related message.
  """
  r = requests.get('https://api.wmdb.tv/api/v1/top?type=Imdb&skip=0&limit=250&lang=En')
  if r.status_code == 200:
    Movie_json = r.json()
    df1 = pd.json_normalize(Movie_json)
    df2 = pd.json_normalize(Movie_json, "data")
    df = pd.concat([df2, df1.iloc[:,5:18]], axis=1)

    y = np.sort(df['year'].unique()).tolist() #available years in the TOP250
    if str(year) not in y:
      raise AssertionError(f'Year not available in the TOP250 movies')
    else:
      movie_y = df[df['year'] == str(year)]
      return movie_y[["name","genre","language","year","country","imdbRating","rottenRating", "doubanRating"]]
  else:
    print(f'Request error code:400')
