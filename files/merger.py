from PyPDF2 import PdfFileMerger

def merger(files, filename):
    output_file = './files/' + filename + '.pdf'
    merger = PdfFileMerger()

    for pdf in files:
        merger.append(open(pdf, 'rb'))

    with open(output_file, 'wb') as output:
        merger.write(output)