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

    # Get top 10 languages and graph on bar graph.
    top_10_langs = analyzer.getTopLanguages(10)
    grapher.top_bar_chart(top_10_langs[0], top_10_langs[1], "Repo Count", "Top 10 Languages")

if __name__ == "__main__":
    main()
