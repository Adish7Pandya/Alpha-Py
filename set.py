myset = set([1, 2, 3, 4, 5])
print(myset) 
#set is mutable, unordered, no duplicate values

myset.add(6)
print(myset)

myset.remove(3)
print(myset)

myset.remove(7)
print(myset)

set1 = {1, 2, 3, 4, 5}
set2 = {1,2,3}

print(set1.issubset(set2))  
print(set1.isdisjoint(set2))  
# Output: False
set1 = frozenset{1, 2, 3, 4, 5}


