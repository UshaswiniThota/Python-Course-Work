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