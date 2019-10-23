from lib.parser import parse
from lib.entrez_gene import toID
from lib.TCGA import retrieve
from lib.analyzer import summarize


def main():
    geneSymbols = parse()
    geneIDs = toID(geneSymbols)
    symbolMap = {symbol: gID for symbol, gID in zip(geneSymbols, geneIDs)}
    # ToDo this fails silently for unrecognized gene symbols
    samples = retrieve(symbolMap)
    outputDict = summarize(samples, symbolMap)
    # Symbol:   [mutationFraction, copyNumberFraction]
    # Geneset:  [mutationFraction]
    print(outputDict)
    # for k, v in outputDict.items():
    #     if v["error"]:
    #         print(f"{k} failed. {v['error']}")
    #     else:
    #         mutationPercentage = (
    #             v["singleCopy"] + v["noCopy"] + v["multiCopy"]) / v["total"]
    #         s1 = "{0} is mutated in {1:.2%} of all cases.\n".format(
    #             k, mutationPercentage)
    #         copyNumberPercentage = (v["noCopy"] + v["multiCopy"]) / v["total"]
    #         s2 = "{0} is copy number altered in {1:.2%} of all cases.\n".format(
    #             k, copyNumberPercentage)
    #         print(s1 + s2, end="")


if __name__ == "__main__":
    main()
