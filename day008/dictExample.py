students ={'Ali':18,'Rahim':12,'Karim':22,'Joya':25}
print('All Item:')
print(students)
print('print by key Rahim:')
print(students['Rahim'])

print (dir(students))

#we use the method students.update to
print('add sarah to our existing students')
students.update({"sarah":9})
print(students)
print('if exist update students')
students.update({'Karim':12})
print(students)

print('Delete by key')
del students['Ali']
print(students)

print('Print Items')
print("Students Name:%s"% students.items())
print('Convent dic to list:')
print("Students Name: %s" % list(students.items()))
 
print('print only keys:')
for key in students.keys():
    print(key)

print('print only values:')
for val in students.values():
    print(val)

print('print only key and value:')
for key in students.keys():
    print(key+"_"+str(students[key]))


print("# Loop over irtems and unpack each item.")
for k,v in students.items():
    #Display key and value
    print(k,v)


