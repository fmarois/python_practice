#!/usr/bin/python

#Script test for a vlookup in python

#

import sys, getopt

#Elements to find

def main(argv):
    listtofind = ''
    filetolook = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hl:i:o:",["lfile=","ifile=","ofile="])
    except getopt.GetoptError:
        print 'first_pr.py -l <listtofind> -i <filetolook> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'first_pr.py -l <listtofind> -i <filetolook> -o <outputfile>'
            sys.exit()
        elif opt in ("-l","--lfile"):
            listtofind=arg
        elif opt in ("-i","--filetolook"):
            filetolook= arg
        elif opt in ("-o","--outputfile"):
            outputfile=arg
    
    print listtofind
    print filetolook
    print outputfile

if __name__ == "__main__":
    main(sys.argv[1:])

