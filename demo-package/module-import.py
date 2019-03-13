# 第一种import方式
# import packages.a
# import packages.b
# import packages.c
# print(packages.a, packages.b, packages.c)

# 第二种import方式
# from packages import a
# from packages import b
# from packages import c
# print(a)
# print(b)
# print(c)

# 第三种import方式 - 需要在__init__.py文件中设置“__all__”
# from packages import *
# print(a, b, c)