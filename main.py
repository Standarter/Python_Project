import program_class
import func.default_functions

def main():
    print(ProgramClass.system_args)
    pass

ProgramClass = program_class.ProgramClass(main, args=[])
ProgramClass.main()


