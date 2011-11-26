

import re, sys, optparse

import GeneratorFile

def AddOptions(parser):
    parser.add_option("-f", "--file", dest="filename", 
                      help="File to read the simulation configuration")


def main():
    
    parser = optparse.OptionParser()
    AddOptions(parser)
    (opts, args) = parser.parse_args()
    generator = GeneratorFile.GeneratorFile(opts.filename)
    generator.parse()
    



if __name__ == "__main__":
    main()

