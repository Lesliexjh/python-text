""""
演示操作之：list列表的常用操作
"""

my_list = ["L","e","s","l","i","e"]
#1.1查找某元素再；列表内的下标索引
index = my_list.index("e")
print(index)
#1.2如果被查找的元素不存在，会报错
# index = my_list.index("a")
# print(index)

#2.修改特定下标索引的值
my_list[0]='l'
print(my_list)

#3.在指定的下标位置插入新元素
my_list.insert(1,"lucifer")
print(my_list)

#4.在list尾部追加单个新元素
my_list.append('s')
print(my_list)

#5.在list尾部追加一批新元素
my_list2 = ['l','u','s','f','e','r']
my_list.extend(my_list2)
print(my_list)

#6.删除指定下标索引的元素（2种方式）
my_list=['l','u','s','f','e','r']
#6.1.方式1:del 列表[下标]
del my_list[0]
print(my_list)
#6.2.方式2：列表.pop[下标]----删除该元素，且能返回该元素
quchu=my_list.pop(1)
print(quchu)
print(my_list)

#7.删除某元素再列表中的第一个匹配项
my_list=['l','e','s','l','i','e']
my_list.remove(my_list[1])
print(my_list)

#8.清空列表
my_list.clear()
print(my_list)

#9.统计表中某元素数量
my_list=['l','u','s','f','e','r']
count=my_list.count('e')
print(count)

#10.统计列表中全部元素的数量
my_list=['l','u','s','f','e','r']
count= len(my_list)
print(count)
