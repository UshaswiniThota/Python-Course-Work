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