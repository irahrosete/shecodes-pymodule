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
moths_in_house = True
# moths_in_house = False
mitch_is_home = True
# mitch_is_home = False

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch.")
