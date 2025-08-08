# mutable
# l=[10,20,30,40,50,"Hello"]
# print(type(l))

# print(l[3],l[5])
# print(l[0:2])
# print(l[0::2])
# print(l[3:])
# print(l[-3::-1])
# print("="*30)
 
# l=[10,20,30,40,50,60]
# t=len(l)
# print(t)
# for n in range(t):
#     print(l[n])
#     print("&"*30)
# for n in range(t-1,-1,-1):
#     print(l)
# for n in range(t-1,-1,-3):
#     print(l[n])

# list iteration
# l=[10,20,30,40,50,60,70,80,90]
# t=len(l)
# for a in range(t):
#     print(l[a])

# for a in l:
#     print(a)

#     for a in range(t-1,-1,-1):
#         print(l[a])

# list comprehension


# l=[]
# for a in range(1,101):

#     l.append(a)
# print(l)
# print("&"*30)
# n=[h for h in range(1,101) if h % 2==0]
# print(n)

# print(*range(1,101,2))

# s="hello"
# d=[g for g in s]
# print(d)

# functions for delete element in list
# del()
# pop()
# remove()
# clear()

# l=[10,20,30,40,50,60]
# del l[1]   # it will delete 1st index
# print(l)

# pop()
# l=[10,20,30,40,50,60]
# l.pop(3)   # it will ignore/remove 3rd index
# print(l)
# l=[10,20,30,40,50,60]
# print(l.pop(2))   

# # remove()
# l=[10,20,30,40,50,60]
# l.remove(30)   
# print(l)

# clear()
# l=[10,20,30,40,50,60]
# l.clear()    # clear all the list
# print(l)

# l=[20,30,40,50,60]
# l[0]=10
# print(l)  # it changes 0th index  from 20 to 10

# function for update element from list
#insert()
# l=[20,30,40,50,60]
# l.insert(0,10)
# print(l)

# #append
# l=[20,30,40,50,60]
# l.append(70) # append the list 70 will add at the end
# print(l)

# l=[20,30,40,50,60]
# n=[50,60]
# l.append(n) # append list in list
# print(l)

# # extend
# l=[20,30,40,50,60]
# n=[50,60]
# l.extend(n) # extend list in main list
# print(l)

# list function

# l=[10,20,10,40,50,60]
# a=l.count(10)
# print(a)         # it will count how many times a particular value is there in the list

# # max
# l=[10,20,10,40,50,60]
# m=max(l)
# print(m) # will give max value

# n=['Hello','World']
# m=max(n)
# print(m) # find the longest word instead of the max alphabetically!

# #min
# l=[10,20,10,40,50,60]
# m=min(l)
# print(m) # will give min value

# #sort
# l=[100,20,60,40,30,80]
# l.sort() # sort the elements int the list
# print(l)

# # reverse
# l=[100,20,60,40,30,80]
# l.reverse() # print in reverse order
# print(l)

# # index
# l=[100,20,60,40,30,80]
# l.index(20) # print index 
# print(l)

# index
l=[100,20,60,40,80]
l1=[10,20,10,40,50,60]
for a,b in zip(l,l1):
    print(l)
