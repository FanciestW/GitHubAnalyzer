import argparse

def main():
    # Get CLI arguments for program required options.
    argparser = argparse.ArgumentParser(description='GitHub Data Analyzer.')
    argparser.add_argument(
        "--file",
        "-f",
        type=str,
        default="data/sameple0.json", help="File with data to analyze."
    )
    args = argparser.parse_args()

    print(args.file)

if __name__ == "__main__":
    main()
