# ## mgfarkas final project
#
def main():

    import csv
    import os

    def target_ihpa_log(thewords):
        try:
            content = thewords.index('log')+2
            target = thewords[content:content+1]
            return target
        except:
            return "X"


    def target_county(thewords):
        try:
            content = thewords.index('county:')+1
            content1 = thewords.index('quadrangle:')
            target = thewords[content:content1]
            return target
        except:
            return "X"

    outfile = open('doc_data.csv', 'w', encoding='utf-8')

    csvout = csv.writer(outfile)

    csvout.writerow(['doc_no','ihpa_log','county'])

    path = 'small_test'

#    txtfilenames = []
#    reportcontent = []

    for file in os.scandir(path):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            txtfilename = filename[11:-4]
            infile = open(filename, 'rt')
            contents = infile.read()
            infile.close()

            contentslower = contents.lower()

            thewords = contentslower.split()

            ihpa_log = ','.join(target_ihpa_log(thewords))
            county = ','.join(target_county(thewords))

            row = [txtfilename, ihpa_log, county]
            csvout.writerow(row)


#        print(contents)


#    print(reportcontent)
#   print(txtfilenames)


main()
