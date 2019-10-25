import requests
import json


def retrieve(symbolMap, study="gbm_tcga_gistic"):
    """
    retrieve takes a dictionary of symbols and their IDs. 
    I.E. {"TP53": "1", "FAT4": "2", "PCLO": "3"} and returns 
    the mutation data associated with them in the study.

    Args:
        symbolList: A map of string Gene Symbol: string Gene Entrez ID.
        study: A string of the study ID. 
    Returns:
        A list of dictionaries where each dictionary is a gene in the study.
    Raises:
        Standard http errors if there is a problem with the request.
     """
    url = f"http://www.cbioportal.org/api/molecular-profiles/{study}/discrete-copy-number/fetch"
    querystring = {
        "discreteCopyNumberEventType": "ALL",
        "projection": "SUMMARY"
    }
    payload = {
        "entrezGeneIds": list(symbolMap.values()),
        "sampleListId": "gbm_tcga_cnaseq"
    }
    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "www.cbioportal.org",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request(
        "POST",
        url,
        json=payload,
        headers=headers,
        params=querystring
    )

    return response.json()
