
# importing required modules 
import PyPDF2
import glob, os
import codecs
import docx2txt
import win32com.client


app = win32com.client.Dispatch("Word.Application")
pathsdoc="YOU FULL PATH NAME"#Full path for word application
outfolder="txtfiles/"#path output files 
#convert pdf to txt
def convertpdf(infile,outfile):
    #open a pdf file
    pdfFileObj = open(infile, 'rb') #filename,Opens a file for reading only in binary format.
    #write permission for craeted txt file 
    outfile = codecs.open(outfolder+outfile,'w+',"utf-8") 
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

#convert docx to txtfile
def convertdocx(infile,outfile):
    docx_txt = docx2txt.process(infile)
    outfile = codecs.open(outfolder+outfile,'w+',"utf-8")
    outfile.write(docx_txt)
    outfile.close()
    

#convert doc to txtfile
def convertdoc(infile,outfile):
    try:
        
        outfile = codecs.open(outfolder+outfile,'w+',"utf-8")
        app.visible = False
        wb = app.Documents.Open(pathsdoc+str(infile))
        doc = app.ActiveDocument
        outfile.write(doc.Content.Text)
    except Exception as e:
        print(e)
    finally:
        outfile.close()
        app.Quit()
        
def findatype(infile):
    # this will return a tuple of root and extension
    split_tup = os.path.splitext(infile)
    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
    ex=str(file_extension)
    txt=".txt"
    outfile=str(file_name+txt)
    # chech the file extension to call the function
    if ex == ".pdf":
        convertpdf(infile,outfile)
    elif ex == ".docx":
        convertdocx(infile,outfile)
    elif ex == ".doc":
        convertdoc(infile,outfile)
    
# findatype(infile)
def folderssurf(folder):
    os.chdir(folder)
    for file in glob.glob("*.*"):
        infile=str(file)
        print(infile)
        findatype(infile)
folderssurf("pdfs")
