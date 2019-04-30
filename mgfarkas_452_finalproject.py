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
            contentstart = thewords.index('county:')+1
            contentend = thewords.index('quadrangle:')
            target = thewords[contentstart:contentend]
            return target
        except:
            return "X"

    def target_guadrangle(thewords):
        try:
            contentstart = thewords.index('quadrangle:')+1
#            contentend = thewords.index('project type/title:')
            target = thewords[contentstart:contentstart +4]
            return target
        except:
            return "X"


    def target_archaeologist(thewords):
        try:
            contentstart = thewords.index('contractor:')+1
            contentend = thewords.index('address/phone:')
            target = thewords[contentstart:contentend]
            return target
        except:
            return "X"


    def target_agency(thewords):
        try:
            contentstart = thewords.index('agency:')+1
            target = thewords[contentstart:contentstart+2]
            return target
        except ValueError:
            pass
        try:
            contentstart2 = thewords.index('agencies:')+1
            target2 = thewords[contentstart2:contentstart2+2]
            return target2
        except:
            return "X"



    outfile = open('doc_data2.csv', 'w', encoding='utf-8', newline = '')

    csvout = csv.writer(outfile)

    csvout.writerow(['doc_no','ihpa_log', 'agency', 'archaeologist', 'county', 'quadmap'])

    path = 'small_test'


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
            archaeologist_dirty = ','.join(target_archaeologist(thewords))
            county = ''.join(target_county(thewords))
            quad_map_dirty = ','.join(target_guadrangle(thewords))
            quadmap_clean = quad_map_dirty.replace(',',' ')
            archaeologist = archaeologist_dirty.replace(',',' ')
            agency = ' '.join(target_agency(thewords))

            row = [txtfilename, ihpa_log, agency, archaeologist, county, quadmap_clean]
            csvout.writerow(row)


#            print(archaeologist_dirty)


#    print(reportcontent)
#   print(txtfilenames)


main()

