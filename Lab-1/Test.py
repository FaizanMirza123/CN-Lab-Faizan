import math

# Q1
name=['a','b','c']
name=name[::-1]
print (name)

# Q2
x=8
x=math.sqrt(x)
x=int(x)
print(x)

# Q3
s="A man, a plan, a canal: Panama"
new=""
for i in s:
    if i.isalnum():  
        new += i

print(new)
size=len(new)
condition = True  


divider = size // 2
start2 = size - 1


for start1 in range(divider):
    if new[start1].lower() != new[start2].lower():
        print("not a palindrome")
        condition = False  
        break
    start2 -= 1


if condition:
    print("a palindrome")