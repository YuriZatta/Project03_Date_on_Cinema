### 3 Classes!
import requests
from datetime import datetime as time
import pandas as pd
from matplotlib import pyplot as plt
import tmdbsimple
import numpy as np

class DataBase:
    """
    This parent class takes the 'BoxOffice 90's - 2020' Dataset archived
    inside a .csv file, and clean it using Pandas! Then returns the Data 
    Frame assining it to the object 'self.clean_DataSet' to be used by
    the child classes!
    """
    """
    When we need to create objects refering to dates such 1990, we will
    use '90' instead, '70', '60' and so on. If you see '90_20' that can
    be seen as 'from the 90s until 2020'. The past should always come
    first! There is no 'from the 1990 until 1950', only 1950 until 1990!
    --> 'BO' and 'bo' stands for BoxOffice! 
    --> 'bo_90_20' stands for: BoxOffices from the 90s until 2020
    --> TMDb stands for The Movie DataBase.org
    --> IMDb stands for the famous IMDb
    --> BOMDb stands for BoxOffice Mojo DataBase
    """
    """
    For now, our app relys on this single dataset ('BoxOffice 90's - 2020') 
    but in the future it will have methods to request data from APIs,
    and methods to mix the requested data with all collected DataFrames 
    in one single obj 'self.clean_DataSet' that is already in use.
    """
    """
    ## Commented Methods ## are there to be pseudo-codes for future updates!
    """
    def __init__(self):
        # to be used if we need to create our own dataframe .csv file!
        self.file_path = ''
        # The clean DataSet that will be used by all users iteration!
        self.clean_DataSet = None
        # When we have to store Data Frames made by collecting info from
        # the following websites APIs.
        self.TMDb = None
        self.IMDb = None
        self.BOMDb = None
        
        # The BoxOffice Dataset from the 90's until April 2020, 
        # WITH release date!
        self.__bo_90_20 = 'dataset_mojo_budget_update_from_1990_until_04_20.csv'
        # The BoxOffice Dataset from all years until 2019,
        # WITHOUT release date!
        self.__bo_all_19 = 'datasets_boxoffice_alltime_until_august_2019.csv'

    # # def __TMDb_cleaning(self):
    # #     requests TMDb API
    # #     Pandas
    # #     Data Frame
    # #     pass

    # # def __IMDb_cleaning(self):
    # #     Requests API
    # #     Pandas
    # #     Data Frame
    # #     pass

    # # def __BOMDb_cleaning(self):
    # #     Requests API
    # #     Pandas
    # #     Data Frame
    # #     pass

    def BO_DS_cleaning(self):
        """
        This method clean the local stored .csv file that holds the
        'BoxOffice 90's - 2020' data, using Pandas, then return a single
        Data Frame inside the object 'self.clean_DataSet' to be used by
        child Classes!
        """
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

    # # def __DataSet_generator(self):
    # #     if Public TMDb, IMDb and BOMDb exists:
    # #         if Day Date == Today:
    # #             Pandas
    # #             Data Set
    # #     else:
    # #         Call __private_method_TMDb_cleaning.requests()
    # #         Pandas
    # #         DataSet
    # #     pass

    # #private = property(__BOMDb_cleaning)

