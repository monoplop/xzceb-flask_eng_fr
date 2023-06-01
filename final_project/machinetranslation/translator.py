from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    text = englishText
    frenchText = MyMemoryTranslator(source='en', target='fr').translate(text)
    # used for testing output to terminal
    #print(englishText + " translates to " + frenchText)
    return frenchText

def frenchToEnglish(frenchText):
    text = frenchText
    englishText = MyMemoryTranslator(source='fr', target='en').translate(text)
    # used for testing output to terminal
    #print(frenchText + " translates to " + englishText)
    return englishText

# used for testing output to terminal
# test = input()
# englishToFrench(test)