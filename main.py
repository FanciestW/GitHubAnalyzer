import argparse
from GitHubAnalyzer.Grapher import Grapher
from GitHubAnalyzer.Analyzer import Analyzer

def main():
    # Get CLI arguments for program required options.
    argparser = argparse.ArgumentParser(description='GitHub Data Analyzer.')
    argparser.add_argument(
        "--file",
        "-f",
        type=str,
        default="data/sample0.csv", help="File with data to analyze."
    )
    args = argparser.parse_args()

    # Initialize data analyzer and results grapher.
    analyzer = Analyzer(args.file)
    grapher = Grapher()

    # # Get top 10 languages and graph on bar graph.
    # top_10_langs = analyzer.topLanguages(10)
    # grapher.top_bar_chart(top_10_langs[0], top_10_langs[1], 'Repo Count', 'Top 10 Languages')

    # Get top 10 location for repository contributions and corresponding top 10 languages.
    top_actor_countries = analyzer.topActorLocations(10)[0]
    top_country_langs = [analyzer.countryTopLanguages(x, 10) for x in top_actor_countries]
    # for i, country in enumerate(top_actor_countries[0]):
    #     top_actor_countries[]
    grapher.top_country_langs(top_actor_countries, top_country_langs)

if __name__ == "__main__":
    main()
