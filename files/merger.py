from PyPDF2 import PdfFileMerger
import os

def merger(filename, files):
    output_file = './files/result/' + filename

    old_files = os.listdir('./files/temp')
    old_results = os.listdir('./files/result')

    for file in old_results:
        os.remove('./files/result/' + file)

    if os.path.exists(output_file):
        os.remove(output_file)

    merger = PdfFileMerger()

    for pdf in files:
        merger.append(open(pdf, 'rb'))

    with open(output_file, 'wb') as output:
        merger.write(output)
    
    for file in old_files:
        os.remove('./files/temp/' + file)






