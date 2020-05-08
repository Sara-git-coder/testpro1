class Person:
    #构造方法
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender}我在吃")
    def drink(self):
        print (f"name:{self.name},age:{self.age},gender:{self.gender}我在喝")
    def sing(self):
        print (f"name:{self.name},age:{self.age},gender:{self.gender}我在唱歌")
sara = Person("sara",30,"female")
print (sara.drink ())
