import sys
import resources.info as Program_Info
class ProgramClass:
    system_args = []
    program_args = []
    program_name = ""
    program_func = ""
    program_info = {}
    version = ""
    author = ""
    lastupdatedate = ""
    def __init__(self, function, args):
        self.program_args = args
        self.program_func = function
        self.program_info = Program_Info.Program_Info
        self.version = self.program_info["Program_Version"]
        self.author = self.program_info["Author"]
        self.lastupdatedate = self.program_info["LastUpdateDate"]
    def main(self):
        self.system_args = sys.argv
        self.program_name = self.system_args[0]
        self.system_args = self.system_args[1:]
        self.program_func(*self.program_args)
