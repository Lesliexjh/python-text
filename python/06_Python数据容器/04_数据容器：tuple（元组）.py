# 定义元组的字面量
# ('元素','元素','元素')
# 定义元组变量
# 变量名称=('元素','元素','元素')
# 定义空元组
# 变量名称=()         #方式一
# 变量名称=tuple()    #方式二
from operator import index

#定义元组
t1=(1,2,3)
t2=()
t3=tuple()
t4=('leslie',555,'lucifer')
t5=tuple(['leslie',555,'lucifer'])
t6=tuple(t4)


#定义单个元素的元组
t7=('leslie',)
print(type(t7))

#元组的嵌套
t8=((1,2,3),(4,5,6))
print(type(t8))
t9=((1,2,3))
print(type(t9))
print(t8[1][2])

#index() 查找某个数据，如何数据存在则返回对应的下标，否则报错
print(t8.index((4,5,6)))
#count() 统计某个数据在当前元组出现的次数
print(t7.count(('leslie',)))
#len() 统计元组内的元素个数
print(len(t8))