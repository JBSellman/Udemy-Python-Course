#/intro to obkjects, statements, variables etc

print('helloworld')

##concatenate practice

temp= "hurt " +str( 50+61 ) + ' bone'

print(temp)

b=temp.split(' ')[2]
print(b)

a= ["b",'c','d']
a1=a[2]
print(a1)



print( "I struggled with Question "+["b",'c','d'][1])

#Dictionary practice

lib1= {"name":"James","age": 23,'hobby':"python"}

print(lib1["name"])

array1 = [13,23,4,423,52,43,10,15]
print(len(array1))
print(sorted(array1))
array2=['3','3.12','1.05','h','3.90','A','H','b']
print(len(array2))
print(sorted(array2))


#user-defined funtions

def first_funciton():
    a="defferently spaced"
    print(a+" Hi")

def second_funciton(name,age):
    sentence="Hi my name is " + name + " and I am " + str(age) + " years old"
    print(sentence)

first_funciton()
second_funciton("James",23)

def gossip_function(topic="random goss",area="world"):
    print(topic,"is the hottest story in the", area)

gossip_function( None ,"Tommy's nipple hair")