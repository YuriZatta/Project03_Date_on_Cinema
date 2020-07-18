### 3 Classes!
import requests
from datetime import datetime as time
import pandas as pd
from matplotlib import pyplot as plt
import tmdbsimple

class DataBase:
    """
    It will have methods to request data from APIs, and methods to mix
    the requested data with each other in one single public
    object/DataSet
    """
    def __init__(self):
        self.file_path = ''
        # The clean DataSet that will be used by all user iteration!
        self.clean_DataSet = None
        self.TMDb = None
        self.IMDb = None
        self.BOMDb = None
        
        # The BoxOffice Dataset from the 90's until April 2020, WITH release date!
        self.__bo_90_20 = 'dataset_mojo_budget_update_from_1990_until_04_20.csv'
        # The BoxOffice Dataset from all years until 2019, WITHOUT release date!
        self.__bo_all_19 = 'datasets_boxoffice_alltime_until_august_2019.csv'

    # def __method_TMDb_cleaning(self):
    #     requests TMDb Api
    #     Pandas
    #     Data Frame
    #     pass

    # def __method_IMDb_cleaning(self):
    #     Pandas
    #     Data Frame
    #     pass

    def BOMDb_cleaning(self):
        bo_df = pd.read_csv(self.__bo_90_20)
        bo_df.drop(labels = [
            'trivia','mpaa','run_time','distributor','director',
            'composer','cinematographer','writer','main_actor_1',
            'main_actor_2','main_actor_3','main_actor_4','producer','html'
            ], axis='columns', inplace=True)
        # print('\n')
        # print('raw dataframe')
        # print(bo_df.head(5))
        # print('\n')
        # print('clean dataframe')
        
        bo_df['date'] = bo_df['year'].astype(str) + ' ' + bo_df['release_date']
        cols = bo_df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        bo_df = bo_df[cols]
        bo_df['budget'] = bo_df['budget']/1000000
        bo_df['date'] = pd.to_datetime(bo_df['date'])
        bo_df.drop(labels = ['year','release_date'], axis='columns', inplace=True)
        # print(bo_df.head(5))
        # print('\n')
        #print(bo_df.tail(5))
        self.clean_DataSet = bo_df
        return self.clean_DataSet
    # def __DataSet_generator(self):
    #     if Public TMDb, IMDb and BOMDb exists:
    #         if Day Date == Today:
    #             Pandas
    #             Data Set
    #     else:
    #         Call __private_method_TMDb_cleaning.requests()
    #         Pandas
    #         DataSet
    #     pass

    #private = property(__BOMDb_cleaning)

