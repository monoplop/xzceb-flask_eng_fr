"""
Tests for verifying tanslation between english and french
"""
import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    """
    Tests for verifying tanslation from english to french
    """

    def test1(self):
        # test that hello translates to bonjour.
        self.assertEqual(english_to_french('hello'), 'bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    """
    Tests for verifying tanslation from french to english
    """

    def test1(self):
        # test that bonjour translates to hello.
        self.assertEqual(french_to_english('bonjour'), 'hello')


unittest.main()
