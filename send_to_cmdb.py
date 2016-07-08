#!/usr/bin/env python

import argparse
import json
import os.path
import sys

import requests

class SendToCMDB(object):
    def __init__(self, opts):
        self.opts = opts
        self.cmdb_read_url_base = opts.cmdb_read_endpoint
        self.cmdb_write_url_base = opts.cmdb_write_endpoint
        self.cmdb_auth = (opts.cmdb_user, opts.cmdb_password)
        self.service_id = opts.service_id
        self.remote_images = {}
        self.local_images = {}


    def retrieve_remote_images(self):
        print "Retrieving remote images"
        url = "%s/service/id/%s/has_many/images" % (self.cmdb_read_url_base,
                                                    self.service_id)
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            json_answer = r.json()
            json_images = json_answer["rows"]
            if len(json_images) > 0:
                for image in json_images:
                    cmdb_image_id = image["id"]
                    cmdb_image = {'cmdb_image_id': cmdb_image_id}
                    image_id = image["value"]["image_id"]
                    for key, val in image["value"].iteritems():
                        cmdb_image[key] = val
                    self.remote_images[image_id] = cmdb_image
            else:
                print "No images for service %s" % self.service_id
        else:
            print "Unable to retrieve remote images: %s" % r.status_code
            sys.exit(1)


    def retrieve_local_images(self):
        print "Retrieving local images"
        json_input = ''
        for line in sys.stdin.readlines():
            json_input += line.rstrip('\n')
        self.local_images = json.loads(json_input)
        print self.local_images

    def update_remote_images(self):
        self.retrieve_remote_images()
        print self.remote_images
        self.retrieve_local_images()
        #r = requests.get(url, auth=(self.cmdb_auth))

        print "Updating remote images"

def parse_opts():
    parser = argparse.ArgumentParser(
        description='Submit images to CMDB',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        fromfile_prefix_chars='@',
        conflict_handler="resolve",
    )

    parser.add_argument(
        '--cmdb-read-endpoint',
        default='http://indigo.cloud.plgrid.pl/cmdb',
        help=('URL of the CMDB endpoint'))

    parser.add_argument(
        '--cmdb-write-endpoint',
        default='http://couch.cloud.plgrid.pl/indigo-cmdb-v2',
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
