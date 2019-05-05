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

    analyzer = Analyzer(args.file)
    top_10_langs = analyzer.getTopLanguages(10)

if __name__ == "__main__":
    main()
