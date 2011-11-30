
import re, ConfigParser
import replacements
from replacements import GetReplacement
import os, sys

class GeneratorFile:
    def __init__(self, filename):
        self.filename = filename
        self._filecounter = 0
        self._simfiles = []
        #self.iterate_re = re.compile("(\w+)\s*=\s*\[([[\d]+\.[\d]+]|[\d+])..([[\d]+\.[\d]+]|[\d+])\] step ([[\d]+\.[\d]+]|[\d+])")
        
        #self.iterate_re = re.compile("(\w+)\s*=\s*\[([\d]*\.{0,1}[\d]*)..([\d]*\.{0,1}[\d]*)\]\s+step\s+([\d]*\.{0,1}[\d]*)")
        
    def parse(self):
        # Configuration parameters
        self.params = {}
        
        parser = ConfigParser.ConfigParser()
        parser.read(self.filename)
        config_params = parser.items("main")
        #print config_params
        
        for (param_name, param_value) in config_params:
            self.params[param_name] = GetReplacement(param_value)

        #print self.params
        
        
    def writeSimFile(self, simfile, destinationdir):
        print "Writing files...",
        sys.stdout.flush()

        f = open(simfile)
        simfile_string = f.read()
        params_names = self.params.keys()
        not_seen_list = params_names[1:]
        current_param = params_names[0]
        for i in range(self.params[params_names[0]].GetNumberOfValues()):
            seen_dict = {current_param: self.params[current_param].GetNextValue()}
            self._recursive_traverse(seen_dict, not_seen_list, simfile_string, destinationdir)
        
        print "Done"
        
    def _recursive_traverse(self, seen_dict, not_seen_list, simfile_string, destinationdir):
        
        if len(not_seen_list) == 0:
            # Write out the file.
            self.WriteFile(simfile_string, seen_dict, destinationdir)
            return
        
        # Recursively call the next layer of variables
        new_not_seen_list = not_seen_list[1:]
        current_param = not_seen_list[0]
        for i in range(self.params[current_param].GetNumberOfValues()):
            seen_dict[current_param] = self.params[current_param].GetNextValue()
            self._recursive_traverse(seen_dict, new_not_seen_list, simfile_string, destinationdir)
            
            
    def WriteFile(self, simfile_string, replace_dict, destinationdir):
        output_filename = os.path.join(destinationdir, "submit%i.simconfig" % self._filecounter)
        self._filecounter += 1
        self._simfiles.append(output_filename)
        
        f = open(output_filename, 'w')
        f.write(simfile_string % replace_dict)
        f.close()
        
        
    
    
        
            
            
            
        