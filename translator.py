#English to Bangali Translator
from googletrans import Translator
 
translator = Translator()
f = open("English.txt","r", encoding="utf-8")
g = open("Bengali.txt","w", encoding="utf-8")

val = (f.read())
translations = translator.translate( [str(val)], dest='bn')
for translation in translations:
    g.write(str(translation.text))
g.close()
print("Translation Completed")
f.close()