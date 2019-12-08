Question1:¶

Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary. Add a new key value pair about qualification then update the qualification value to high academic level then delete it.

In [1]:

information = {"first_name": "Aiman", "last_name": "adeeb", "age": 20, "city": "Karachi"} # printing each piece of information in dictionary print(information) 

{'first_name': 'Aiman', 'last_name': 'adeeb', 'age': 20, 'city': 'Karachi'} 

In [2]:

information["Qualification"] = "Intermediate" # updating key with qualification information 

Out[2]:

{'first_name': 'Aiman', 'last_name': 'adeeb', 'age': 20, 'city': 'Karachi', 'Qualification': 'Intermediate'}

In [5]:

del information['Qualification'] # deleting key with del function print(information) 

Out[5]:

{'first_name': 'Aiman', 'last_name': 'adeeb', 'age': 20, 'city': 'Karachi'}

Question2:

Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

In [2]:

cities = {"Karachi": "karachi is the city of Pakistan, 25 crore, The city have shrine of Quaid e Azam" ,"Lahore": "20 crore population, the city have babri mosque" ,"Islamabad": "20, The city is beautyful "} cities 

Out[2]:

{'Karachi': 'karachi is the city of Pakistan, 25 crore, The city have shrine of Quaid e Azam', 'Lahore': '20 crore population, the city have babri mosque', 'Islamabad': '20, The city is beautyful '}

Question3:

A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

In [14]:

age = int(input("Please enter your age: ")) if age < 3: print("Welcome!! your entry is free") elif age>3 and age<12: print("your ticket charges is $10") elif age >12: print("your ticket charges is $15") 

Please enter your age: 15 your ticket charges is $15 

In [ ]:

Question4:

Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

In [16]:

def favorite_book(title): return "my favorite books is "+title print(favorite_book("Alice in Wonderland")) 

my favorite books is Alice in Wonderland 

In [ ]:

Question5:

Guess the number game Write a program which randomly generate a number between 1 to 30 and ask the user in input field to guess the correct number. Give three chances to user guess the number and also give hint to user if hidden number is greater or smaller than the number he given to input field.

In [8]:

# for generate random number importing a library import random generate_num = random.randint(1,30) guess_limit = 0 while guess_limit < 3: guess = int(input("guess any number ")) guess_limit+= 1 if guess == generate_num: print("you win") break else: print("try again you fail") print("right answer is "+str(generate_num)) 

guess any number 5 guess any number 8 guess any number 1 try again you fail right answer is 29 

In [ ]:

