"""Python module reading csv files exercises"""
# pylint: disable=invalid-name
import csv

# Q1. Write a program that reads in colours_20_simple.csv and output the colour data.
with open("csv_files/colours_20.csv", encoding="utf8") as colours_file:
    reader = csv.reader(colours_file)
    for line in reader:
        print(f"{line[1].lstrip():<12} {line[2].lstrip():<8} {line[4].lstrip()}")

# Q2. Write a program that reads in colours_20_simple.csv and outputs the colour data in order
# English, Hex then RGB.
with open("csv_files/colours_20_simple.csv", encoding="utf8") as colours_file:
    reader = csv.reader(colours_file)
    next(reader)
    for line in reader:
        print(f"{line[2]}, Hex: {line[1]}, RGB: {line[0]}")

# Q3. Write a program that reads in colours_20.csv and output the colour data in order
# English, Hex then RGB.
with open("csv_files/colours_20.csv", encoding="utf8") as colours_file:
    reader = csv.reader(colours_file)
    next(reader)
    for line in reader:
        print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")

# Q4. Using the same colour csv files, write a program that outputs the number of times
# each of the following colours appear in the English Name:
# ● red
# ● green
# ● blue
# ● yellow
red = 0
green = 0
blue = 0
yellow = 0

with open("csv_files/colours_20.csv", encoding="utf8") as colours_file:
# with open("csv_files/colours_213.csv", encoding="utf8") as colours_file:
    reader = csv.reader(colours_file)
    next(reader)

    for line in reader:
        if "red" in line[4]:
            red += 1
        elif "green" in line[4]:
            green += 1
        elif "blue" in line[4]:
            blue += 1
        elif "yellow" in line[4]:
            yellow += 1

print(f"Red: {red}\nGreen: {green}\nBlue: {blue}\nYellow: {yellow}")

# Q5. galaxies.py contains data about 82 different galaxies and their velocities (km/sec).
# Using this data, output the galaxy with the slowest velocity, and the galaxy with
# the highest velocity.
min_galaxy = ""
min_velocity = 1000000000
max_galaxy = ""
max_velocity = 0

with open("csv_files/galaxies.csv", encoding="utf8") as galaxies_file:
    reader = csv.reader(galaxies_file)
    next(reader)

    for line in reader:
        if int(line[1]) < int(min_velocity):
            min_velocity = line[1]
            min_galaxy = line[0]
        if int(line[1]) > int(max_velocity):
            max_velocity = line[1]
            max_galaxy = line[0]

print(f"Galaxy {min_galaxy} has the min velocity of {min_velocity}km/sec.")
print(f"Galaxy {max_galaxy} has the min velocity of {max_velocity}km/sec.")


# writing to csv file
# population = []
# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     for age_group in population:
#         csv_writer.writerow([age_group[1], age_group[0]])
