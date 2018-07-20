"""
#Function for checking the divisibility
# Notice the indentation after function declaration
# and if and else statements
def checkDivisibility(a, b):
    if a % b == 0 and a!=b :
        print (b, end=" ")
    else:
        return
#Driver program to test the above function
num = int(input("Enter ingeter value  =  "))
print(num," is divisible by ", end=" ")
for x in range(2,100):
    checkDivisibility(num, x)

"""

"""
#Transpose of a matrix
mat = [[1,2], [3,4], [5,6]]
for row in mat:
    print(row)

option = input("Choose option 1/2/3 :  ")

if option == 1:
    t_matrix = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
elif option == 2:
    import numpy
    t_matrix = numpy.transpose(mat)
else:
    t_matrix = zip(*mat)

print("\n")
for row in t_matrix:
    print(row)


"""

"""

#Linear Search Algorithm
def lsearch(arr, x):
    n = len(arr)
    for i in range(0,n):
        if x == arr[i]:
            return i
    return -1

print("Enter an array of integers")
arr = list(map(int, input().split()))
x = int(input("Enter element to be searched :  "))
print(lsearch(arr,x))

"""

"""

#remove duplicate elements from a string
str = str(input("Enter a string :  "))
new_string   = "".join(set(str))
print(new_string)

#remove duplicate workds from a sentence
str = (input("Enter a string :  "))
l = list(str.split(" "))
print(l)
new_l = " ".join(set(l))
print(new_l)


"""


"""
#reverse a string

s = input("Enter string 1:  ")
str = list(s)
str.sort(reverse=True)
s= "".join(str)
print(s)

"""

"""
#fibonacci series
def fibonacci(prev, curr, n):
    print(prev)
    if n-2 == 0:
        print curr
        return
    fibonacci(curr, curr+prev, n-1)

n = input("Enter no. of terms (>=2) :   ")
print("Fibonacci series :  ")
fibonacci(0, 1, n)

"""


"""
#reverse array by 'd' elements

arr = list(map(int, input().split()))
print(arr)
d = int(input("Reverse array from index:  "))
a = arr[:d]
a.sort(reverse=True)
a+= arr[d:]

print(a)
"""

"""
#diagonal sum

m = int(input("Enter number of columns:  "))
n = int(input("Enter number of rows:  "))
print("Input array in row major order")
arr = [[int(input()) for j in range(n)] for i in range(m) ]
print(arr)

sum = 0

for i in range(len(arr[0])):
    sum+= arr[i][i]

print(sum)
"""
