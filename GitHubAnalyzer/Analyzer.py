import pandas as pd
from datetime import datetime
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
        lang_rank = lang_rank.nlargest(num, ['repository_url'])
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
        country_rank = country_count.nlargest(num, ['repository_url'])
        top_actor_countries = country_rank['repository_url']
        return (top_actor_countries.index.values, top_actor_countries.values)

    def topRepoLocation(self, num):
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
        location_dict = dict()
        unique_repos = self.data['repository_url'].value_counts().index.values
        for repo in unique_repos:
            owner = self.data[self.data['repository_url'] == repo].iloc[0]['repository_owner']
            owner_actions = self.data[self.data['actor_attributes_login'] == owner]
            if not owner_actions.empty:
                location = owner_actions.iloc[0]['actor_attributes_location']
                if location:
                    if location in location_dict:
                        location_dict[location] += 1
                    else:
                        location_dict[location] = 1
        print(location_dict)

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
        lang_rank = lang_rank.nlargest(num, ['repository_url'])
        top_country_languages = lang_rank['repository_url']
        return (top_country_languages.index.values, top_country_languages.values)

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
        repo_event_count = self.data['repository_url'].value_counts()
        top10 = repo_event_count.nlargest(num)
        return (top10.index.values, top10.values)

    def getWatchersContributors(self, repo_url):
        """
            Returns the peak number of watchers of a repository at any point
            and unique contributors count as a tuple of ints.

            Parameters
            ----------
            repo_url: str
                The url of the target repository.
            
            Returns
            -------
            tuple: (int, int)
                The peak number of watchers and unique contributors.
        """
        repo_data = self.data[self.data['repository_url'] == repo_url]
        contribution_events = repo_data[repo_data['type'] != 'WatchEvent']
        watchers = repo_data['repository_watchers'].max()
        contributors = len(contribution_events['actor_attributes_login'].unique())
        return (watchers, contributors)

    def repoDescriptionSearchYears(self, keyword):
        """
            Returns a list of years and occurrence count corresponding to the years
            a repository with a keyword in their description was created.

            Parameters
            ----------
            keyword: str
                The keyword to search for in the repository description.

            Returns
            -------
            list: tuples
                List of tuples containing the years and their occurrence count.
        """
        repos = self.data[self.data['repository_description'].str.contains(keyword, case=False, na=False)]
        repos = repos.drop_duplicates('repository_url').sort_values(by=['repository_created_at'])
        years = repos.groupby(repos['repository_created_at'].str[:4])
        year_counts = [(g, years.groups[g].size) for g in years.groups]
        return year_counts

    def timeOfDayActivity(self, chunks=4):
        """
            Gets activity count based on time of day. Broken into four 6 hour chunks.

            Parameters
            ----------
            chunks: int
                The number of chunks to break up a 24 hour day into. Must be a factor of 24.

            Returns
            -------
            list: (int)
                A list of integers containing total activity at each time of day.
        """
        if 24 % chunks != 0:
            raise ValueError('Bad chunk value. Chunk value must be factor of 24.')
        dt_data = pd.to_datetime(self.data['created_at'], format='%Y-%m-%d %H:%M:%S')
        hours = dt_data.dt.hour
        time_of_day = hours.floordiv(24/chunks)
        counts = time_of_day.groupby(time_of_day).count()
        return counts.values

    def activityType(self):
        """
            Gets the count of the different activity types.
        """
        pass
