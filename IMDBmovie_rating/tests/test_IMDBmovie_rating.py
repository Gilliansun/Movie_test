from IMDBmovie_rating import IMDBmovie_rating
#import all the related packages
import requests
import pytest
import os
import pandas as pd
import numpy as np
import json
from requests.exceptions import HTTPError

#check Function 2 if AssertionError is raised if movie available if input
def test_poster_get():
    with pytest.raises(AssertionError):
        IMDBmovie_rating.poster_get('The Shwsshank Redemption')

#check Function 5 if AssertionError is raised if year unavailable is input
def test_get_movies():
    with pytest.raises(AssertionError):
        IMDBmovie_rating.get_movies(1937)
