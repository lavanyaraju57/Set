"""SET"""

# v={1,2,3}
# print(v,type(v))

# v={1,2.6,"hello",("hi",2)}
# print(v,type(v))

"""FROZENSET"""

# d={1,2,3}
# print(d,type(d))
# k=frozenset(d)
# print(k)
# print(k,type(k))

'''SET METHODS'''

'''ADD'''

# a={1,2,3}
# b='hello',1,2,3
# a.add(b)
# print(a)

'''CLEAR'''

# b={1,2,3}
# b.clear()
# print(b)

'''INTERSECTION'''

# a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}

# print(a.intersection(b))
# print(a.intersection(c))
# print(a.intersection(d))
# print(b.intersection(d))
# print(c.intersection(a))
# print(d.intersection(c))
# print(d.intersection(a))
# print(d.intersection(b))

'''UNION'''

# a={1,2,3}
# b={4,3,5}
# print(a.union(b))
# print(b.union(a))

'''UPDATE'''

# a={1,2,3}
# b={4,3,5}
# c={4,3,7}
# a.update(b)
# a.update(c)
# c.update(a)
# print(c)

'''DIFFERENCE'''

# a={5,10,20,25,30}
# b={10,21,5}
# print(a.difference(b))
# print(b.difference(a))
# print(a-b)
# print(b-a)

'''DISCARD'''

# z={55,56,57,73,45,23}
# z.discard(4)
# print(z)
# z.discard(73)
# print(z)

'''POP'''

# v={26,7,11,4,23}
# v.pop()
# print(v)

'''ISDISJOINT'''

# A={1,2,3,4}
# B={5,6,7}
# C={4,5,6}
# print('Are A and B disjoint?',A.isdisjoint(B))
# print('Are A and C disjoint?',A.isdisjoint(C))
# print('Are B and C disjoint?',B.isdisjoint(C))

'''ISSUBSET'''

# A={1,2,3}
# B={1,2,3,4,5}
# C={1,2,4,5}
# print(A.issubset(B))
# print(B.issubset(A))
# print(A.issubset(C))
# print(C.issubset(B))

'''DIFFERENCE_UPDATE'''

# a={5,12,15,18,20}
# b={15,18,21,25}
# a.difference_update(b)
# b.difference_update(a)
# print(a)
# print(b)

'''COPY'''

# a={1,2,3,4,5}
# a.copy()
# print(a)

'''SYMMETRIC_DIFFERENCE_UPDATE'''

# a={5,12,15,18,20}
# b={15,18,21,25}
# a.symmetric_difference_update(b)
# print(a)
# b.symmetric_difference_update(a)
# print(b)

'''intersection_update'''

# a={5,12,15,18,20}
# b={15,18,21,25}
# a.intersection_update(b)
# print(a)
# b.intersection_update(a)
# print(b)

'''INTERSECTION'''

# a={8,9,10,12,14}
# b={15,18,21,25}
# print(a.intersection(b))
# print(b.intersection(a))

'''REMOVE'''

# a={8,9,10,12,14}
# a.remove(14)
# print(a)

'''ISSUPERSET'''

# a={8,9,10,12,14}
# b={10,14,15,1}
# print(a.issuperset(b))
# a={8,9,10,12,14}
# b={8,9,10}
# print(a.issuperset(b))
# print(b.issuperset(a))
