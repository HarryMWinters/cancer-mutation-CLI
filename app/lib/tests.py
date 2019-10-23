import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from symbol_ID import toID
from data_retrieval import retrieve

GENE_LIST = ["TP53", "ADIPOQ", "TTR"]
GENE = ["TP53"]

ID_LIST = ["7157", "9370", "7276"]
ID = ["7157"]


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


if __name__ == '__main__':
    unittest.main()
