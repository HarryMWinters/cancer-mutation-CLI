#!/usr/bin/env python3

from lib.parser import parse
from lib.symbol_ID import toID
from lib.data_retrieval import retrieve
from lib.data_analysis import summarize
from lib.prettify import formatAndPrint


def main():
    geneSymbols, toJSON = parse()
    geneIDs = toID(geneSymbols)
    symbolMap = {symbol: gID for symbol, gID in zip(geneSymbols, geneIDs)}
    # TODO: this fails silently for unrecognized gene symbols
    samples = retrieve(symbolMap)
    outputDict = summarize(samples, symbolMap)
    formatAndPrint(outputDict, toJSON=toJSON)


if __name__ == "__main__":
    main()
