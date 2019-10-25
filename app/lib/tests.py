#!/usr/bin/env python3

import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from symbol_ID import toID
from data_retrieval import retrieve
from data_analysis import summarize

GENE_LIST = ["TP53", "ADIPOQ", "TTR"]
GENE = ["TP53"]

ID_LIST = ["7157", "9370", "7276"]
ID = ["7157"]

MULTI_GENE_ID_MAP = {gene: id for gene, id in zip(GENE_LIST, ID_LIST)}
SINGLE_GENE_ID_MAP = {"TP53": "7157"}

SINGLE_GENE_SAMPLE = [
    {
        "uniqueSampleKey": "VENHQS0wMi0wMDMzLTAxOm51bGw",
        "uniquePatientKey": "bnVsbDpudWxs",
        "molecularProfileId": "gbm_tcga_gistic",
        "sampleId": "TCGA-02-0033-01",
        "entrezGeneId": 7157,
        "alteration": alteration
    } for alteration in [+1, -1, 0, "NA", +2, -2]
]

MULTI_GENE_SAMPLE = [
    {
        "uniqueSampleKey": "VENHQS0wMi0wMDMzLTAxOm51bGw",
        "uniquePatientKey": "bnVsbDpudWxs",
        "molecularProfileId": "gbm_tcga_gistic",
        "sampleId": "TCGA-02-0033-01",
        "entrezGeneId": geneID,
        "alteration": alteration
    } for alteration in [+1, -1, 0, "NA", +2, -2] for geneID in [7157, 9370, 7276]
]


class CancerMutationFinderCLI(unittest.TestCase):

    def test_toID_with_single_value(self):
        result = toID(GENE)
        self.assertEqual(result, ID)

    def test_toID_with_multiple_values(self):
        result = toID(GENE_LIST)
        self.assertListEqual(result, ID_LIST)

    def test_toID_with_incorrect_value(self):
        self.assertRaises(LookupError, toID, ["FOOBAR7"])

    # TODO this function should be tested from various call execution sites
    # since changing path variables represent a possible point of failure.

    @patch("requests.request")
    def test_retrieve_with_single_value(self, mock_requests):
        retrieve({"_": ID})
        self.assertTrue(mock_requests.called)
        self.assertListEqual(
            mock_requests.mock_calls[0][2]["json"]["entrezGeneIds"][0],
            ID
        )

    @patch("requests.request")
    def test_retrieve_with_multi_value(self, mock_requests):
        retrieve({"_": ID_LIST})
        self.assertTrue(mock_requests.called)
        self.assertListEqual(
            mock_requests.mock_calls[0][2]["json"]["entrezGeneIds"][0],
            ID_LIST
        )

    @patch("requests.request")
    def test_retrieve_with_NO_value(self, mock_requests):
        retrieve({"_": []})
        self.assertTrue(mock_requests.called)
        self.assertListEqual(
            mock_requests.mock_calls[0][2]["json"]["entrezGeneIds"][0],
            []
        )

    def test_summarize_with_single_value(self):
        # TODO Test values mutation type count for each type individually.
        result = summarize(SINGLE_GENE_SAMPLE, SINGLE_GENE_ID_MAP)
        expected = {
            'geneset': {
                'mutated': 4.0,
                'totalCount': 6.0
            },
            'TP53': {
                'NA': 1,
                'singleCopy': 2,
                'noCopy': 1,
                'multiCopy': 1,
                'noChange': 1
            }
        }
        self.assertEqual(expected, result)

    def test_summarize_with_multi_value(self):
        result = summarize(MULTI_GENE_SAMPLE, MULTI_GENE_ID_MAP)
        expected = {
            'geneset': {
                'mutated': 4,
                'totalCount': 6.0
            },
            'TP53': {
                'NA': 1,
                'singleCopy': 2,
                'noCopy': 1,
                'multiCopy': 1,
                'noChange': 1
            },
            'ADIPOQ': {
                'NA': 1,
                'singleCopy': 2,
                'noCopy': 1,
                'multiCopy': 1,
                'noChange': 1
            },
            'TTR': {
                'NA': 1,
                'singleCopy': 2,
                'noCopy': 1,
                'multiCopy': 1,
                'noChange': 1
            }
        }
        self.assertEqual(expected, result)

    def test_summarize_with_NO_value(self):
        self.assertRaises(IOError, summarize, [], {"_": []})


if __name__ == '__main__':
    unittest.main()
