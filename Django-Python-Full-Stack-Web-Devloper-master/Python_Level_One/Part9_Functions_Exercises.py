# #####################################
# #### PART 9: FUNCTION EXERCISES #####
# #####################################


# # Complete the tasks below by writing functions! Keep in mind, these can be
# # really tough, its all about breaking the problem down into smaller, logical
# # steps. If you get stuck, don't feel bad about having to peek to the solutions!

# #####################
# ## -- PROBLEM 1 -- ##
# #####################

# # Given a list of integers, return True if the sequence of numbers 1, 2, 3
# # appears in the list somewhere.

# # For example:

# # arrayCheck([1, 1, 2, 3, 1]) → True
# # arrayCheck([1, 1, 2, 4, 1]) → False
# # arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
  # CODE GOES HERE
	compare = [1,2,3]
	for x in range(len(nums)):
		if x+2 < len(nums):
			result = [nums[x], nums[x+1], nums[x+2]]
			if compare == result:
				return True
	return False

result1 = arrayCheck([1, 1, 2, 1, 2, 3])
print(result1)


# #####################
# ## -- PROBLEM 2 -- ##
# #####################

# # Given a string, return a new string made of every other character starting
# # with the first, so "Hello" yields "Hlo".

# # For example:

# # stringBits('Hello') → 'Hlo'
# # stringBits('Hi') → 'H'
# # stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  # CODE GOES HERE
	return str[::2]

result2 = stringBits('Heeololeo')
print(result2)


# #####################
# ## -- PROBLEM 3 -- ##
# #####################

# # Given two strings, return True if either of the strings appears at the very end
# # of the other string, ignoring upper/lower case differences (in other words, the
# # computation should not be "case sensitive").
# #
# # Note: s.lower() returns the lowercase version of a string.
# #
# # Examples:
# #
# # end_other('Hiabc', 'abc') → True
# # end_other('AbC', 'HiaBc') → True
# # end_other('abc', 'abXabc') → True

def end_other(a, b):
  # CODE GOES HERE
	a, b = a.lower(), b.lower()
	x = a.split(b)
	y = b.split(a)
	if (len(x) > 1 and x[len(x)-1] == '') or (len(y) > 1 and y[len(y)-1] == ''):
		return True
	else:
		return False

result3 = end_other('abc', 'abcXabc')
print(result3)


# #####################
# ## -- PROBLEM 4 -- ##
# #####################

# # Given a string, return a string where for every char in the original,
# # there are two chars.

# # doubleChar('The') → 'TThhee'
# # doubleChar('AAbb') → 'AAAAbbbb'
# # doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
  # CODE GOES HERE
	res = ''
	for i in range(len(str)):
		res = res + str[i]*2
	return res

result4 = doubleChar('The')
print(result4)


# #####################
# ## -- PROBLEM 5 -- ##
# #####################

# # Read this problem statement carefully!

# # Given 3 int values, a b c, return their sum. However, if any of the values is a
# # teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# # and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# # takes in an int value and returns that value fixed for the teen rule.
# #
# # In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# # Define the helper below and at the same indent level as the main no_teen_sum().
# # Again, you will have two functions for this problem!
# #
# # Examples:
# #
# # no_teen_sum(1, 2, 3) → 6
# # no_teen_sum(2, 13, 1) → 3
# # no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  # CODE GOES HERE
	return (fix_teen(a)+fix_teen(b)+fix_teen(c))

def fix_teen(n):
  # CODE GOES HERE
	if n>=13 and n<=19:
		if n==15 or n==16:
			return n
		else:
			return 0
	else:
		return n

result5 = no_teen_sum(2,1,14)
print(result5)

# #####################
# ## -- PROBLEM 6 -- ##
# #####################

# # Return the number of even integers in the given array.
# #
# # Examples:
# #
# # count_evens([2, 1, 2, 3, 4]) → 3
# # count_evens([2, 2, 0]) → 3
# # count_evens([1, 3, 5]) → 0

def count_evens(nums):
  # CODE GOES HERE
	return len(list(filter(lambda num: num%2==0, nums)))
	
result6 = count_evens([2, 1, 2, 3, 4,45,65,12])
print(result6)

