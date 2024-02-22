import array as arr
'''
My_array = arr.array('i',[1,2,3,4])
My_list = [1,'abc',1.20]
print(My_array)
print(My_list)

arr = [[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
for i in range(0,4):
    print(arr[i].pop())

class Employee:
    def __init__(self, i):
        self.id = id
        id = 10
Res = Employee(789)
print(Res.id)

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod

def cal_salary(self,sal):
    pass

class Developer(Employee):
    def cal_salary(self,sal):
        TSalary=sal*1.10
        return TSalary

emp_1=Developer()
print(emp_1.cal_salary(10000))


mylist = [1,5,4,6,8,11,3,12]
new_list=list(filter(lambda x: (x%2 == 0), mylist))
print(new_list)

def f(value, values):
    v = 1
    values[0]=44

t=3
v=[1,2,3]
f(t,v)
print(t,v[0])

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)

f = None
for i in range(5):
    with open(data)

def multiplexers():
    return[lambda n:index * n for index in range(4)]

print([m(2) for m in multiplexers()])

item = {n: n*2 for n in range(10)}
print(item)


item = {n*2 for n in range(10)}
print(item)

try:
    if '1'!=1:
        raise "some error"
    else:
        print("someerror has not ocurred")
except "someError":
    print("someerror has ocurred")

import re
sentence = 'Learn python'
test = re.match(r'(.*)(.*?)(.*)', sentence)
print(test.group())

'''