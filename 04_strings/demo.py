# # strings

# # Using '' or "" or """ is valid for single line strings
# # data_1 = "hello"
# # data_2 = 'hello'
# # data_3 = '''hello'''
# # data_4 = """hello"""
# # print('data_1')
# # print("data_2")


# # multi line strings -> """ are must
# # Below is not valid
# # python_desc = "Python is a high-level, general-purpose 
# # programming language. Its design philosophy emphasizes 
# # code readability with the use of significant indentation"

# python_desc = """Python is a high-level, general-purpose 
# programming language. Its design philosophy emphasizes 
# code readability with the use of significant indentation"""

# question = "How are you ?"
# # using a single quote inside single quotes is not valid
# # if you want to include single quote, use double quotes
# # answer = 'i'
# # m fine' not valid
# #print(answer)
# # answer = "i'm good"
# # print(answer)

# # # answer = "im "good""
# # answer = 'im "good"'
# # print(answer)

# # if you need both use ''' or """
# # answer = """ i'm fine and "good" """
# # print(answer)

# # Accessing
# #  
# # text = "python"
# # print(text[0])
# # print(text[6]) # OUT OF RANGE AS 6TH INDEX IS NOT PRESENT
# # print(text[5])
# # print(text-2])

# # text = "python"
# # # using for loop to access each character
# # for i in text:
# #     print(i)

# # text = "python"
# # print(text[1])
# # print(text[2])
# # print(text[3])


# # Slicing
# # text = "My name is shravan"
# #print(text[0:3]) # last is excluded -> My
# #print(text[1:4]) # last is excluded -> y n
# #print(text[1:]) # last is excluded -> y name is shravan
# #print(text[:4]) # last is excluded -> My n
# #print(text[:]) # last is excluded -> My name is shravan

# # if step is not defined, default step is 1
# # print(text[1:4:1]) # last is excluded -> yth
# # text = "Mynameisshravan"
# # text1 = "My name is shravan"
# # print(text[0:10:2]) # last is excluded -> Mnmis
# # print(text1[0:10:2]) # last is excluded -> M aei


# # For negative indexing default step is 1
# # text = "python" # ValueError: slice step cannot be zero
# # print(text[1:4:0]) 
# # text = "shravan"
# # print(text[-5:-1]) # rava
# # print(text[-5:-1:1]) # rava
# #print(text[-5:-1:-1]) # Start from index -5 ('y'), go towards index -1 ('n'), stepping backwards (-1).

# # Important rule:
# # When using a negative step, the start index must be greater than the stop index (i.e., it counts backwards).
# # Here, -5 is less than -1, so nothing will be returned.

# # print(text[-4:-1:-1]) # 
#         #     0  1  2  3  4  5 (positive)
#         #     p  y  t  h  o  n 
#         #    -6 -5 -4 -3 -2 -1 (negative)
# # start -4 -> index -> 2 -> t
# # end -1 -> index -> 5 -> n (excluded)
# # step -1 -> move backwards

# # IMP: You starting at index 2 and trying to go backward to
#     # index 5 -> nothing

# # text = "python"
# # print(text[1:4:-1])
#         #     0  1  2  3  4  5 (positive)
#         #     p  y  t  h  o  n 
#         #    -6 -5 -4 -3 -2 -1 (negative)
# # start 1 -> index -> 1 -> y
# # end 4 -> index -> 4 -> o (excluded)
# # step -1 -> move backwards
# # Typical use case of backward step
# text = "python"
# # print(text[::-1])


# print(text[-2:-5:1]) you are going backward so output will be empty
# print(text[-2]+text[-3]+text[-5]) #ohy

# String Immutability
# TypeError: 'str' object does not support item assignment
# text = "python"
# # text[0] = "P"
# print(text)

# Reassigning is okay 
# text = "python"
# text = "Python" # new 
# print(text)

# new_text = "J" + text[1:]
# print(new_text)

# Concat(+) Join Strings 
# Repeat (*) Repeat Strings
# Concat -> join multiple strings
# str = "hi"
# print(str * 5)

# # String Operations -> String Methods
# print(dir(str))

# mobile_number = input("Enter Mobile Number: ")
# valid_number = mobile_number.isdigit()
# print(valid_number)

# pan_number = input("Enter PAN Card Number: ")
# valid_pan_number = pan_number.isalnum()
# fomart_valid_pan_number = pan_number.upper()
# print(fomart_valid_pan_number)

#LOWER, UPPER, TITLE AND CAPATALISE FUNCTIONS 


# FOR printing in lower case
w = "My Name Is Shravan"
n=w.lower()
print(n)

# FOR printing in title case
t=w.title()
print(t)

# FOR printing in upper case
u=w.upper()
print(u)

# FOR printing in capatalise case
c=w.capitalize()
print(c)

# # FOR finding the particular letter
# w="welcome"
# print(w.find('el'))     # will print 1
# print(w.find('c'))      # 3
# print(w.find('e',0))    # 1


# FOR finding the particular index
w="welcome"
print(w.index('c'))      # 3
print(w.index('c',2))    # 3

print(w.isalpha())      # true all alphabets are present in w

w="123"
print(w.isalpha())      # false bcoz only digits are present
print(w.isdigit())      # it checks whether all are digits or not

w="welcome123"
print(w.isalnum())      # true -  it will always be true if it is alphabet or digit 
                        # it will be false only if it is special character
w="welcome#123@"                      
print(w.isalnum())      # false 