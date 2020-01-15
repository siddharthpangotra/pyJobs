names = ['sid', 'kom', 'mary', 'simba', 'jana']
names_2 = ['shankar', 'musi']
# print(names)
# print(names[1:3])#includes first index but ignores the second
# print(names[-2]) #this gives the seconf last value from the list
# this gives you the list of operations that can be performed on list
print(dir(names))

# sorting the values asc(by default)
# names.sort()
# print(names)

# names.sort(reverse=True)
# print('#reverse sorting')
# print(names)


# names.insert(5, 'kukka')
# print('#adding a string @ index 5')
# print(names)

# adds a list into a list at index 6
names.insert(6, names_2)
print('#adding a list at index 6')
print(names)

# removes the last index
names.pop()
print('#removing the last index')
print(names)

# finding values in list returns bool
print('jana' in names_2)

# coverting list to a string
names3 = '-'.join(names)
print(names3)

# converting string to a list
list1 = names3.split('-')
print(list1)
tuple1 = ('tup1', 'tup2', 'tup3')
print(tuple1)
tuple2 = ('tup4', 'tup5')
tuple2[0] = 'tup2'
