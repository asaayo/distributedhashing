# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# import timeit
from itertools import product
from hashlib import md5

__author__="Brandon"
__date__ ="$Apr 15, 2015 2:55:22 PM$"

#Starting simple
def main():
    hash = "54d0b65dbce1bcae13e1329438d021bf"
#    t = timeit.Timer("md5('sixsix').hexdigest()", setup='from hashlib import md5')
#    print t.timeit(1000)
    
    
    for c in product('abcdefghijklmnopqrstuvwxyz',repeat=6):
        s=''.join(c)
        print s
        temp = md5(s).hexdigest()
        if temp in hash:
            print "Found",s
    


if __name__ == '__main__':
    main()
