#!/usr/bin/env python

### created by bl4de | bloorq@gmail.com | twitter.com/_bl4de    ###
### github.com/bl4de | hackerone.com/bl4de                      ###

import sys
import hashlib

description = """
hasher.py - hash string using SHA1, MD5
usage: ./hasher.py [string_to_hash]

"""


def usage():
    print description
    exit(0)


def main(s):
    print "[+] SHA1\t\t{}".format(hashlib.sha1(s).hexdigest())
    print "[+] MD5 \t\t{}".format(hashlib.md5(s).hexdigest())


if __name__ == "__main__":
    if (len(sys.argv) == 2):
        arguments=sys.argv[1:]
        main(arguments[0])
    else:
        usage()
