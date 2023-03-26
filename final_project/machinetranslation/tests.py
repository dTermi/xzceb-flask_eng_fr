import unittest
from translator import EnglishToFrench, FrenchToEnglish

class TestEtF(unittest.TestCase):
    def test1(self):
        self.assertEqual(EnglishToFrench(' '), ' ') # test when null is given as input the output is null.
        self.assertEqual(EnglishToFrench('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.

class TestFtE(unittest.TestCase):
    def test1(self):
        self.assertEqual(FrenchToEnglish(' '), ' ') # test when null is given as input the output is null.
        self.assertEqual(FrenchToEnglish('Bonjour'), 'Hello') # test when 'Hello' is given as input the output is 'Bonjour'.

if __name__ == '__main__':
    unittest.main()