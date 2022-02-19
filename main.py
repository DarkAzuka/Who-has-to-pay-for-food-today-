import random

print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Welcome to Who Pays Today!*:･ﾟ✧\n')
print(''''         ,-"-.
       _r-----i          _
       \      |-.      ,###.
        |     | |    ,-------.
        |     | |   c|       |                       ,--.
        |     |'     |       |      _______________ C|  |
        (=====)      =========      \_____________/  `=='   cww
(HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH)''')

print('Fun dynamic with friends, to see who pays for food today, randomly')

test_seed = int(input("Write a random number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_names = len(names)

number_random = random.randint(0, number_names -1)

#I changed my list in str so that it would print without any problem <3
persons_random = str(names[number_random])

print(f'{persons_random} is going to buy the meal today!')