class Date(DataBase):
    """
    It will uses Pandas to iterate over the public object/DataSet using
    the 'date of release' as a filter( .query() ?). Maybe using the
    datatime library!
    """
    
    def __Pandas_filter(self,date = None):
        
        DataBase.BOMDb_cleaning(self)
        df = self.clean_DataSet 
        # print(df)
        # https://stackoverflow.com/questions/52494128/call-function-without-optional-arguments-if-they-are-none
        # Die Hard 2 release date in U.S.
        default_date = '1990-07-06'
        date = default_date if date is None else date
        try:
            self.date = pd.to_datetime(date)
            # print(df.query("date == @self.date"))
            self.df_filter = df.query("date == @self.date")
            return self.df_filter
        except ValueError:
            print('Please insert a valide date format!')

    def __method_date_input(self,date=None):
        
        while True:
            try:
                date = input("\nWhat date do you want to analize?\nExample: 21 November 2019, or 2019-11-21\n\tType one style here->")
                
                if date == '':
                    date = None
                    self.input_date = date
                else:
                    self.input_date = pd.to_datetime(date)
            except ValueError:
                print("\nSorry, I didn't understand that.\nExemples of valid formats are:\n21 November 2019 or 2019-11-21")
                #better try again... Return to the start of the loop
                continue
            else:
                # date was successfully parsed!
                # we're ready to exit the loop.
                break
        
        # self.input_date = pd.to_datetime(date)
        self.__Pandas_filter(self.input_date)
        

    def graphic_view(self):

        self.__method_date_input()
        df_plot_full = self.clean_DataSet
        df_cut = self.df_filter
        print(df_cut)
        # print('\n')
        # print('\n\t this is the graphic_view working!')
        # print(df_plot_full['title'].head(1))
        # print('\n')
        # print('\tprinted by the df_filter\n')
        # print(self.df_filter)
        # print('\n')
        # print('\tThis is the matplot time to work!\n')
        # df_knives_gen = df_plot_full[df_plot_full['title'] == 'Knives Out']['genre_1']
        # df_knives_bud = df_plot_full[df_plot_full['title'] == 'Knives Out']['budget']

        # df_21_gen = df_plot_full[df_plot_full['title'] == '21 Bridges']['genre_1']
        # df_21_bud = df_plot_full[df_plot_full['title'] == '21 Bridges']['budget']

        # df_t_min = df_plot_full[df_plot_full['budget'] == df_plot_full['budget'].min()]['budget']
        # df_t_max = df_plot_full[df_plot_full['budget'] == df_plot_full['budget'].max()]['budget']
        
        # 
        
        # # print(df_knives_gen)
        # # print(df_knives_bud)
        # # print('\n')
        # # print(df_21_gen)
        # # print(df_21_bud)
        # # print(df_t_min)
        # # print(df_t_max)
        # print(df_cut)
        # print(self.clean_DataSet.head(5))
        # mask_1 = df_plot_full['date'] == self.date
        # plt.bar(df_cut['genre_1'], label='Title')
        # plt.legend()
        # plt.xlabel("genre_1")
        # plt.ylabel("budget")
        # plt.show()
        # display Pandas df['movies name']['date']
        # displey genre graphic bar
        # maybe display BoxOffice graphic bar, but no guarantee
        
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('some numbers')
        # plt.show()
        """
        Front Page!
        plt.bar(df_plot['genre_1'],df_plot['budget'], label='Knives Out')
        plt.xlabel("genre_1")
        plt.ylabel("budget")
        plt.show()
        """

class Name(DataBase):
    """
    It will uses pandas to iterate over the public object/DataSet using
    the 'movie name' as a filter( .query() ?).
    If duplicated names exists, maybe it will return a data frame with
    the duplicated names and their release date, then it activates the
    'class Date()' for the user to insert their chosen date!
    """
    
    def __Pandas_filter(self,name = None):
        DataBase.BOMDb_cleaning(self)
        df = self.clean_DataSet 
        # print(df)
        # Get Out as default name if nothing is typed!
        default_name = 'Get Out'
        name = default_name if name is None else name
        try:
            self.name = name
            print(df.query("title == @self.name"))
            self.df_name_filter = df.query("title == @self.name")
            return self.df_name_filter
        except ValueError:
            print('Please insert a valide name!')
        
        
    def method_name_input(self,name=None):
        
        while True:
            try:
                name = input("\nWhat movie name do you want to analize?\nExample: Die Hard 2, or Get Out\n\tType one name here->")
                
                if name == '':
                    name = None
                    self.input_name = name
                else:
                    self.input_name = str(name)
            except ValueError:
                print("\nSorry, I didn't understand that.\nCan you try again?")
                #better try again... Return to the start of the loop
                continue
            else:
                # date was successfully parsed!
                # we're ready to exit the loop.
                break
        
        # self.input_name = pd.to_datetime(name)
        self.__Pandas_filter(self.input_name)

        df_name = self.df_name_filter
        # print(df_name[['title', 'date', 'budget']])
        # check if duplicate
        if len(df_name.index) > 1:
            print('It should have duplicateds!')
            # print(df_name)
            print("\nPlease, choose one of the dates and insert next!\n")
            better_method = Date()
            better_method.graphic_view()
        else:
            print(df_name[['title', 'date', 'budget']])


# '21 November 2019'
# '2019-11-21'

a = DataBase()
a.BOMDb_cleaning()
# a.private

b = Date()
# b.Pandas_filter('1990-05-25')
# b.Pandas_filter('25 May 1990')
# b.method_date_input()
# b.method_date_input()
# b.method_date_input()
b.graphic_view()

n = Name()
n.method_name_input()
