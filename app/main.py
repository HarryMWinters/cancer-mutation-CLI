from lib.parser import parse


def main():
    geneIDs = parse()
    print(geneIDs)
    # Map symbols to entrez gene ID's
    # Retrieve (and cache?) data
    # Analyze (and cache?) data
    # Print Summary
    pass


if __name__ == "__main__":
    main()
