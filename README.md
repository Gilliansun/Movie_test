# MovieRatingComparison_ChinaWestern

This package provides five interesting and useful functions that let you search movies and see their ratings on IMDb, Rotten Tomatoes, and Douban websites. You could also get the poster of a specific movie.

## Introduction
As a movie lover from China, when I want to watch a movie, I usually search the IMDb website and Rotten Tomatoes to see the ratings and reviews of audience. China also has a website which could provide the movie ratings and it is called Douban.
I keep the habbit of checking the three webistes, IMDb, Rotten Tomatoes, and Douban to searh for movies' basic info, ratings and reviews.
This API client provides the users a simple way to search a specific movie and see its ratings, basic info and get its poster image.

## How to use
### Function 1: `IMDBmovie_rating.name_get(movie='')`
* Users can use this function to get the basic information and IMDb, rotten tomatoes and douban ratings of a movie by search its title. The search is keyword fuzzy search.
* Parameters: movie: a string. Users need to enter the movie name they want to search. e.g. The Shawshank Redemption
* Returns: A dataframe including all the related movies and their basic info.

### Function 2: `IMDBmovie_rating.poster_get(movie='')`
* A function to get the poster image of a movie by search its title. The search is keyword fuzzy search
* Parameters: movie: a string. Enter the movie name you want to search. e.g. The Shawshank Redemption
* Returns: the image of the movie's poster.

### Funciton 3: `IMDBmovie_rating.movie_data()`
* A function to get the top N movies among the imdb TOP250 movies.
* Parameters: top: an integer, number of the top movies you want to get. Default =1
* Returns: A dataframe showing the basic information of the movies.

### Function 4: `IMDBmovie_rating.y_range()`
* A function wich could show you the year range of the top 250 imdb movies and the latest and the earliest release years. You do not need to enter any parameters.
* Returns: The latest release year, the earliest release year and the year range of TOP250 movies.

### Funciton 5: `IMDBmovie_rating.get_movies(year)`
* A function to get the movies produced in a specific year in TOP250 list.
* Parameters: year: an integer. e.g. 1921
* Returns: A data frame showing the basic information and ratings of the movies. If no such movies are produced in the specific year, return the related message.

## API Source
Thanks a lot to the API source and here is the github page: https://github.com/iiiiiii1/douban-imdb-api
(Note: The github page is in Chinese.)