class Date(DataBase):
    """
    This child Class from 'class DataBase()' asks the user input using
    the '__date_input()', and with the input provided by the user
    the '__Pandas_filter()' will uses Pandas to iterate over the public 
    self.clean_DataSet from the Parent Class, using the 'date' column as
    a filter with the '.query()' method. All of this is activated by the
    'graphic_view()' public method, this calls for the other 2, and with
    what they return 'graphic_view()' will pass the DataFrame values to
    MatPlotLib built-in methods to display a graphic view! 
    """
    
    def __Pandas_filter(self,date = None):
        """
        This method activates the parent Class DataBase() and assign the
        'self.clean_DataSet' into a local 'df' object. Then uses the 
        user input Date to filter the DF and return only the info asked.
        If the users by mistake hits 'enter' without providing any date,
        this method will assume a default date of '1990-07-06', when 
        Die Hard 2 was released. 
        """
        
        DataBase.BO_DS_cleaning(self)
        df = self.clean_DataSet 
        # print(df)
        # Die Hard 2 release date in U.S.
        default_date = '1990-07-06'
        # this format was the only one that manage to work, link beneath
        date = default_date if date is None else date
        # https://stackoverflow.com/questions/52494128/call-function-without-optional-arguments-if-they-are-none
        try:
            self.date = pd.to_datetime(date)
            # print(df.query("date == @self.date"))
            self.df_filter = df.query("date == @self.date")
            return self.df_filter
        except ValueError:
            print('\nPlease insert a valide date format!\n')

    def __date_input(self,date=None):
        """
        This method uses a While Loop to ask the User for a valid input,
        if the user cannot meet the creterea of typing the date asked in
        the '21 November 2019, or 2019-11-21' formats, the loop will
        keep asking the User to try again. This formats are the ones
        accepted by Pandas built-in method '.to_datetime()', which was
        used to convert the 'date' column inside our DataFrame, and will
        be used again to validate the users input!
        The provided input will be assigned as 'self.input_date' and 
        this method will call for 'self.__Pandas_filter()' passing the
        input as an argument! 
        Besides that, if the user by mistake hits 'enter' without 
        providing anything, the input will be seen as 'None' and passed 
        to the 'self.__Pandas_filter()' method anyway, activating it's
        Default Date value.
        """
        DataBase.BO_DS_cleaning(self)
        df = self.clean_DataSet 
        while True:
            try:
                date = input("\nWhat date do you want to analize?\nExample: 21 November 2019, or 2019-11-21\n\tType one style here->")
                
                if date == '':
                    date = None
                    self.input_date = date
                    # print('\n DONE None \n')
                    # Exit the loop if success!
                    break
                else: 
                    self.input_date = pd.to_datetime(date)
                    does_it_exist = df.isin([self.input_date]).any().any()
                    # print('\nit cames this far\n')
                    if does_it_exist:
                        self.input_date = pd.to_datetime(date)
                        # print('\n DONE to Date Time \n')
                        # Exit the loop if success!
                        break
                    else:
                        print("\nMaybe this isn't in our database, try some another date in between the 90's and 2020-04-01!\n")
                    # Exit the loop if success!
                    
            except ValueError: 
                print("\nSorry, I didn't understand that.\nExemples of valid formats are:\n21 November 2019 or 2019-11-21\n")
                # let's try again without breaking the code...
                continue
        
        # self.input_date = pd.to_datetime(date)
        self.__Pandas_filter(self.input_date)
        
    def graphic_view(self):
        """
        This is the only public method of the child Class Date()! It
        calls for 'self.__date_input()', which will asks for the users
        input in date format. 
        It'll take the returned values from the methods above and their
        public self.objects and use it to generate a graphic view of the
        results of 'self.__Pandas_filter()' !!!
        """
        self.__date_input()
        df_plot_full = self.clean_DataSet
        df_cut = self.df_filter
        print('\n')
        print(df_cut)
        print('\n')
        
        plt.bar(df_cut['budget'], df_plot_full['budget'], label='Title')
        plt.legend()
        plt.xlabel("genre_1")
        plt.ylabel("budget")
        plt.show()

        movies_budget = df_plot_full['budget']
        movies_genres = df_plot_full['genre_1']
        x = np.arange(len(df_plot_full['genre_1']))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, movies_genres, width, label='Genre')
        rects2 = ax.bar(x + width/2, movies_budget, width, label='Budget')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()


        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')


        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()

        plt.show()

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
    Instead of using date as a filter to iterate over our Parent Class' 
    "self.clean_DataSet" obj, this class will ask for the user to input 
    the full name of the desired movie! It uses the 'name_input()' 
    method to ask for the user to provide a name. After a valid input, 
    this class calls for the "__Pandas_filter()" method to generate a DF.
    Then, this method checks if the name is a duplicated element in the 
    'title' columns inside our Data Frame.
    If duplicated names exists, 'name_input()' will return a Data Frame 
    with the duplicated names and their release date, then it calls the
    'class Date()' for the user to insert their chosen date instead, 
    giving a more accurated result!
    If it's not duplicated, it simples call for the 'Date.graphic_view()'
    method passing the current DF filtered by 'title'.
    """
    
    def __Pandas_filter(self,name = None):
        """
        This method activates the parent Class DataBase() and assign the
        'self.clean_DataSet' into a local 'df' object. Then uses the 
        user input Name to filter the DF and return only the info asked.
        If the users by mistake hits 'enter' without providing any Title,
        this method will assume a default name of 'Get Out'. 
        """
        DataBase.BO_DS_cleaning(self)
        df = self.clean_DataSet 
        # print(df)
        # Get Out as default name if nothing is typed!
        default_name = 'Get Out'
        name = default_name if name is None else name
        try:
            self.name = name
            print('\n')
            #print(df.query("title == @self.name"))
            self.df_name_filter = df.query("title == @self.name")
            return self.df_name_filter
        except ValueError:
            print('\nPlease insert a valide name!\n')
        
        
    def name_input(self,name=None):
        """
        This method uses a While Loop to ask the User for a valid input,
        if the user cannot meet the creterea of typing a valid movie 
        name, the loop will keep asking the User to try again. 
        This Loop will help us in the case of the User assuming that a
        certain movie should exists in our DataBase, if the User is
        wrong, or if the DataBase is lacking information, either way the
        code will not break, and the loop will simply ask again for any
        valid name! 
        Besides that, if the user by mistake hits 'enter' without typing
        anything, the input will be seen as 'None' and be passed to the 
        'self.__Pandas_filter()' method anyway, activating it's
        Default Name value.

        After 'self.__Pandas_filter()' generates a DF that will be 
        assigned to "df_name", We'll check if the name is a duplicated 
        element in the 'title' columns inside our Data Frame. If True,
        'name_input()' will return a DF with the duplicated elements and
        their release dates, then it calls the 'class Date()' for the 
        user to insert their chosen date instead, giving a more 
        accurated result!
        If it's not duplicated, it simples call for the Data() method
        'Date.graphic_view()' passing the current DF filtered by 'title'.
        """
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
                    print("\nMaybe this isn't in our database, try one movie released between the 90's and April 2020!\n")
            except ValueError: 
                print("\nSorry, I didn't understand that.\nCan you try again?")
                # let's try again without breaking the code...
                continue
        
        
        # self.input_name = pd.to_datetime(name)
        self.__Pandas_filter(self.input_name)

        df_name = self.df_name_filter
        # print(df_name[['title', 'date', 'budget']])
        # check if duplicate
        if len(df_name.index) > 1:
            print('\n')
            print(self.df_name_filter)
            print('\nIt should have duplicateds!\n')
            # print(df_name)
            print("\nPlease, choose one of the dates and insert next!\n")
            better_method = Date()
            better_method.graphic_view()
        else:
            print('\n')
            print(df_name[['title', 'date', 'budget','genre_1']])
            print('\n')
            print('Type the date of this movie next!')
            better_method = Date()
            better_method.graphic_view()

    


# '21 November 2019'
# '2019-11-21'

a = DataBase()
a.BO_DS_cleaning()
# a.private

b = Date()
# b.Pandas_filter('1990-05-25')
# b.Pandas_filter('25 May 1990')
# b.method_date_input()
# b.method_date_input()
# b.method_date_input()
b.graphic_view()
# b.Testardor_input()

n = Name()
n.name_input()
# n.exists_input()

# """
# Similar to the 'Date.__Pandas_filter()' version, this one takes
# the value returned by 'name_input()', and instead of filtering
# by 'date', it'll filter by 'name' using the 'title' column.
# It'll also assume that if the value of 'name' provided by 
# 'name_input()' is None, the 'Default Name' to check should be of
# the movie Get Out, returning a result anyway instead of break.
# """

