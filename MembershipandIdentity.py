#membership
s1="apple is a fruit"
s2="apple"
s3="fruit"
s4="mango"

print(s4 in s1)
print(s2 in s3)
print('a' in s4)
print(s3 not in s2)

#identity
a=10
b=20
c='10'
d=10.1
print(a is b)
print(b is d)
print(d is not a)
print(a is not b)