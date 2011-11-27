

import re
from replacements.GenericReplacement import GenericReplacement

range_re = re.compile("^\s*\[([\d]*\.{0,1}[\d]*)\.\.([\d]*\.{0,1}[\d]*)\]")


class Iterate(GenericReplacement):
    def __init__(self, iterate_string):
        
        self.iterate_string = iterate_string
        self._parse(self.iterate_string)
        
        self.pointer = self.start
        self.repeat_counter = 0
        
        
    def _parse(self, iterate_string):
        # First, split the string
        segments = iterate_string.split()
        
        # Segments should be:
        # <range> step <step_size> [default <default_number] [repeat <repeat_number>]
        # Where repeat is optional, default = 1
        
        # Get the range
        range_match = range_re.match(iterate_string)
        (self.start, self.end) = range_match.groups()
        self.start = float(self.start)
        self.end = float(self.end)
        #print "Start = %s" % self.start
        #print "End = %s" % self.end
        
        # Get the step
        try:
            self.step_size = float(segments[2])
            #print "Step = %lf" % self.step_size
        except:
            print "Error parsing step: %s" % segments[2]
        
        # Check for options parameters
        parsed_optional_params = segments[3:]
        self.optional_params = {}
        param_name = ""
        for param in parsed_optional_params:
            if param_name == "":
                param_name = param
            else:
                self.optional_params[param_name] = param
                param_name = ""

        #print self.optional_params


    def GetNextValue(self):
        '''
        Get the next value in the iteration.  
        The values will roll over after GetNumberOfValues calls.
        '''
        if self.optional_params.has_key("repeat"):
            self.repeat_counter += 1
            if self.repeat_counter >= int(self.optional_params["repeat"]):
                self.repeat_counter = 0
            else:
                return self.pointer
        
        # If repeat is turned off, or it's time to iterate
        toReturn = self.pointer
        self.pointer += self.step_size
        if self.pointer > self.end:
            self.pointer = self.start
            
        return toReturn

        
    def GetNumberOfValues(self):
        if self.optional_params.has_key("repeat"):
            return int((self.end - self.start) / self.step_size) * int(self.optional_params["repeat"])
        else:
            return int((self.end - self.start) / self.step_size)
    
    
        