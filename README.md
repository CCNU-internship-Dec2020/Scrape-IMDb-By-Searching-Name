# Scrape-IMDb-By-Searching-Name
Movie details scraping in Python3.

## First step: Get the searching URL
We are given the [data set](https://github.com/CCNU-internship-Dec2020/Scrape-IMDb-By-Searching-Name/blob/main/movies.dat) which contains the movie names. In the first step we should use the name to search the matching movies preview in the IMDb website.
```
python3 get_url.py
```
This script convert the string of movie name and its release year to IMDb's searching format in order to make the result more correct, which means the first searching result in list is what we want.

## Second step: Get the movie's title id in IMDb
Use the 'hand-made' URL to search movies in the website. Extract the <a> tag which contains a relative file path to find the sole movie-id.
```
python3 get_ttid.py
```
We save the data in format to [excess_log.txt](https://github.com/CCNU-internship-Dec2020/Scrape-IMDb-By-Searching-Name/blob/main/excess_log.txt)

## The Last step: Locate the Summary and Poster
Go to the movies detail website to scrape the summary and poster of the film. Then store the data to [Scrape_IMDb.txt](https://github.com/CCNU-internship-Dec2020/Scrape-IMDb-By-Searching-Name/blob/main/Scrape_IMDb.txt)
```
python3 content.py
```
They provide picture host for us. Enjoy our script!