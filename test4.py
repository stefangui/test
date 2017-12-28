import sys

for i in range(1,10):
    for j in range(1,i+1):
        str = "%d * %d = %d" % (i,j,i*j)
        print (str.ljust(14," "),end=" ",)
        #print  ("{}*{}={}".format(j,i,j*i)," ",end="")
    print()