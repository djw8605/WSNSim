

import re, sys, optparse

import GeneratorFile

def AddOptions(parser):
    parser.add_option("-f", "--file", dest="filename", 
                      help="File to read the simulation configuration")
    parser.add_option("-s", "--simfile", dest="simfile",
                      help="File to replace parameters in")
    parser.add_option("-d", "--destinationdir", dest="destinationdir",
                      help="Directory to put templates into")


def main():
    
    parser = optparse.OptionParser()
    AddOptions(parser)
    (opts, args) = parser.parse_args()
    generator = GeneratorFile.GeneratorFile(opts.filename)
    generator.parse()
    
    generator.writeSimFile(opts.simfile, opts.destinationdir)



if __name__ == "__main__":
    main()

