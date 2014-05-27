x = 0
x = x & 1
print x
x |= 1
x |= 2
print x

x = 0
print x
#x = x | 1
x |= 2
print x
x ^= 1
print x

print '---------'

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

b1 = 1 << 0
b2 = 1 << 1
b3 = 1 << 2
b4 = 1 << 3
b5 = 1 << 4

print b1, b2, b3, b4, b5

mask = b1 | b2 | b3 | b4 | b5 

print mask, ~mask
print bin(mask), bin(~mask)

policy = 4
print bin(policy)
print ~mask & policy > 0

policy = 100
print bin(policy)
print ~mask & policy > 0