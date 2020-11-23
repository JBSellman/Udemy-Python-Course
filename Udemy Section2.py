# intro to objects, statements, variables etc

print('helloworld')

# concatenate practice

temp = "hurt " + str(50+61) + ' bone'

print(temp)

b = temp.split(' ')[0]
print(b)

a = ["b", 'c', 'd']
a1 = a[2]
print(a1)

print("I struggled with Question "+["b", 'c', 'd'][1])

# Dictionary practice

lib1 = {"name": "James", "age": 23, 'hobby': "python"}

print(lib1["name"])

array1 = [13, 23, 4, 423, 52, 43, 10, 15]
print(len(array1))
print(sorted(array1))
array2 = ['3', '3.12', '1.05', 'h', '3.90', 'A', 'H', 'b']
print(len(array2))
print(sorted(array2))


# user-defined functions

def first_funciton():
    a = "defferently spaced"
    print(a+" Hi")


def second_function(name, age):
    sentence="Hi my name is " + name + " and I am " + str(age) + " years old"
    print(sentence)


first_funciton()
second_funciton("James", 23)


def gossip_function(topic="random goss",area="world"):  # defing a funciton with KEYWORD arguments
    print(topic, "is the hottest story in the", area)


gossip_function("Tommy's nipple hair")     # example of referencing first argument
gossip_function(area="the universe")        # referencing second argument


# testing loops

temp_array = ["sausage", "fennel", "aching", "tempest"]

bool_practice = True
bool_practice2 = bool(1)

while bool_practice:  # bool practice = True so this condition is effective checking if 1==1 or True==Ture
    print(temp_array[1])
    bool_practice = False

# The below doesn't work it struggles to turn bool_practice2 into a false statement
# # while bool_practice2:
# #     print(temp_array[0])
# #     bool_practice = bool(0)

for index in temp_array:
    print("I am a silly", index)
