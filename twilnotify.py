#!/usr/bin/python
#
# The below are all bogus credentials. Just giving an idea of what I'm trying to shoot for
# twinotify --account AC421124bfab3052ad108f3e8c7a119cfb --token 35abced35627245245245235234 --devapncert DevNotifyCert.12  --prodapncert ProdNotifyCert.p12 --fcm 12398123984798231434

import argparse

from PEMExports import PEMExports

import sys

if __name__ == '__main__':

    ## TODO: Refactor parser into its own class/factory

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(title="commands", dest="command")

    # pem files
    pem_parser = subparsers.add_parser('pem', help='pem files help')

    pem_parser.add_argument('p12file', help='p12 file exported from keychain')

    pem_parser.add_argument('--name', help='prefix for names files are saved to')

    # credentials
    credentials_parser = subparsers.add_parser('credentials', help='credentials helps')

    
    args = parser.parse_args()

    if args.command == 'pem':

        extractor = PEMExports(args.p12file)

        if args.name:

            keyfd = file(args.name + "_key" + ".pem", "w")

            keyfd.write(extractor.private_key)
            
            keyfd.close()

            certfd = file(args.name + "_cert" + ".pem", "w")

            certfd.write(extractor.certificate)

            certfd.close()

        else:

            print extractor.private_key
        
            print extractor.certificate
    
    elif args.command == 'credentials':

        pass

