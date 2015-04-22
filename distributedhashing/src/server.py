# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
import sys

__author__="Brandon"
__date__ ="$Apr 22, 2015 3:40:09 PM$"


def main():
    #hash = "0b4e7a0e5fe84ad35fb5f95b9ceeac79" #aaaaaa
    hash = "54d0b65dbce1bcae13e1329438d021bf" #sixsix
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address=('localhost',13337)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        connection, client_address = sock.accept()
        try:
            print >> sys.stderr, 'connection from' , client_address
            connection.sendall(hash)
        finally:
            connection.close()


if __name__ == "__main__":
    main()
