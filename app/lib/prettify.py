import json


def formatAndPrint(results, toJSON=False):
    if toJSON:
        print(json.dumps(results))
        return
    s = ""
    totalCount = results["geneset"]["totalCount"]
    for symbol, stats in results.items():
        if symbol != "geneset":
            s += "{} is mutated in {:.2%} of all cases.\n".format(
                symbol,
                (totalCount - stats["noChange"]) / totalCount)
            s += "{} is copy number altered in {:.2%} of all cases.\n".format(
                symbol,
                (stats["noCopy"] + stats["multiCopy"]) / totalCount
            )

    if len(results) > 2:
        # Print aggregate stats more than one gene in results.
        s += "The gene set is altered in {:.2%} of all cases.".format(
            results["geneset"]["mutated"] / totalCount
        )
    print(s, end="")
