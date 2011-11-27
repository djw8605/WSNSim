
import re, ConfigParser
import replacements
from replacements import GetReplacement

class GeneratorFile:
    def __init__(self, filename):
        self.filename = filename
        #self.iterate_re = re.compile("(\w+)\s*=\s*\[([[\d]+\.[\d]+]|[\d+])..([[\d]+\.[\d]+]|[\d+])\] step ([[\d]+\.[\d]+]|[\d+])")
        
        #self.iterate_re = re.compile("(\w+)\s*=\s*\[([\d]*\.{0,1}[\d]*)..([\d]*\.{0,1}[\d]*)\]\s+step\s+([\d]*\.{0,1}[\d]*)")
        
    def parse(self):
        # Configuration parameters
        self.params = {}
        
        parser = ConfigParser.ConfigParser()
        parser.read(self.filename)
        config_params = parser.items("main")
        print config_params
        
        for (param_name, param_value) in config_params:
            self.params[param_name] = GetReplacement(param_value)
