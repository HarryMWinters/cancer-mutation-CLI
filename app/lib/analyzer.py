def summarize(geneData):
    if type(geneData) != list:
        return {"error": geneData}
    caseCount = len(geneData)
    for case in geneData:
        # Counts
        noChange = NA = singleCopy = noCopy = multiCopy = 0
        alteration = case["alteration"]
        # Data not available
        if alteration == "NA":
            NA += 1
        # single copy of gene is lost or gained
        elif alteration in [-1, 1]:
            singleCopy += 1
        # both copies of the gene are deleted
        elif alteration == -2:
            noCopy += 1
        # multiple copies of the gene are observed
        elif alteration == +2:
            multiCopy += 1
        elif alteration == 0:
            noChange += 1
        else:
            RuntimeWarning(f"Encountered unexpected value in field 'alteration'.\
                 Value: {alteration}. Sample {case['uniqueSampleKey']}.")
    return {
        "total": caseCount,
        "NA": NA,
        "singleCopy": singleCopy,
        "noCopy": noCopy,
        "multicopy": multiCopy,
        "noChange": noChange,
        "error": None
    }
