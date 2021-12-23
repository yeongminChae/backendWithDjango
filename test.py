import googletrans
from googletrans import Translator
 
# print(googletrans.LANGUAGES)
 
text1 = "Hello welcome to my website!"
 
translator = Translator()
trans1 = translator.translate(text1, src='en', dest='ko')
print("English to Japanese: ", trans1.text)

# LANGUAGES = {
    # 'en': 'english',    
    # 'it': 'italian',
    # 'ko': 'korean',
    # 'pt': 'portuguese',
    # 'ru': 'russian',
    # 'es': 'spanish',
    # 'tr': 'turkish',
    # 'de': 'german',}