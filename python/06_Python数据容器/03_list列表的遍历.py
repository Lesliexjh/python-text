"""
演示while循环和for循环的列表遍历
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list = ['leslie','lucifer','fcxs']
    #循环控制变量通过下标索引来控制，默认0
    #每一次循环将下标索引变量+1
    #循环条件：下标索引变量<列表的数量

    #定义一个变量用来标记列表的下标
    index = 0      #初始值为0
    while index < len(my_list):
        #通过index变量取出对应下标的元素
        print(my_list[index])
        index += 1
list_while_func()


def list_for_func():
    my_list = ['leslie','lucifer','fcxs']
    for index in range(len(my_list)):
        print(my_list[index])

    for x in my_list:
        print(x)

list_for_func()


#练习
Leslie_list=[1,2,3,4,5,6,7,8,9,10]
lucifer_list=[]
for x in Leslie_list:
    if x % 2 == 0:
        lucifer_list.append(x)
print(lucifer_list)

Lucifer_list=[]
x=0
while x < len(Leslie_list):
    if Leslie_list[x] % 2 == 0:
        Lucifer_list.append(Leslie_list[x])
    x+=1
print(Lucifer_list)