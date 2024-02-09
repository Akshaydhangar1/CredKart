
#  Initialization of set by curly {}brackets
# y={'y', 'n', 't', 'p', 'h', 'o'}
# x={1,2,3,4,5}
# z={50,'Amit',10000,"Pune",'CSE'}
# print('curly {}brackets y: ', y)
# print('curly {}brackets x: ', x)
# print('curly {}brackets z: ', z)
# print(type(x))
# print(type(y))
# print(type(z))

#
# Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
# print(Days)
# print(type(Days))
#
# # create a set of integer type
# student_id = {112, 114, 116, 118, 115}
# print('Student ID:', student_id)
# print(type(student_id))
#
# # create a set of string type
# list_a=['a', 'e', 'i', 'o', 'u', 'a']
# print("List ye dikhayega",list_a)
# tuple_b=('a', 'e', 'i', 'o', 'u', 'a')
# print("Tuple ye dikhayega",tuple_b)
# set_c = {'a', 'e', 'i', 'o', 'u', 'a'}
# print("Set ye dikhayega",set_c) # unique

#
# # # create a set of mixed data types
# mixed_set = {'Hello', 101, -2, 'Bye',101.6}
# print('Set of mixed data types:', mixed_set)
# print(type(mixed_set))
# #
# set()
# emp1 = set ("Yusuf")
# emp2 = set ((101,102,"Amit","Priya","Priya"))
# emp3=set([101,102,"yusuf","Akashay",101,"Akshay"])
# # #
# print(emp1)
# print(emp2)
# print(emp3)
#
# emp4=set("Yusuf")
# print(emp4)
# emp5=set(("Yusuf","Pooja"))   # In this Tupple in which two elements are present
# print(emp5)
# emp5=set("Yusuf","Pooja")  # TypeError: set expected at most 1 argument, got 2
# #
# print(emp5)


# Initialization of set by set() Constructor
# x = set("python")
# print('By set() constructor: ', x)
# Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
# print(Days)
# print(type(Days))
# Days1 = set(("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
# print(Days1)
# print(type(Days1))       # In This After Set((Tupple is element))
#
# # # create an empty set
# empty_set = set()
# # # create an empty dictionary
# empty_dictionary = {}
# #
# print(empty_set)
# #
# # # check data type of empty_set
# print('Data type of empty_set:', type(empty_set))
# #
# print(empty_dictionary)
# #
# # # check data type of dictionary_set
# print('Data type of empty_dictionary', type(empty_dictionary))
#
# {101} --#Set
# {101,102}--#Set
# {101,102,"YUsuf"} --#Set

## {}--#Empty set --ye galat hai {} ye hamesha empty disctionary hoti hai jo ham dekhne vale hai.



# numbers = {2, 4, 6, 6, 2, 8}
# print(numbers)   # {8, 2, 4, 6}
#
# numbers = {2, 4, 6, 6, 2, 8}
# numbers[0]=101
# print(numbers) # TypeError: 'set' object does not support item assignment
#
# numbers = {21, 34, 54, 12}
# print('Initial Set:',numbers)

# # # # using add() method

# numbers.add(90)
# numbers.add(150)
# print('Updated Set:', numbers)

# companies = {'Lacoste', 'Ralph Lauren'}
# companies.add("TCS")
# print(companies)
#
# companies = {'Lacoste', 'Ralph Lauren'}
# companies.add(("Cogni","Capg"))    #add(Tupple)
# print(companies)

# companies = {'Lacoste', 'Ralph Lauren'}
# companies.add(["Cogni","Capg"])  #TypeError: unhashable type: 'list'
# print(companies)
# #
# companies = {'Lacoste', 'Ralph Lauren'}
# tech_companies = ['cogni', 'capg', 'cogni']
# companies.update(['cogni', 'capg', 'cogni'])      # Same As Below Both Having same meaning
# companies.update(tech_companies)                # Same As Above both having same meaning
# #
# print(companies)
#
# x={1,6}
# y={2,3,4,5}
# print('Set y: ', y)
# print('Set x: ', x)
#
#
# # Update y to set x
# x.update(y)

