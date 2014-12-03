#!/usr/bin/python
#
# HTML source analyzer
# bl4de | bloorq@gmail.com | Twitter: @_bl4de
#
import sys


class _PefOutput:
    Black = '\33[30m'
    Red = '\33[31m'
    Green = '\33[32m'
    Yellow = '\33[33m'
    Blue ='\33[34m'
    Magenta = '\33[35m'
    Cyan = '\33[36m'
    White = '\33[37m'
    _endline = '\33[0m'
    
    efMsgFound = "exploitable function call"
    efMsgGlobalFound = "global variable explicit call"


_ident = "unknown"

def main():
    _file = open(sys.argv[1], "r")
    i = 0
    print _PefOutput.Green, "=" * 26, "HTML Analyze", "=" * 26
    print "-" * 6, " GitHub: bl4de | Twitter: @_bl4de | bloorq@gmail.com ", "-" * 6, _PefOutput._endline
    
    print
    for _line in _file:
        i = i + 1
        analyzeLine(_line, i)
        identify(_line)
    showStats(_file, i)
    

# using osftare recognition
def identify(_line):
    if "Jommla" in _line:
        _ident = "Joomla CMS"
    if "wp-content" in _line:
        _ident = "WordPress CMS"
        
    
def showStats(_file, i):
    print _PefOutput.Green, "\n------ SUMMARY -------\n"
    print "total lines of code: %d" % (i)
    print "identified software: %s" %(_ident), _PefOutput._endline
    # end of summary
    print "\n"
    
# find interesting string(s)
def analyzeLine(_line, i):
    if "<!--" in _line:
        print _PefOutput.White, "line %d:" % (i), _PefOutput.Yellow, "comment found at line %d: %s" % (i, _line.rstrip()), _PefOutput._endline
    if "admin" in _line:
        print _PefOutput.White, "line %d:" % (i), _PefOutput.Red, "'admin' string found at line: %d" % (i), _PefOutput._endline
    if "debug" in _line:
        print _PefOutput.White, "line %d:" % (i), _PefOutput.Red, "debug information found at line %d" % (i), _PefOutput._endline
    if "<script>" in _line:
        print _PefOutput.White, "line %d:" % (i), _PefOutput.Cyan, "inline JavaScript found at line %d" % (i), _PefOutput._endline
    if "\"/" in _line:
        print _PefOutput.White, "line %d:" % (i), _PefOutput.Magenta, "possible directory path found at line %d" % (i), _PefOutput._endline
    
# main program
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print "Enter HTML file name"