# This is a basic example of a "for loop" 
# range(0, len(array)) : is the same as (0, 1, 2, 3, 4)
array = ['10','20','30','40','50']

for i in range(0, len(array)) :
    array[i] = int(array[i])
print(array)

# This is a basic example of a "while loop" 
array = ['10','20','30','40','50']
i=0
while i < len(array) :
    array[i] = int(array[i])
    i = i + 1
print(array)

# This is a basic example of an if statement
# The different comparison operators are: ==, !=, >, <, >=, <=
array = ['10','20','30','40','50']
i=0
if i > len(array) :
    print(array[i])
    i = i + 1 #this is the same as i += 1
    print(array)
elif i == 0:
    print('different message')
else:
    print('shits failed you')
    