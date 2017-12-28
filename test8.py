def output(i,j):
    if j == 0:
        return
    print(i[j-1],end='')
    output(i, j-1)

s = input('请输入一段字符串: \n\n')
output(s ,len(s))

