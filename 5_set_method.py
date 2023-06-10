b = set()
print(type(b))

#adding values to an empty set
b.add(2)
b.add(5)
b.add(5)
b.add(5)
b.add((4, 8, 9, 10)) # we can add the tuples in set.

#Accessing elements
#b.add([1, 5, 8, 9]) # i can not add the list in set. not hashable
print (b)

#length of the set
print(len(b)) # print the length of this set

# removel of an Items
b.remove(5) #remove 5 from set b
#b.remove(8) # throws an error while tryong to remove 8(which is not in set represented)
print(b)

# this will remove the number form there
print(b.pop())
print(b)


print(b.union({8, 11, 48}))
print(b)

print(b.intersection({8, 11, 48}))
print(b)