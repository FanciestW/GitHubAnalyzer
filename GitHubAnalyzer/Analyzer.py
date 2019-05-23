import pandas as pd
import numpy as np
from tqdm import tqdm
from halo import Halo
import glob
class Analyzer:

    filename: str                   # The name of the input file for data.
    data: pd.DataFrame              # Data as pandas dataframes.
    countries: pd.DataFrame         # Location and Country data.

    def __init__(self, file, dir_path=None):
        """
            Create an Analyzer object and sets the dataframes to input file data.

            Parameters
            ----------
            file: str
                Path to input data file. Either a JSON or CSV file.
            dir: str
                Optional directory path to multiple input csv files.
        """
        cols = [
            'repository_url', 'repository_created_at', 'repository_name',
            'repository_description', 'repository_owner', 'repository_open_issues',
            'repository_watchers', 'repository_language', 'actor_attributes_login',
            'actor_attributes_name', 'actor_attributes_location', 'created_at',
            'payload_action', 'payload_number','payload_issue', 'actor', 'url', 'type'
        ]
        df_types = {
            'repository_url': str, 'repository_created_at': str, 'repository_description': str,
            'repository_owner': str, 'repository_open_issues': str, 'repository_watchers': str,
            'repository_language': str, 'actor_attributes_login': str, 'actor_attributes_name': str,
            'actor_attributes_location': str, 'created_at': str, 'payload_action': str,
            'payload_number': str, 'payload_issue': str, 'actor': str, 'url': str, 'type': str
        }
        if dir_path:
            all_files = glob.glob(dir_path + '/*.csv')
            li = []
            pbar = tqdm(all_files)
            for file in pbar:
                pbar.set_description("Reading %s" % file)
                df = pd.read_csv(file, usecols=cols, dtype=df_types, header=0)
                li.append(df)
            self.data = pd.concat(li, axis=0, ignore_index=True)
        else:
            f_spinner = Halo(text='Loading', spinner='dots')
            self.filename = file
            if file.endswith('.csv'):
                f_spinner.start()
                self.data = pd.read_csv(self.filename, usecols=cols, dtype=df_types)
                f_spinner.succeed(f'{file} Successfully Read!')
            elif file.endswith('.json'):
                f_spinner.start()
                self.data = pd.read_json(self.filename, lines=True)
                f_spinner.succeed(f'{file} Successfully Read!')
            else:
                print('File must be a JSON or CSV file.')
                sys.exit(0)
        spinner = Halo(text='Processing Data', spinner='dots')
        spinner.start()
        self.countries = pd.read_csv('data/countries.csv')
        self.data['created_at'] = pd.to_datetime(self.data['created_at'], format='%Y-%m-%d %H:%M:%S')
        self.data = self.data.join(self.countries.set_index('actor_attributes_location'), on='actor_attributes_location')
        self.data['country'].replace('No Results', '', inplace=True)
        spinner.succeed('Data Successfully Proccessed!')

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
        spinner = Halo(text='Analyzing Top Languages', spinner='dots')
        spinner.start()
        lang_count = self.data.groupby('repository_language').count()
        lang_rank = lang_count.sort_values('repository_url', ascending=False)
        lang_rank = lang_rank.nlargest(num, ['repository_url'])
        top_langs = lang_rank['repository_url']
        spinner.succeed('Top Languages Analysis Complete!')
        return (top_langs.index.values, top_langs.values)

    def topActorCountries(self, num):
        """
            Returns the top countires for repository contribution in descending order.

            Parameters
            ----------
            num: int
                The number of top locations to return.

            Returns
            -------
            list: tuple
                A list of tuples containing the top countries and their contribution
                counts based on how many actors contributed to the repositories.
        """
        spinner = Halo(text='Analyzing Top Actor Countries', spinner='dots')
        spinner.start()
        country_count = self.data.loc[self.data['country'] != ''].groupby('country').count()
        country_rank = country_count.sort_values('repository_url', ascending=False)
        country_rank = country_count.nlargest(num, ['repository_url'])
        top_actor_countries = country_rank['repository_url']
        spinner.succeed('Top Country Analysis Complete!')
        return (top_actor_countries.index.values, top_actor_countries.values)

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
        spinner = Halo(text='Analyzing Country Top Languages', spinner='dots')
        spinner.start()
        country_data = self.data.loc[self.data['actor_attributes_location'] == country]
        count = country_data.groupby('repository_language').count()
        lang_rank = count.sort_values('repository_url', ascending=False)
        lang_rank = lang_rank.nlargest(num, ['repository_url'])
        top_country_languages = lang_rank['repository_url']
        size = len(top_country_languages)
        languages = np.pad(top_country_languages.index.values, (0,num-size), 'constant', constant_values=(''))
        values = np.pad(top_country_languages.values, (0,num-size), 'constant', constant_values=(0))
        spinner.succeed('Country Top Language Analysis Complete!')
        return (languages, values)

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
        spinner = Halo(text='Analyzing Most Popular Repositories', spinner='dots')
        spinner.start()
        repo_event_count = self.data['repository_url'].value_counts()
        top10 = repo_event_count.nlargest(num)
        spinner.succeed('Most Popular Repository Analysis Complete!')
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
        spinner = Halo(text='Analyzing Watchers and Contributors', spinner='dots')
        spinner.start()
        repo_data = self.data[self.data['repository_url'] == repo_url]
        contribution_events = repo_data[repo_data['type'] != 'WatchEvent']
        watchers = repo_data['repository_watchers'].max()
        contributors = len(contribution_events['actor_attributes_login'].unique())
        spinner.succeed('Watcher and Contributors Analysis Complete!')
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
        spinner = Halo(text=f'Analyzing for "{keyword}"" Repositories', spinner='dots')
        spinner.start()
        repos = self.data[self.data['repository_description'].str.contains(keyword, case=False, na=False)]
        repos = repos.drop_duplicates('repository_url').sort_values(by=['repository_created_at'])
        years = repos.groupby(repos['repository_created_at'].str[:4])
        year_counts = [(g, years.groups[g].size) for g in years.groups]
        spinner.succeed(f'Analysis of "{keyword}" Repositories Completed!')
        return year_counts

    def timeOfDayActivity(self, chunks=4, main_country='United States'):
        """
            Gets activity count based on time of day. Broken into four 6 hour chunks.

            Parameters
            ----------
            chunks: int
                The number of chunks to break up a 24 hour day into. Must be a factor of 24.

            Returns
            -------
            list: (dict)
                A list of dict containing total activity at each time of day and respective activity type.
        """
        spinner = Halo(text='Analyzing Time of Day Activities', spinner='dots')
        spinner.start()
        if 24 % chunks != 0:
            raise ValueError('Bad chunk value. Chunk value must be factor of 24.')
        dt_data = self.data.sort_values('created_at')
        dt_data['tod'] = dt_data['created_at'].dt.hour.floordiv(24/chunks)

        # All time of day data.
        event_group = dt_data.groupby(['tod', 'type']).groups
        events = [{t: 0 for t in dt_data['type'].unique()} for _ in range(chunks)]
        for t, e in event_group:
            events[int(t)][e] = event_group[(t, e)].size

        # Main country vs other countries time of day data.
        dt_data = dt_data.loc[dt_data['country'] != '']
        main_tod = dt_data[dt_data['country'] == main_country]
        other_tod = dt_data[dt_data['country'] != main_country]
        main_counts = main_tod.groupby('tod')['repository_url'].count().values
        other_counts = other_tod.groupby('tod')['repository_url'].count().values
        country_data = list(zip(main_counts, other_counts))
        spinner.succeed('Time of Day Analysis Complete!')
        return events, country_data

    def countryActivity(self, chunks=4, main_country='United States'):
        """
            Returns a tuples of the contribution count of the main country and
            other countries. Will ignore activities without a proper country.

            Parameters
            ----------
            chunks: int
                The number of chunks to break up a 24 hour day into. Must be a factor of 24.
            main_country: str
                The name of the country to compare to all other countries.

            Returns
            -------
            tuple: (int, int)
                The first int is the contribution count of the main country followed by all other countries.
        """
        spinner = Halo(text='Analyzing Country Activities', spinner='dots')
        spinner.start()
        if 24 % chunks != 0:
            raise ValueError('Bad chunk value. Chunk value must be factor of 24.')
        dt_data = self.data.sort_values('created_at')
        dt_data['tod'] = dt_data['created_at'].dt.hour.floordiv(24/chunks)

        dt_data = dt_data.loc[dt_data['country'] != '']
        main_tod = dt_data[dt_data['country'] == main_country]
        other_tod = dt_data[dt_data['country'] != main_country]
        main_counts = main_tod.groupby('tod')['repository_url'].count().values
        other_counts = other_tod.groupby('tod')['repository_url'].count().values
        country_data = list(zip(main_counts, other_counts))
        spinner.succeed('Country Activity Analysis Complete!')
        return country_data

    def dayOfWeek(self, chunks=4):
        """
            Gets data on time of day activity broken into days of the week.

            Parameters
            ----------
            chunks: int
                The number of chunks to break up a 24 hour day into. Must be a factor of 24.

            Returns
            -------
            list: list
                A list of list containing chunks of data for each day of the week.
                Each list within the list represents the data for one weekday.
        """
        spinner = Halo(text='Analyzing Days of the Week Activities', spinner='dots')
        spinner.start()
        if 24 % chunks != 0:
            raise ValueError('Bad chunk value. Chunk value must be factor of 24.')
        dt_data = self.data.sort_values('created_at')
        dt_data['tod'] = dt_data['created_at'].dt.hour.floordiv(24/chunks)
        dt_data['weekday'] = dt_data['created_at'].dt.weekday
        tod_by_week = list()
        for i in range(chunks):
            tod_data = dt_data.groupby('tod').get_group(i)[['url', 'weekday']]
            d = tod_data.groupby('weekday').count()['url'].values
            tod_by_week.append(d)
        spinner.succeed('Days of Week Activity Analysis Complete!')
        return np.transpose(tod_by_week)

    def issueResolution(self, repo_url):
        """
            Gets the resolution times for a repository's issues.

            Parameters
            ----------
            repo_url: str
                The respository url to analyze issue resolution time.

            Returns
            -------
            list: int
                A list of all the issue resolution times. With last value being
                the number of unresolved issues.
        """
        spinner = Halo(text='Analyzing Repository Issues', spinner='dots')
        spinner.start()
        repo_issues = self.data[
            (self.data['repository_url'] == repo_url) &
            (self.data['type'] == 'IssuesEvent')
        ].drop_duplicates().sort_values('created_at')[['payload_issue', 'payload_action', 'created_at']]
        opened_issues = repo_issues[repo_issues['payload_action'] == 'opened'].sort_values('created_at').drop_duplicates(subset='payload_issue', keep='first')
        closed_issues = repo_issues[repo_issues['payload_action'] == 'closed'].sort_values('created_at').drop_duplicates(subset='payload_issue', keep='last')
        open_times = opened_issues[['payload_issue', 'created_at']]
        closed_times = closed_issues[['payload_issue', 'created_at']]
        issues = pd.merge(open_times, closed_times, on='payload_issue')
        issues['resolution_time'] = issues['created_at_y'] - issues['created_at_x']
        time_data = issues[issues['resolution_time'] > pd.Timedelta(0)]
        resolution_times = time_data['resolution_time'].dt.days
        spinner.succeed('Respository Issues Anaysis Complete!')
        return resolution_times.values
