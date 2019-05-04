import pandas as pd

class Analyzer:

    filename = None         # The name of the input file for data.
    data = None             # Data as pandas dataframes.

    def __init__(self):
        pass

    def getTopLanguages(self, num):
        """
            Gets the top repository languages in descending order.
            
            Parameters
            ----------
            num: int
                The number of top languages to return.
            
            Returns
            -------
            list: str
                A list of strings containing the top languages.
        """
        pass

    def getTopCountries(self, num):
        """
            Gets the top countries for repository creation in descending order.

            Parameters
            ----------
            num: int
                The number of top countries to return.

            Returns
            -------
            list: str
                A list of strings containing the top countries.
        """
        pass

    def getPopularRepo(self, num):
        """
            Gets the top most popular repositories.

            Parameters
            ----------
            num: int
                The number of top respositories to return.

            Returns
            -------
            list: str
                A list of strings containing the most popular repositories.
        """
        pass