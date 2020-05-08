#列表作为堆栈使用
# stack = [1,2,3,4,5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# #列表作为队列使用
# from collections import deque
# quene = deque(["eric","John","Michael"])
# quene.append("Terry")
# quene.append("Frank")
# print (quene.popleft ())
# print (quene)

#列表推导式
"""
如果我们想生成一个平方列表，比如【1,4,9...】,使用for循环怎么写，使用列表生成表达式又怎么写
"""
# list_square=[]
# for i in range(1,10):
#     list_square.append(i**2)
# print (list_square)

# list_square = [i**2 for i in range(1,10)]
# print (list_square)
#
# combs=[(x,y) for x in range(1,5) for y in range(1,5) if(x!=y)]
# print (combs)
#
# vec = [[1,2,3],[4,5,6],[7,8,9]]
# list_vec = [(num,num**2) for item in vec for num in item]
# print (list_vec)

# from math import pi
# yzl=[str(round(pi,i)) for i in range(1,20)]
# print (yzl)
#矩阵转置
matrix = [[1,2,3,4,15],[5,6,7,8,16],[9,10,11,12,17]]
# matrix_reverse = [[row[i] for row in matrix] for i in range(5)]
# print (matrix_reverse)
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print (transposed)
print (list (zip (*matrix)))

#关于列表
# list_hogwarts=[1,2,3]
# list_hogwarts.append(0)
# list_hogwarts.insert(2,9)
# # list_hogwarts.remove(1)
# # item = list_hogwarts.pop(1)
# # print(item)
# # list_hogwarts.sort(reverse=True)
# list_hogwarts.reverse()
# print (list_hogwarts)

#元祖的定义
# tuple_hogwarts = (1,2,3)
# print("tuple_hogwarts",tuple_hogwarts)

#集合
# a = {1,2,3}
# b = {1,5,6}
# print (a.union (b))
# print (a.intersection (b))
# print (a.difference (b))
# print (a.add ("b"))
# print(a)
#
# print ({i for i in "123456aaaa33ddcc"})
#
# c="aaaaaaffffff3333eeringbbbertyuiodnhd"
# print (set (c))

# hogwart_dict = dict(a=1,b=2)
# hogwart_dict2 = {"a":1,"b":2}
# print("hogwart_dict",hogwart_dict)
# print("hogwart_dict2",hogwart_dict2)
# print (hogwart_dict.keys ())
# #返回被删除的键值对
# print (hogwart_dict.popitem ())
# #返回被删除的键值对后剩余的元素
# print (hogwart_dict)


