import pandas as pd

class Analyzer:

    filename = None         # The name of the input file for data.
    data = None             # Data as pandas dataframes.

    def __init__(self, file: str):
        if file.endswith(".csv"):
            pass
        elif file.endswith(".json"):
            pass
        else:
            print("File must be a JSON or CSV file.")
            sys.exit(0)
        self.filename = file
        file = open(self.filename)
        pass

    def getTopLanguages(self, num: int) -> list:
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

    def getTopCountries(self, num: int) -> list:
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

    def getPopularRepo(self, num: int) -> list:
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