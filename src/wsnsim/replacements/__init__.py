

import re

from replacements import Iterate 


# This file defines the different type of iterators available
iterate_re = re.compile("^\s*\[[\d|\.]*\]\s+step\s+[\d|\.]+.*")

def GetReplacement(param_string):
    
    if iterate_re.match(param_string):
        print "Found iterates"
        return Iterate.Iterate(param_string)
    
    
