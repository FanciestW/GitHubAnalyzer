import argparse
import numpy as np
from GitHubAnalyzer.Grapher import Grapher
from GitHubAnalyzer.Analyzer import Analyzer

def main():
    # Get CLI arguments for program required options.
    argparser = argparse.ArgumentParser(description='GitHub Data Analyzer.')
    argparser.add_argument(
        '--file',
        '-f',
        type=str,
        default='data/sample.csv',
        help='File with data to analyze.'
    )
    argparser.add_argument(
        '--dir',
        '-d',
        type=str,
        help='Directory with all the input files as CSV files.'
    )
    args = argparser.parse_args()

    # Initialize data analyzer and results grapher.
    analyzer = Analyzer(args.file, args.dir)
    grapher = Grapher()

    # # Get top 10 languages and graph on bar graph.
    # top_10_langs = analyzer.topLanguages(10)
    # grapher.top_bar_chart(top_10_langs[0], top_10_langs[1], 'Repo Count', 'Top 10 Languages')

    # # Get top 10 location for repository contributions and corresponding top 10 languages.
    # top_actor_countries = analyzer.topActorCountries(10)
    # grapher.top_bar_chart(top_actor_countries[0], top_actor_countries[1], 'Repo Count', 'Top 10 Countries')
    # top_country_langs = [analyzer.countryTopLanguages(x, 10) for x in top_actor_countries[0]]
    # grapher.top_country_langs(top_actor_countries[0], top_country_langs)

    # Get Popular Repos
    pop_repos = analyzer.getPopularRepo(10)
    # pop_repos_watcher_contributors = [analyzer.getWatchersContributors(r) for r in pop_repos[0]]
    # grapher.watcher_contributor_scatter(pop_repos_watcher_contributors, pop_repos[0])

    # # Graph security repository creations dates based on year.
    # repo_years = analyzer.repoDescriptionSearchYears('security')
    # grapher.repoYearLine(repo_years, 'Security Repos Overtime')

    # # Graph the most active time of the day for GitHub activities types.
    # activity, country = analyzer.timeOfDayActivity(4)
    # times = ['12AM-6AM', '6AM-12PM', '12PM-6PM', '6PM-12AM']
    # types = [key for key in activity[0]]
    # activity_types = [[t[key] for key in t] for t in activity]
    # activity_count = [sum(i) for i in activity_types]
    # grapher.activityHist(activity_count, times)
    # types_data = np.transpose(np.array(activity_types))
    # grapher.activityTypesBar(types_data, times, types)
    # grapher.countryContributionBar(country, times, ['United States', 'Other Countries'])

    # # Graph and animate days of the week data.
    # weekday_data = analyzer.dayOfWeek()
    # grapher.weekday_animated_graph(weekday_data, times)

    analyzer.issueResolution(pop_repos[0][1])

if __name__ == "__main__":
    main()
