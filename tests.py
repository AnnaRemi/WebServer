import unittest
from PyDictionary import PyDictionary


class API_Tester(unittest.TestCase):
    ok = 200

    def setUp(self):
        self.dictionary = PyDictionary

    def test_meaninig(self):
        self.assertEqual(self.dictionary.meaning("play").status_code, ok)

<<<<<<< HEAD
    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "fr").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "zh-Hant").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "de").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "it").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "hi").status_code, ok)

    def test_translate(self):
        self.assertEqual(self.dictionary.translate("go", "es").status_code, ok)
=======
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
>>>>>>> e994ed6a6cbed90a05c59b00761c03c47809ef5f


if __name__ == '__main__':
    unittest.main()
<<<<<<< HEAD


=======
>>>>>>> e994ed6a6cbed90a05c59b00761c03c47809ef5f
