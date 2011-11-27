

import re

range_re = re.compile("^\s*\[([\d]*\.{0,1}[\d]*)\.\.([\d]*\.{0,1}[\d]*)\]")


class Iterate:
    def __init__(self, iterate_string):
        
        self.iterate_string = iterate_string
        self._parse(self.iterate_string)
        
    def _parse(self, iterate_string):
        # First, split the string
        segments = iterate_string.split()
        
        # Segments should be:
        # <range> step <step_size> [default <default_number] [repeat <repeat_number>]
        # Where repeat is optional, default = 1
        
        # Get the range
        range_match = range_re.match(iterate_string)
        (self.start, self.end) = range_match.groups()
        print "Start = %s" % self.start
        print "End = %s" % self.end
        
        # Get the step
        try:
            self.step_size = float(segments[2])
            print "Step = %lf" % self.step_size
        except:
            print "Error parsing step: %s" % segments[2]
        
        # Check for options parameters
        parsed_optional_params = segments[3:]
        print parsed_optional_params
        self.optional_params = {}
        for param_name, param_value in parsed_optional_params:
            self.optional_params[param_name] = param_value

        print self.optional_params

        