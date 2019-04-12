import os

# set this to directory where files are stored
path = 'files'

# for now, accumulating everything as lists
# will define variables and find that info in file next
txtfilenames = []
reportcontent = []

for file in os.listdir(path):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        txtfilenames.append(filename[0:-4])# slicing off the file extension to create document number
        f = open(filename, 'rt')
        contents = f.read()
        reportcontent.append(contents)
#        print(contents)

print(reportcontent)
print(txtfilenames)
