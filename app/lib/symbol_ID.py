import csv


def toID(symbolList):
    """
    toID takes a list of gene symbols as string I.E. ["TP53", "FAT4", "PCLO"] and 
    returns a list of their entrez ID. If a provided gene symbol isn't found in 
    data/gene_id_symbol_map.csv raises an error.

    Args:
         symbolList: A list of strings.
    Returns:
         A list of entrez gene IDs.
    Raises:
        LookupError if element of symbolList cannot be found in look up table.

    """
    IDList = []
    IDMap = {}
    with open("./data/gene_id_symbol_map.csv") as csvFile:
        for geneID, symbol in csv.reader(csvFile):
            IDMap[symbol] = geneID
    for symbol in symbolList:
        IDList.append(IDMap.get(symbol, None))
        if IDList[-1] is None:
            raise LookupError(f"Unable to find Entrez Gene ID for {symbol}")
    return IDList
