#方式1：使用print直接输出类型信息
print(type("加油"))
print(type(123))
print(type(12.3))


#方式2：使用变量存储type()语句的结果
string_type=type("加油")
print(string_type)
int_type=type(123)
print(int_type)
float_type=type(12.3)
print(float_type)

#方式3使用type()查看变量中存储的数据类型信息
name="加油"
print(type(name))
a=123
print(type(a))
b=12.3
print(type(b))