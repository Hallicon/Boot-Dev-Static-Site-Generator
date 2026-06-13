import unittest
from main import *


class TestMain(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(
            extract_title("# Hello"),
            "Hello"
        )


if __name__ == "main":
    unittest.main()
