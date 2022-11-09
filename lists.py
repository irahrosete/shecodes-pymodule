"""Python module lists exercises"""
# pylint: disable=invalid-name

# Q1. Given the list of foods below, output:
  # 1. The first item in the list.
  # 2. The third item in the list.
  # 3. The last item in the list.
  # 4. The first three items in the list.
  # 5. The last three items in the list.
  # 6. The last item in the sublist.
foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][-1])

# Q2. Format and print the following list:
mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]

for item in mailing_list:
    print(item[0] + ": " + item[1])

# Q3. Ask the user for three names, add them to a list, then print the list.
names = []

for name in range(3):
    names.append(input("Enter a name: "))
print(names)

# Q4. Using the following starter code:
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []
# Produce the following lists:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = [a, b, c]
print(newlist)

new_newlist = []
new_newlist.extend(a)
new_newlist.extend(b)
new_newlist.extend(c)
print(new_newlist)

# alternatives:
print(a + b + c)
print([*a, *b, *c])

# def flatmap(new_list, sublist):
#     """flatmap"""
#     for item in sublist:
#         for subitem in item:
#             new_list.append(subitem)

# alpha = []
# flatmap(alpha, newlist)
# print(alpha)
