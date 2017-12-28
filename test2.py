import sys

i = int(input("净利润:"))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(6):
    if( i > arr[idx] ):
        current =  (i - arr[idx]) * rat[idx]
        r += current
        print ("高于 ",arr[idx]," 档位的奖金为：",current)
        i = arr[idx]
print ("总奖金为: ",r)