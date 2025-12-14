t=()
>>> t=tuple()
>>> t=(1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> t=(1,2,2,4,5,6)
>>> t
(1, 2, 2, 4, 5, 6)
>>> t=(1,3,2.2,"ushaswini",[],(),{},{1,2,3})
>>> t
(1, 3, 2.2, 'ushaswini', [], (), {}, {1, 2, 3})
>>> t=((1,2),(2,3)(4,5))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t=((1,2),(2,3)(4,5))
TypeError: 'tuple' object is not callable
>>> t=((1,2),(2,3),(4,5))
>>> t
((1, 2), (2, 3), (4, 5))
>>> t=(1,2,3)
>>> s=(5,6,7)
>>> t+s
(1, 2, 3, 5, 6, 7)
>>> t*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> 4 in t
False
i in t
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    i in t
NameError: name 'i' is not defined
>>> l in t
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l in t
NameError: name 'l' is not defined
>>> 1 in t
True
>>> lang=('java','python','c','c++','javascript','css','bootstrap')
>>> lang[3]
'c++'
>>> lang[0]
'java'
>>> lang[-3]
'javascript'
>>> lang[:3]
('java', 'python', 'c')
>>> lang[-3:]
('javascript', 'css', 'bootstrap')
>>> lang[3:5]
('c++', 'javascript')
>>> lang[::2]
('java', 'c', 'javascript', 'bootstrap')
>>> t=(1,2,3)
>>> a,b,c=t
>>> a
1
>>> b
2
>>> c
3
>>> res=("devik","devik@gmail.com","dev@123")
>>> res[1]
'devik@gmail.com'
>>> res[2]
'dev@123'
>>> res[3]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    res[3]
IndexError: tuple index out of range
>>> username,mail,pswd
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    username,mail,pswd
NameError: name 'username' is not defined
>>> username,mail,pswd=res
>>> pswd
'dev@123'
>>> username
'devik'
>>> mail
'devik@gmail.com'
>>> res
('devik', 'devik@gmail.com', 'dev@123')
>>> res.count
<built-in method count of tuple object at 0x00000195631B6E58>
>>> res.indexx
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    res.indexx
AttributeError: 'tuple' object has no attribute 'indexx'
>>> res.index
<built-in method index of tuple object at 0x00000195631B6E58>
>>> res.count('devik')
1
>>> res.index('devik@123')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    res.index('devik@123')
ValueError: tuple.index(x): x not in tuple
>>> res.index('dev@123')
2
>>> len(res)
3
>>> min(res)
'dev@123'
>>> max(res)
'devik@gmail.com'
>>> sorted(res)
['dev@123', 'devik', 'devik@gmail.com']
>>> t=(1,2,3,4,5)
>>> sum(t)
15
>>> t=(1,2,3,[4,5],6,9)
>>> t[3].append(9)
>>> t
(1, 2, 3, [4, 5, 9], 6, 9)
>>> t=({1,2},{3,4}
t
       
SyntaxError: invalid syntax
>>> d={]
       
SyntaxError: invalid syntax
>>> d={}
       
>>> d={1:2,2:3,}
       
>>> d
       
{1: 2, 2: 3}
>>> 2 in d
       
True
>>> 3 in d
       
False
>>> data={'name':'devik','batchno':44,'course':'pfs'}
       
>>> data
       
{'name': 'devik', 'batchno': 44, 'course': 'pfs'}
>>> data['name']
       
'devik'
>>> data.get('age')
       
>>> data.get('name')
       
'devik'
>>> data.get('age','key is not there')
       
'key is not there'
>>> data.get('name','key is not there')
       
'devik'
>>> data.setdefault('age',21)
       
21
>>> data
       
{'name': 'devik', 'batchno': 44, 'course': 'pfs', 'age': 21}
>>> data.setdefault('name','ushaswini')
       
'devik'
>>> data.setdefault('dob')
       
>>> data.setdefault('dob','05-11-2003')
       
>>> data
       
{'name': 'devik', 'batchno': 44, 'course': 'pfs', 'age': 21, 'dob': None}
>>> d[{1:2}]='dict'
       
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    d[{1:2}]='dict'
TypeError: unhashable type: 'dict'
>>> d[1.2]='float'
       
>>> d['str']='string'
       
>>> d[[1,2,3]]='list'
       
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
>>> d['str']='string datatype'
       
>>> d
       
{1: 2, 2: 3, 1.2: 'float', 'str': 'string datatype'}
>>> 
