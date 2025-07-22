import PyPDF2
import sys
import os
#merger pdf files into 1 file

merger = PyPDF2.PdfFileMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combinedDocs.pdf")
