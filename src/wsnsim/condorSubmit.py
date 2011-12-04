


class CondorSubmit:
    def __init__(self, submission_file):
        self.submit_file = submission_file
        self.additional_input = []
        self.init_submission_dict()
        
    def init_submission_dict(self):
        self.submission_dict = {"universe": "vanilla",
                                "log": "condor.log",
                                "output": "output",
                                "error": "error",
                                "executable": "share/submission.sh",
                                "should_transfer_files": "YES",
                                "when_to_transfer_output": "ON_EXIT"
                                }
        self.submission_dict["transfer_input_files"] = []
        for file in self.additional_input:
            self.submission_dict["transfer_input_files"].append(file)
        
    
    def setSimulationFiles(self, simulationFiles):
        self.simulationFiles = simulationFiles
    
    def setAdditionalTransferInputFiles(self, inputfiles):
        for file in inputfiles:
            self.additional_input.append(file)    
    
    def writeSubmissionFile(self):
        fpointer = open(self.submit_file, 'w')
        
        for file in self.simulationFiles:
            self._writeCondorFile(file, fpointer)
            
        fpointer.close()


    def _writeCondorFile(self, file, fpointer):
        # Set the submission dict
        self.init_submission_dict()
        self.submission_dict["output"] = file + ".out"
        self.submission_dict["error"] = file + ".err"
        self.submission_dict["arguments"] = file
        self.submission_dict["transfer_input_files"].append(file)
        
        f = open(self.submit_file, 'a')
        fpointer.write(self._formatDict(self.submission_dict))
        fpointer.write("queue\n")

        
    
    
    def _formatDict(self, fdict):
        toReturn = ""
        for key in fdict.keys():
            if key == "transfer_input_files":
                toReturn += "%s = %s\n" % (key, ", ".join(fdict[key]))
            else:
                toReturn += "%s = %s\n" % (key, fdict[key])
        return toReturn
        
        