#
# print('Set y: ', y)
# print('Set x after update: ', x)
#
# y.update(x)
# print('Set y after update: ', y)

# # Initialization of set x
# x={'Python','Java','PHP','Angular'}
# print('Set x: ', x)
# x.remove('Java')
# print('Set x after remove: ', x)
# #
# x.discard('PHP')
# print('Set x after discard: ', x)
#
# # # Initialization set x
# x={1,2,"py"}
# print('Print set x: ', x)
# # # pop random element from the set x
# z=x.pop()
# print('Random Pop element of set x: ', z)
# print(x)
# #
# A = {'f', 'b', 'd', 'e'}
# removed_item = A.pop()
# print(removed_item)
# print(A)
#
# # Output:
# # set of prime numbers
#
# # clear all element from set
# A.clear()
# print('Print set x after clear: ', A)
#
# # set of prime numbers
# primeNumbers = {2, 3, 5, 7}
# print(primeNumbers)
# # # clear all elements
# primeNumbers.clear()
# # #
# print(primeNumbers)

# first set
# A = {1, 3, 5,2}
#
# # second set
# B = {0, 2, 4, 1}
#
# perform union operation using |
# print('Union using | operator:', A | B)
# #
# # perform union operation using union() method
# print('Union using union() method:', A.union(B))


# first set
# A = {1, 3, 5}
# #
# # # second set
# B = {1, 2, 3}
# #
# # # perform intersection operation using &
# print('Intersection using & Operator:', A & B)
# #
# # # perform intersection operation using intersection()
# print('Intersection using intersection():', A.intersection(B))


# first set
# A = {2, 3, 5}
# # # #
# # # # # second set
# B = {1, 2, 6,5}
# # # #
# # # # perform difference operation using &
# print('Difference using &:', A - B)
# # #
# # # # perform difference operation using difference()
# print('Difference using difference():', A.difference(B))
# # #
# print('Difference using &:', B - A)
# print('Difference using difference():', B.difference(A))
# #
# # perform difference operation using &
# print('using ^:', A ^ B)
#
# # using symmetric_difference()
# print('using symmetric_difference():', A.symmetric_difference(B))


# # Initialization of set x and y
# x={1,2}
# y={1,2,3,4}
# #
# # # check if set x is subse of y
# print(x.issubset(y))
#
# z=x.issubset(y)
# print('Check if x is subset of y: ', z)

# # Initialization set x and y
# x={1,2}
# y={3,4}
# #
# # # Check if set x and y are disjoint
# print(x.isdisjoint(y))
# z=x.isdisjoint(y)
# print('Check if set x and y are disjoint:', z)
#
#
# # # Initialization of set x and y
# # x = {'a','b','c'}
# # y = {'a','b','c'}
# # print('Set x: ', x)
# # print('Set y: ', y)
# # #
# # # # Operator with set
# # print('Set x == y: ', x==y)
# # # #
# # print('Set x != y: ', x != y)
# #
# # # Initialization of set x and y
# x = {1,2}
# y = {1,2,4,5}
# print('Set x: ', x)
# print('Set y: ', y)
# #
# print('Set x <= y: ', x <= y)
# # #
# print('Set x < y: ', x < y)
# #
# # # Initialization of set x and y
# x = {1,2,3,4,5}
# y = {1,2,3}
# # print('Set x: ', x)
# # print('Set y: ', y)
# print('Set x superset y:', x >= y)
# print('Set x proper superset y:', x > y)
#
# x = {1,2,8}
# y = {1,2,4,5}
# print('Intersection  x & y:', x & y)
# print('Union of x & y:', x | y)
# print('Difference of x & y:', x - y)
# print('Difference of y & x:', y - x)
# print('Symmetric Difference of  x & y:', x ^ y)

