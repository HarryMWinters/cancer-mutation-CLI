import csv


def toID(symbolList):
    # TODO: Docstring
    IDlist = []
    idMap = {}
    with open("./data/gene_id_symbol_map.csv") as csvFile:
        for geneID, symbol in csv.reader(csvFile):
            idMap[symbol] = geneID
    for symbol in symbolList:
        IDlist.append(idMap.get(symbol, "ID404"))
    return IDlist
