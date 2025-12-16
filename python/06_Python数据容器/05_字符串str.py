#定义一个字符串
my_str="Leslie and Lucifer"

#通过下标索引取值
print(my_str[0])

#index方法
print(my_str.index("L"))

#count方法
print(my_str.count("L"))

#replace方法:替换
my_str1=my_str.replace("and","")
print(my_str1)

#split方法
my_str2=my_str.split(" ")
print(my_str2)

#字符串规整操作 字符串.strip()---去除前后空格
my_str3=' leslie and lucifer '
print(my_str3)
print(my_str.strip())
#字符串.strip(字符串)---去除前后指定字符串
my_str4='llwww rrrfsadrr'
print(my_str4)
print(my_str4.strip('lr'))

#统计字符串的长度
print(len(my_str))