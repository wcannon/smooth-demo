#!/usr/bin/env python
"""Usage: smooth-demo.py <inputfile> [options]

Valid colors are: grey red green yellow blue magenta cyan white
Valid --char-delay = float / int
Valid --[comment|command|command-output]-sleep = float / int

Options:
    <inputfile>  		Path to file to read in comments and commands
    --comment-color 		Color to use for comments 
    --command-color 		Color to use for commands
    --command-output-color 	Color to use for output of return from commands
    --char-delay	 	Delay time to pause between printing characters
    --comment-sleep	 	Delay time to pause after printing a comment
    --command-sleep	 	Delay time to pause after printing a command
    --command-output-sleep	Delay time to pause after printing output of return from command
    --shell-prompt		Change terminal shell prompt
    -h --help
"""
# from __future__ import print_function
from docopt import docopt
import sys, time
import subprocess, shlex
from termcolor import colored

def print_slowly(somestr=None, char_delay=0.3, sleep_delay=5.0, color=None):
    for c in somestr:
        char = colored(c, color)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    time.sleep(sleep_delay)
    return

def run_cmd(command_str, color='red'):
    try:
        output = subprocess.check_output(command_str, shell=True, stderr=subprocess.STDOUT)
        output.rstrip('\n')
        colored_output = colored(output, color)
        print(colored_output)
    except Exception as e:
        output = "Command produced error: {}".format(e.output)
        colored_output = colored(output, color)
        print(colored_output)
        raise
    return

def load_file(filename):
    lines = []
    try:
        f = open(filename, 'r')
        lines = f.readlines()
    except Exception as e:
        print(("Unable to load file: {}".format(filename)))
        raise
    return lines

def get_line_type(line):
    if not line or line == '' or line == '\n':
        return 'empty'
    elif line.startswith('#'):
        return 'comment'
    else:
        return 'command'

def validate_color(color, line_type):
    '''Given a color, and line_type, return an appropriate default, or the color given if valid'''
    valid_colors = "grey red green yellow blue magenta cyan white".split() # for termcolor library
    ret_color = color 
    if color not in valid_colors: # includes if value is None
        if line_type == 'comment':
            ret_color = 'cyan'
        elif line_type == 'command':
            ret_color = 'green'
        elif line_type == 'command_output':
            ret_color = 'red'
        else:
            ret_color = 'green'
    return ret_color

def validate_sleep(sleep_time, sleep_type):
    '''Given a sleep_time, and a sleep_type, return an appropriate default, or the time given if valid'''
    if type(sleep_time) == str:
        sleep_time = float(sleep_time)
    if type(sleep_time) == float or type(sleep_time) == int:
        ret_sleep_time = sleep_time
    elif sleep_type == 'char_delay':
        ret_sleep_time = 0.05
    elif sleep_type == 'comment':
        ret_sleep_time = 2
    elif sleep_type == 'command':
        ret_sleep_time = 2
    elif sleep_type == 'command_output':
        ret_sleep_time = 4 
    else: 
        ret_sleep_time = 4 
    return ret_sleep_time
   
def main(inputfile, char_delay, comment_color, comment_sleep,
         command_color, command_sleep, command_output_color,
         command_output_sleep, shell_prompt):
    # TODO:
    # catch user hitting space bar, and pause program until space bar hit again
    try:
        lines = load_file(sys.argv[1])
    except:
        sys.exit(1)
    run_cmd('clear')
    for l in lines:
        t = get_line_type(l)
        if t == 'empty':
            continue
        if t == 'comment':
            length = len(l)
            char = colored('-', comment_color)
            print((char * length))
            # def print_slowly(somestr, char_delay=0.2, sleep_delay=5, color)
            print_slowly(somestr=l, char_delay=char_delay, sleep_delay=comment_sleep, color=comment_color)
            print((char * length))
        if t == 'command':
            #l.rstrip('\n')
            #l_as_list = shlex.split(l)
            #print('{} '.format(shell_prompt)),
            print_slowly(somestr=l, char_delay=char_delay, sleep_delay=command_sleep, color=command_color)
            #time.sleep(2)
            try:
                #run_cmd(l_as_list, command_output_color)
                run_cmd(l, command_output_color)
            except:
                pass
            time.sleep(command_output_sleep)
            run_cmd('clear')

if __name__ == "__main__":
    ARGS = docopt(__doc__)
    # print(ARGS)
    char_delay = validate_sleep(ARGS['--char-delay'], 'char_delay')
    # print "char_delay after validation: {}".format(char_delay)
    comment_color = validate_color(ARGS['--comment-color'], 'comment')
    # print "comment_color: {}".format(comment_color)
    comment_sleep = validate_sleep(ARGS['--comment-sleep'], 'comment')
    # print "comment_sleep: {}".format(comment_sleep)
    command_color = validate_color(ARGS['--command-color'], 'command')
    # print "command_color: {}".format(command_color)
    command_sleep = validate_sleep(ARGS['--command-sleep'], 'command')
    # print "command_sleep: {}".format(command_sleep)
    command_output_color = validate_color(ARGS['--command-output-color'], 'command_output')
    # print "command_output_color: {}".format(command_output_color)
    command_output_sleep = validate_sleep(ARGS['--command-output-sleep'], 'command_output')
    # print "command_output_sleep: {}".format(command_output_sleep)
    inputfile = ARGS['<inputfile>']
    shell_prompt = ARGS['--shell-prompt']
    if shell_prompt == "None" or shell_prompt == None:
        shell_prompt = '$ > '
    main(inputfile, char_delay, comment_color, comment_sleep,
         command_color, command_sleep, command_output_color,
         command_output_sleep, shell_prompt)
