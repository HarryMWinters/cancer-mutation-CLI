def summarize(samples, symbolMap):
    if type(samples) != list:
        raise IOError("Unable to retrieve data from web.")
    genes = symbolMap.values()
    geneCount = {
        "total": 0,
        "NA": 0,
        "singleCopy": 0,
        "noCopy": 0,
        "multiCopy": 0,
        "noChange": 0,
    }
    countDict = {int(gene): geneCount.copy() for gene in genes}
    print(f"countdict = {countDict}")
    countDict["Geneset"] = {"mutated": 0}
    countDict["totalCount"] = len(samples) / len(genes)

    i = 0
    while i < len(samples):
        sample = samples[i: i + len(genes)]
        _checkSample(countDict, sample)
        i += len(genes)

    return countDict


def _checkSample(countDict, sample):
    isMutated = False
    for gene in sample:
        geneID = gene["entrezGeneId"]
        alteration = gene["alteration"]
        # Data not available
        if alteration == "NA":
            countDict[geneID]["NA"] += 1
        # single copy of gene is lost or gained
        elif alteration in [-1, 1]:
            countDict[geneID]["singleCopy"] += 1
            isMutated = True
        # both copies of the gene are deleted
        elif alteration == -2:
            countDict[geneID]["noCopy"] += 1
            isMutated = True
        # multiple copies of the gene are observed
        elif alteration == +2:
            countDict[geneID]["multiCopy"] += 1
            isMutated = True
        elif alteration == 0:
            countDict[geneID]["noChange"] += 1
        else:
            RuntimeWarning(f"Encountered unexpected value in field 'alteration'.\
                Value: {alteration}. Sample key: {gene['uniqueSampleKey']}.")

    if isMutated:
        countDict["Geneset"]["mutated"] += 1

    return
