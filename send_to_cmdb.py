#!/usr/bin/env python

import argparse
import os.path

class SendToCMDB(object):
    def __init__(self, opts):
        self.opts = opts

    def retrieve_remote_images(self):
        print "Retrieving remote images"
        self.remote_images = {}	

    def retrieve_local_images(self):
        print "Retrieving local images"
        self.local_images = {}	

    def update_remote_images(self):
        self.retrieve_local_images()
        self.retrieve_remote_images()

        print "Updating remote images"

def parse_opts():
    parser = argparse.ArgumentParser(
        description='Submit images to CMDB',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        fromfile_prefix_chars='@',
        conflict_handler="resolve",
    )

    parser.add_argument(
        '--cmdb-endpoint',
        default='http://couch.cloud.plgrid.pl/indigo-cmdb-v2',
        required=True,
        help=('URL of the CMDB endpoint'))

    parser.add_argument(
        '--cmdb-user',
        required=True,
        help=('Username to use to contact the CMDB endpoint'))

    parser.add_argument(
        '--cmdb-password',
        required=True,
        help=('Password to use to contact the CMDB endpoint'))

    parser.add_argument(
        '--service-id',
        required=True,
        help=('CMDB target service ID'
              'Images will be linked to this service ID'))

    return parser.parse_args()


def main():
    opts = parse_opts()

    sender = SendToCMDB(opts)
    sender.update_remote_images()


if __name__ == '__main__':
    main()
