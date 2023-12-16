import random
#Show me love
list1 = []
a = random.randint(0,10)
if a == 1:
    print(a, "Good game")
elif a == 2:
    print(a, "Baby don't hurt me")
else:
    print(f'{a} "What is love"')
    list1.append(a)

print(list1)