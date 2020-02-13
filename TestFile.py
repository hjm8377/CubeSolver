import copy


def sync(k):
    k += 1
    print("num", id(k), k)
    return k

a = 0
print("a", id(a), a)
a = sync(a)
print("a", id(a), a)

print(a)
