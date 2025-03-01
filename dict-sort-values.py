name= input("enter name: ")
dict1={}
while name != "stop":
    age= input("enter age: ")
    dict1[name]=str(age)
    name= input("enter name: ")

print (dict1)    

new_dict ={}

for i in dict1:
    age_value= dict1[i]
    if age_value in new_dict:
        new_dict[age_value].append(i)
    else:
        new_dict[age_value]= [i]
    

print(new_dict)

