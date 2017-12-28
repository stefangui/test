a = ['12', '32', '42', '54', '6546', '76', '8', '67', '55', '121']
#for i in range(9):
#    a.append(input('请输入数字(限制十位): \n'))
print(a)

for i in range(9):
    for j in range(i+1, 10):
        if int(a[i]) > int(a[j]):
            a[i], a[j] = a[j], a[i]
print(a)
