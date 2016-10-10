#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by ayalamih on Oct. 8, 2016
# 

import sys, getopt

print len(sys.argv)
print sys.argv

def main(argv):
    print "argv:", argv

    inputfile = ""
    outputfile = ""
    targetfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:o:t:",["infile=", "outfile=", "target="])
        print "opts:", opts
        print "args:", args
    except getopt.GetoptError:
        print 'usage: -i -o -t'
        print '     : --infile= --outfile= --target='
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print 'usage: -i  -o -t'
            print '     : --infile= --outfile= --target='
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg
        elif opt in ("-o", "--outfile"):
            outputfile = arg
        elif opt in ("-t", "--target"):
            targetfile = arg

    print 'Input File : ', inputfile
    print 'Out File : ', outputfile
    print 'Target File : ', targetfile


if __name__ == "__main__":
    main(sys.argv[1:])