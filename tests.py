import unittest
from PyDictionary import PyDictionary


class API_Tester(unittest.TestCase):
    ok = 200

    def setUp(self):
        self.dictionary = PyDictionary

    def test_meaninig(self):
        self.assertEqual(self.dictionary.meaning("play").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "cy").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "es").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "de").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "it").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "hi").status_code, ok)


if __name__ == '__main__':
    unittest.main()
