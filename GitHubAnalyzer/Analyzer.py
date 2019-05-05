import pandas as pd

class Analyzer:

    filename: str                   # The name of the input file for data.
    data: pd.DataFrame              # Data as pandas dataframes.

    def __init__(self, file):
        """
            Create an Analyzer object and sets the dataframes to input file data.

            Parameters
            ----------
            file: str
                Path to input data file. Either a JSON or CSV file.
        """
        self.filename = file
        if file.endswith('.csv'):
            self.data = pd.read_csv(self.filename)
        elif file.endswith('.json'):
            self.data = pd.read_json(self.filename, lines=True)
        else:
            print('File must be a JSON or CSV file.')
            sys.exit(0)

    def topLanguages(self, num):
        """
            Returns the top repository languages in descending order.
            
            Parameters
            ----------
            num: int
                The number of top languages to return.
            
            Returns
            -------
            list: tuple
                A list of tuples containing the top languages and their
                popularity based on how many repositories used that language.
        """
        lang_count = self.data.groupby('repository_language').count()
        lang_rank = lang_count.sort_values('repository_url', ascending=False)
        lang_rank = lang_rank.nlargest(num, ['repository_url'], keep='all')
        top_langs = lang_rank['repository_url']
        return (top_langs.index.values, top_langs.values)

    def topActorLocations(self, num):
        """
            Returns the top locations for repository contribution in descending order.

            Parameters
            ----------
            num: int
                The number of top locations to return.

            Returns
            -------
            list: tuple
                A list of tuples containing the top locations and their contribution
                counts based on how many actors contributed to the repositories.
        """
        country_count = self.data.groupby('actor_attributes_location').count()
        country_rank = country_count.sort_values('repository_url', ascending=False)
        country_rank = country_count.nlargest(num, ['repository_url'], keep='all')
        top_actor_countries = country_rank['repository_url']
        return (top_actor_countries.index.values, top_actor_countries.values)

    def topRepoLocations(self, num):
        """
            Returns the top locations for creating repositories.

            Parameters
            ----------
            num: int
                The number of top locations to return.

            Returns
            -------
            list: tuple
                A list of tuples containing the top locations based on repository count.
        """
        pass

    def countryTopLanguages(self, country, num):
        """
            Returns a given countries top list of programming languages.

            Parameters
            ----------
            country: str
                The country name to get top languages on.
            num: int
                The number of top languages to return.

            Returns
            -------
            list: tuple
                A list of tuples containing the top languages and their repository count.
        """
        country_data = self.data.loc[self.data['actor_attributes_location'] == country]
        count = country_data.groupby('repository_language').count()
        lang_rank = count.sort_values('repository_url', ascending=False)
        lang_rank = lang_rank.nlargest(num, ['repository_url'], keep='all')
        top_country_languages = lang_rank['repository_url']
        return (top_country_languages.index.values, top_country_languages.values)

    def getPopularRepo(self, num: int):
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