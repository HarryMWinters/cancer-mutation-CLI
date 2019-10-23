from lib.parser import parse
from lib.entrez_gene import toID
from lib.TCGA import retrieve
from lib.analyzer import summarize


def main():
    geneSymbols = parse()
    geneIDs = toID(geneSymbols)
    outputDict = {}
    for symbol, gID in zip(geneSymbols, geneIDs):
        outputDict[symbol] = retrieve(gID)
    for k, v in outputDict.items():
        outputDict[k] = summarize(v)
    for k, v in outputDict.items():
        print(f"{k}: {v}")
    # Analyze (and cache?) data
    # Print Summary
    pass


if __name__ == "__main__":
    main()
