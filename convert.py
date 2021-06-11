# importing required modules 
import PyPDF2
import glob, os
import codecs
import docutils

def convertpdf(infile,outfile):
    pdfFileObj = open(infile, 'rb') 
    basicfile = open(outfile, 'x')
    outfile = codecs.open(outfile,'w',"utf-8")
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file 
    pages=pdfReader.numPages 
    for page in range(0,pages):
        # creating a page object
        pageObj = pdfReader.getPage(page)
        # extracting text from page 
        pagetxt=pageObj.extractText()
        outfile.write(pagetxt)
    # closing the pdf file object 
    pdfFileObj.close()
    outfile.close()
    basicfile.close()

def findatype(infile):
    # this will return a tuple of root and extension
    split_tup = os.path.splitext(infile)
    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
    print("File Name: ", file_name)
    print("File Extension: ", file_extension)
    ofile=".txt"
    efile=str(file_name+ofile)
    convertpdf(infile,efile)
# findatype(infile)
def folderssurf(folder):
    os.chdir(folder)
    for file in glob.glob("*.pdf"):
        infile=str(file)
        findatype(infile)
folderssurf("pdfs")
