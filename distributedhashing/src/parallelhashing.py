# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from itertools import product
from hashlib import md5
from multiprocessing import Process

__author__="Brandon"
__date__ ="$Apr 15, 2015 3:40:20 PM$"

def doit(start, end, hash):
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
        if(counter % 10000 == 0 and s[0]=='s'):
            print str(counter) + " " + s
        counter+=1
        temp = md5(s).hexdigest()
        if temp in hash:
            print "Found",s
            return s
            
def main():
    hash = "54d0b65dbce1bcae13e1329438d021bf"
    threads = []
    for i in range(0,8):
        threads.append( Process(target=doit, args=(i*4,i*4+4,hash,)) )
        threads[i].start()
    for i in range(0,8):
        threads[i].join()

if __name__ == "__main__":
    main()
