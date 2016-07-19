#! /usr/bin/env python

import sys
try:
    from optparse import OptionParser
except:
    print 'optparse module required'
    exit(0)
from soapy.conf import load_cfg
#from soapy.fill import fill_header, fill_footer

if __name__ == '__main__':
    optpar = OptionParser()
    optpar.add_option('-o', '--output',
                    action = 'store', type = 'string',
                    dest = 'output', help = 'output html file')
    optpar.add_option('-c', '--config',
                    action = 'store', type = 'string',
                    dest = 'config', help = 'config file to specify code source and etc, must be json format')
    (options, args) = optpar.parse_args()
    if (not options.output) or (not options.config):
        print 'Incorrect usage!\nSee usage with "python gen.py --help".'
        sys.exit(0)
    elif not options.output.endswith('.html'):
        print 'output file must end with .html'
        sys.exit(0)
        print 'output', options.output
    elif not options.config.endswith('.json'):
        print 'output file must be json format'
        sys.exit(0)
    else:
        print load_cfg(options.config)
        #fille_header()
