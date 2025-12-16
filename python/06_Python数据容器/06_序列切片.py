"""
切片演示
"""
#对list进行切片演示
my_list=[1,2,3,4,5,6,7,8,9]
print(my_list[2:7])#步长为1，则省略

#对tuple进行切片
my_tuple=(1,2,3,4,5,6,7,8,9)
print(my_tuple[::2])

#对str进行切片
my_str='123456789'
print(my_str[2:8:3])

#对str进行逆序切片
print(my_str[6:2:-1])


my_str1="Leslie,love,lucifer"
my_str=my_str1[10:6:-1]
print(my_str)