

import re, sys, optparse

import GeneratorFile

def AddOptions(parser):
    parser.add_option("-f", "--file", dest="filename", 
                      help="File to read the simulation configuration")


def main():
    
    parser = optparse.OptionParser()
    AddOptions(parser)
    
    



if __name__ == "__main__":
    main()

