#tuples
# empty_tuple = ()
# print(type(empty_tuple))
# print(empty_tuple)

# #numbers
# tuple_nums = (10,20,30,40,50)
# print(tuple_nums)

# # texts
# tuple_courses = ("python","java","cloud")
# print(tuple_courses)

# # mixed texts
# tuple_mixed = (10,20,30,"python","java","cloud")
# print(tuple_mixed)

# # tuple_int = tuple(10) # invalid
# # tuple_int = tuple((10))  # invalid

# # list
# list_nums = [10,20,30,40,50]
# print(list_nums)

# # Accessing the data in list
# tuple_nums = (10,20,30,40,50)
# first_tuple_nums = tuple_nums[0]
# last_tuple_nums = tuple_nums[-1]

# # Indexing
# print(first_tuple_nums)
# print(last_tuple_nums)

# # Slicing
# tuple_nums = (10,20,30,40,50)
# print(tuple_nums[:])
# print(tuple_nums[1:4:-1])
# print(tuple_nums[::-1])
# print(tuple_nums[1:4:1])

# tuple_nums = [10,20,30,40,50]
# for i in tuple_nums:
#     print(i)

# using range
# tuple_nums = tuple(range(0,26,5))
# print(tuple_nums)

# # perform any operations with operators
# tuple_nums = tuple(range(0,26,5))
# for i in tuple_nums:
#     print(i*2)

# perform some conditionals
days = ("sun","mon","tue","wed","thu","fri","sat")
day = input("Enter day name in a week:")
if day in days:
    print("day exists")
else:
    print("invalis day exists")

#duplicates are allowed
tuple_nums = [10,20,30,40,50,10,20]
print(tuple_nums)

# count() -> counts and returns number of times a element present
tuple_nums = (10,20,30,40,50,10)
print(tuple_nums.count(10))





