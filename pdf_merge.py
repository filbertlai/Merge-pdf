import os 
import PyPDF2

print('Welcome to the < Merge PDF program > made by Lai Filbert! Version: 2.3')
print('Please copy this program to the folder that contains the pdfs to merge')


# Name the merged pdf
new_filename=input("\nName the merged pdf: ")
new_filename+='.pdf'


# Initialization
pdfs=[]
pdf_order=[]
pdfWriter=PyPDF2.PdfFileWriter() # Create a new PdfFileWriter object which is a blank PDF document
page_count=0


# Scan pdf files
files=os.listdir('.')
for file in files:
    if (file[-4:]=='.pdf'):
        pdfs.append(file)
print('\nDetected',len(pdfs),'pdf files out of',len(files),'files!\n')


# List the order to merge
for i in range(len(pdfs)):
    print(i+1,':',pdfs[i])
    pdf_order.append(i)


# Not to merge some pdf if needed
delete=input('\nNeed to not merging some pdf(s)? (y/n) ')
if (delete=='y'):
    while (True):
        delete_order=int(input('(\'0\' if done) The number of pdf not to merge: '))
        if (delete_order==0):
            break
        else:
            delete_order-=1
            del pdfs[delete_order]
            print("Okay!")
            for i in range(len(pdfs)):
                print(i+1,':',pdfs[i])
            print()


# Change the order to merge if needed
change_order=input('\nNeed to change the order? (y/n) ')
if (change_order=='y'):
    for i in range(len(pdfs)):
        pdf_order[i]=int(input(str(i+1)+' th file should be number: '))-1
        

# Add all pages in those pdf to target pdf
for i in range(len(pdfs)):
    pdfFile=open(pdfs[pdf_order[i]],'rb') # Open the pdf file
    
    pdfReader=PyPDF2.PdfFileReader(pdfFile) # Read the file

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj) # Add page to the target pdf file
        page_count+=1


# Ouput target pdf
pdfOutputFile = open(new_filename, 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile.close()
print('\nMerged Successfully that named as <',new_filename,'> with',page_count,'pages !')
end=input()
