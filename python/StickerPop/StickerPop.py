'''
StickerPop.py
An implementation of STIG for MACOSX 10.12
./StickerPop --pop all
./StickerPop --popThese [feature1] [feature2(optional)]...[featuren(optional)]
./StickerPop --popCATI
./StickerPop --popCATII (TO BE IMPLEMENTED)
./StickerPop --popCATIII (TO BE IMPLEMENTED)
'''

import os
import sys
from commands import getstatusoutput
import CATI

sys.path.insert(1, os.path.abspath('.'))
import argparse


def parse_options(argv):
    parser = argparse.ArgumentParser()
    parser.description = 'STIG defintions for Apple OSX 10.12 Sierra \
    Release: 3 Benchmark Date: 27 Apr 2018'

    subparsers = parser.add_subparsers()
    dump_config = subparsers.add_parser('dump-config')
    dump_config.description = 'Parse and print something'

    show_workstation = subparsers.add_parser('show-workstation')
    show_workstation.description = 'List the supported servers and descriptions.'

    stickerpop_parser = subparsers.add_parser('StickerPop')
    stickerpop_parser.description = 'Performs automated workstation configuration.'
    stickerpop_parser.add_argument('--pop',
        action='store_true',
        help="Don't really do anything (echo implied)")
    stickerpop_parser.add_argument('--echo',
        action='store_true',
        help='Echo each command to the console')
    stickerpop_parser.add_argument('--module',
        action='store_true',
        help='Execute the indicated module')
    stickerpop_parser.add_argument('--popThese',
        action='store_true',
        help="Execute the specified STIG requirement")
    stickerpop_parser.add_argument('--popCATI',
        action='store_true',
        help="runs all CAT-I severity STIG requirements")
    stickerpop_parser.add_argument('--popCATII',
        action='store_true',
        help="runs all CAT-II severity STIG requirements")
    stickerpop_parser.add_argument('--popCATIII',
        action='store_true',
        help="runs all CAT-III severity STIG requirements")

    options = parser.parse_args(argv)
    return argv[0], options

def StickerPop(options):
    #run the associated command
    if 'popCATI' in options:
        catclass = CATI.CATI()
        catclass.CATI_RUNALL()
        print "completed, check console for errors"
        return

    elif 'popCATII' in options:
        print 'NOT IMPLEMENTED'
        return

    elif 'popCATIII' in options:
        print 'NOT IMPLEMENTED'
        return

    elif 'pop' in options:
        print 'NOT IMPLEMENTED'
        return
    else:
        print 'wrong command entered'
        return


def main(argv=sys.argv):
    command, options = parse_options(argv[1:])
    command = command.replace('-', '_')
    globals()[command](options)

if __name__=='__main__':
    main()
