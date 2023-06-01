import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('hello'), 'bonjour') # test that hello translates to bonjour.

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('bonjour'),'hello') # test that bonjour translates to hello.

unittest.main()