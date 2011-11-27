

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
        # <range> step <step_size> [repeat <repeat_number]
        # Where repeat is optional, default = 1
        
        # Get the range
        range_match = range_re.match(iterate_string)
        (start, end) = range_match.groups()
        print "Start = %s" % start
        print "End = %s" % end
        
        # Get the step
        try:
            step_size = float(segments[2])
            print "Step = %lf" % step_size
        except:
            print "Error parsing step: %s" % segments[2]
        
        
        
        

        