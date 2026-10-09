firstname="fardin"
lastname='islam'
country='Bangladesh'
city='Dhaka'
age=23
is_married=False
skill=['html','css','js','react','python']
personal_info={
  'firstname':'Fardin',
  'lastname':'islam',
  'country': 'Bnaladesh',
  'city' :'Dhaka'
}

# Printing the values stored in the variables

print('First name:', firstname)
print('First name length:', len(firstname))
print('Last name: ', lastname)
print('Last name length: ', len(lastname))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skill)
print('Person information: ', personal_info)

#declearing multiple variable in one line:

first_name ,last_name,country,city,age='fardin','islam','Bangladesh','Dhaka',23

#taking user input using built in funtion input()

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
