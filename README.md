# Scrape-IMDb-By-Searching-Name
Movie details scraping in Python3.

### First step: get the searching URL
We are given the (data set)[movies.dat] which contains the movie names. In the first step we should use the name to search the matching movies preview in the IMDb website.
```
python3 get_url.py
```
This script convert the string of movie name and its release year to IMDb's searching format.

### Second step: get the movie's title id in IMDb
### The Last step: Locate the Summary and Poster
