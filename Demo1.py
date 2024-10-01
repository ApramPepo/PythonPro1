# Greet the user and ask them for their name.

print ('Welcome to Python!')
name = input('type your name: ')
name = name.strip().title()
print ('Hello, ' + name + '!' + ' Welcome to the program!')

# Ask users about their information

color = input('What is your favorite color? ')
color = color.strip().capitalize()
print ("Your favorite color is " + color, end="? ")
print ("Wow, you're awesome!")
age = input('What is your Birth year? ')
print("You're age the age of: ", end=""), print (2024 - int(age))
weight = input ("What is your weight in pound? ")
print("Your weight in kilogram is: ", end="")
print(0.45 * float(weight))

# Add location

country = input("Which country do you live in? ")
country = country.strip().capitalize()
print ("Cool to know you're from"+country, end="!")

city = input(" Would you mind if you tell us which city? ")
city = city.strip().capitalize()
print (city+"?", "Wow! Awesome!")



print('''
This is the first program made in python by Abram.
      Looking forward to understand more about this,
      and looking forward to make more.

      This is just the beginning of my Joruney. Thank You!
''')
