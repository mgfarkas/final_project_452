# ## mgfarkas final project bAD
#
def main():

    import csv
    import os

    def target_ihpa_log(thewords):
        try:
            content = thewords.find('ihpa log ')
            temptarget = thewords[content:content+25]
            temptarget2 = temptarget.split()
            result = temptarget2[3:]
            target = ''.join(result)
            return target
        except:
            return "missed"


    def target_county(thewords):
        try:
            contentstart = thewords.find('county:')
            contentend = thewords.find('quadrangle:')
            temptarget = thewords[contentstart:contentend]
            temptarget2 = temptarget.split()
            result = temptarget2[1:]
            target = ''.join(result)
            return target
        except:
            return "missed"


    def target_quadrangle(thewords):
        try:
            contentstart = thewords.find('quadrangle:')
            contentend = thewords.find('project type/title:')
            temptarget = thewords[contentstart:contentend]
            temptarget2 = temptarget.split()
            result = temptarget2[1:]
            target = ''.join(result)
            return target
        except:
            return "missed"

    def target_archaeologist(thewords):
        try:
            contentstart = thewords.find('archaeological contractor:')
            contentend = thewords.find('address/phone:')
            temptarget = thewords[contentstart:contentend]
            temptarget2 = temptarget.split()
            result = temptarget2[2:]
            target = ''.join(result)
            return target
        except:
            return "missed"


    outfile = open('doc_data_mgfarkas.csv', 'w', encoding='utf-8', newline = '')

    csvout = csv.writer(outfile)

    csvout.writerow(['doc_no','ihpa_log', 'archaeologist','county', 'quadmap'])

    path = 'small_test'


    for file in os.scandir(path):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            txtfilename = filename[11:-4]
            infile = open(filename, 'rt')
            contents = infile.read()
            infile.close()

            contentslower = contents.lower()


#            thewords = contentslower.split()

            ihpa_log = target_ihpa_log(contentslower).capitalize()
            county = target_county(contentslower).capitalize()
            quadmap = target_quadrangle(contentslower).capitalize()
            archaeologist = target_archaeologist(contentslower).capitalize()
            row = [txtfilename, ihpa_log, archaeologist, county, quadmap]
            csvout.writerow(row)
#            print(row)


#        print(contents)


#    print(reportcontent)
#   print(txtfilenames)


main()
