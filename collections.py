from collection import defaultdict, namedtuple, deque
d.append(1)
d.append(2)

d.appendleft(0)
print(d)

d.extend([3, 4, 5])
print(d)

d.rotate(2)
print(d)