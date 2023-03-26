""" Import packages"""
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('p-pEv8tlg9qPZnt_fmwyQ5qaa6OJ_cCI0QAfnA5so1Ai')
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_translator.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com')

def EnglishToFrench(English_Text):
    """English to French Translator"""
    TranslationEF = language_translator.translate(English_Text, model_id='en-fr').get_result()
    if TranslationEF == '':
        return()

    return TranslationEF['translations'][0]['translation']

def FrenchToEnglish(French_Text):
    """French to English Translator"""
    TranslationFE = language_translator.translate(French_Text, model_id='fr-en').get_result()
    if TranslationFE == '':
        return()

    return TranslationFE['translations'][0]['translation']

EnglishText = input('\nEnter the English text:')
translatedFrench = EnglishToFrench(EnglishText)
print('Translated French Text:', translatedFrench)

FrenchText = input('\nEnter the French text:')
translatedEnglish = FrenchToEnglish(FrenchText)
print('Translated English Text:', translatedEnglish)
