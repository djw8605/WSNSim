
import re


class GeneratorFile:
    def __init__(self, filename):
        self.filename = filename
        self.iterate_re = re.compile("(\w+)\s*=\s*\[([[\d]+\.[\d]+]|[\d+])..([[\d]+\.[\d]+]|[\d+])\] step ([[\d]+\.[\d]+]|[\d+])")
        self.iterate_re = re.compile("(\w+)\s*=\s*\[([\d]*\.{0,1}[\d]*)..([\d]*\.{0,1}[\d]*)\]\s+step\s+([\d]*\.{0,1}[\d]*)")
        
    def parse(self):
        f = open(self.filename)
        for line in f.readlines():
            iterate_match = self.iterate_re.search(line)
            if iterate_match:
                print "Found iterate"
                print iterate_match.groups()
