import cmd

class InteractiveOrCommandLine(cmd.Cmd):
    """Accepts commands via the normal interactive prompt or on the command line."""

    prompt = '>> '
    intro = "Line Interpreter: Type help to get help to see available commands"
    doc_header = 'Commands\n   To get help type <help command>'
    misc_header = 'Commands with help available'
    undoc_header = 'To exit type'
    ruler = '-'
    file_name = ''

    def help_file_name(self):
        print ('\n'.join([ 'file_name [file_name]',
        'Gets the filename to download data from',
        ]))

    def help_args(self):
        print ('\n'.join([ 'Command Line : $ python cmd_argv.py args',
                           'Interactive >> enter commands',
                           'Type <help command> for further help'
        ]))

    def do_file_name(self, line):
        file_name = line
        print ('File name is :,', line)

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        InteractiveOrCommandLine().onecmd(' '.join(sys.argv[1:]))
    else:
        InteractiveOrCommandLine().cmdloop()