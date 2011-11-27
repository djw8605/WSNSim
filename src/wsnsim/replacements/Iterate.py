

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
        # <range> step <step_size> [repeat <repeat_number>]
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
        
        # Check for a repeats option
        self.has_repeat = False
        if len(segments) > 3:
            self.has_repeat = True
            try:
                self.repeat = int(segments[4])
                print "Repeats = %i" % self.repeat
            except:
                print "Error parsing repeat: %s" % segments[4]
        

        