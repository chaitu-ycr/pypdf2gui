from PyPDF2.pdf import PdfFileReader
from PyPDF2 import PdfFileMerger


class PyPdf2:
    def __init__(self):
        pass

    def merge_pdf(self, list_of_pdf):
        pass


pdf_file1 = PdfFileReader("dummy_pdf_file_1.pdf")
pdf_file2 = PdfFileReader("dummy_pdf_file_2.pdf")
pdf_file3 = PdfFileReader("dummy_pdf_file_3.pdf")
output = PdfFileMerger()
output.append(pdf_file1)
output.append(pdf_file2)
output.append(pdf_file3)
output.write("merged.pdf")
