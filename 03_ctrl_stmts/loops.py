 # Implementation Of Loops

# while loop
# while condition:
#     statement

# PRINT VALUES FROM 1 TO 5
# i = 1    
# while i <= 5:
#     print("AAAA", i)
#     i += 1

# PRINT VALUES FROM 10 TO 1

# i = 10   
# while i >= 1:
#         print(i)
#         i -= 1

# PRINT multiples of 3 FROM 1 TO 30 / 3 table 

# i = 1
# while i <= 10:
#     print(3*i)
#     i+=1

# a = 10
# while a >= 1:
#     print(a,"shravan")
#     a-=1
# print(a)

# best usecase to understand while
# password = "python123"
# user_input = ""

# while user_input != password:
#     user_input = input("ENTER PASSWORD")
# print("Access Granted")

# text = "python"
# for i in text:
#     print(i)

# num = 10
# for i in num:
#      print(num) #TypeError: 'int' object is not iterable

# num = [10] # LIST -- iterable objects
# for i in num:
#      print(num)

# we cannot use for to iterable objects
# just_num = [10] 
# print(dir(just_num))   


# for elements in sequence
#statements

# text = "python"
# print (dir(text))
# for i in text:
#    print(i) 

#manual work
print("hi")
#say 10 times hi - manually
# print("hi")
# print("hi")
# print("hi")
# print("hi")
# print("hi")
# print("hi")
# print("hi")
# print("hi")
# print("hi")
# print("hi")

#say 10 times hi - automated
# for i in range(10):
#     print("hi")


# for i in range(5,10,3):
#     print(i)

#lets print even nums between 1-20 -> while
# i=2
# while i<=20:
#     print(i)
#     i+=2

#2nd approach
# i=2
# while i<=20:
#     if i%2 == 0:
#         print(i)
#         i+=2

# Nested loops
# maths table

# for i in range(1,4):
#     for j in range(1,11):
#         print(f"{i}X{j} = {i*j}")

# # using while loop
# i=1
# while j<4:
#     print(f"{i} X {j} = {i*j}")
#     j=+1
# i+=1

# break demo
# for i in range(5):
#     if i == 3:
#         break #TERMINATE THE LOOP when i is 3
#     print(i)

# continue demo
for i in range(5):
    if i == 3:
        continue #skip loop when i is 3 (based on index)
    print(i)

# pass demo
if(5>9):
    pass 
