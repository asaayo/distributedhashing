# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
import math
import time

__author__="Brandon"
__date__ ="$Apr 22, 2015 3:40:09 PM$"


def main():
    numclients = 0
    solved = 0
    #hash = "0b4e7a0e5fe84ad35fb5f95b9ceeac79" #aaaaaa
    #hash = "54d0b65dbce1bcae13e1329438d021bf" #sixsix
    hash = "87515d7cdc7afd8f3bcbf3eef49faef0" #thilly
    #hash = "75e393ffa3dfea6ab39d5361a5906ba1" #parson
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address=('localhost',13337)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        connection, client_address = sock.accept()
        try:
            start = time.time()
            data = connection.recv(1024)
            print 'connection from' , client_address , " data: ", data
            #print data
            if(data == "Ready"):
                numclients += 1
                current = time.time()
                start = math.floor(25-25/numclients)
                if numclients == 1:
                    end = 13
                else:
                    end = 25
                range = ":" + str(start) + "-" + str(end)
                sending = hash + range
                print 'sending hash' , sending
                connection.sendall(sending)
            if "Solved" in data:
                solved = 1
                print data
            if "status" in data:
                if solved:
                    connection.sendall("solved")
                    numclients-=1               
        finally:
            connection.close()
        if solved:
            if numclients == 0:
                break


if __name__ == "__main__":
    main()
