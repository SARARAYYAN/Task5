name = input('Name: ')
age = input('Age: ')
street = input('Street: ')
city = input('City: ')
country = input('Country: ')
print("\"Name: ", name ,"\"")
#
print("\"Age: ", age ,"\"")
print("\"Address: ", street,"," ,city, "," , country , "\"")
newAge = int(age) - 5
print("\"Hello" ,"{",name, "}" , "your age is " ,newAge , "Years Old, Your Address: ", street,"," ,city, "," , country , "\"")
print(type(name))
print(type(age))
print(type(street))
print(type(city))
print(type(country))
print("\"Hello" ,"{",name, "}","How are you?\\"",""your age is ""\"" ,newAge,"\"", ",+And Your Country Is:", country)
print("\"Hello" ,"{",name, "}","How are you?\\")
print("your age is ""\"" ,newAge,"\"")
print("+And Your City Is:", city,)

#
name = 'ITF Gsg Python'
print(f'First Letter Is "{name[0]}"')
print(f'Third Letter Is "{name[2]}"')
print(f'Last Letter Is "{name[-1]}"')
print(name[-3] , name[-2] ,name[-1] )
print(name[0] , name[1] ,name[2] )
print(name[0] , name[2] , name[4] ,name[6] )
print(name[-1] , name[-2] ,name[-3] ,name[-4] ,name[-5] ,name[-6] )

name = "$&$&Mohammed$&$&"
cleaned_name = name.strip("$&")
print(cleaned_name)
msg = "I %7 Python And Although I %7 GSG with Zakaria"
msg = msg.replace("%7", "Love")
print(msg)
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
num1 = num1.zfill(5)
num2 = num2.zfill(5)
num3 = num3.zfill(5)
num4 = num4.zfill(5)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)

first_name =input('Name: ')
print("***********", first_name,"\n","***********",first_name ,"***********","\n",first_name,"***********")

title= "hello world"
print(title.capitalize())

title2="sara rayyan"
print(title2.capitalize())

name_one = "SaMER"
name_two = "Abed"
#print(name_one.capitalize())
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
if name_one.isupper():
    print("name_one contains only uppercase letters.")
    print("yes")
if name_two.islower():
    print("name_two contains only lowercase letters.")
    print("yes")





