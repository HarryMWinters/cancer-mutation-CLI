import unittest
from symbol_ID import toID


class TestParser(unittest.TestCase):

    def test_toID_with_single_value(self):
        result = toID(["TP53"])
        self.assertEqual(result, ["7157"])

    def test_toID_with_multiple_values(self):
        result = toID(["TP53", "ADIPOQ", "TTR"])
        self.assertListEqual(result, ["7157", "9370", "7276"])

    def test_toID_with_incorrect_value(self):
        self.assertRaises(LookupError, toID, ["FOOBAR7"])


if __name__ == '__main__':
    unittest.main()
