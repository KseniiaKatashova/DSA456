# Part A - Recursive functions
# •	Write the following python functions recursively.
# •	A non-recursive solution that works will not be given credit (even if it passes testing)
# function 1:
# This function is passed a number and returns
#  (number)(number-1)(number-2)...(3)(2)(1). By definition, 0! = 1
# Only a recursive solution will be accepted!

def factorial(number):
    f= 1
    if(number>1):
        f = number * factorial(number-1)
    return f

print(factorial(5))

#function 2:
#Write the RECURIVE function linear_search. linear_search() is passed a list of values and a key. If a matching key is found in the list, function returns index of where the key was found. If the key is not found, function returns -1.

def linear_search(list, key):
     return linear_search_rec(list, key, 0, len(mylist) -1)

def linear_search_rec(list, key, first, last):
    if first > last:  
        return -1
    if list[first]==key:
        return first
    return linear_search_rec(list, key, first + 1, last)

mylist =[5,1,47,35,6,98]
key = 6

print(linear_search(mylist, 6))

#function 3:
# Write the RECURIVE function binary_search. binary_search() is passed a sorted list of values and a key. If a matching key is found in the list, function returns index of where the key was found. If the key is not found, function returns -1.
# Note: you are not allowed to use any of the built in list functions for this problem. The only function you are allowed to use is len()
def binary_search(list, key):
     return binary_search_rec(list, key, 0, len(list)-1)

def binary_search_rec(list, key, first, last):
    if first <= last:  
        mid = (first + last)//2
        
        if list[mid] == key:
            return mid
        elif key < list[mid]:
            return binary_search_rec(list, key, first, mid-1,)
        elif key > list[mid]:
            return binary_search_rec( list, key, mid+1, last)
    else:
        return -1

mylist=[5, 12, 36, 54, 78]

print(binary_search(mylist, 36))


#Part B Analysis
# Perform an analysis of the following recursive functions.
# Analyze the following functions with respect to numbers:

Part A: Recursive functions											Student: Kseniia Katashova											
											Student ID# 138164207											
	Function 1:																					
																						
	def factorial(number):																					
	    f= 1																					
	    if(number>1):																					
	        f = number * factorial(number-1)																					
	    return f																					
																						
	print(factorial(5))																					
	Output: 120																					
																						
																						
																						
	Function 2:																					
																						
	def linear_search(list, key):																					
	     return linear_search_rec(list, key, 0, len(list) -1)																					
																						
	def linear_search_rec(list, key, first, last):																					
	    if first > last:  																					
	        return -1																					
	    if list[first]==key:																					
	        return first																					
	    return linear_search_rec(list, key, first + 1, last)																					
																						
	mylist =[5,1,47,35,6,98]																					
	key = 6																					
	print(linear_search(mylist, 6))																					
	Output: 4																					
																						
																						
																						
																						
	Function 3:																					
																						
	def binary_search(list, key):																					
	     return binary_search_rec(list, key, 0, len(list)-1)																					
																						
	def binary_search_rec(list, key, first, last):																					
	    if first <= last:  																					
	        mid = (first + last)//2																					
	        																					
	        if list[mid] == key:																					
	            return mid																					
	        elif key < list[mid]:																					
	            return binary_search_rec(list, key, first, mid-1,)																					
	        elif key > list[mid]:																					
	            return binary_search_rec( list, key, mid+1, last)																					
	    else:																					
	        return -1																					
																						
	mylist=[5, 12, 36, 54, 78]																					
	print(binary_search(mylist, 54))																					
	Output: 3																					
																						
																						
																						
	Function 4:																					
																						
	def hanoi_tower(n, source,  middle, destination):																					
		if n==1:																				
			print ("Move disk 1 from ", source," to ", destination)																			
			return																			
		hanoi_tower(n-1, source,  destination, middle)																				
		print ("Move disk",n," from ", source," to ", destination)																				
		hanoi_tower(n-1, middle,  source, destination)																				
																						
																						
																						
	hanoi_tower(3,' A','B','C')																					
																						
																						
																						
																						
																						
Part B: Analysis																						
																						
																						
	Function 1:																					
																						
	def function1(value, number):										T(n)											
		if (number == 0):									1											
			return 1																			
		elif (number == 1):									1											
			return value																			
		else:																				
			return value * function1(value, number-1)								1+1+T(n-1)											
																						
										T(n)=1+1+1+1+T(n-1)												
										T(n) =4+T(n-1)												
										T(n-1)=4+4+T(n-2)…etc												
										T(1) =3 	This is a base case											
										T(n)=4+T(n-1) +3 => 4n+4+3=>7+4n												
										O(n)												
																						
	Function 2:																					
																						
	def recursive_function2(mystring,a, b):											T(m)			T(m/2+1)+3							
		if(a >= b ):										1										
			return True																			
		else:																				
			if(mystring[a] != mystring[b]):									1										
				return False																1245678		123456789
			else:																			
				return recursive_function2(mystring,a+1,b-1)								T(m)+(a+1)+(b-1)+3								9/2+1		10/2 +1
																				5		6
	def function2(mystring):											T(n)			T(m) - worst case is a very long palindrome							
		return recursive_function2(mystring, 0,len(mystring)-1)										3+T(m)			2+2+T(n/2+1)							
																						
												3+2+2+T(n/2 +1)=> 7+.5n										
												O(n)										
