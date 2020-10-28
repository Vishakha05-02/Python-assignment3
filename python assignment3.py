"""1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()"""


lst = [1, 2, 3, 4, 5]
# initialising variable a with 0th index variable
a = lst[0]

def myreduce(add, lst):
    return a

def add(a, b):
    return a + b

for i in range(1, len(lst)):
    b = lst[i]
    a = add(a, b)
# calling the function
print(myreduce(add, lst))




"""1.2 Write a Python program to implement your own myfilter() function which works exactly\n"
 like Python's built-in function filter"""

def myfilter(odd,lst1):
    return odd(a)
lst1=[2,3,4,5,6,7,8,9,10]
lst2=[]
def odd(a):

# condition for finding odd number
    for i in lst1:
        if i%2 != 0:
            lst2.append(i)
    print(lst2)

# to call the function
myfilter(odd,lst1)


"""2. Implement List comprehensions to produce the different lists. """
# first list--> ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

lst1 = ['x', 'y', 'z']
lst2 = [i*j for i in lst1 for j in range(1,5)]
print(lst2)


# second list--> ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

lst1 = ['x', 'y', 'z']
lst2 = [i*j for i in range(1, 5) for j in lst1]
print(lst2)

# third list-->[[2], [3], [4], [3], [4], [5], [4], [5], [6]]

lst = [2, 3, 4]
new_lst = [[a+b] for a in lst for b in range(0,3)]
print(new_lst)

# forth list--> [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

lst1 = [1,2,3]
lst2 = [1,2,3]
lst3 = [(b,a) for a in lst1 for b in lst2]
print(lst3)

#fifth list--> [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
lst = [2, 3, 4, 5]
new_lst = [[a+b for a in lst] for b in range(0,4)]
print(new_lst)