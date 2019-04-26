# final project 452
final project for IS 452 AO class

I'm Michael. I'm an archaeologist as well as a MSLIS Student at the iSchool and the University of Illinois


This project entails creation of Python code to read through some fairly standardized Illinois archaeological compliance documents and extract some key elements. These will be saved as a CSV file for use in creation of, or, later importing new records into, a database containing the key elements of these documents.

Initially I was looking at Textract, PyPDF2, and pdfminer to extract pdf text into plain text. Difficulty getting any of these modules installed in my Windows environment has caused me to shelve that portion of the plan. This will hopefully be a later addition to my code. For now, the files were converted to plain text using Acrobat.

I hope to enhance the identification of target text elements in future versions. I hope to begin by exploration of REGEX to identify my target text and set index positions for slicing.

# TO USE
1) Convert your text files to plain text and store these in a directory on your machine.
     I have experienced issues with the encoding of the files exported from Acrobat. Acrobat was set to export as UTF-8. However, there was      some issue here. The files are actually windows-1252. 
     
2) Set you directory in the .py file to the directory where the text files are located. This is assigned to the 'path' variable in the script.

3) The output file is named 'doc_data.csv'. You can rename this in the file. Or, if making multiple use of the script, copy or rename the csv after each run. Otherwise, the file will be overwritten.

With the current version, the output csv will require data cleaning! This is due to the use of non-standard format of the supposedly standarized document. 
