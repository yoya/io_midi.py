# -*- coding: utf-8 -*-
# ref) http://d.hatena.ne.jp/rudi/20100805/1281020304

import argparse
from io_midi import IO_MIDI
# from pprint import pprint

parser = argparse.ArgumentParser(description='MIDI dump tool')
parser.add_argument('midifile')
parser.add_argument('-H', action='store_true', default=False,
                    dest='hexdump',
                    help='switch to hexdump mode')
parser.add_argument('-v', action='store_true', default=False,
                    dest='verbose',
                    help='switch to verbose mode')
args = parser.parse_args()

print(args)

opts = { 'hexdump':args.hexdump, 'verbose':args.verbose }


mididata = open(args.midifile).read()

midi = IO_MIDI()
midi.parse(mididata)
midi.dump(opts=opts)

'''
mididata = file_get_contents(options['f'])

midi = IO_MIDI()
midi.parse(mididata)



midi.dump(opts)
'''
