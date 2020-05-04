#!/usr/bin/env python
import pdf_translator, os.path


file_to_translate = ""
while True:
    file_to_translate = raw_input("PDF File To Translate : ")
    if os.path.exists(file_to_translate):
        break
    else:
        print("[-] The Indicated File Does Not Exist")
        continue

output_path = raw_input("Output Destination : ")

translator = pdf_translator.PDF_English_To_Spanish_Translator(file_to_translate, output_path)
translator.translate()