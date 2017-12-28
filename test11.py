
a = [1,4,6,9,13,16,19,28,40,100,200]

print('原始列表为：',a,end=' ')

number = int(input('插入的数字为: \n'))

a.append(number)
a.sort()

print('排序后的列表为：',a,end=' ')