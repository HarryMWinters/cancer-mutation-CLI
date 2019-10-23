import requests
import json


def retrieve(symbolMap):

    study = "gbm_tcga_gistic"
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
