 from deep_translator import MyMemoryTranslator

 def englishToFrench(englishText):
    text = englishText
    frenchText = MyMemoryTranslator(source='en', target='fr').translate(text)
    return frenchText

def frenchToEnglish(frenchText):
    text = frenchText
    englishText = MyMemoryTranslator(source='fr', target='en').translate(text)
    return englishText