# dead matplotlib method codes:
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

# def __date_input(self,date=None):
    # """
    # This method uses a While Loop to ask the User for a valid input,
    # if the user cannot meet the creterea of typing the date asked in
    # the '21 November 2019, or 2019-11-21' formats, the loop will
    # keep asking the User to try again. This formats are the ones
    # accepted by Pandas built-in method '.to_datetime()', which was
    # used to convert the 'date' column inside our DataFrame, and will
    # be used again to validate the users input!
    # The provided input will be assigned as 'self.input_date' and 
    # this method will call for 'self.__Pandas_filter()' passing the
    # input as an argument! 
    # Besides that, if the user by mistake hits 'enter' without 
    # providing anything, the input will be seen as 'None' and passed 
    # to the 'self.__Pandas_filter()' method anyway, activating it's
    # Default Date value.
    # """
    # while True:
    #     try:
    #         date = input("\nWhat date do you want to analize?\nExample: 21 November 2019, or 2019-11-21\n\tType one style here->")
            
    #         if date == '':
    #             date = None
    #             self.input_date = date
    #         else:
    #             self.input_date = pd.to_datetime(date)
    #     except ValueError:
    #         print("\nSorry, I didn't understand that.\nExemples of valid formats are:\n21 November 2019 or 2019-11-21")
    #         #better try again... Return to the start of the loop!
    #         continue
    #     else:
    #         # date was successfully given!
    #         # we're ready to exit the loop.
    #         break
    
    # # self.input_date = pd.to_datetime(date)
    # self.__Pandas_filter(self.input_date)

# def exists_input(self,name=None):
    #         DataBase.BO_DS_cleaning(self)
    #         df = self.clean_DataSet 
    #         while True:
    #             try:
    #                 name = input("\nWhat movie name do you want to analize?\nExample: Die Hard 2, or Get Out\n\tType one name here->")
    #                 does_it_exist = df.isin([name]).any().any()
    #                 if does_it_exist:
    #                     self.input_name = str(name)
    #                     print('Done 1')
    #                     break
    #                 elif name == '':
    #                     name = None
    #                     self.input_name = name
    #                     print('Done NONE!')
    #                     break
    #                 else:
    #                     print("\nMaybe this isn't in our database, try one movie released between the 90's and April 2020!\n")
    #             except ValueError: 
    #                 print("\nSorry, I didn't understand that.\nCan you try again?")
                    
    #                 continue
            # while True:
            #     try:
            #         name = input("\nWhat movie name do you want to analize?\nExample: Die Hard 2, or Get Out\n\tType one name here->")
                    
            #         if name == '':
            #             name = None
            #             self.input_name = name
            #         else:
            #             self.input_name = str(name)
            #     except ValueError:
            #         print("\nSorry, I didn't understand that.\nCan you try again?")
            #         #better try again... Return to the start of the loop
            #         continue
            #     else:
            #         # date was successfully parsed!
            #         # we're ready to exit the loop.
            #         break
            
            
            # self.__Pandas_filter(self.input_name)

            # df_name = self.df_name_filter
            
            # if len(df_name.index) > 1:
            #     print('It should have duplicateds!')
                
            #     print("\nPlease, choose one of the dates and insert next!\n")
            #     better_method = Date()
            #     better_method.graphic_view()
            # else:
            #     print(df_name[['title', 'date', 'budget']])