# Этот код находит все PDF документы внутри текущей папки в подпапках,
# и переименовывет их согласно кадастровому номеру из документа

import os
import os.path
import re
from PyPDF2 import PdfFileReader
from pdfrw import PdfReader, PdfWriter


def GetCadastralNumber(filename):
    with open(filename, "rb") as filehandle:
        pdf = PdfFileReader(filehandle)
        pages = pdf.getNumPages()
        for i in range(pages):
            page = pdf.getPage(i)
            txt = page.extractText()
            x = re.search("Кадастровый номер:", txt)
            if x.end(0) > 0:
                step = 25
                string = txt
                find = string[x.end(0):x.end(0) + step]
                x2 = re.search("\n", find)
                find = string[x.end(0) + 1:x.end(0) + x2.start(0)]
                print(find)
                return find


def GetPDFFiles():
    s = []
    pdf = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            s.append(filename)

    for i in s:
        x = re.search(r".pdf", i)
        if x is not None:
            pdf.append(i)
            # print(i)
    return pdf


def Start():
    for i in GetPDFFiles():
        newName = GetCadastralNumber(i).replace(":", "_")
        # print(i)
        if not os.path.exists(newName + ".pdf"):
            os.rename(i, newName + ".pdf")


Start()  # код начинается здесь
