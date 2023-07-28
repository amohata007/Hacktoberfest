import pypdf2
import pyttsx3
book=open("ops.pdf","rb")
pdfReader = pypdf2.pdfFileReader(book)
pageg = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getpage(7)
for num in range(7,pages):
    page = pdfReader.getpage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
