# 1)Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9]]
# student = [
#     {'first_name': 'Michael', 'last_name': 'Jordon'},
#     {'first_name' : 'John', 'last_name': 'Rosales'}
# ]
# sports_dictionary = {
#     'basketball' : ['Kobe', 'Jordon', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z=[{'x': 10, 'y' : 20}]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# x[1][0]=15
# print(x)


# Change the last_name of the first student from 'Jordan' to 'Bryant'

# student[0]['last_name']='Bryan'
# print(student)


# In the sports_directory, change 'Messi' to 'Andres'

# sports_dictionary['soccer'][0]='Andres'
# print(sports_dictionary)


# Change the value 20 in z to 30

# z[0]['y']=30
# print(z)





# 2)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterateDictionary(some_list):
#     for idx in range(len(some_list)):
#         for key in some_list[idx]:
#             print(key, '-', some_list[idx][key])

# students = [
#     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# iterateDictionary(students)





# 3) Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output: Michael  John  Mark  KB.
# And iterateDictionary2('last_name', students) should output:Jordan Rosales Guillen    Tonel
# def iterateDictionary2(key_name, some_list): 
#     for idx in range(len(some_list)):
#         print(some_list[idx][key_name])
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)




# 4)Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 
# For example:


def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]),key.upper())
        for val in some_dict[key]:
            print(val)
dojo={
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC','Burbank'],
    'instroctors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon












