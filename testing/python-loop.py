# #for 循环
# result = 0
# for i in range(2,101,2):
#     # if i%2==0:
#     print(i)
#     result = result +i
#     print(result)

# a=1
# while a==1:a = a+1
# else:
#     print("a!=1")
#     print(a)

"""
猜数字游戏
计算机给出1个1~100之间的随机数有人来猜
计算机根据人猜的数字分别
给出大一点、小一点、猜对啦的提示
"""
import random
# guess_number = 0
computer_number = random.randint(1,100)
#print(computer_number)
while True:
    guess_number = int(input("请输入一个数字："))
    if(guess_number>computer_number):
        print("小一点")
    elif(guess_number<computer_number):
        print("大一点")
    else:
        print("猜对啦")
        break