"""
Program for translating text between english and french
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    tanslation from english to french
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    tanslation from french to english
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
