# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from itertools import product
from hashlib import md5
from multiprocessing import Process, Value
import socket
import sys
import time

__author__="Brandon"
__date__ ="$Apr 15, 2015 3:40:20 PM$"


def doit(start, end, hash, num):
#    print start
#    print end
    counter = 0
    startlist = []
    charlist = []
    #build a list of the lower case characters so I don't have to type them
    for i in range(97,123):
        charlist.append(chr(i))
    if(end > 26):
        end = 26
    for i in range(97+start, 97+end):
        startlist.append(chr(i))
#    print startlist
#    print charlist
    for c in product(startlist, charlist, charlist, charlist, charlist, charlist):
        s=''.join(c)
        #if(counter % 100000 == 0):
        #    print str(counter) + " " + s
        counter+=1
        if(num.value == 1):
            break
        temp = md5(s).hexdigest()
        if temp in hash:
            num.value=1
            print "Found",s
            two = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address=('localhost',13337)
            #two.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            two.connect(server_address)
            response = "Solved, hash is: \t" + str(s)
            try:
                two.sendall(response)
            finally:
                two.close()
            return s

            
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('localhost', 13337)
    sock.connect(server_address)
    try:
        sock.sendall("Ready")
        hash = sock.recv(1024)
    finally:
        sock.shutdown(1)
        sock.close()
    print hash
    counter = 0
    num = Value('i', 0)
    print"Starting..."
    #hash = "0b4e7a0e5fe84ad35fb5f95b9ceeac79" #aaaaaa
    #hash = "54d0b65dbce1bcae13e1329438d021bf" #sixsix
    threads = []
    for i in range(0,7):
        threads.append( Process(target=doit, args=(i*4,i*4+4,hash,num)) )
        threads[i]
        threads[i].start()
        
    #timeout/exit loop
    while num.value==0:
        time.sleep(5)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = ('localhost', 13337)
        sock.connect(server_address)
        try:
            sock.sendall("status")
            status = sock.recv(1024)
            if "solved" in status :
                num.value=1
        finally:
            sock.shutdown(1)
            sock.close
        
#    for i in range(0,7):
#        threads[i].join()
        
#    while(num.value == 0):
#        counter = 0
    
#    print "Killing threads"
#    for i in range(0,7):
#        threads[i].terminate()

if __name__ == "__main__":
    main()
