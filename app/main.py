from lib.parser import parse
from lib.entrez_gene import toID
from lib.TCGA import retrieve


def main():
    geneSymbols = parse()
    geneIDs = toID(geneSymbols)
    outputDict = {}
    for symbol, gID in zip(geneSymbols, geneIDs):
        outputDict[symbol] = retrieve(gID)
    for k, v in outputDict.items():
        print(f"{k}: {v}\n")
    # Retrieve (and cache?) data
    # Analyze (and cache?) data
    # Print Summary
    pass


if __name__ == "__main__":
    main()
