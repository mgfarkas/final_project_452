# final project 452
final project for IS 452 AO class

I'm Michael. I'm an archaeologist as well as a MSLIS Student at the iSchool and the University of Illinois


This project entails creation of Python code to read through some fairly standardized Illinois archaeological compliance documents and extract some key elements. These will be saved as a CSV file for use in creation of, or, later importing new records into, a database containing the key elements of these documents.

Initially I was looking at Textract, PyPDF2, and pdfminer to extract pdf text into plain text. Difficulty getting any of these modules installed in my Windows environment has caused me to shelve that portion of the plan. This will hopefully be a later addition to my code. For now, the files were converted to plain text using Acrobat.

I hope to enhance the identification of target text elements in future versions. I hope to begin by exploration of REGEX to identify my target text and set index positions for slicing.

# TO USE
Best results derive from the code in the file named [mgfarkas_452_finalproject](/mgfarkas_452_finalproject.py)  I recommend using this.
An earlier and slightly differnt version also works but the results are not as clean and slightly different. Use code [mgfarkas_452_abandondedfinalproject.py](mgfarkas_452_abandondedfinalproject.py)  to experiment with this version.


## READ ME
This Python program attempts to extract information from text file formats of the State of Illinois Archaeological Short Survey Report form (ASSR).
It was only tested in a Windows environment!
# To use, please ensure the following:
NOTE: I have exported the files to txt and placed in a directory with the required name. The original pdf file sizes are too large to submit via moodle.
1) Place the directory of files in a directory on your computer. 
2) Place the Python file (mgfarkas_452_finalproject.py)  one directory level below the directory containing the text files.
	For example, if the files you intend to process are located at
	\\documents\files_to_process  you should place the python files in the \\documents directory
3) The output file will be formatted as csv and be named “extracted_data.csv”. In the above example of directory path, the output file will be produced in the \\documents directory. The output name can be changed by editing the file name at line 65 of the python file.
4) Run the file py file (mgfarkas_452_finalproject.py).
5) once done, open the csv file in the application of your choice and inspect the results. An entry of X in any cell indicates the targeted information could not be identified. This does not imply that information is not in the file.



With the current version, the output csv will require data cleaning! This is due to the use of non-standard format of the supposedly standarized Illinois HPA document. 
