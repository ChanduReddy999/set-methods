"""
set data type
set is represented by { } with element inside it
but we cannot represented an empty set.
if we keep an empty set { } it will treated as dictionary (dict) 
set can contain several data types in it but
we cannot have a list and one more set inside it.
set cannot have one more set inside it.
set is mutable , modifications can be made.
i.e we can add and remove from set
but frozenset is immutable . we cannot add and remove elements in it.
set is unordered.
"""

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

'''clear'''
# b={3,4,55,6}
# b.clear()
# print(b)            # set()

'''intersection'''
# a={1,2,3,4}; b={3,4,5,6}; c={2,3,5,7}; d={1,4,5,7}
# print(a.intersection(b))            # {3,4}
# print(a.intersection(c))        # {2,3}
# print(a.intersection(d))            # {1,4}
# print(b.intersection(d))            # {4,5}

'''union'''
# c={1,2,3,'hello'}
# d={4,5,3,'hey'}
# print(c.union(d))       # {1, 2, 3, 4, 5, 'hello', 'hey'
# print(d.union(c))       # {1, 2, 3, 4, 5, 'hello', 'hey'

'''update'''
# a={1,2,3,8}
# b={4,5,6}
# c={4,3,7}
# a.update(b)
# print(a)                # {1, 2, 3, 4, 5, 6, 8}
# a.update(c)
# print(a)                # {1, 2, 3, 4, 5, 6, 7, 8}
# b.update(a)
# print(b)                # {1, 2, 3, 4, 5, 6, 7, 8}

'''update'''
# a={1,2,3,8}
# b=[4,5,6]
# c={4,3,7}
# a.update(b)
# print(a)                # {1, 2, 3, 4, 5, 6, 8}
# a.update(c)
# print(a)                # {1, 2, 3, 4, 5, 6, 7, 8}
# b.update(a)
# print(b)                # AttributeError: 'list' object has no attribute 'update'

'''difference'''
# a={5,10,15,20,25,30}
# b={10,21,5}
# print(a.difference(b))          # {25, 20, 30, 15}
# print(b.difference(a))          # {21}
# print(a-b)                  # {25, 20, 30, 15}
# print(b-a)                  # {21}

'''discard'''
# x={35,40,45,50,55,60,65}
# x.discard(45)
# print(x)                # {65, 50, 35, 55, 40, 60}
# x.discard(55)
# print(x)                # {65, 50, 35, 40, 60}
# x.discard(34)
# print(x)                # {65, 50, 35, 40, 60}

'''remove'''
# a={14,15,46,57,38,29}
# a.remove(5)
# print(a)            # KeyError: 5
# a.remove(15)
# print(a)            # {38, 14, 57, 29, 46}

'''pop'''
# v={20,30,40,45,50}
# v.pop()
# print(v)            # {20, 40, 45, 30}
# v.pop()
# print(v)            # {40, 45, 30}     # random element gets poped

'''isdisjoint'''
# A={1,2,3,4}
# B={5,6,7,8,11}
# C={2,7,12}
# print('Are A and B disjoint?', A.isdisjoint(B))     # True
# print('Are A and C disjoint?', A.isdisjoint(C))     # False
# print('Are B and C disjoint?', B.isdisjoint(C))     # False

'''issubset'''
# A={1,2,3,4,5}
# B={1,2,3,4,5,6,7,8}
# C={1,2,3,7,8}
# print(A.issubset(B))            # True
# print(B.issubset(A))            # False
# print(A.issubset(C))            # False
# print(C.issubset(A))            # False
# print(B.issubset(C))            # False
# print(C.issubset(B))            # True

'''issuperset'''
# A={1,2,3,4,5}
# B={1,2,3,4,5,6,7,8}
# C={1,2,3,7,8}
# print(A.issuperset(B))          # False
# print(B.issuperset(A))          # True
# print(A.issuperset(C))          # False
# print(C.issuperset(A))          # False
# print(B.issuperset(C))          # True
# print(C.issuperset(B))          # False
