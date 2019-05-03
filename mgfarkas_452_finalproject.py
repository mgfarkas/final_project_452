# ## mgfarkas 452 final project
#
def main():

#importing the two required modules
    import csv
    import os

# defining first function. Identifies and slices out the IHPA Log number in the file
    def target_ihpa_log(thewords):
        try:
            content = thewords.index('log')+2# start of the log id string
            target = thewords[content:content+1]# slicing out my first target
            return target
        except:
            return "X"# on error (unable to find the slice start or end) returns an X

# second function. Identifies and slices out the county name.
    def target_county(thewords):
        try:
            contentstart = thewords.index('county:')+1# slice start is word past the start
            contentend = thewords.index('quadrangle:')# the slice end.
            target = thewords[contentstart:contentend]# The county name is between "County:" and "Quadrangle:"
            return target
        except:
            return "X"# on error (unable to find the slice start or end) returns an X

# third function. Finds and slices the map name (quadrangle is map name).
    def target_guadrangle(thewords):
        try:
            contentstart = thewords.index('quadrangle:')+1# the slice start
#            contentend = thewords.index('project type/title:')# initially was slice end (based on official format of document. But, in reality, the end was inconsistent
            target = thewords[contentstart:contentstart +4]# sliced on 4 positions after start. Leaves some errant stuff in slice but best results overall
            return target
        except:
            return "X"

# fourth function targets the name of the archaeological contractor
    def target_archaeologist(thewords):
        try:
            contentstart = thewords.index('contractor:')+1
            contentend = thewords.index('address/phone:')
            target = thewords[contentstart:contentend]# info should be between "contractor:" and "address/phone:"
            return target
        except:
            return "X"

# fifth function targets the agency for whome report completed
    def target_agency(thewords):
        try:
            contentstart = thewords.index('agency:')+1
            target = thewords[contentstart:contentstart+2]# target is an acronym after "agency:"
            return target
        except ValueError:# realized many documents use "agencies" rather than the official "agency"
            try:# so created a nested try except
                contentstart2 = thewords.index('agencies:')+1
                target2 = thewords[contentstart2:contentstart2+2]
                return target2
            except:
                return "X"



# set my outfile. Added "newline = '' " otherwise output created alternating blank rows in output csv
    outfile = open('extracted_data.csv', 'w', encoding='utf-8', newline = '')

# set the variable csvout to the csv writer function and outfile as the parameter
    csvout = csv.writer(outfile)

# writing the csv header row
    csvout.writerow(['doc_no','ihpa_log', 'agency', 'archaeologist', 'county', 'quadmap'])

# setting the path variable to the directory holding the files I will iterate over
    path = path = 'files_to_process'

# the for loop where I iterate over the files in the path
    for file in os.scandir(path):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):# filtering so to only try to process text files
            txtfilename = filename[17:-4]# capturing the file name and slicing off leading directory path and the .txt extension
            infile = open(filename, 'rt')# now opening the file and assigning to infile variable
            contents = infile.read()# using .read to grab entire file contents as a single string
            infile.close()# closing the file

            contentslower = contents.lower()# all to lower case to help the .index in the functions find targets due to inconsistent text entryin the documents

            thewords = contentslower.split()# converting the string to a list (each word complete with punctation (to index pattern "word: ")

# assigning variables for my targeted text. Feeding the list of words into my functions
# then using .join to convert the list to string
# and minor additional cleaning by re-inserting a whitespace for commas for some where output required
            ihpa_log = ','.join(target_ihpa_log(thewords))
            archaeologist_dirty = ','.join(target_archaeologist(thewords))
            county = ''.join(target_county(thewords))
            quad_map_dirty = ','.join(target_guadrangle(thewords))
            quadmap_clean = quad_map_dirty.replace(',',' ')
            archaeologist = archaeologist_dirty.replace(',',' ')
            agency = ' '.join(target_agency(thewords))

# creating a list called row and adding my collected variables from above.
# order matches the csv header from above
# then writing that row to the csv file
            row = [txtfilename, ihpa_log, agency, archaeologist, county, quadmap_clean]
            csvout.writerow(row)



main()
