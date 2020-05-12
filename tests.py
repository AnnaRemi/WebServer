import unittest
from PyDictionary import PyDictionary

class API_Tester(unittest.TestCase):
    def setUp(self):
        self.dictionary = PyDictionary
    def test_meaninig(self):
        self.assertEqual(self.dictionary.meaning("play").status_code, 200)
    def test_translate(self):
        self.assertEqual(self.dictionary.translate("play", "cy").status_code, 200)
    def test_translate(self):
        self.assertEqual(self.dictionary.translate("play", "es").status_code, 200)
    def test_translate(self):
        self.assertEqual(self.dictionary.translate("play", "de").status_code, 200)
    def test_translate(self):
        self.assertEqual(self.dictionary.translate("play", "it").status_code, 200)
    def test_translate(self):
        self.assertEqual(self.dictionary.translate("play", "hi").status_code, 200)


if __name__ == '__main__':
    unittest.main()
        
        
