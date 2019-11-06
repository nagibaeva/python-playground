for value in range(1,21):
    print(value)
a = list(range(1,21))
print(a)

a = list(range(1,1000001))
print(min(a))
print(max(a))
print(sum(a))

bs = list(range(1,21,2))
for b in bs:
    print(b)

by_3s = list(range(3,30,3))
print(by_3s)

threes = []
for value in range(3,30):
    three = value**3
    threes.append(three)
print(threes)

cubes = [value**3 for value in range(1,10)]
print(cubes)

print("Done with Try It Yourself from 4.3 to 4.9")