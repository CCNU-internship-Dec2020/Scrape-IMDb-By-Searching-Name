# Scrape-IMDb-By-Searching-Name
Movie details scraping in Python3.

```
.
├── LICENSE
├── README.md
├── Scrape_IMDb.txt                Full scrape data writen in line.
├── add_pic_clarity.py      5-     Improve the sharpness of pictures.
├── content.py              3-     The main scrape script.
├── data.txt                       The final data in a list of lists.
├── excess_log.txt                 Data of getting the title_id in IMDb in line.
├── find_lost.py            4-     A script of finding which movie do not have the summary or poster.
├── get_ttid.py             2-     Use the given movie name to search movie_id in IMDb website.
├── get_url.py              1-     A script of encodeURIComponent() like function.
├── lost_id_1.txt                  Result of find_lost.py
├── movie_id_sort.py        6-     A script of mixing data and sorting.
├── movies.dat                     The original data.
├── searchMovUrlList.txt           The encode URLs.
├── searchMovUrlList_byLine.txt    The encode URLs in line.
└── table.html                     bs4
```
## [New update]: Begin from step three

## First step: Get the searching URL
We are given the [data set](https://github.com/CCNU-internship-Dec2020/Scrape-IMDb-By-Searching-Name/blob/main/movies.dat) which contains the movie names. In the first step we should use the name to search the matching movies preview in the IMDb website.
```
python3 get_url.py
```
This script convert the string of movie name and its release year to IMDb's searching format in order to make the result more correct, which means the first searching result in list is what we want.

## Second step: Get the movie's title id in IMDb
Use the 'hand-made' URL to search movies in the website. Extract the `<a> tag` which contains a relative file path to find the sole movie-id.
```
python3 get_ttid.py
```
We save the data in format to [excess_log.txt](https://github.com/CCNU-internship-Dec2020/Scrape-IMDb-By-Searching-Name/blob/main/excess_log.txt)

## Step three: Locate the Summary and Poster
Go to the movies detail website to scrape the summary and poster of the film. Then store the data to [Scrape_IMDb.txt](https://github.com/CCNU-internship-Dec2020/Scrape-IMDb-By-Searching-Name/blob/main/Scrape_IMDb.txt)
```
python3 content.py
```
They provide picture host for us.

## Step four: Find the lost Summary and Poster
In step three, several movie details like poster can be scraped unsuccessfully because of the ttid is not correct, or other reasons. What we should do is compare the movie_id of `excess_log.txt` and `Scrape_IMDb.txt`, output the details to `lost_id_1.txt` in format like `excess_log.txt`.
```
python3 find_lost.py
```
Then change the ttid manually, and use the new output file repeat Step three and Step four!

## Step five: Improve the sharpness
The poster is a preview and not clearly enough. Use the script to improve the sharpness of images by modify the picture's URL.
```
python3 add_pic_clarity.py
```

## The final step: Sort data
The step four would add many new data which are unordered. In this step, sorting the data and get them in a list of lists.
```
python3 movie_id_sort.py
```

Well done! Enjoy our script!