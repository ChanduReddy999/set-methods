# a={}
# print(e, type(e)) #{} <class 'dict'>

# a={1,2.4,"hello",("hi",2)}
# print(a,type(a))                # {'hello', 1, 2.4, ('hi', 2)} <class 'set'>

# n={1,2,3,4,5}
# print(n[1])             # TypeError: 'set' object is not subscriptable

# a={1,2,3}
# b='hello',1,2,3
# a.add(b)
# print(a)                # {1, 2, 3, ('hello', 1, 2, 3)}

# a={1,2,3}
# b={'hello',1,2,3}
# a.add(b)
# print(a)                # TypeError: unhashable type: 'set'


# a={1,2,3}
# b=['hello',1,2,3]
# a.add(b)
# print(a)                # TypeError: unhashable type: 'list'

# b={3,4,55,6}
# b.clear()
# print(b)            # set()

# a={1,2,3,4}; b={3,4,5,6}; c={2,3,5,7}; d={1,4,5,7}
# print(a.intersection(b))            # {3,4}
# print(a.intersection(c))        # {2,3}
# print(a.intersection(d))            # {1,4}
# print(b.intersection(d))            # {4,5}

# c={1,2,3,'hello'}
# d={4,5,3,'hey'}
# print(c.union(d))       # {1, 2, 3, 4, 5, 'hello', 'hey'
# print(d.union(c))       # {1, 2, 3, 4, 5, 'hello', 'hey'




