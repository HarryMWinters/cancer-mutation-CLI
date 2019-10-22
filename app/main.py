from lib.parser import parse
from lib.entrez_gene import toID


def main():
    geneSymbols = parse()
    geneIDs = toID(geneSymbols)
    for symbol, gID in zip(geneSymbols, geneIDs):
        print(f"{symbol}: {gID}")
    # Map symbols to entrez gene ID's
    # Retrieve (and cache?) data
    # Analyze (and cache?) data
    # Print Summary
    pass


if __name__ == "__main__":
    main()
