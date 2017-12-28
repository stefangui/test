begin = int(input('请输入一个开始数字: \n'))
end   = int(input('请输入一个结束数字: \n'))

for i in range(begin, end+1):
    if(i > 1):
        for j in range(2, i):
            if(i % j == 0): break
        else:
            print(i)

