#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install PyPDF2')


# In[2]:


from PyPDF2 import PdfFileReader,PdfFileWriter


# In[4]:


### open the current pdf
file_pdf=PdfFileReader('C:/Users/sshas/OneDrive/Desktop/Resume/LOR.pdf')
### Object for pdf writer
out_pdf=PdfFileWriter()


# In[5]:


file_pdf


# In[6]:


for i in range(file_pdf.numPages):
    page_details=file_pdf.getPage(i)
    ### Add to the output page
    out_pdf.addPage(page_details)


# In[7]:


password="shank@2021"

out_pdf.encrypt(password)


# In[8]:


with open("encryptedLOR.pdf","wb") as filename:
    out_pdf.write(filename)


# In[ ]:




