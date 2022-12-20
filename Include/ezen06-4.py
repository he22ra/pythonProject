'''
  5) 딕셔너리(Dictionary) 자료형
    - {Key1:Value1, Key2:Value2, ...}
    - {'name':'Jessica', 'age':19}
    - stu = {'name':['Susan', 'Jessica', 'John', 'Michael'], 'age':[19, 15, 16, 17]}

'''
stu = {'name':['Susan', 'Jessica', 'John', 'Michael'], 'age':[19, 15, 16, 17]}
print(stu)
print(type(stu))

stu['math'] = [50, 100, 70, 80]
print(stu)

del stu['math']
print(stu)

for key, value in stu.items():
  print(key, value)