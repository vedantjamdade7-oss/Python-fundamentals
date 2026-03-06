# Nested Dictionary - A Dict inside a Dict.
students = {
"student1": {
    1:"class-x",
    'name':'karan',
    'age': 20,
    'city':'mathura'
 },
"student2" : {
    1:"class-x",
    'name':'vedant',
    'age': 21,
    'city':'nagpur'
 }
}

print(students["student1"]["name"])
print(students["student2"]["name"])
print(students["student1"]["age"])
print(students["student2"]["age"])
print(students["student1"]["city"])
print(students["student2"]["city"])
print(students["student2"])

print("-------------")

for key,value in students.items():
    print(key,value)