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
        default="data/sample.json", help="File with data to analyze."
    )
    args = argparser.parse_args()
    print(args.file)

    analyzer = Analyzer(args.file)

if __name__ == "__main__":
    main()
