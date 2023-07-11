import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pagenos = pdfreader.numPages

for num in range(0, pagenos):
    pagenos = pdfreader.getPage(num)
    text = pagenos.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()

    