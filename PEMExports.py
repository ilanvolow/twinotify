
import sys

from OpenSSL import crypto

class PEMExports:

    def __init__(self, fd):

        self.fd = fd

        self.private_key = None

        self.certificate = None

        self.read_p12()

    def read_p12(self):

        try:

            p12_stream = file(self.fd, 'rb')

            p12_content = p12_stream.read()

            p12 = crypto.load_pkcs12(p12_content, '')

            self.private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())

            self.certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())

        except:

            print("Unexpected error:", sys.exc_info()[0])

            raise