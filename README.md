# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Final Project: Python

## Project due date: 7/23/2020, at 5:00 PM EST

#### Your code must:
- Be properly indented  
- Be written with semantic Python code  
- Be commented for the other developers  

#### Standard Python project must:
- Be a working, interactive, Python application
- Must consist of GOOD OOP design
- Must at least 3 classes
- Must include public, private variables
- You may use files, or dictionaries as storage unit
- Must use any third party libraries such as request, PrettyTable, colored

#### Data Science project must:
- Be a working, interactive, Python application
- Must include grouping and data aggregation, and standard functions such as max, min, sum, and std etc
- Must have at least 2 .apply methods()
- Must have data visualization 

#### A Killer Project Proposal:
- What is your project is all about
- What are the three classes (or more), be ready to discuss it's functionality
- If it's Data Science project, you must provide the link to the data set prior to the project approval

#### For the project:
- Regadless of your what type of application you intend to build it must have a GitHub repo(USE YOUR PERSONAL GITHUB REPO)
- Data Science project must include the dataset in the GitHub repo along with the Jupyter Notebook
- DO NOT UPLOAD THE PROJECT FILES TO GITHUB, you must push your code the GitHub as you build the application

<hr>

## Project Schedule

This schedule will be used to keep track of your progress throughout the week and align with our expectations.  

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Priority Matrix / Timeline | Complete
|Day 3| Core Application | Incomplete
|Day 4| MVP & Bug Fixes | Incomplete
|Day 5| Final Touches | Incomplete
|Day 6| Deploy to GitHub | Incomplete

## Future web link!
[Yuri's Project]() 

## Project Description

Project DateOnCinema Data Analizes!

### MVP

First I'm creating a Python Data Analizes App inside Jupyter Notebook that will iterate over a dataset of movies released from the 90s until 2017. The app accepts two types of inputs to Analize Data. 
- The first option let the user to type a date of the calendar,e.g. 18/05/17, this input will return which movies were released at the same day¹ and a bar graphic highlighting how many movies per genre were released at that period.
- The second option let the user to type the name of the movie,e.g. Jaws, this input will check how many moviews with duplicated name we have and return to the user a Data Frame with 'name','date' and 'genre' as columns, and each of the movie options per 'row'. Beneath the Data Frame we will have the first option described earlier, so the user can type the date of one of the duplicated names if wanted. 

- I'll take in consideration the free version of the Dataset provided by IMDb. I may use the TMDB free API to create my own Dataset to compare with IMDb's one. And I may use another 2 datasets provided for free by kaggle and data.org.   

¹. I'm not sure if there will be enough movies released at the same day, because usualy the big companies try their best to not release their movies at the same week. Thus I may change the data analizes to months instead. 

### PostMVP

My PostMVP goal here is to create a webpage in which the user can: 
- click in any date from the calendar, and the page should give a graphic with the names of all movies released in that particular day, highlighting their genre, when they started the production, their budget, their first week profit, their all time profit and their rating scores.
- Or type any movie name into the search bar to get the same as above.
- The same as the two options above will also be available for games, and they will be showcased simutaneosly with the movies, but in a graphic of their own.
- All data related to money should be converted by one 'inflation' filter, taking in consideration the money inflationary nature and how many people existed in the world at that period of time. 
- The home page (if no date from calendar was selected or if no movie/game name was searched) should have a graphic comparing how much money was invested at NBA, FIFA, SuperBowl, Holly Wood, Game Business, Theaters and Netflix since 1980. Making a comparision between them.
- This page should grab data from IMDb, Rotten Tomatoes, TMDB and any other relevant webpage forums like Kaggle and Data.org.


## Functional Components

### 3 Classes!

- class DataBase():
    """
    It will have methods to request data from APIs, and methods to mix the requested data with each other in one single public object/DataSet
    """
- class Date(DataBase):
    """
    It will uses Pandas to iterate over the public object/DataSet using the 'date of release' as a filter( .query() ?). Maybe using the datatime library!
    """
- class Name(DataBase):
    """
    It will uses pandas to iterate over the public object/DataSet using the 'movie name' as a filter( .query() ?). If duplicated names exists, maybe it will return a data frame with the duplicated names and their release date, then it activates the 'class Date()' for the user to insert their chosen date!
    """

### Pseudo Code!
```python

class DataBase():
    public var/obj holding the DataSet
    public TMDb obj/dic
    public IMDb obj/dic
    public BOMDb obj/dic

    def __private_method_TMDb_cleaning():
        requests TMDb Api
        Pandas
        Data Frame
    
    def __private_method_IMDb_cleaning():
        Pandas
        Data Frame
    
    def __private_method_BOMDb_cleaning():
        Pandas
        Data Frame
    
    def __private_DataSet_generator():
        if Public TMDb, IMDb and BOMDb exists:
            if Day Date == Today:
                Pandas
                Data Set
        else:
            Call __private_method_TMDb_cleaning.requests()
            Pandas
            DataSet
    
class Date(DataBase):
    def __private_method_Pandas_filter():
        public_data_set
        Filter by day/month/year (maybe .query()?)
        default date = Jaws release date of 20 June 1975

    def method_date_input():
        datetime library
        try/except input
        call __private_method_Pandas_filter() with inputed date!
    
    def method_MatPlotLib():
        call method_date_input()
        display Pandas df['movies name']['date']
        displey genre graphic bar
        maybe display BoxOffice graphic bar, but no guarantee
    
class Name(DataBase):
    def __private_method_pandas_filter():
        public_data_set
        filter by 'movie name' (maybe .query())
        default = Get Out
    def method_name_input():
        try/except input():
        check if duplicate
        if yes: 
            output ['name']['date']
            call Date()
        else:
            call Date()
    
```

#### MVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Data Base Reaserch | H | 8hr | 24hr | -hr|
| Cleaning Data Tests | M | 8hr | -hr | -hr|
| MatPlotLib and other Libraries tests | L | 8H | -hr | -hr|
| class DataBase() | H | 6hr| -hr | -hr |
| class Date(DataBase) | H | 6hr | -hr | -hr|
| class Name(DataBase) | H | 6hrs| -hr | -hr |
| Total | H | 42hrs| -hr | -hr |

#### PostMVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Calendar Search & Search by Name (earch bar / Games) | M | 3hr | -hr | -hr|
| Money Convertion | L | 1hr | -hr | -hr|
| HTML | M | 4hr | -hr | -hr|
| CSS | M | 4hr | -hr | -hr|
| JavaScript | L | 4hr | -hr | -hr|
| Sports vs Holly Wood vs Game Business Home Page Graphic | L | 4hr | -hr | -hr|
| Total | H | 20hrs| -hrs | -hrs |

## Additional Libraries
 For now the used libraries are, but not limited to:
 - requests
 - datetime
 - pandas
 - matplotlib
 - tmdbsimple

## Code Snippet
Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```python
def foo(bar):
    pass
```

## Issues and Resolutions

 - For now my biggest problem is the availability of DataSets and what they include, e.g. 'year 2018' instead of the full date '01/01/2018'.

 - My second problem that I'm predicting is that some DataSets, like TMDb give more than one genre per movie, e.g. 'Matrix: Action, Science-Fiction'. And I'm not sure the most correct approach to deal with that when analizing the data and returning a minimalistic visual graphic of it.

#### SAMPLE.....
**ERROR**:  Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object

## How to submit project 01
- Use your own GitHub

In the comment section, you must add the following:
```text
* Comfortability [0 to 5]
* Completeness [0 to 5]
* What was a win?
* What was a challenge?
* Any other comments
```
