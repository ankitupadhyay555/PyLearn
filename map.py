# Python program to demonstrate working 
# of map. 

# Return double of n 
def addition(n): 
	return n + n 

# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers)
#Map takes 2 args, func and iter.
#func is a function that i calls
#Iter is iterable item that is passed one by one
#The output is a generator object
#which can be accessed by converting it into one of the iterable objects like a list, tuple etc
print(result)
print(list(result)) 


#Both are same, so you cannot print a map object directly. But you can assign it.
#if you want to print type casting is necessary
# >>> a,b = map(int,input().split())
# 1 2
# >>> a
# 1
# >>> b
# 2
# >>> a,b = list(map(int,input().split()))
# >>> a
# 1
# >>> b
# 2