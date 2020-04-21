import pdf2image
import PyPDF2
from PIL import Image
import matplotlib.pyplot as plt


def showImage(nPage):

    images = pdf2image.convert_from_path('prueba.pdf')

    for index, val in enumerate(images):
        if index == nPage:
            plt.imshow(val)
            plt.show()
            print("encontrao")
            break

def searchWord(word):

    pdfFileObj = open('prueba.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    for page in range(pdfReader.numPages): 
        pageObj = pdfReader.getPage(page)
        text = pageObj.extractText()
        if text.find(word) != -1:
            showImage(page)

    pdfFileObj.close()