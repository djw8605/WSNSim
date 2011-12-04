

import re, sys, optparse
import ConfigParser
import GeneratorFile
import condorSubmit

def AddOptions(parser):
    parser.add_option("-f", "--file", dest="filename", 
                      help="File to read the simulation configuration")
    parser.add_option("-s", "--simfile", dest="simfile",
                      help="File to replace parameters in")
    parser.add_option("-d", "--destinationdir", dest="destinationdir",
                      help="Directory to put templates into")
    parser.add_option("-u", "--submissionfile", dest="submissionfile",
                      help="File to create for condor submission")


def main():
    
    parser = optparse.OptionParser()
    AddOptions(parser)
    (opts, args) = parser.parse_args()
    generator = GeneratorFile.GeneratorFile(opts.filename)
    generator.parse()
    
    simfiles = generator.writeSimFile(opts.simfile, opts.destinationdir)
    
    condor_submit = condorSubmit.CondorSubmit(opts.submissionfile)
    condor_submit.setSimulationFiles(simfiles)
    
    config_parser = ConfigParser.ConfigParser()
    config_parser.read(opts.filename)
    tcl_location = config_parser.get("submission", "tcl_loc")
    ns_location = config_parser.get("submission", "ns_loc")
    condor_submit.setAdditionalTransferInputFiles([tcl_location, ns_location])
    condor_submit.writeSubmissionFile()


if __name__ == "__main__":
    main()

