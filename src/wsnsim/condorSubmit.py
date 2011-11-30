


class CondorSubmit:
    def __init__(self, submission_file):
        self.submit_file = submission_file
        self.init_submission_dict()
        
    def init_submission_dict(self):
        self.submission_dict = {"universe": "vanilla",
                                "log": "condor.log",
                                "out": "output",
                                "error": "error",
                                "executable": "submission.sh",
                                "should_transfer_files": "YES",
                                "when_to_transfer_output": "ON_EXIT"
                                }
    
    def setSimulationFiles(self, simulationFiles):
        self.simulationFiles = simulationFiles
        
    
    def writeSubmissionFile(self):
        fpointer = open(self.submit_file, 'w')
        
        for file in self.simulationFiles:
            self._writeCondorFile(file, fpointer)
            
        fpointer.close()


    def _writeCondorFile(self, file, fpointer):
        # Set the submission dict
        self.submission_dict["out"] = file + ".out"
        self.submission_dict["error"] = file + ".err"
        self.submission_dict["arguments"] = file
        self.submission_dict["transfer_input_files"] = file
        
        f = open(self.submit_file, 'a')
        fpointer.write(self._formatDict(self.submission_dict))
        fpointer.write("queue\n")

        
    
    
    def _formatDict(self, fdict):
        toReturn = ""
        for key in fdict.keys():
            toReturn += "%s = %s\n" % (key, fdict[key])
        return toReturn
        
        