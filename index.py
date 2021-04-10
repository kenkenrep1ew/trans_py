from googletrans import Translator
src = "สวัสดี"
translator = Translator(service_urls=['translate.googleapis.com'])
print(translator.translate(src, dest="en").text)