import pyperclip
from googletrans import Translator

translator = Translator()

while True:
    pyperclip.waitForNewPaste()
    copied_text = pyperclip.paste()
    tr = translator.translate(copied_text, dest='pl').text
    print(tr)