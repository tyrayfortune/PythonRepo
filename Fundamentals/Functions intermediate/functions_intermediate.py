x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x[1][0])


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'bryant'
print (students)


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
(sports_directory['soccer'][0]) = 'Andres'
print(sports_directory['soccer'][0])

z = [ {'x': 10, 'y': 20} ]
(z[0]['y']) = 30
print(z)

students =[
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(students_list): 
    for students in students_list:
        print(f"first_name - {students['first_name']}, last_name - {students['last_name']}")
    
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for students in some_list:
        print(students[key_name])



iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print(len(some_dict['locations']), "locations")
    for locations in some_dict['locations']:
        print(locations)
    print()
    print(len(some_dict['instructors']), "instructors")
    for instructors in some_dict['instructors']:
        print(instructors)


printInfo(dojo)






