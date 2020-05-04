#!/usr/bin/env python
from googletrans import Translator
import PyPDF2, os, subprocess

class PDF_English_To_Spanish_Translator:

    def remove_file_permissions(self, path_file_name):
        subprocess.check_call(["chmod", "777", path_file_name])
        print("[+] Removing Administrator Permissions From " + str(path_file_name))

    def __init__(self, pdf_name, output_destination):
        self.translator = Translator()
        self.pdf_book = open(pdf_name, "rb")
        self.pdfreader  = PyPDF2.PdfFileReader(self.pdf_book)
        self.pdf_book_translated_pages = {}
        pdf_name_to_use = pdf_name.replace(".pdf", "")
        self.output_path = "{}/{}{}".format(output_destination, pdf_name_to_use," Translated.txt")
        self.delete_options = ["1", "2"]

    def translate(self):
        for page in self.pdfreader.pages:
            page_num = self.pdfreader.getPageNumber(page)+1
            total_translated_text = ""
            try:
                for text in self.translator.translate(page.extractText(), "es", "en").text.split():
                    total_translated_text = total_translated_text + " " + text.replace(str(page_num), "")
                print("[+] Translating Page " + str(page_num))
            except TypeError:
                print("[!] Page Number {} has no text".format(str(page_num)))
                continue
            self.pdf_book_translated_pages[page_num] = total_translated_text
        try:
            os.mknod(self.output_path)
        except OSError:
            print("""[!] The file already exists in such path
Do you wish to delete it ?
1) Yes
2) No
""")
            while True:
                delete = raw_input("> ")
                if delete not in self.delete_options:
                    print("[-] Enter a valid option")
                    continue
                elif delete == "1":
                    os.remove(self.output_path)
                    print("[+] Removing File")
                    break
                else:
                    print("[!] Program Quitting...")
                    exit()

        with open(self.output_path, "w") as file:
            print("[+] Making Output File")
            for page in self.pdf_book_translated_pages:
                file.write((self.pdf_book_translated_pages[page] + "\n").encode(encoding="utf-8"))
            print("[+] Translation Successful")
        self.remove_file_permissions(self.output_path)