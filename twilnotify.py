
#
# twinotify --account AC421124bfab3052ad108f3e8c7a119cfb --token 35abced35627245245245235234 --devapncert DevNotifyCert.12  --prodapncert ProdNotifyCert.p12 --fcm 12398123984798231434

from PEMExports import PEMExports

import sys

if __name__ == '__main__':

    extractor = PEMExports(sys.argv[1])

    print extractor.private_key

    print extractor.certificate