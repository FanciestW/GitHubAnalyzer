import pandas as pd

class Analyzer:

    filename: str                   # The name of the input file for data.
    data: pd.DataFrame              # Data as pandas dataframes.

    def __init__(self, file: str):
        self.filename = file
        if file.endswith('.csv'):
            self.data = pd.read_csv(self.filename)
        elif file.endswith('.json'):
            self.data = pd.read_json(self.filename, lines=True)
        else:
            print('File must be a JSON or CSV file.')
            sys.exit(0)

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
                A list of tuples containing the top languages and their
                popularity based on how many repositories used that language.
        """
        lang_count = self.data.groupby('repository_language').count()
        lang_rank = lang_count.sort_values('repository_url', ascending=False)
        lang_rank = lang_rank.nlargest(num, ['repository_url'], keep='all')
        top_langs = lang_rank['repository_url']
        return list(zip(top_langs.index.values, top_langs.values))

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