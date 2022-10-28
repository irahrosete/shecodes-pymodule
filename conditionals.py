"""Python module conditionals exercises"""

# Q1. Kate’s cat, Roary, loves catching moths. Write a program that
# determines whether or not it is time for Roary to catch moths.
# moths_in_house = True
# # moths_in_house = False

# if moths_in_house:
#     print("Get the moths!")
# else:
#     print("No threats detected.")

# Q2. But Roary can’t actually get the moths by herself! Amend the previous program
# to determine whether or not it is time for Roary to go moth hunting.
# moths_in_house = True
# # moths_in_house = False
# mitch_is_home = True
# # mitch_is_home = False

# if moths_in_house and mitch_is_home:
#     print("Hoooman! Help me get the moths!")
# elif not moths_in_house and not mitch_is_home:
#     print("No threats detected.")
# elif moths_in_house and not mitch_is_home:
#     print("Meooooooooooooow! Hissssss!")
# elif not moths_in_house and mitch_is_home:
#     print("Climb on Mitch.")

# Q3. Write a program that implements the algorithm for Red Light Cameras.
# light_colour = "Red"
# # light_colour = "Amber"
# # light_colour = "Green"
# car_detected = False
# # car_detected = True

# if car_detected and light_colour == "Red":
#     print("Flash!")
# else:
#     print("Do nothing.")

# Q4. Write a program that asks the user for their height, and determines whether or not
# they are tall enough to ride the rollercoaster, which has a height requirement of 120cms.
# height = int(input("What is your height? "))

# if height < 120:
#     print("Sorry, not today :(")
# else:
#     print("Hop on!")

#Q5. Write a program that asks the user to enter their username and password, and outputs a success
# message if they are correct, or a failure message if they are incorrect.
username = "fleur"
password = "password123"

username_input = input("Username: ")
password_input = input("Password: ")

if username_input == username and password_input == password:
    print("Correct!")
else:
    print("Incorrect!")
