import sys
class ProgramClass:
    system_args = []
    program_args = []
    program_name = ""
    program_func = ""
    def __init__(self, function, args):
        self.program_args = args
        self.program_func = function
    def main(self):
        self.system_args = sys.argv
        self.program_name = self.system_args[0]
        self.system_args = self.system_args[1:]
        self.program_func(*self.program_args)
