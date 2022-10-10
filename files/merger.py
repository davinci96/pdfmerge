from PyPDF2 import PdfFileMerger

def merger(files):
    output_file = './files/test.pdf'
    merger = PdfFileMerger()

    for pdf in files:
        merger.append(open(pdf, 'rb'))

    with open(output_file, 'wb') as output:
        merger.write(output)