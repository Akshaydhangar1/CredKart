oxford= {"flabbergasted":"greatly surprised or Astonished","Happy":"Always Smiling"}
print(oxford)
# #
# employee = {"id" : 101, "name": "Yusuf", "salary" : 80000}
# print(employee)
# #
# oxford= {"flabbergasted":"greatly surprised or Astonished","Shocked":"greatly surprised or Astonished"}
# print(oxford)
# #
# oxford= {"flabbergasted":"greatly surprised or Astonished","flabbergasted":"Always Smiling"}
# print(oxford)
# #
# employee = {"id" : 101, "id": 102, "salary" : 80000}
# print(employee)
# employee = {"Id" : 101, "id": 102, "salary" : 80000}
# print(employee)
# #

# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev',
#      'city': 'New York',
#      'email': 'bob@web.com'}
# print(D)
# #
# D1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print(D1)
# #
# D1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
# print(D1)
# #
# L = [('name', 'Bob'),
#      ('age', 25),
#      ('job', 'Dev')]
# # #
# print(L)
# D = dict(L)
# print(D)
# # #
# T = (['name', 'Bob'],
#      ['age', 25],
#      ['job', 'Dev'])
# # #
# print(T)
#
# D = dict(T)
# print(D)
#
# keys = ['name', 'age', 'job']
# values = ['Bob', 25, 'Dev']
# #
# D = dict(zip(keys, values))
# #
# print(D)
#
# keys = ['a', 'b', 'c']
# defaultValue = 10
# D = dict.fromkeys(keys,defaultValue)
#
# print(D)


# D = {'name': 'Bob',
#      'age': 25,
#      'name': 'Jane'}
# print(D)
#
# D = {"Age": 25,
#      "Surname" : 'aradhe',
#      'name': 'Bob'}
#
# print(D)
# #
# D = {101: 25,
#      True: 'a',
#      'name': 'Bob'}
# print(D)
# #
# # #
# D = {(2,2): 25,
#      True: 'a',
#      'name': 'Bob'}
# print(D)
# #
# D = {('fname', 'jane'): 25,
#      True: 'a',
#      'name': 'Bob'}
# print(D)
#
# D = {[2,2]: 25,
#      'name': 'Bob'}
# print(D)  #TypeError: unhashable type: 'list'
#
# D = {'a':[1,2,3],
#      'b':{1,2,3},
#      'c':(1,2,3)}
# print(D)
# print(type(D))
#
# D = {'a':[1,2],
#      'b':[1,2],
#      'c':[1,2]}
# print(D)
# #
# D = {'a':(1,2),
#      'b':(1,2),
#      'c':(1,2)}
# print(D)
#
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}
# print(D)
# print("Name Of Emp :",D["name"])
# print("Age Of Emp :", D["age"])
# print("Job type Of Emp :", D["job"])
# print(D['salary'])
# #
# print(D.get('name'))
# print(D.get('salary'))
#
# # Creating a Dictionary within dictionary
Dict = {'key1': {1: 'Geeks'},
        'key2': {'Name': 'Yusuf'}}
# print(Dict)
# # # # Accessing element using key
# print(Dict['key1'])
# print(Dict['key2'])
#
# print(Dict['key1'][1])
# print(Dict['key2']['Name'])
# # #
# employee = {'emp1': {101: {"Name":"Yusuf","City": {"Street Name":"MG ROAD", "Flat No":"108", "City":"Pune","Pincode":411001}},
#         'emp2': {'102': 'Amit'}}}
#
# print(employee)
# print(employee['emp1'])
# print(employee['emp1'][101])
# print(employee['emp1'][101]["City"])
# print(employee['emp1'][101]["City"]["Street Name"])

# # # #
# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
# print(D)
# D['name'] = 'Sam'
# print(D)
# # #
# D['city'] = 'New York'
# D['salary'] = 100000
# # #
# print(D)
#
# # Creating an empty Dictionary
# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)
# #
# # # # Adding elements one at a time
# Dict[0] = 'Geeks'
# Dict[2] = 'For'
# Dict[3] = 1
# print("\nDictionary after adding 3 elements: ")
# print(Dict)
# #
# # # Adding set of values
# # # to a single Key
# Dict['Value_set'] = 2, 3, 4
# print("\nDictionary after adding 3 elements: ")
# print(Dict)
# #
# # # Updating existing Key's Value
# Dict[2] = 'Welcome'
# print("\nUpdated key value: ")
# print(Dict)
# #
# # # Adding Nested Key value to Dictionary
# Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
# print("\nAdding a Nested Key: ")
# print(Dict)
# print(Dict[5]['Nested']['1'])
# print(Dict[5]['Nested']['2'])

# D1 = {'name': 'Bob',
#       'age': 25,
#       'job': 'Dev'}
#
# D2 = {'age': 30,
#       'city': 'New York',
#       'email': 'bob@web.com'}
# print(D1)
# print(D2)
# D1.update(D2)
# print(D1)
#
# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
# # #
# x = D.pop('age')
# print(D)
# #
# # # get removed value
# print(x)
# # Prints 25
#
# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
#
# del D['age']
# print(D)

# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
# print(D)
#
# x = D.popitem()
# print(D)
# #
# # # get removed pair
# # print(x)
#
# # D = {'name': 'Bob',
# #      'age': 25,
# #      'job': 'Dev'}
# # print(D)
# # D.clear()
# # print(D)
#
# D = {'name': 'Yusuf',
#      'age': 31,
#      'job': 'Tester'}
# #
# # # get all keys
# print(D.keys())
# # # Prints ['name', 'age', 'job']
# #
# # # get all values
# print(D.values())
# # # Prints ['Bob', 25, 'Dev']
# #
# # # get all pairs
# print(D.items())
# # # Prints [('name', 'Bob'), ('age', 25), ('job', 'Dev')]
# #

D = {'name': 'Yusuf',
     'age': 31,
     'job': 'Tester'}
# #
# # # get all keys
# print(D.keys())
# print(list(D.keys()))
# # # Prints ['name', 'age', 'job']
# #
# # # get all values
# print(D.values())

# print(list(D.values()))
# # # Prints ['Bob', 25, 'Dev']
# #
# # # get all pairs
# print(D.items())

# print(list(D.items()))
# # # Prints [('name', 'Bob'), ('age', 25), ('job', 'Dev')]

# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
#
# print('name' in D.keys())
# print('salary' in D.keys())

# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
# print('Bob' in D.values())
# print('Amarprem' in D.values())

# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
#
# print(len(D))

# dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
#
# # copy() method
# dict2 = dict1.copy()
# print(dict1)
# print(dict2)

# print(dict2.get(1))
# dict2.update({3: "C++"})
# print(dict2)
#
# dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}
# print(any({'':'','':'','':''}))
# print(any({'':'','':'',3:'Ram'}))
#
# # #
# print(all({1:'',2:'','':''}))
# print(all({1:'',2:'',3:'',4:''}))
#
# print(sorted(dict) )

# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
# print(D)
# D['name'] = "Sam"
# print(D)

# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
# print(D)
# #
# D['name'] = input('name ')
# D['age'] = input('age ')
# D['job'] = input('job ')
# print(D)

