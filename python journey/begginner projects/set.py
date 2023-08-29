'''myset = set()


myset.add(9)
myset.add(78)
myset.add(8)

print(myset.pop())'''

odds = {1,3,5,7,9}
even = {0,2,4,6,8}
prime = {2,3,5,7}
u = odds.union(even)
print(u)

odds.update(even)
print(odds)
prime.intersection_update(even)
print(prime)

oddss =  odds.copy


print(oddss)
print(oddss)