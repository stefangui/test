import os
a = [m+n for m in 'ABCDE' for n in 'UVWXY']
b = [d for d in os.listdir('.')]
print(b)