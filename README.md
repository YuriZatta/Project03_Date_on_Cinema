# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Final Project: Python

## Future web link!
[Yuri's Project]() 

## Project Description

Project DateOnCinema Data Analizes!

### MVP

First I'm creating a Python Data Analizes App that will iterate over a dataset of movies released from the 90s until 2017. The app accepts two types of inputs to Analize Data. 
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

## DataSets

- TMDb: Api requests
- IMDb: https://datasets.imdbws.com/
- Kaggle: https://www.kaggle.com/eliasdabbas/boxofficemojo-alltime-domestic-data?select=boxoffice_august_2019.csv
- Kaggle: https://www.kaggle.com/igorkirko/wwwboxofficemojocom-movies-with-budget-listed?select=Mojo_budget_update.csv
- Data World: https://data.world/eliasdabbas/boxofficemojo-alltime-domestic-data

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
| Data Base Reaserch | H | 8hr | 24hr | 32hr|
| Cleaning Data Tests | M | 8hr | 8hr | 16hr|
| MatPlotLib and other Libraries tests | L | 8H | 9hr | 17hr|
| class DataBase() | H | 6hr| 4hr | 10hr |
| class Date(DataBase) | H | 6hr | 6hr | 12hr|
| class Name(DataBase) | H | 6hrs| 5hr | 11hr |
| Total | H | 42hrs| 56hr | 98hr |

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
It's not fancy, but I'm proud of comming up with this idea of how to deal with the users input. First it checks if the name inputed is in our DataBase, if it isn't it'll check if the user pressed enter by mistake, and finally, if the user haven't pressed enter without input, nor given any know name to us, we will active a method that will save the inputed name in another .csv file. This unlock a loop that will never let the code crash by wrong input! This will also allow us in the future to decide how to deal with half complete names inputs, and a class that requests only the missing names from APIs and lately add up to our data. It'll also help us in future updates to create a class that analizes which are the most searched names and have a grasp of what kind of titles interest people the most!

```python
    DataBase.BO_DS_cleaning(self)
    df = self.clean_DataSet 
    while True:
        try:
            name = input("\nWhat movie name do you want to analize?\nExample: Die Hard 2, or Get Out\n\tType one name here->")
            does_it_exist = df.isin([name]).any().any()
            if does_it_exist:
                self.input_name = name
                # Exit the loop if success!
                break
            elif name == '':
                name = None
                self.input_name = name
                # Exit the loop if success!
                break
            else:
                self.input_name = name
                self.__collecting_missing_names(self.input_name)
                print("\nMaybe this isn't in our database, try one movie released between the 90's and April 2020!\n")
        except ValueError: 
            print("\nSorry, I didn't understand that.\nCan you try again?")
            # let's try again without breaking the code...
            continue
```

## Issues and Resolutions

 - The idea is to collect a very specific date input from the user, Year-Month-Day, after that we can provide analizes from the very specific day, then for that specific month, and later for the year. To do so, one simple way would be to using slicing! It's easier to cut out what we have that it is to create from 0 when needed. But slicing Pandas DateTime (TimeStamp) objects / columns are not so easy. For almost every attempt I run into some type of wrong object type operation, fortunatly, the following code fixed the issue.

#### SAMPLE.....
**ERROR**:  TimeStamp does not support str slicing                                
**RESOLUTION**: 
```python
# Function that clean/slice '1990-05-25' into '1990-05'
self.clean_DataSet.iloc[0,0].strftime("%Y-%m")
def extract_month(month):
    month = month.strftime("%Y-%m-%d")
    clean_month = month[0:7]
    return clean_month

# Droping out NaN values to not run into an error!
df_plot_full = df_plot_full.dropna(subset=['date', 'genre_1'])

# Applying the above function to a whole column 'date' and creating a Series from it!
date_from_full = pd.Series(df_plot_full['date'].apply(extract_month))
date_from_cut = pd.Series(df_cut['date'].apply(extract_month))

# Inserting the series into our DFs as a new column Month!
df_plot_full.insert(0, "Month", date_from_full)
df_cut.insert(0, "Month", date_from_cut)

# Filtering out the main DF with the User DF to create a graphics with only that range of time!
cut_and_full_df = df_plot_full[df_plot_full.Month.isin(df_cut.Month)]
```

## Persistent Issues 

 - For now my biggest problem is the availability of DataSets and what they include, e.g. 'year 2018' instead of the full date '01/01/2018'. Or having data for 'budget' but not for 'revenue', nor 'release date' at all. This enforces me to drop more movies titles that I would like to do.

 - My second problem that I'm predicting is that some DataSets, like TMDb, give more than one genre per movie, e.g. 'Matrix: Action, Science-Fiction'. And I'm not sure what should be the most correct approach to deal with that when analizing the data and returning a minimalistic visual graphic of it.

 - Like the issues above, we relly on community and other API users to provide and correct the data already collected. Which means that sometimes, if we collect the data using requests, if someone is updating information of these particular data aswell, we might collect half-provided data, which will crash the code that I have designed to iterate over each Movie ID from key [0] to [-1] of the API json.

