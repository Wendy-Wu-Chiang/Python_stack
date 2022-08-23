# 1) Basic - Print all integers from 0 to 150.

# def basic():
#     for i in range (151):
#         print(i)
# basic()



# 2) Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# def multiple_of_five():
#     for i in range (5, 1001, 5):
#         print(i*i)
# multiple_of_five()    



# 3) Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

# def dojo_way():
#     for i in range (1, 101):
#         if i % 5 == 0:
#             print("Coding")
#         elif i % 10==0:
#             print("Coding Dojo")
#         else:
#             print(i)
# dojo_way()    



# 4) Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# def add_odds():
#     sum=0
#     for i in range (1, 500001, 2):
#         sum=sum+i
#     print(sum)
# add_odds() 




# 5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

# def down_fours():
#     for i in range (2008, 0, -4):
#         print(i)
# down_fours()



# 6) Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
 
# def flexible_num(low, high, mult):
#     for i in range(low, high, 1):
#         if i % mult ==0:
#             print(i)
# flexible_num(0, 10, 4)
