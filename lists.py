"""Python module lists exercises"""
# pylint: disable=invalid-name

#Q1. Given the list of foods below, output:
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
foods_num = len(foods)
print(foods[(foods_num-3):foods_num+1])
print(foods[6][-1])

#Q2. Format and print the following list:
mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]

for item in mailing_list:
    print(item[0] + ": " + item[1])
